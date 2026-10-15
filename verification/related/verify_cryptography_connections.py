"""Exact finite checks for the cryptography-connections note.

Run from any directory with Python 3.10 or later. Only the standard library
is used. These checks supply regression evidence, not proofs or a security
claim for a cryptographic construction. The large-parameter calculations use
exact Fractions; their decimal strings are compact, rounded display values.
"""

from __future__ import annotations

import argparse
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import factorial
from pathlib import Path
from time import perf_counter


def load_sequence():
    """Load only the repository's standard-library sequence implementation."""
    path = Path(__file__).resolve().parents[1] / "verify_a183068.py"
    spec = spec_from_file_location("a183068_core_verifier", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load sequence implementation: {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.a


def require(condition: bool, description: str) -> None:
    """Keep checks active even if Python is run with optimization enabled."""
    if not condition:
        raise AssertionError(description)


def factorial_definition(n: int) -> int:
    total = 0
    for k in range(n + 1):
        term, remainder = divmod(
            factorial(2 * n + 2 * k),
            factorial(k) ** 4 * factorial(n - k) ** 2,
        )
        require(remainder == 0, f"Nonintegral factorial summand: n={n}, k={k}")
        total += term
    return total


def check_residue_collisions() -> dict:
    a = load_sequence()
    for n in range(13):
        require(a(n) == factorial_definition(n), f"Sequence mismatch at n={n}")

    ranges = {2: 12, 3: 8, 5: 6, 7: 4, 11: 4}
    cases = 0
    toy_examples = []
    for p, maximum_m in ranges.items():
        for m in range(1, maximum_m + 1):
            r = (m + 1) // 2
            modulus = p**m
            for n in range(1, 5):
                x, y = n * p ** (r - 1), n * p**r
                hx, hy = a(x) % modulus, a(y) % modulus
                require(x != y, "Collision inputs must be distinct")
                require(hx == hy, f"Residue collision failed: p={p}, m={m}, n={n}")
                # A deterministic function of the residue cannot distinguish
                # inputs whose residues already coincide. This is only a toy
                # postprocessing function, not a proposed hash construction.
                post_x = (hx * hx + 17 * hx + 3) % 257
                post_y = (hy * hy + 17 * hy + 3) % 257
                require(post_x == post_y, "Postprocessing separated equal residues")
                if n == 1 and m == maximum_m:
                    toy_examples.append(
                        {"p": p, "m": m, "x": x, "y": y,
                         "residue": hx, "postprocessed": post_x}
                    )
                cases += 1

    # These checks concern only the input domain at large m; they do not
    # attempt exponentially large exact sequence evaluations.
    for m in range(2, 257):
        r = (m + 1) // 2
        x, y = 1 << (r - 1), 1 << r
        require(0 <= x < y < (1 << m), f"Inputs outside the m-bit domain: m={m}")
    binary_boundary = [a(n) % 2 for n in (0, 1)]
    require(len(set(binary_boundary)) == 2, "The one-bit boundary should be injective")

    return {
        "factorial_cross_checks": 13,
        "direct_residue_cases": cases,
        "deterministic_postprocessing_cases": cases,
        "binary_domain_only_checks_m_2_through_256": 255,
        "one_bit_boundary_outputs": binary_boundary,
        "toy_examples": toy_examples,
    }


def all_binary_matrices(r: int, t: int):
    """All t-by-r matrices, each represented by t integer row masks."""
    mask = (1 << r) - 1
    for code in range(1 << (r * t)):
        yield tuple((code >> (i * r)) & mask for i in range(t))


def gf2_rank(rows: tuple[int, ...]) -> int:
    """Gaussian elimination, independent of output-frequency enumeration."""
    pivots: dict[int, int] = {}
    for row in rows:
        value = row
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def apply_map(rows: tuple[int, ...], x: int) -> int:
    return sum(((row & x).bit_count() % 2) << i for i, row in enumerate(rows))


def enumerate_output_frequencies(rows: tuple[int, ...], r: int, shift: int) -> list[int]:
    frequencies = [0] * (1 << len(rows))
    for x in range(1 << r):
        frequencies[apply_map(rows, x) ^ shift] += 1
    return frequencies


def total_variation_from_uniform(frequencies: list[int]) -> Fraction:
    samples = sum(frequencies)
    outputs = len(frequencies)
    return Fraction(sum(abs(count * outputs - samples) for count in frequencies),
                    2 * samples * outputs)


def rank_count_formula(r: int, t: int, k: int) -> int:
    if k < 0 or k > min(r, t):
        return 0
    answer = Fraction(1)
    for i in range(k):
        answer *= Fraction(((1 << t) - (1 << i)) * ((1 << r) - (1 << i)),
                           (1 << k) - (1 << i))
    require(answer.denominator == 1, f"Nonintegral rank count for r={r}, t={t}, k={k}")
    return answer.numerator


def full_row_rank_probability(r: int, t: int) -> Fraction:
    if t > r:
        return Fraction(0)
    answer = Fraction(1)
    for i in range(t):
        answer *= Fraction((1 << r) - (1 << i), 1 << r)
    return answer


def distance_at_rank(k: int, t: int) -> Fraction:
    return Fraction((1 << t) - (1 << k), 1 << t)


def check_all_small_matrices() -> dict:
    matrices = translations = rank_frequency_checks = 0
    parameter_cases = []
    for r in range(5):
        for t in range(4):
            input_size, output_size = 1 << r, 1 << t
            matrix_count = 1 << (r * t)
            rank_frequencies: Counter[int] = Counter()
            joint_tv_numerator = 0
            for rows in all_binary_matrices(r, t):
                rank = gf2_rank(rows)
                rank_frequencies[rank] += 1
                expected_tv = distance_at_rank(rank, t)
                for shift in range(output_size):
                    frequencies = enumerate_output_frequencies(rows, r, shift)
                    observed_tv = total_variation_from_uniform(frequencies)
                    require(observed_tv == expected_tv,
                            f"TV mismatch: r={r}, t={t}, rows={rows}, shift={shift}")
                    require(sum(count > 0 for count in frequencies) == (1 << rank),
                            "Image cardinality disagrees with elimination rank")
                    require(all(count in (0, input_size // (1 << rank))
                                for count in frequencies), "Image fibers are unequal")
                    if shift == 0:
                        # Independently accumulate the discrepancy for the
                        # joint (public matrix seed, output) distribution.
                        joint_tv_numerator += sum(
                            abs(count * output_size - input_size) for count in frequencies
                        )
                    translations += 1
                matrices += 1

            for k in range(min(r, t) + 1):
                require(rank_frequencies[k] == rank_count_formula(r, t, k),
                        f"Rank-frequency mismatch: r={r}, t={t}, k={k}")
                rank_frequency_checks += 1
            require(sum(rank_frequencies.values()) == matrix_count, "Missing matrices")
            observed_joint_tv = Fraction(joint_tv_numerator,
                                         2 * input_size * output_size * matrix_count)
            rank_weighted_tv = sum(
                (Fraction(count, matrix_count) * distance_at_rank(k, t)
                 for k, count in rank_frequencies.items()), Fraction(0)
            )
            formula_weighted_tv = sum(
                (Fraction(rank_count_formula(r, t, k), matrix_count) * distance_at_rank(k, t)
                 for k in range(min(r, t) + 1)), Fraction(0)
            )
            require(observed_joint_tv == rank_weighted_tv == formula_weighted_tv,
                    f"Joint seeded distance mismatch: r={r}, t={t}")
            observed_full_rank = Fraction(rank_frequencies[t], matrix_count)
            require(observed_full_rank == full_row_rank_probability(r, t),
                    f"Full-row-rank mismatch: r={r}, t={t}")
            if t > r:
                require(observed_full_rank == 0 and observed_joint_tv > 0,
                        "More output bits than source dimensions cannot be uniform")
            parameter_cases.append(
                {"r": r, "t": t, "matrices": matrix_count,
                 "joint_tv_exact": str(observed_joint_tv),
                 "full_row_rank_probability_exact": str(observed_full_rank)}
            )

    zero_map_tv = total_variation_from_uniform(enumerate_output_frequencies((0, 0), 3, 0))
    require(zero_map_tv == Fraction(3, 4), "The zero map must fail to extract two uniform bits")
    return {
        "parameter_pairs": len(parameter_cases),
        "matrices_exhaustively_enumerated": matrices,
        "matrix_and_translation_cases": translations,
        "rank_frequency_checks": rank_frequency_checks,
        "zero_map_r_3_t_2_tv_exact": str(zero_map_tv),
        "parameter_cases": parameter_cases,
    }


def check_linear_leakage() -> dict:
    # X is uniform on F_2^3; Z=x_0+x_1. Conditional on either Z, X is
    # uniform on a two-dimensional affine subspace. L is an independent,
    # uniform one-row map, and is included in the public output.
    actual: Counter[tuple[int, int, int]] = Counter()
    marginals: Counter[tuple[int, int]] = Counter()
    for row in range(8):
        for x in range(8):
            z = (x & 0b011).bit_count() % 2
            y = (row & x).bit_count() % 2
            actual[row, z, y] += 1
            marginals[row, z] += 1
    total = 64
    tv = sum(
        (abs(Fraction(actual[row, z, y], total) - Fraction(marginals[row, z], 2 * total))
         for row in range(8) for z in range(2) for y in range(2)), Fraction(0)
    ) / 2
    rank_formula_tv = sum(
        (Fraction(rank_count_formula(2, 1, k), 4) * distance_at_rank(k, 1)
         for k in range(2)), Fraction(0)
    )
    require(tv == rank_formula_tv == Fraction(1, 8), "Linear-leakage joint distance mismatch")
    return {"raw_source_bits": 3, "conditional_affine_dimension": 2,
            "joint_seed_and_input_cases": total, "joint_tv_exact": str(tv)}


def check_seed_dependent_source() -> dict:
    # Every public one-row map on F_2^2 has a nonzero kernel vector. Select
    # that vector after seeing the seed, then choose uniformly from {0,v}.
    # Each conditional source has one bit of entropy, but the tag is always
    # zero: independence of the source and seed is indispensable.
    actual: Counter[tuple[int, int]] = Counter()
    chosen_vectors = []
    for row in range(4):
        vector = next(v for v in range(1, 4) if (row & v).bit_count() % 2 == 0)
        chosen_vectors.append(vector)
        for x in (0, vector):
            actual[row, (row & x).bit_count() % 2] += 1
    tv = sum((abs(Fraction(actual[row, y], 8) - Fraction(1, 8))
              for row in range(4) for y in range(2)), Fraction(0)) / 2
    require(tv == Fraction(1, 2), "Seed-dependent kernel source should have a constant tag")
    require(all(actual[row, 0] == 2 and actual[row, 1] == 0 for row in range(4)),
            "Kernel source did not produce only zero tags")
    return {"seeds": 4, "conditional_source_size": 2,
            "chosen_nonzero_kernel_vectors": chosen_vectors, "joint_tv_exact": str(tv)}


def compact_fraction(value: Fraction) -> dict:
    with localcontext() as context:
        context.prec = 12
        decimal = Decimal(value.numerator) / Decimal(value.denominator)
    return {"rounded_scientific": f"{decimal:.10E}",
            "exact_numerator_bits": value.numerator.bit_length(),
            "exact_denominator_bits": value.denominator.bit_length()}


def check_large_rank_formulas() -> list[dict]:
    results = []
    for r, t in ((16, 8), (64, 32), (128, 64)):
        counts = [rank_count_formula(r, t, k) for k in range(t + 1)]
        matrix_count = 1 << (r * t)
        require(sum(counts) == matrix_count, f"Large rank counts do not partition matrices: {r}, {t}")
        full_rank = full_row_rank_probability(r, t)
        require(Fraction(counts[t], matrix_count) == full_rank,
                "Large full-row-rank formulas disagree")
        joint_tv = sum((Fraction(counts[k], matrix_count) * distance_at_rank(k, t)
                        for k in range(t + 1)), Fraction(0))
        require(0 < joint_tv < 1 - full_rank, "Unexpected large-parameter distance")
        results.append({"r": r, "t": t,
                        "joint_tv": compact_fraction(joint_tv),
                        "rank_failure_probability": compact_fraction(1 - full_rank)})
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Also save the JSON summary to this path")
    arguments = parser.parse_args()
    start = perf_counter()
    result = {
        "status": "all exact checks passed",
        "scope": "Finite regression evidence; no cryptographic security or novelty claim.",
        "residue_collisions": check_residue_collisions(),
        "affine_privacy_amplification": check_all_small_matrices(),
        "linear_side_information": check_linear_leakage(),
        "seed_dependent_source_counterexample": check_seed_dependent_source(),
        "large_parameter_formula_checks": check_large_rank_formulas(),
    }
    result["elapsed_seconds"] = round(perf_counter() - start, 3)
    summary = json.dumps(result, indent=2) + "\n"
    if arguments.json is not None:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(summary, encoding="utf-8")
    residues = result["residue_collisions"]
    affine = result["affine_privacy_amplification"]
    print(f"factorial definition checks: {residues['factorial_cross_checks']}")
    print(f"direct residue collisions: {residues['direct_residue_cases']}")
    print(f"binary matrices enumerated: {affine['matrices_exhaustively_enumerated']}")
    print(f"matrix/translation cases: {affine['matrix_and_translation_cases']}")
    print("linear-leakage joint TV: 1/8; seed-dependent counterexample TV: 1/2")
    print(f"all exact checks passed in {result['elapsed_seconds']} seconds")
    if arguments.json is not None:
        print(f"JSON summary: {arguments.json}")


if __name__ == "__main__":
    main()

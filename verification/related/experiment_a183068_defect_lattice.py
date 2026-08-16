"""Exact valuation-defect lattice for the A183068 proof.

This is an exploratory visualization aid, not a proof and not a spin-foam
model.  Each summand is treated as a lattice site.  The two local obligations
in the proof become nonnegative defect energies:

* p does not divide k: F(N, k) must vanish modulo p^(2r);
* p divides k: F(N, k) must transfer to F(N/p, k/p) modulo p^(2r).

Run from the repository root, for example:

    python verification/related/experiment_a183068_defect_lattice.py \
        --output data/a183068_defect_lattice.tsv

Only Python integers and the standard library are used.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from functools import cache
from math import comb
from pathlib import Path


@cache
def summand(n: int, k: int) -> int:
    """Return F(n,k) as the exact six-part multinomial coefficient."""
    if not 0 <= k <= n:
        raise ValueError("expected 0 <= k <= n")

    parts = (k, k, k, k, n - k, n - k)
    remaining = sum(parts)
    value = 1
    for part in parts:
        value *= comb(remaining, part)
        remaining -= part
    return value


@cache
def sequence(n: int) -> int:
    """Return a(n) exactly."""
    return sum(summand(n, k) for k in range(n + 1))


def valuation(value: int, prime: int) -> int | None:
    """Return v_prime(value), using None for the valuation of zero."""
    if prime < 2:
        raise ValueError("prime must be at least 2")
    if value == 0:
        return None

    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


@dataclass(frozen=True)
class Site:
    prime: int
    level: int
    multiplier: int
    upper_index: int
    summand_index: int
    stratum: str
    valuation: int | None
    target: int
    slack: int | None
    violation_energy: int


def site(prime: int, level: int, multiplier: int, k: int) -> Site:
    """Evaluate one local proof obligation at N=multiplier*prime^level."""
    n_upper = multiplier * prime**level
    upper = summand(n_upper, k)
    target = 2 * level

    if k % prime:
        stratum = "vanish"
        value = upper
    else:
        stratum = "transfer"
        value = upper - summand(n_upper // prime, k // prime)

    exponent = valuation(value, prime)
    slack = None if exponent is None else exponent - target
    energy = 0 if exponent is None else max(0, -slack)
    return Site(
        prime=prime,
        level=level,
        multiplier=multiplier,
        upper_index=n_upper,
        summand_index=k,
        stratum=stratum,
        valuation=exponent,
        target=target,
        slack=slack,
        violation_energy=energy,
    )


def lattice(
    primes: tuple[int, ...], levels: int, multipliers: int
) -> list[Site]:
    """Build the finite defect lattice requested on the command line."""
    sites: list[Site] = []
    for prime in primes:
        for level in range(1, levels + 1):
            for multiplier in range(1, multipliers + 1):
                n_upper = multiplier * prime**level
                sites.extend(
                    site(prime, level, multiplier, k)
                    for k in range(n_upper + 1)
                )
    return sites


def write_tsv(path: Path, sites: list[Site]) -> None:
    """Write the exact site data in a diff-friendly format."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(asdict(sites[0]))
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, dialect="excel-tab")
        writer.writeheader()
        writer.writerows(asdict(item) for item in sites)


def check_global_cases(
    primes: tuple[int, ...], levels: int, multipliers: int
) -> int:
    """Check the assembled supercongruence on the same finite box."""
    checks = 0
    for prime in primes:
        for level in range(1, levels + 1):
            modulus = prime ** (2 * level)
            for multiplier in range(1, multipliers + 1):
                upper = multiplier * prime**level
                lower = multiplier * prime ** (level - 1)
                assert (sequence(upper) - sequence(lower)) % modulus == 0
                checks += 1
    return checks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--primes",
        default="2,3,5",
        help="comma-separated primes (default: 2,3,5)",
    )
    parser.add_argument(
        "--levels",
        type=int,
        default=2,
        help="largest p-adic level r (default: 2)",
    )
    parser.add_argument(
        "--multipliers",
        type=int,
        default=3,
        help="largest multiplier n (default: 3)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="optional TSV destination",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    primes = tuple(int(value) for value in args.primes.split(","))
    if args.levels < 1 or args.multipliers < 1:
        raise ValueError("levels and multipliers must be positive")

    sites = lattice(primes, args.levels, args.multipliers)
    violations = [item for item in sites if item.violation_energy]
    finite_slacks = [item.slack for item in sites if item.slack is not None]
    sharp = sum(slack == 0 for slack in finite_slacks)
    global_checks = check_global_cases(primes, args.levels, args.multipliers)

    assert not violations, violations[:5]
    if args.output:
        write_tsv(args.output, sites)

    print(f"local sites: {len(sites)}")
    print(f"global cases: {global_checks}")
    print(f"sharp local sites: {sharp}")
    print(f"minimum finite slack: {min(finite_slacks)}")
    print("violation energy: 0 at every tested site")
    if args.output:
        print(f"wrote: {args.output}")


if __name__ == "__main__":
    main()

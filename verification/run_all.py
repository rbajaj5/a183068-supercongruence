"""Run every exact checker included in this repository."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = (
    "verification/check_repository_integrity.py",
    "verification/verify_a183068.py",
    "verification/related/verify_arithmetic_frobenius_packet_framework.py",
    "verification/related/verify_landau_supercongruence.py",
    "verification/related/verify_catalan_ballot_supercongruences.py",
    "verification/related/verify_bala_oeis_supercongruences.py",
    "verification/related/verify_bala_110_campaign.py",
    "verification/related/verify_a365029_first_two_levels.py",
    "verification/related/verify_binomial_quotient_cancellation.py",
    "verification/related/verify_a288470_odd_prime_tower.py",
    "verification/related/verify_multinomial_power_towers.py",
    "verification/related/verify_odd_unit_block_towers.py",
    "verification/related/verify_q_calculus_supercongruence.py",
    "verification/related/verify_weighted_lift_collision_synthesis.py",
    "verification/related/verify_dwork_period_supercongruence.py",
    "verification/related/verify_finite_field_determinant_bias.py",
    "verification/related/verify_finite_field_pfaffian_bias.py",
    "verification/related/verify_hyperdeterminant_fourier.py",
    "verification/related/verify_hyperdeterminant_entropy.py",
    "verification/related/verify_zhang_four_matrix_counterexample.py",
    "verification/related/verify_jacobian_counterexample_counts.py",
    "verification/related/verify_jacobian_degree_four.py",
    "verification/related/verify_jacobian_degree_five.py",
    "verification/related/verify_eta_prime3.py",
    "verification/related/verify_cooper_level11.py",
    "verification/related/verify_dwork_boundaries.py",
    "verification/related/verify_gaussian_twists.py",
    "verification/related/verify_bala_gaussian_twist_pilot.py",
    "verification/related/verify_binomial_power_frobenius.py",
    "verification/related/verify_quadratic_gaussian_queue.py",
    "verification/related/verify_cyclotomic_coefficient_pair.py",
    "verification/related/verify_euler_product_gaussian_tower.py",
    "verification/related/verify_dyadic_hypercube_defect.py",
    "verification/related/verify_dyadic_hypercube_walsh.py",
    "verification/related/verify_affine_spectrum_hashing.py",
    "verification/related/verify_chowla_dwork_evans_defect.py",
    "verification/related/verify_gaussian_power_sums.py",
    "verification/related/verify_gaussian_wolstenholme.py",
    "verification/related/verify_gaussian_product_isometry.py",
    "verification/related/experiment_gaussian_product_dynamics.py",
    "verification/related/verify_gq2_orientation_lifts.py",
    "verification/related/verify_gq2_appendices.py",
    "verification/related/verify_gq2_finite_abelian_counts.py",
    "verification/related/verify_gq2_dihedral_counts.py",
    "verification/related/verify_gq2_quaternion_counts.py",
    "verification/related/verify_gq2_maximal_cyclic_counts.py",
    "verification/related/verify_lattice_walk_frobenius.py",
    "verification/related/verify_black_noise_chaos_filter.py",
    "verification/related/verify_dyadic_affine_mixed_cohomology.py",
    "verification/related/verify_dyadic_dehn_twist_sampler.py",
    "verification/related/verify_dyadic_dehn_twist_cayley.py",
    "verification/related/verify_dyadic_twist_grammar.py",
    "verification/related/verify_dyadic_dehn_twist_conjugacy.py",
    "verification/related/verify_higher_degree_box_polynomial.py",
    "verification/related/verify_gaussian_erdos_moser.py",
)


def main() -> None:
    for relative in SCRIPTS:
        print(f"\n=== {relative} ===", flush=True)
        subprocess.run(
            [sys.executable, str(ROOT / relative)],
            cwd=ROOT,
            check=True,
        )
    print(f"\nall {len(SCRIPTS)} verification programs passed")


if __name__ == "__main__":
    main()


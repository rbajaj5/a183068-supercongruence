"""Run every exact checker included in this repository."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = (
    "verification/verify_a183068.py",
    "verification/related/verify_landau_supercongruence.py",
    "verification/related/verify_q_calculus_supercongruence.py",
    "verification/related/verify_weighted_lift_collision_synthesis.py",
    "verification/related/verify_frobenius_obstruction_automata.py",
    "verification/related/verify_frobenius_transfer_thermodynamics.py",
    "verification/related/verify_padic_valuation_expansion.py",
    "verification/related/verify_dwork_period_supercongruence.py",
    "verification/related/verify_finite_field_determinant_bias.py",
    "verification/related/verify_finite_field_pfaffian_bias.py",
    "verification/related/verify_determinant_pfaffian_convolution.py",
    "verification/related/verify_hyperdeterminant_fourier.py",
    "verification/related/verify_hyperdeterminant_convolution.py",
    "verification/related/verify_usamo_hamming_supercongruence.py",
    "verification/related/verify_jacobian_counterexample_counts.py",
    "verification/related/verify_jacobian_degree_four.py",
    "verification/related/verify_jacobian_degree_five.py",
    "verification/related/verify_jacobian_degree_six.py",
    "verification/related/verify_jacobian_degree_seven.py",
    "verification/related/verify_eta_prime3.py",
    "verification/related/verify_cooper_level11.py",
    "verification/related/verify_dwork_boundaries.py",
    "verification/related/verify_gaussian_twists.py",
    "verification/related/verify_gaussian_power_sums.py",
    "verification/related/verify_gaussian_angular_residue.py",
    "verification/related/verify_gaussian_kakeya_spectrum.py",
    "verification/related/verify_gaussian_wolstenholme.py",
    "verification/related/verify_gaussian_product_isometry.py",
    "verification/related/experiment_gaussian_product_dynamics.py",
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


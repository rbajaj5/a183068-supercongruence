"""Structural checks for the 110-record Bala proof-campaign ledger."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "data" / "bala_110_campaign.tsv"

EXPECTED_ROUTES = {"T": 40, "C": 37, "F": 14, "M": 14, "D": 5}
EXPECTED_STATUSES = {
    "proved-here": 10,
    "published-source": 12,
    "partial": 6,
    "no-explicit-open": 3,
    "queued": 79,
}


def main() -> None:
    with LEDGER.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, dialect="excel-tab"))

    assert len(rows) == 110
    assert len({row["oeis"] for row in rows}) == 110
    assert all(
        len(row["oeis"]) == 7
        and row["oeis"].startswith("A")
        and row["oeis"][1:].isdigit()
        for row in rows
    )
    assert Counter(row["route"] for row in rows) == EXPECTED_ROUTES
    assert Counter(row["status"] for row in rows) == EXPECTED_STATUSES
    assert all(row["evidence"] for row in rows)
    assert all(row["next_action"] for row in rows)

    proved = sorted(row["oeis"] for row in rows if row["status"] == "proved-here")
    sourced = sorted(
        row["oeis"] for row in rows if row["status"] == "published-source"
    )
    partial = sorted(row["oeis"] for row in rows if row["status"] == "partial")
    no_open = sorted(
        row["oeis"] for row in rows if row["status"] == "no-explicit-open"
    )

    print("Bala 110-record campaign ledger passed")
    print(f"route counts: {EXPECTED_ROUTES}")
    print(f"status counts: {EXPECTED_STATUSES}")
    print(f"proved here: {proved}")
    print(f"published sources: {sourced}")
    print(f"partial: {partial}")
    print(f"no explicit open target: {no_open}")


if __name__ == "__main__":
    main()

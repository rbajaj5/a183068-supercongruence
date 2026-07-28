"""Exact predictive-state audit of the degree-seven Frobenius cycle."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256

from verify_frobenius_transfer_thermodynamics import (
    DEGREE_SEVEN,
    MODULUS,
    PERIOD,
    PRECISION,
    START,
    correction,
    extend_traces_mod,
    truncated_valuation,
)


MINIMAL_MEMORY = 1_824
WITNESS_INDICES = (11_839, 15_739)
WITNESS_PHASES = (11_856, 15_756)
WITNESS_NEXT_VALUES = (4, 3)
WITNESS_HISTORY_HASH = (
    "7ddbcdcae2330f4f474659bbf0678d3213c1196f2c78d7557ddc9fc39a8d9d8e"
)
WITNESS_HISTORY_COUNTS = {0: 1_498, 1: 255, 2: 52, 3: 15, 4: 3}


def valuation_word() -> list[int]:
    traces = extend_traces_mod(
        DEGREE_SEVEN, START + 2 * PERIOD + 1, MODULUS
    )

    def packet(r: int) -> int:
        return (2 * traces[r] + correction(r)) % MODULUS

    return [
        truncated_valuation(packet(r - 1) - packet(r))
        for r in range(START + 1, START + PERIOD + 1)
    ]


def minimal_period(word: list[int]) -> int:
    """Return the least linear period when the word length is a multiple."""
    length = len(word)
    prefix = [0] * length
    for i in range(1, length):
        j = prefix[i - 1]
        while j and word[i] != word[j]:
            j = prefix[j - 1]
        if word[i] == word[j]:
            j += 1
        prefix[i] = j
    candidate = length - prefix[-1]
    return candidate if length % candidate == 0 else length


def cyclic_history(word: list[int], index: int, length: int) -> bytes:
    size = len(word)
    return bytes(
        word[(index - length + 1 + offset) % size]
        for offset in range(length)
    )


def transition_sets(word: list[int]) -> dict[int, set[int]]:
    size = len(word)
    return {
        value: {
            word[(index + 1) % size]
            for index, current in enumerate(word)
            if current == value
        }
        for value in sorted(set(word))
    }


def verify_minimal_memory(word: list[int]) -> None:
    left, right = WITNESS_INDICES
    shorter = MINIMAL_MEMORY - 1
    left_history = cyclic_history(word, left, shorter)
    right_history = cyclic_history(word, right, shorter)
    assert left_history == right_history
    assert (
        word[(left + 1) % PERIOD],
        word[(right + 1) % PERIOD],
    ) == WITNESS_NEXT_VALUES
    assert sha256(left_history).hexdigest() == WITNESS_HISTORY_HASH
    assert dict(sorted(Counter(left_history).items())) == WITNESS_HISTORY_COUNTS
    assert (
        START + 1 + left,
        START + 1 + right,
    ) == WITNESS_PHASES

    full_histories = {
        cyclic_history(word, index, MINIMAL_MEMORY)
        for index in range(PERIOD)
    }
    assert len(full_histories) == PERIOD


def main() -> None:
    word = valuation_word()
    assert len(word) == PERIOD
    assert minimal_period(word) == PERIOD
    assert transition_sets(word) == {
        0: {0, 1, 2, 3, 4},
        1: {0, 1, 2},
        2: {0, 1, 3},
        3: {0, 1, 2, 3, 4},
        4: {0, 1, 2, 3},
    }
    verify_minimal_memory(word)

    print("cycle length and minimal output period:", PERIOD)
    print("one-step transition sets:", transition_sets(word))
    print(
        "length-1823 witness phases and next values:",
        WITNESS_PHASES,
        WITNESS_NEXT_VALUES,
    )
    print("unique length-1824 histories:", PERIOD)
    print("PASS")


if __name__ == "__main__":
    main()

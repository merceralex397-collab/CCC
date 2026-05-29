"""Returns suggested rounding increments - does not select the final figure.

The engineer's reasoned judgement remains authoritative.
"""

from __future__ import annotations

import sys


def suggested_increment(value: float) -> int:
    if value < 2_000:
        return 50
    if value < 10_000:
        return 100
    if value < 30_000:
        return 250
    return 500


def rounded_options(value: float) -> dict[str, float | int]:
    increment = suggested_increment(value)
    lower = int(value // increment) * increment
    upper = lower if lower == value else lower + increment
    nearest = round(value / increment) * increment
    return {"increment": increment, "lower": lower, "nearest": nearest, "upper": upper}


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if len(argv) != 1:
        print("Usage: round_valuation.py <value>", file=sys.stderr)
        return 2
    options = rounded_options(float(argv[0].replace(",", "")))
    print(options)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

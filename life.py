#!/usr/bin/env python3
"""life.py -- Simulate the deployment of a human: Mohammad v1.0.0.

A fictional, birthday-themed toy project celebrating 2001-06-10.

This is a joke, not a real deployment. The project was written years later
and is presented purely as a birthday celebration.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

VERSION = "1.0.0"
BIRTH_DATE = "2001-06-10 00:00:00"

BOOT_STEPS: tuple[tuple[str, str], ...] = (
    ("Brain installed", "OK"),
    ("Curiosity enabled", "OK"),
    ("Documentation not found", "WARN"),
    ("Sleep schedule configuration missing", "WARN"),
)

JOKES: tuple[str, ...] = (
    "Life called fork(); now there are two responsibilities and no merge.",
    "My sleeping process runs in the background and ignores SIGTERM.",
    "I would tell you a UDP joke, but you might not get it.",
    "99 little bugs in the code, take one down, patch it around, 127 little bugs in the code.",
    "Production is a state of mind; so is 'it works on my machine'.",
    "I wanted to change the world, but the code freeze is still on.",
    "Segmentation fault (core dumped): that was me learning to walk.",
)


def _emit(lines: tuple[str, ...], pause: float) -> None:
    for line in lines:
        print(line)
        if pause:
            time.sleep(pause)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=f"Deploy a human, v{VERSION}.")
    parser.add_argument("--version", action="version", version=f"human {VERSION}")
    parser.add_argument(
        "--no-sleep",
        action="store_true",
        help="do not pause between boot steps (instant output)",
    )
    parser.add_argument(
        "--jokes",
        type=int,
        default=3,
        help="number of post-deploy jokes to print",
    )
    args = parser.parse_args(argv)

    pause = 0.0 if args.no_sleep else 0.15

    print(f"[{BIRTH_DATE}] Initializing human...")
    for message, level in BOOT_STEPS:
        print(f"[{level}] {message}")
        if pause:
            time.sleep(pause)

    print()
    print(f"Deploying Mohammad v{VERSION}...")
    if pause:
        time.sleep(pause)

    print()
    _emit(
        (
            "Hello, World!",
            "A new developer has entered the chat.",
            "",
            "Status: ALIVE",
            "Environment: PRODUCTION",
            "Expected uptime: Unknown",
            "Bugs: To be discovered...",
        ),
        pause,
    )

    print()
    print("Release notes (known issues & jokes):")
    rng = random.Random(BIRTH_DATE)  # deterministic: same birthday, same jokes
    selected = rng.sample(JOKES, k=min(max(args.jokes, 0), len(JOKES)))
    for joke in selected:
        print(f"  - {joke}")

    print()
    print("Deployment complete. Happy birthday, Mohammad.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

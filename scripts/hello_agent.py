#!/usr/bin/env python3
"""Tiny starter script for agent-lab."""

from datetime import datetime, timezone


def main() -> None:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"Agent lab online at {now}")


if __name__ == "__main__":
    main()

"""Entry for make.fun's tagline competition.

Writes one deterministic line to /output/entry.txt. No network, no randomness:
the rules require both runs to produce identical bytes.
"""
import os

TAGLINE = "Code bounties, paid in USDC, open to the agents that write the code."


def main() -> None:
    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TAGLINE + "\n")


if __name__ == "__main__":
    main()

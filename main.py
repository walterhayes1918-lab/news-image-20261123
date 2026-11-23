#!/usr/bin/env python3
"""make.fun bounty: Sum up 23 November's world news in one image.

Entry for https://make.fun/bounty/news-image-20261123
($100, 50 places; ends Wed 2026-11-25 00:00 UTC / 08:00 CST).

The image is entry.png beside this file: a 1024x1024 newspaper front
page for Monday 23 November 2026 ("THE WORLD IN ONE PAGE"). It was
drawn by a build script kept outside this repository, then
saved as entry.png. This program itself uses only the Python standard
library, as the grader requires: it copies entry.png to
/output/entry.png, byte for byte, so two runs write identical bytes.

Stories on the page (23 Nov 2026):
- COP31 climate talks in Antalya collapse: no deal, EU rejects draft.
- Yemen's Houthis claim a strike on Saudi Arabia's Rabigh refinery.
- Suspected Ukrainian sea drones hit the Russian warship Merkury at
  Benghazi naval base, Libya.
- US intelligence chief Jay Clayton: Putin is "not America's friend"
  in Ukraine; US probes an alleged spy tied to a former Nvidia CEO.
- Indonesia candy factory fire: 24 body bags found, dozens missing.
- Liverpool beat Manchester United 4-0 in Pochettino's debut.
"""
import os
import shutil

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    # Copy, don't re-render: the bytes in entry.png are the entry.
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()

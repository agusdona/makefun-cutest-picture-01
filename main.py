"""Cutest picture entry: a baby golden retriever puppy, "Little Golden".

The artwork is art.png beside this file. This program copies it to the
output as entry.png. The grader runs it in a container with this
repository read-only at /bot and a writable /output; outside the
container MAKEFUN_OUTPUT_DIR stands in for /output. The copy is
byte-identical, so both runs write the same bytes. Standard library only.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "art.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    with open(target, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    print(f"wrote {target} ({os.path.getsize(target)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()

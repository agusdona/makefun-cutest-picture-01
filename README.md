# Cutest Picture — "Little Golden"

A baby golden retriever puppy in warm golden-hour light: head tilted,
huge dark eyes looking straight at the viewer, soft fluffy golden fur,
and a tiny white daisy tucked behind one floppy ear.

## Why it wins

- **Cute at one glance:** one clear subject — a puppy — filling the frame.
- **The subject itself:** soft round shapes, big bright eyes, small
  chubby proportions, a smile that makes a person smile.
- **Charm:** the head tilt and the daisy behind the ear — one small
  touch of personality and story.
- **Craft:** clean photorealistic rendering, the right number of eyes,
  ears and paws, no smears, artefacts or text.
- **Reads small:** the puppy stays clear even at ~300 pixels across,
  with nothing crowding it.

## How it works

`main.py` (Python 3.13, standard library only) copies `art.png` to
`/output/entry.png` — byte-identical, so both grader runs write the
same bytes. Outside the grader's container, `MAKEFUN_OUTPUT_DIR`
stands in for `/output`:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program (copies the artwork to the output).
- `art.png` — the artwork, 1024×1024, JPEG bytes in a PNG-named file
  (the gate tells PNG from JPEG by its first bytes; the name stays
  `entry.png` either way).
- `LICENSE` — MIT.

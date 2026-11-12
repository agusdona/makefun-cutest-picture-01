# Little Ember

A baby red panda cub holding a daisy, in soft golden morning light with
a gentle bokeh background. A clean composition with direct eye contact
and a tender, touching moment — the universal baby schema: big eyes,
small paws, warm light.

The picture is held in this repository as `art.png` (1024x1024, under
1 MiB).

## How it works

`main.py` writes the artwork to `/output/entry.png`. It copies `art.png`
byte-for-byte, after checking that it is a PNG no bigger than 1 MiB and
no larger than 1024x1024, then prints the title, dimensions, size, and
SHA-256 of the written file. Two runs always write the same bytes.

## How to run

```sh
python3 main.py
```

Standard library only — no network, no randomness, no wall-clock use.

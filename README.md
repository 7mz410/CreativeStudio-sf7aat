<p align="center">
  <img alt="sf7aat" src="docs/studio/sf7aat.svg" width="140">
</p>

<h1 align="center">sf7aat</h1>

<p align="center">
  <b>Free, open-source PDF documents — part of the Creative Studio creative suite.</b><br>
  <b>ملفات PDF، مجاني ومفتوح المصدر — جزء من حزمة Creative Studio.</b>
</p>

<p align="center">
  <a href="https://studio.creative.ps/">studio.creative.ps</a>
</p>

<p align="center">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-555555">
  <img alt="Based on PdfCraft" src="https://img.shields.io/badge/based%20on-PdfCraft-943235">
</p>

## Built on PdfCraft

sf7aat is a fork of **[PdfCraft](https://github.com/storytold/pdfcraft)**, the
open-source, clean-room PDF application written in Rust by the
**[ArtCraft](https://getartcraft.com/)** team and the PdfCraft contributors. Almost everything
that makes this app work is their work. Thank you. If you like sf7aat, please star and
support the upstream project as well.

What we add: the Creative Studio identity, an Arabic interface laid out right to left (planned), and Arabic
features to come. Our changes are listed in [`studio/CHANGES.md`](studio/CHANGES.md).
Upstream's own README, with the full feature list and build instructions, is in
[`docs/UPSTREAM-README.md`](docs/UPSTREAM-README.md).

## The Creative Studio suite

| App | What it's for | Based on |
|---|---|---|
| [Creative Studio rsm](https://github.com/7mz410/CreativeStudio-rsm) | Vector illustration | VectorCraft |
| [Creative Studio ttshat](https://github.com/7mz410/CreativeStudio-ttshat) | Photo library and raw development | LightCraft |
| [Creative Studio tlween](https://github.com/7mz410/CreativeStudio-tlween) | Image editing | PhotoCraft |
| [Creative Studio tsweer](https://github.com/7mz410/CreativeStudio-tsweer) | Video editing | FilmCraft |
| [Creative Studio effectat](https://github.com/7mz410/CreativeStudio-effectat) | Motion graphics and effects | EffectCraft |
| **sf7aat** | PDF documents | PdfCraft |

More apps are on the way: see [studio.creative.ps](https://studio.creative.ps/).

## Building

```sh
cargo run --release -p pdfcraft
# after merging upstream:
git fetch upstream && git merge upstream/main && python3 studio/rebrand.py
```

## Licence

Code: MIT OR Apache-2.0 (`LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE`), like upstream. The Creative Studio
name and logos in `docs/studio/` belong to the Creative Studio project.

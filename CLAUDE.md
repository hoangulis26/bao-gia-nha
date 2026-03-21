# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

An interactive HTML quotation tool for interior renovation costs ("báo giá nội thất") for a family house. Two versions exist:

- **`index.html`** — Personal view (Nhà Anh Huy), with per-person cost splitting (÷3 shared floors)
- **`bao-gia-family.html`** — Family-facing view, same structure

Both are standalone single-file HTML apps using Tailwind CSS (CDN) and vanilla JS. No build step.

## Running Locally

```bash
npm start          # serves on http://localhost:3000 via npx serve
```
Or open either HTML file directly in a browser — no server needed for basic use.

## Code Architecture

Both HTML files are self-contained: CSS (`<style>`), HTML structure, and JavaScript (`<script>`) are all inline.

**Item state machine** — each `.item-row` element cycles through states via `cycleState(btn)`:
- `state-keep` (green) → `state-cut` (strikethrough) → `state-buy` (blue, negotiation mode) → back to keep
- `data-state`, `data-price`, `data-section`, `data-disc` attributes drive all calculations

**Discount system** — `.disc-pill` buttons appear only in `state-buy`. `setDisc(btn, pct)` stores discount on the row; `recalc()` applies it.

**`recalc()`** — the central function. Reads all `.item-row` elements, sums by `data-section`, updates total display spans by ID. Called on every toggle/discount interaction and on `DOMContentLoaded`.

**Sections** map to floor/room IDs: `phadot2` (T2 demolition, shared ÷3), `thot3`, `thot4` (WC rough work), `ng` (T4 bedroom furniture), `thietke` (design fee), etc.

**Lightbox** — `ẢNH RENDER PHƯƠNG ÁN/` folder contains render images; thumbnails in the HTML open a fullscreen lightbox.

## Regenerating `detail.html`

`detail_gen.py` generates `detail.html` programmatically using Python helper functions (`item_row`, `section_card`, etc.). Run:

```bash
python detail_gen.py
```

The script has a hardcoded absolute path — update `path` at line 4 if the directory moves.

## One-off Fix Scripts

`fix_index.py` is a one-off patch script (was used to fix `index.html`). It's safe to delete once its changes are confirmed in the HTML. Check git history if context is needed.

## Key Conventions

- All prices are in Vietnamese Dong (VND), formatted with `fmt_vnd()` / JS `fmt()` helpers
- Section IDs in `data-section` must match the `id` attributes on total `<span>` elements (e.g., `data-section="ng"` → `id="ng-total"`)
- The shared T2 floor cost is divided by 3 (`phadot2-share` span) — don't include it in per-person totals without dividing
- Vietnamese text in HTML is sometimes Unicode-escaped (`&#x1EEF;` etc.) — both forms work, but be consistent within a block

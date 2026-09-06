# The catalogue — `data/catalogue.json`

The fixed dataset every intern builds and benchmarks against. It is a **real building-materials
catalogue** (manhole covers, drainage, tree guards), sanitised: real product specs, representative
prices, **no brand identity**. The copilot answers about "a building-materials manufacturer".

## Shape

```json
{
  "_meta": { "source", "note", "branches": [...], "size_unit": "inch", "price_note": "representative" },
  "skus": [ { ...one product... }, ... ]     // 35 products
}
```

## A product record

| Field | Meaning | Example |
|---|---|---|
| `code` | product code (the SKU) | `"MHC 102"` |
| `category` | product family | `"square"`, `"round"`, `"rectangular"`, `"drain_cover"`, `"drain_ditch"`, `"tree_guard"` |
| `size` | nominal size (inches) | `"12x12"` |
| `load_ton` | load rating (tonnes) | `5` |
| `colours` | available colours | `["dark grey"]` |
| `handle` | handle material | `"SS304"` |
| `mrp` | representative price (INR) | `1200` |
| `image_ref` | product image path | `"products/manhole_square_grey.png"` |
| `frame_size_cm`, `cover_size_cm`, `frame_thickness_cm`, `cover_thickness_cm`, `weight_kg` | dimensions & weight | `"30 x 30"`, `"5.5"` |
| `extra_heavy` | present on the heavy-duty line | `true` |

## Facts you'll design around

- **35 SKUs**, 7 categories (`square` is the largest at 14).
- Prices **₹1,200 – ₹16,600**.
- **Not every field is on every record** — `extra_heavy` only on the heavy line; some dimensions
  vary. Your data handling must tolerate missing fields (this is real catalogue mess, not a bug).
- Sizes are strings (`"12x12"`), not numbers — normalising them is part of the `data` work.
- `branches` in `_meta` are the seven where stock is checked (the stock tool answers per branch).

## Why 35, when the business has 1000+

This clean 35-SKU set is your **thin-slice + gold-set** data (weeks 4–5). Reaching real scale is a
later, deliberate step: in Phase 2 the **ingestion pipeline** parses the fuller PDF catalogues into
this same shape — which is where flat search collapses and Reality Day happens. Start here; grow to
scale by building the pipeline, not by being handed a big file.

## The rule that never bends

An answer's every fact — a size, a price, a load rating — comes **from this file**, or the copilot
refuses. The `mrp` is representative; never present it as a live quote.

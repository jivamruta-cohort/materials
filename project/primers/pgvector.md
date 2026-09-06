# Primer — pgvector (T3, Sprint 2)

`pgvector` is a Postgres extension that stores vectors (lists of numbers) in a column and finds the
nearest ones fast. That's all retrieval needs: put each product's embedding in a column, then ask
"which rows are closest to this query vector."

## The three things you need

**1 · Enable it, add a vector column**
```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE products (
  code      text PRIMARY KEY,
  name      text,
  category  text,
  mrp       int,
  embedding vector(384)      -- the embedding dimension your model produces
);
```

**2 · Insert a row with its embedding**
```python
# embedding is a list[float] of length 384 from your embedder
cur.execute(
    "INSERT INTO products (code, name, category, mrp, embedding) VALUES (%s,%s,%s,%s,%s)",
    (p["code"], p["name"], p["category"], p["mrp"], embedding),
)
```

**3 · Find the nearest (this is retrieval)**
```sql
SELECT code, name, embedding <=> %s AS distance   -- <=> is cosine distance
FROM products
ORDER BY distance
LIMIT 5;
```
Smaller distance = closer. That query, with the query's embedding bound in, *is* dense retrieval.

## Make it fast (when you have many rows)
```sql
CREATE INDEX ON products USING hnsw (embedding vector_cosine_ops);
```
An HNSW index turns the search from "scan every row" into "jump to the neighbourhood." You won't
need it at 35 SKUs; you will when the ingestion pipeline loads the full catalogue.

## Watch for
- **Dimension must match your embedder.** `vector(384)` but a 768-dim embedding → error. Pin one.
- **Distance operators**: `<=>` cosine, `<->` L2, `<#>` inner product. Use cosine for text/CLIP
  embeddings (that's what they're normalised for).
- **Embed at ingestion, not per query.** Store the vector once; only the query is embedded live.

## Your task uses this for
`ProductKB` on pgvector, and the dense leg of hybrid retrieval. Structured-first still comes first
(P0 #2) — pgvector is the *fallback* that catches what exact field-matching misses.

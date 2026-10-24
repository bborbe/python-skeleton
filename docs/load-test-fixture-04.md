# Cache Invalidation

The result cache is keyed by request parameters and invalidated on write.

## Key

The key is the SHA-256 of the canonical JSON of the request parameters. Key
ordering is normalised, so two dicts with the same content produce the same
key. Floats are serialised with repr, which means 0.1 and 0.10 differ — this is
intentional and documented.

## Invalidation

Writes invalidate every key whose first component matches the affected entity.
This is a prefix scan over the cache, which is O(n) in the number of cached
entries. With the current cache size of roughly 50k entries a single write
invalidates in about 40 ms.

## TTL

Entries also expire after 15 minutes. The TTL is not refreshed on read, so a
hot key expires while it is still being served, causing a thundering herd at
expiry time.

## Metrics

Two counters are exported: `cache_hit_total` and `cache_miss_total`. There is no
counter for invalidations, so the cost of the prefix scan cannot be measured in
production.

## Decision

Keep the prefix scan. A per-entity index was prototyped and removed because it
doubled the memory footprint, and invalidation latency was not the bottleneck.

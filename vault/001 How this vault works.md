---
id: "001"
title: "How this vault works"
tags: [kinovea, type/meta]
---

# How this vault works

This vault is a Zettelkasten built from the Kinovea reference manual (source: github.com/Kinovea/kinovea-docs @ `375e293`) plus an API and integration reference compiled from the Kinovea source code (github.com/Kinovea/Kinovea @ `13d0236`).

## Note IDs (Folgezettel)

Every note has an ID that encodes its position in the tree, alternating numbers and letters:

| ID | Level | Example |
|---|---|---|
| `5` | Part (structure note) | [[5 Measurement]] |
| `5c` | Chapter (structure note, or an atomic note if it has no sub-notes) | [[5c Lens distortion calibration]] |
| `5c2` | Atomic note: one topic | a section of that chapter |

IDs never change, so links stay stable. To add your own note *between* or *under* existing ones, branch the ID: a note continuing `5c2` becomes `5c2a`, the next one `5c2b`, and so on.

## Note types (tag `type/…`)

- `type/structure` — the [[000 Kinovea Index]], part notes and chapter notes. They hold the hierarchy and link down to their children with a one-line summary.
- `type/permanent` — atomic notes with the actual content.
- `source/code-derived` — notes from the API part, written from the Kinovea source code rather than the official manual. Where the two disagree, the code is what actually runs.

## Status tags: read these before trusting a note

The official manual is a 2025 rewrite that is still in progress (kinovea-docs @ `375e293`, latest commit "wip glossary and other pages"). The vault marks its gaps instead of hiding them:

- `status/stub` — 23 notes that are **empty or outline-only in the official manual**, including 7 of the 8 Tracking chapters. Each carries a warning callout and, where possible, links to related notes that do cover the topic. Search `tag:#status/stub` to list them.
- `status/obsolete` — 9 notes from the **previous** manual's tracking pages ([[15 Legacy documentation (obsolete)]]). No longer linked from the official docs and possibly outdated, but the only written coverage of tracking until the stubs are filled.

Three images referenced by the official manual were never committed to its repository; they appear as their alt text (e.g. `[Record]`).

## Navigation

- Frontmatter `up:` and the footer line give **⬆ parent**, **⬅ previous** and **➡ next** sibling, so you can read a chapter in sequence.
- Cross-references from the manual are converted to `[[wikilinks]]`; open the **Backlinks** pane to see every note that points to the current one.
- Use **Graph view** filtered by `tag:#kinovea/<part>` to see one part's cluster.
- Images live in `_attachments/` and are embedded with `![[…]]`.

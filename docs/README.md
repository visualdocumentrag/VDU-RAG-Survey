# The website

`index.html` reads `groups.json` and `../data/screened_pool.csv` at load
time. Nothing is hard-coded, so adding a paper touches two files and
never the HTML.

## Adding a paper

1. Add a row to `data/screened_pool.csv`
2. Put its `key` in the right group in `docs/groups.json`

That is all. The counts at the top, the tables, the search and the
filter chips all follow.

## Adding a section

Append to `sections` in `groups.json`:

```json
{
  "id": "short-id",
  "title": "Section heading",
  "short": "Chip label",
  "note": "One line under the heading.",
  "groups": [
    { "title": "Subsection",
      "finding": "A claim in bold, if the group makes one.",
      "keys": ["key1", "key2"] }
  ]
}
```

`finding` is the field that matters. A list of papers tells a reader
what exists; the finding line tells them what it means, and it is what
someone scrolling will remember.

## Publishing

GitHub → **Settings → Pages** → Source: *Deploy from a branch* →
branch `main`, folder `/docs`. Live in about a minute at
`https://anon-repo.github.io/VDU-RAG-Survey/`.

## Previewing locally

Opening `index.html` by double-clicking will not work: browsers block
`fetch` on `file://` URLs. Run a server from the repository root:

```powershell
python -m http.server
```

Then visit `http://localhost:8000/docs/`.

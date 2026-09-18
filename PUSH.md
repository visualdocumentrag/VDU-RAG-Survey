# Posting this, step by step

## 1 · Make the repository

<https://github.com/new>, signed in to the **anonymous account**, not
your own.

| Field | Value |
|---|---|
| Name | `VDU-RAG-Survey` |
| Description | Paper list and released record for a survey of retrieval-augmented visual document understanding |
| Visibility | **Public** |
| Add a README | **off** |
| .gitignore | **None** |
| Licence | **None** |

All three of those are already in this folder. Adding them at creation
makes the first push fail for unrelated histories.

## 2 · Upload

**Add file → Upload files.** Open this folder, select **everything
inside it** — the loose files and the `data/`, `docs/` and `.github/`
folders together — and drag them in. GitHub keeps the structure.

Commit message: `Paper list and released record`

If `.github` does not appear in your file manager, enable hidden files.
It carries the issue templates, so the ➕ buttons will not work without
it.

### With Git instead

```
cd path/to/this/folder
git init
git config user.name  "Anonymous"
git config user.email "anon@example.com"
git add .
git commit -m "Paper list and released record"
git branch -M main
git remote add origin https://github.com/ANON-REPO/VDU-RAG-Survey.git
git push -u origin main
```

The two `git config` lines matter. Without them every commit carries
your real name and email, and `git log` is public.

## 3 · Turn on the site

**Settings → Pages → Source: Deploy from a branch → Branch `main`,
folder `/docs` → Save.**

Live in about a minute. If it 404s, check that `docs/index.html`
uploaded and that the folder is `/docs` rather than `/root`.

## 4 · Settings

**About** (the gear, top right of the repo page):

- Website: the Pages URL
- Topics: `survey` `document-understanding`
  `retrieval-augmented-generation` `multimodal-retrieval` `document-ai`
  `ocr` `awesome-list`

**Issues** must be on, or the ➕ buttons go nowhere. Settings →
General → Features → Issues.

## 5 · Check the ➕ works

Open `../../issues/new?template=add-paper.yml` on the live repo. You
should see the form, not a blank issue box. If it is blank, `.github`
did not upload.

---

## Adding papers later

```
python3 scripts/add_paper.py
```

It asks for title, authors, venue, year, identifier and section,
appends the row, and rebuilds both the README list and the site. Or
edit `data/references.csv` by hand and run `python3
scripts/rebuild.py`.

The site and the README are both generated from that one CSV, so they
cannot drift apart.

---

Delete this file once you have posted.

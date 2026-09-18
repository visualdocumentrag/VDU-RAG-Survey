# Reading this repository during review

This is the anonymised copy that accompanies a double-blind submission.
Author names, affiliations and ORCIDs have been removed; the record
itself is complete and unaltered.

---

## For reviewers

Everything the paper points at is here. The paper is bound by a
twenty-page limit, so its tables are compact versions; the full ones are
in the `data/` folder, each named in the paper at the point you would look
for it.

Nothing has been withheld to make the paper look better. Where a value
is unverified it is marked, where a table row is unfilled it is listed
by name, and where a claim rests on our own annotation rather than on a
published source, the text says so.

---

## For the author, before posting this

**1. A fresh account with no history.** GitHub shows the owner on every
page, and a handle that appears anywhere else is enough to identify you.

**2. No commit history.** Git records an author name and email on every
commit. Either upload through the browser — *Add file → Upload files*,
which attributes to the account only — or set a throwaway identity
before the first commit:

```
git config user.name "Anonymous"
git config user.email "anon@example.com"
```

**3. Read the rendered site, not just the files.** Open the Pages URL
and check the header, the citation block and the footer with fresh eyes.

**4. Four places must carry the same URL:** the abstract, Sec. III-E,
the title page comment, and the cover letter. Use the anonymous
repository, or a mirror at <https://anonymous.4open.science> pointing at
it — the mirror hides the URL, but not the contents, so the repository
itself still has to be clean.

---

## One thing that is not a leak

`data/references.csv` and `data/screened_pool.csv` carry the author
names of the **286 cited papers**, and one of those surnames matches a
co-author of this survey. That is a bibliography, not an identity leak:
every survey of this area cites its senior figures, and removing them
would make the record useless and the omission itself conspicuous.

The right response is not to redact. It is one line in the cover letter
noting that a co-author appears in the reference list, which is normal
and which the editor can weigh.

---

## After acceptance

Restore `CITATION.cff`, put the real names back in the citation block,
and add the LaTeX source and the compiled PDF. Not before: the source
carries author names in `front/titlepage.tex`.

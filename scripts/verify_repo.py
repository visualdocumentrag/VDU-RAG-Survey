"""Re-run the release checks of this repository.
Usage:  python scripts/verify_repo.py            (offline checks)
        python scripts/verify_repo.py --online   (also opens every GitHub code link)"""
import re, os, glob, sys, collections, urllib.parse, urllib.request
import pandas as pd
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ok = lambda c, m: print(('PASS ' if c else 'FAIL ') + m) or c
res = []
# 1. bibliography vs references table
bib = re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', open('data/vdu_rag.bib', encoding='utf-8').read())
ref = pd.read_csv('data/references.csv')
res.append(ok(len(bib) == len(set(bib)), f'no duplicate BibTeX keys ({len(bib)} entries)'))
res.append(ok(set(ref.BibKey) <= set(bib), f'all {len(ref)} references have a BibTeX entry'))
res.append(ok(ref.BibKey.is_unique and ref.Title.str.lower().is_unique, 'no duplicate reference keys or titles'))
res.append(ok(ref.Link.notna().all(), 'every reference has a link'))
n_c = (ref.CitedInPaper == 'yes').sum()
res.append(ok(n_c == 217 and len(ref) - n_c == 74, f'{n_c} cited in the paper, {len(ref)-n_c} not included (expected 217 / 74)'))
# 2. methods and datasets point to references
m = pd.read_csv('data/methods.csv'); d = pd.read_csv('data/datasets.csv')
res.append(ok(len(m) == 73 and set(m.BibKey.dropna()) <= set(ref.BibKey), f'{len(m)} methods, all linked to a reference'))
res.append(ok(len(d) == 61 and set(d.BibKey.dropna()) <= set(ref.BibKey), f'{len(d)} benchmarks, all linked to a reference'))
# 3. venue lists
idx = pd.read_csv('data/venues/index.csv'); bad = []
for v in idx.ID:
    a = pd.read_csv(f'data/venues/all/{v}.csv'); r = pd.read_csv(f'data/venues/related/{v}.csv')
    if len(a) != idx.set_index('ID').Records[v]: bad.append(f'{v}: count')
    if a.Title.str.lower().duplicated().any(): bad.append(f'{v}: duplicate title')
    if not r.Title.str.lower().isin(set(a.Title.str.lower())).all(): bad.append(f'{v}: related not in complete list')
    if len(r) != int(idx.set_index('ID').Related_list[v]): bad.append(f'{v}: related count')
res.append(ok(not bad, f'{len(idx)} venue-year lists: counts, duplicates, related subset of complete ({idx.Records.sum():,} papers, {int(idx.Related_list.sum()):,} related)' + (' ' + str(bad) if bad else '')))
# 4. every title in the complete-list pages is a link
unl = 0; rows = 0
for f in glob.glob('pages/lists/*.md'):
    for l in open(f, encoding='utf-8'):
        if re.match(r'\| \d+ \|', l):
            rows += 1; unl += not re.match(r'\| \d+ \| \[', l)
res.append(ok(unl == 0 and rows == idx.Records.sum(), f'{rows:,} rows in the complete-list pages, {unl} without a link'))
# 5. relative links and anchors in every Markdown file
def anchors(f):
    s = open(f, encoding='utf-8').read(); a = set()
    for h in re.findall(r'^#+\s+(.*)$', s, re.M):
        t = re.sub(r'[^\w\- ]', '', h.strip().lower()).replace(' ', '-'); a.add(t)
    return a
broken = []; urls = set(); mds = glob.glob('**/*.md', recursive=True)
for f in mds:
    for mt in re.finditer(r'\]\(([^)\s]+)\)|src="([^"]+)"', open(f, encoding='utf-8').read()):
        u = mt.group(1) or mt.group(2)
        if u.startswith('http'): urls.add(u); continue
        p, _, an = u.partition('#'); t = os.path.normpath(os.path.join(os.path.dirname(f), p)) if p else f
        if not os.path.exists(t): broken.append((f, u))
        elif an and t.endswith('.md') and an not in anchors(t): broken.append((f, u))
res.append(ok(not broken, f'{len(mds)} Markdown files: every relative link and anchor resolves' + (' ' + str(broken[:5]) if broken else '')))
res.append(ok(all(' ' not in u for u in urls), f'{len(urls):,} external URLs well-formed'))
# 6. optional: GitHub links
if '--online' in sys.argv:
    gh = sorted({re.sub(r'[#?].*', '', u).rstrip('/') for u in urls if urllib.parse.urlparse(u).netloc == 'github.com'})
    dead = []
    for u in gh:
        try: urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=20)
        except Exception as e: dead.append((u, str(e)[:40]))
    res.append(ok(not dead, f'{len(gh)} GitHub code links open' + (' ' + str(dead) if dead else '')))
print(f'\n{sum(res)}/{len(res)} checks passed')

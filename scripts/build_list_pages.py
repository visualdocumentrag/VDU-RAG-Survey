"""Rebuild pages/lists/<VenueYear>_pN.md from data/venues/all/<VenueYear>.csv.
Every title is a clickable link; extra links (PDF, arXiv, code, OpenReview, DOI) get their own column.
Where a venue publishes no per-paper URL (BMVC), the title links to an arXiv title search and a
Google Scholar search is added, both labelled as searches."""
import pandas as pd, glob, os, urllib.parse, math
PER = 500
NAMES = {'PatternRecognition':'Pattern Recognition','ICCVW':'ICCV Workshops'}
def esc(s): return str(s).replace('|','\\|').replace('\n',' ').strip()
def ok(v): return isinstance(v,str) and v.startswith('http')
for f in sorted(glob.glob('data/venues/all/*.csv')):
    vid = os.path.basename(f)[:-4]; ven, yr = vid[:-4], vid[-4:]
    d = pd.read_csv(f); n = len(d); parts = math.ceil(n/PER)
    info = [c for c in ['Track','Decision','Kind','Part','Section','Volume','Vol_Issue','Issue','Workshop','Topics'] if c in d.columns]
    for p in range(parts):
        rows = d.iloc[p*PER:(p+1)*PER]
        nav = ' · '.join(f'**{i+1}**' if i==p else f'[{i+1}]({vid}_p{i+1}.md)' for i in range(parts))
        out = [f'# {NAMES.get(ven,ven)} {yr}: complete list (part {p+1} of {parts})', '',
               f'Papers {p*PER+1}-{min(n,(p+1)*PER)} of {n:,}. Parts: {nav}. '
               f'[Venue page](../venues/{vid}.md) · [CSV](../../data/venues/all/{vid}.csv) · [All venues](../../README.md#venues)', '']
        if ven=='BMVC': out += ['> BMVC publishes no stable per-paper URL in its title list, so each title opens an **arXiv title search** and *Scholar* opens a Google Scholar search.', '']
        out += ['| # | Title | Authors | '+(' / '.join(info) if info else 'Info')+' | Type | Links |', '|---:|---|---|---|---|---|']
        for k,(_,r) in enumerate(rows.iterrows()):
            t = esc(r['Title']); q = urllib.parse.quote_plus(str(r['Title']))
            main = next((r[c] for c in ['Paper_Link','Springer_Link','PDF_Link','arXiv_Link','OpenReview'] if c in d.columns and ok(r[c])), None)
            links = []
            for c,lab in [('PDF_Link','PDF'),('arXiv_Link','arXiv'),('OpenReview','OpenReview'),('Code_Link','Code')]:
                if c in d.columns and ok(r[c]) and r[c]!=main: links.append(f'[{lab}]({r[c]})')
            if 'DOI' in d.columns and isinstance(r['DOI'],str) and r['DOI'].strip():
                doi=r['DOI'].strip(); u=doi if doi.startswith('http') else 'https://doi.org/'+doi
                if u!=main: links.append(f'[DOI]({u})')
            if main is None:
                main = r['arXiv_Search'] if 'arXiv_Search' in d.columns and ok(r['arXiv_Search']) else f'https://arxiv.org/search/?searchtype=title&query={q}'
                sch = r['Scholar_Search'] if 'Scholar_Search' in d.columns and ok(r['Scholar_Search']) else f'https://scholar.google.com/scholar?q=%22{q}%22'
                links.append(f'[Scholar]({sch})')
            elif 'Scholar_Search' in d.columns and ok(r['Scholar_Search']): links.append(f"[Scholar]({r['Scholar_Search']})")
            au = esc(r['Authors']) if 'Authors' in d.columns and isinstance(r['Authors'],str) else '-'
            inf = ', '.join(esc(r[c]) for c in info if isinstance(r[c],(str,int,float)) and str(r[c])!='nan') or '-'
            out.append(f"| {p*PER+k+1} | [{t}]({main}) | {au} | {inf} | {esc(r['Type'])} | {' · '.join(links) or '-'} |")
        out += ['', f'[Back to the venue list](../../README.md#venues)', '']
        open(f'pages/lists/{vid}_p{p+1}.md','w',encoding='utf-8').write('\n'.join(out))
    print(vid, n, parts)

"""Rebuild data/methods.md and pages/methods.md from data/methods.csv, in the venue order of paper Tables 4-5."""
import pandas as pd
m=pd.read_csv('data/methods.csv',dtype=str,keep_default_na=False)
ref=pd.read_csv('data/references.csv'); L=dict(zip(ref.BibKey,ref.Link))
def lk(t,u): return f'[{t}]({u})' if u else ''
# data/methods.md
cols=['No','Family','Method','Venue','Year','Objective','Index_Unit','Benchmarks','Contribution','Paper_Link_in_paper','Code','BibKey','Added_2025_2026']
o=['# Methods (73)','','All methods tracked in the survey. The method name links to the paper page; *Link in paper* is the link printed in paper Tables 4-5. Objective, Index / Unit and Benchmarks use the wording of the paper.','','Raw file: [`methods.csv`](methods.csv) · [Back to README](../README.md#visual-document-rag-methods)','','|'+'|'.join(c.replace('_',' ') for c in cols)+'|','|'+'---|'*len(cols)]
for _,x in m.iterrows():
    v=[]
    for c in cols:
        if c=='Method': v.append(lk(x.Method,L.get(x.BibKey,'')) or x.Method)
        elif c=='Code': v.append(lk('code',x.Code))
        elif c=='Paper_Link_in_paper': v.append(lk('link',x[c]))
        else: v.append(x[c].replace('|','/'))
    o.append('|'+'|'.join(v)+'|')
open('data/methods.md','w',encoding='utf-8').write('\n'.join(o)+'\n')
# pages/methods.md grouped by the venue column of the paper
o=['# Methods (73)','','[Paper Table 4 (HD)](figures_tables.md#table-4) · [Table 5 (HD)](figures_tables.md#table-5)','','All visual document RAG methods tracked by the survey, grouped and ordered by venue exactly as in paper Tables 4-5. Cut-off: 24 September 2026.','',
'*Objective*: what the method optimizes. *Index / Unit*: vectors stored per unit and what is returned. *Datasets*: benchmarks named at least three times in the paper\'s full text (or its abstract); the paper shows at most four and "+n" for the rest. **new** = added from the 2025-2026 venue lists. *Paper* opens the paper page; *link in paper* is the link printed in the paper table. Source: [`data/methods.csv`](../data/methods.csv).','',
'[Back to README](../README.md#visual-document-rag-methods)','']
for ven,g in m.groupby('Paper_Venue',sort=False):
    o+=[f'## {ven}','','|Method|Year|Objective|Index / Unit|Datasets evaluated on|Contribution|Paper|Code|','|---|---|---|---|---|---|---|---|']
    for _,x in g.iterrows():
        pl=' · '.join(t for t in [lk('paper',L.get(x.BibKey,'')), lk('link in paper',x.Paper_Link_in_paper) if x.Paper_Link_in_paper and x.Paper_Link_in_paper!=L.get(x.BibKey) else ''] if t)
        o.append(f"|{x.Method}{' **new**' if x.Added_2025_2026=='yes' else ''}|{x.Year}|{x.Objective}|{x.Index_Unit}|{x.Benchmarks}|{x.Contribution}|{pl}|{lk('code',x.Code)}|")
    o.append('')
open('pages/methods.md','w',encoding='utf-8').write('\n'.join(o))
print('ok')

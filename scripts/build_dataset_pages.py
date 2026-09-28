"""Rebuild the dataset tables (README, pages/datasets.md section 1, data/datasets.md) from data/datasets.csv.
The 25 channel-audited benchmarks carry exactly the values of paper Table 8."""
import pandas as pd, re
d=pd.read_csv('data/datasets.csv',dtype=str,keep_default_na=False)
ref=pd.read_csv('data/references.csv'); L=dict(zip(ref.BibKey,ref.Link))
CH=['Text','Layout','Tables','Figures','Equations','Forms','Stamps','Typography']; AB=['Txt','Lay','Tab','Fig','Eqn','Frm','Stp','Typ']
sym={'annotated':'●','present':'○','absent':'–','':''}
def cell(v): return v if v else ' '
t8=d[d.Source_table=='Paper Table 8']
# pages/datasets.md section 1
hdr='|Task|Dataset|Venue|Year|Lang.|Scope|Size|Queries|Metric|'+'|'.join(CH)+'|Public|Paper|Link|'
rows=[hdr,'|'+'---|'*(len(hdr.split('|'))-2)]
for _,x in t8.iterrows():
    rows.append(f"|{x.Group}|{x.Dataset}|{x.Venue}|{x.Year}|{x.Language}|{x.Scope}|{cell(x.Size)}|{cell(x.Queries)}|{cell(x.Metric)}|"+'|'.join(sym[x[c]] for c in CH)+f"|{x.Public}|[paper]({L[x.BibKey]})|[link]({x.Link})|")
p=open('pages/datasets.md',encoding='utf-8').read()
a=p.index('## 1.'); b=p.index('## 2.')
sec=('## 1. Channel coverage of key benchmarks (paper Table 8)\n\nValues are those of paper Table 8. ● annotated, ○ present but not annotated, – absent. Scope: ML multilingual, MD multi-domain, MT multi-type, MM multi-modality, MA multi-agent. "-" in Size or Queries: not applicable; ∼: the authors report only an approximate count.\n\n'+'\n'.join(rows)+'\n\n')
open('pages/datasets.md','w',encoding='utf-8').write(p[:a]+sec+p[b:])
# data/datasets.md
cols=['Group','Dataset','Venue','Year','Language','Scope','Size','Queries','Metric']+CH+['Public','Link','BibKey','Source_table','Focus']
out=['# Datasets and benchmarks (61)','','The dataset name links to the paper; the Link column goes to the data or code. The 25 rows marked *Paper Table 8* carry the values of paper Table 8.','','Raw file: [`datasets.csv`](datasets.csv) · [Back to README](../README.md#datasets)','','|'+'|'.join(cols)+'|','|'+'---|'*len(cols)]
for _,x in d.iterrows():
    v=[]
    for c in cols:
        if c=='Dataset': v.append(f'[{x.Dataset}]({L[x.BibKey]})' if x.BibKey in L else x.Dataset)
        elif c=='Link': v.append(f'[Link]({x.Link})' if x.Link else '')
        else: v.append(str(x[c]).replace('|','/'))
    out.append('|'+'|'.join(v)+'|')
open('data/datasets.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
# README three tables
r=open('README.md',encoding='utf-8').read()
for grp,head in [('Retrieval & RAG','#### Retrieval and RAG Benchmarks'),('Document QA','#### Document QA Benchmarks'),('Channel-specific','#### Channel-specific Datasets')]:
    tb=['|Dataset|Venue|Year|Size|Queries|Language|Channels annotated|Evaluation Metric|Link|','|---|:-:|:-:|:-:|:-:|:-:|---|:-:|:-:|']
    for _,x in t8[t8.Group==grp].iterrows():
        ann=', '.join(ab for c,ab in zip(CH,AB) if x[c]=='annotated') or '-'
        tb.append(f"|[{x.Dataset}]({L[x.BibKey]})|{x.Venue}|{x.Year}|{x.Size or '-'}|{x.Queries or '-'}|{x.Language}|{ann}|{x.Metric or '-'}|[link]({x.Link})|")
    i=r.index(head); j=r.index('\n\n',r.index('|',i))
    r=r[:i]+head+'\n\n'+'\n'.join(tb)+r[j:]
open('README.md','w',encoding='utf-8').write(r)
print('ok',len(t8))

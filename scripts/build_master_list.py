"""Build supplementary/Master_List.pdf: every work of the survey, all clickable."""
import pandas as pd, glob, os, urllib.parse
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from xml.sax.saxutils import escape
ss=getSampleStyleSheet()
H1=ParagraphStyle('h1',parent=ss['Heading1'],fontSize=15,spaceAfter=6)
H2=ParagraphStyle('h2',parent=ss['Heading2'],fontSize=11.5,spaceBefore=8,spaceAfter=4)
B=ParagraphStyle('b',parent=ss['BodyText'],fontSize=8.6,leading=10.5)
C=ParagraphStyle('c',parent=B,fontSize=7.4,leading=9)
PINK='#E4007F'
def L(text,url): 
    t=escape(str(text))
    return f'<link href="{escape(url)}" color="{PINK}">{t}</link>' if isinstance(url,str) and url.startswith('http') else t
def P(x,st=C): return Paragraph(x,st)
def tbl(head,rows,widths):
    data=[[P(f'<b>{h}</b>') for h in head]]+[[c if isinstance(c,Paragraph) else P(escape(str(c)) if str(c)!='nan' else '') for c in r] for r in rows]
    t=Table(data,colWidths=widths,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.25,colors.grey),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E8EEF3')),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F7F9FB')])]))
    return t
W=landscape(A4)[0]-2*1.4*cm
ref=pd.read_csv('data/references.csv'); meth=pd.read_csv('data/methods.csv'); ds=pd.read_csv('data/datasets.csv'); idx=pd.read_csv('data/venues/index.csv')
link_of=dict(zip(ref.BibKey,ref.Link))
REPO='https://github.com/visualdocumentrag/VDU-RAG-Survey'
st=[P('Channel-Aware Visual Document Understanding with RAG: A Survey',H1),
P(f'Master list of every work in the survey and its release. Authors: TBD. Under review at IEEE TPAMI. Literature cut-off: <b>24 September 2026</b>. Repository: {L(REPO,REPO)}. Every title in this PDF is a clickable link (pink). A small number of older works without a stable URL open a Google Scholar search; BMVC titles, and ICDAR 2026 titles without a Springer page, open an arXiv title search.',B),Spacer(1,6),
P('Contents: A. The 217 works cited in the paper · B. The 74 works not included in the paper (page limit) · C. The 73 methods · D. The 61 benchmarks · E. The 42 venue-year lists (counts) · F. The 2,014 related papers of every venue-year, in the venue order of the README.',B),
]
for tag,title,sub in [('A','A. Works cited in the paper',ref[ref.CitedInPaper=='yes']),('B','B. Works not included in the paper (page limit)',ref[ref.CitedInPaper!='yes'])]:
    sub=sub.sort_values('Title',key=lambda s:s.str.lower())
    st+=([PageBreak()] if tag!='A' else [Spacer(1,6)])+[P(f'{title} ({len(sub)})',H2)]
    st.append(tbl(['#','Title (click to open)','Authors','Venue','Year','Link'],[[i,P(L(x.Title,x.Link)),P(escape(str(x.Authors))[:160]),P(escape(str(x.Venue))),x.Year,x.LinkType] for i,x in enumerate(sub.itertuples(),1)],[W*.04,W*.36,W*.25,W*.2,W*.05,W*.1]))
st+=[PageBreak(),P(f'C. The {len(meth)} methods (paper Tables 4-5)',H2)]
st.append(tbl(['#','Method (paper)','Family','Venue','Objective','Index / unit','Benchmarks','Code'],[[x.No,P(L(x.Method,link_of.get(x.BibKey))),P(escape(str(x.Family))),f'{x.Paper_Venue} {x.Year}',P(escape(str(x.Objective))),P(escape(str(x.Index_Unit))),P(escape(str(x.Benchmarks))),P(L('code',x.Code) if isinstance(x.Code,str) else '-')] for x in meth.itertuples()],[W*.04,W*.14,W*.17,W*.08,W*.12,W*.12,W*.25,W*.08]))
st+=[PageBreak(),P(f'D. The {len(ds)} benchmarks (paper Table 8 and Sec. 10)',H2)]
chans=['Text','Layout','Tables','Figures','Equations','Forms','Stamps','Typography']
st.append(tbl(['#','Dataset','Group','Year','Language','Metric','Channels annotated','Paper','Project'],[[i,P(escape(str(x.Dataset))),P(escape(str(x.Group))),x.Year,P(escape(str(x.Language))),P(escape(str(x.Metric))),P(', '.join(c for c in chans if str(getattr(x,c))=='annotated') or '-'),P(L('paper',link_of.get(x.BibKey)) if link_of.get(x.BibKey) else '-'),P(L('project',x.Link) if isinstance(x.Link,str) else '-')] for i,x in enumerate(ds.itertuples(),1)],[W*.04,W*.14,W*.13,W*.05,W*.08,W*.1,W*.26,W*.09,W*.11]))
order=['TPAMI','CVPR','ECCV','ICCV','ICCVW','ICDAR','AAAI','WACV','BMVC','ACCV','PatternRecognition','CVIU','IJCV','NeurIPS','EMNLP','JMLR','ACL','EACL','ICLR','ICML','KDD','IJCAI','ICPR','SIGIR','IJDAR','arXiv']
idx['o']=idx.Venue.map(order.index); idx=idx.sort_values(['o','Year'],ascending=[True,False])
st+=[PageBreak(),P('E. The 42 venue-year lists',H2),P('Venues not held or not yet published at the cut-off: ECCV 2025, ICCV 2026, ACCV 2025 (biennial); ACCV 2026, NeurIPS 2026, EMNLP 2026, CIKM 2026 (after the cut-off); ICPR 2025 (biennial); KDD 2025 and IJCAI 2025 not collected in this release.',B),Spacer(1,4)]
st.append(tbl(['Venue','Year','Type','Papers screened','Related'],[[x.Venue.replace('PatternRecognition','Pattern Recognition').replace('ICCVW','ICCV Workshops'),x.Year,x.Type,f'{x.Records:,}',int(x.Related_list)] for x in idx.itertuples()]+[['Total','','',f'{idx.Records.sum():,}',int(idx.Related_list.sum())]],[W*.3,W*.1,W*.2,W*.2,W*.2]))
st+=[PageBreak(),P('F. Related papers of every venue-year (kept after title/abstract screening)',H2)]
for x in idx.itertuples():
    r=pd.read_csv(f'data/venues/related/{x.ID}.csv')
    lc=next(c for c in ['Paper_Link','Springer_Link','Scholar_Search','arXiv_Search'] if c in r.columns)
    rows=[]
    for i,y in enumerate(r.itertuples(),1):
        u=getattr(y,lc)
        if not (isinstance(u,str) and u.startswith('http')):
            for c in ['Scholar_Search','arXiv_Search']:
                if c in r.columns and isinstance(getattr(y,c),str): u=getattr(y,c);break
            else: u='https://arxiv.org/search/?searchtype=title&query='+urllib.parse.quote_plus(y.Title)
        au=getattr(y,'Authors','') if 'Authors' in r.columns else ''
        rows.append([i,P(L(y.Title,u)),P(escape(str(au) if str(au)!='nan' else '')[:150]),P(escape(str(getattr(y,'Category',''))))])
    name=x.Venue.replace('PatternRecognition','Pattern Recognition').replace('ICCVW','ICCV Workshops')
    st+=[P(f'{name} {x.Year} ({len(r)} related of {x.Records:,})',H2),tbl(['#','Title (click to open)','Authors','Group'],rows,[W*.04,W*.5,W*.3,W*.16])]
def foot(c,d):
    c.saveState(); c.setFont('Helvetica',7); c.drawString(1.4*cm,0.8*cm,'VDU-RAG Survey master list · cut-off 24 September 2026 · authors TBD'); c.drawRightString(landscape(A4)[0]-1.4*cm,0.8*cm,f'page {d.page}'); c.restoreState()
doc=SimpleDocTemplate('supplementary/Master_List.pdf',pagesize=landscape(A4),leftMargin=1.4*cm,rightMargin=1.4*cm,topMargin=1.2*cm,bottomMargin=1.3*cm,title='VDU-RAG Survey: master list',author='TBD')
doc.build(st,onFirstPage=foot,onLaterPages=foot)
print('ok')

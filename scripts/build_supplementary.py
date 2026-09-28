"""Build supplementary/Supplementary_Lists.pdf: the details that do not fit in the paper, all clickable."""
import pandas as pd, re
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
C=ParagraphStyle('c',parent=B,fontSize=7.2,leading=8.8)
PINK='#E4007F'; TITLE='Toward Channel-Aware Visual Document Understanding With RAG: A Survey'
def L(t,u): return f'<link href="{escape(u)}" color="{PINK}">{escape(str(t))}</link>' if isinstance(u,str) and u.startswith('http') else escape(str(t))
def P(x): return x if isinstance(x,Paragraph) else Paragraph(escape(str(x)) if str(x)!='nan' else '',C)
def tbl(head,rows,w):
    t=Table([[Paragraph(f'<b>{h}</b>',C) for h in head]]+[[P(c) for c in r] for r in rows],colWidths=w,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.25,colors.grey),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E8EEF3')),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F7F9FB')])]))
    return t
W=landscape(A4)[0]-2.8*cm
ref=pd.read_csv('data/references.csv'); Lk=dict(zip(ref.BibKey,ref.Link)); R=ref.set_index('BibKey')
idx=pd.read_csv('data/venues/index.csv'); m=pd.read_csv('data/methods.csv',dtype=str,keep_default_na=False); d=pd.read_csv('data/datasets.csv',dtype=str,keep_default_na=False)
order=['TPAMI','CVPR','ECCV','ICCV','ICCVW','ICDAR','AAAI','WACV','BMVC','ACCV','PatternRecognition','CVIU','IJCV','NeurIPS','EMNLP','JMLR','ACL','EACL','ICLR','ICML','KDD','IJCAI','ICPR','SIGIR','IJDAR','arXiv']
idx['o']=idx.Venue.map(order.index); idx=idx.sort_values(['o','Year'],ascending=[True,False])
REPO='https://github.com/visualdocumentrag/VDU-RAG-Survey'
st=[Paragraph(escape(TITLE),H1),Paragraph(f'Supplementary lists: details that do not fit in the page limit. Authors: TBD. Literature cut-off: <b>24 September 2026</b>. Repository: {L(REPO,REPO)}. Every title is clickable (pink).',B),Spacer(1,4),
Paragraph('Contents: A. Venue-year lists · B. The 73 methods (paper Tables 4-5) · C. The 61 benchmarks (paper Table 8 and the release) · D. 21 further benchmarks cited in the text · E. The 74 works not included (page limit) · F. The 217 references in paper order · G. Every reported score with its source table.',B)]
st+=[Paragraph('A. Venue-year lists screened in full',H2),tbl(['Venue','Year','Type','Papers screened','Related','List'],[[x.Venue.replace('PatternRecognition','Pattern Recognition').replace('ICCVW','ICCV Workshops'),x.Year,x.Type,f'{x.Records:,}',int(x.Related_list),Paragraph(L('complete list',f'{REPO}/blob/main/pages/venues/{x.ID}.md'),C)] for x in idx.itertuples()]+[['Total','','',f'{idx.Records.sum():,}',int(idx.Related_list.sum()),'']],[W*.25,W*.08,W*.17,W*.17,W*.1,W*.23])]
st+=[Paragraph('Not held or not yet published at the cut-off: ECCV 2025, ICCV 2026, ACCV 2025, ICPR 2025 (not held); ACCV 2026, NeurIPS 2026, EMNLP 2026, CIKM 2026 (after the cut-off); KDD 2025 and IJCAI 2025 not collected.',B)]
st+=[PageBreak(),Paragraph('B. The 73 methods (paper Tables 4-5)',H2),tbl(['#','Method','Venue','Year','Objective','Index / unit','Datasets','Code'],[[x.No,Paragraph(L(x.Method,Lk.get(x.BibKey)),C),x.Paper_Venue,x.Year,x.Objective,x.Index_Unit,x.Benchmarks,Paragraph(L('code',x.Code) if x.Code else '-',C)] for x in m.itertuples()],[W*.04,W*.13,W*.09,W*.06,W*.14,W*.15,W*.31,W*.08])]
CH=['Text','Layout','Tables','Figures','Equations','Forms','Stamps','Typography']; AB=['Txt','Lay','Tab','Fig','Eqn','Frm','Stp','Typ']
t8=d[d.Source_table=='Paper Table 8']; rest=d[d.Source_table!='Paper Table 8']
st+=[PageBreak(),Paragraph('C. The 61 benchmarks',H2),Paragraph('C.1 The 25 channel-audited benchmarks, with the values of paper Table 8 (∼: the authors report only an approximate count; -: not applicable).',B),
tbl(['Task','Dataset','Venue','Year','Lang.','Size','Queries','Metric','Channels annotated','Link'],[[x.Group,Paragraph(L(x.Dataset,Lk.get(x.BibKey)),C),x.Venue,x.Year,x.Language,x.Size,x.Queries,x.Metric,', '.join(a for c,a in zip(CH,AB) if x[c]=='annotated') or '-',Paragraph(L('link',x.Link),C)] for _,x in t8.iterrows()],[W*.1,W*.12,W*.08,W*.05,W*.07,W*.13,W*.11,W*.14,W*.14,W*.06]),
Spacer(1,6),Paragraph('C.2 The 36 benchmarks released at 2025-2026 venues',B),
tbl(['Group','Dataset','Focus','Paper','Data / code'],[[x.Group,x.Dataset,x.Focus,Paragraph(L('paper',Lk.get(x.BibKey)),C),Paragraph(L('link',x.Link) if x.Link else '-',C)] for _,x in rest.iterrows()],[W*.18,W*.17,W*.45,W*.1,W*.1])]
md=open('pages/datasets.md',encoding='utf-8').read(); sec3=md[md.index('## 3. Other benchmarks'):]
rows=[]
for line in sec3.splitlines():
    mm=re.match(r'\|([^|]+)\|([^|]+)\|(\d{4})\|([^|]+)\|([^|]+)\|\[paper\]\(([^)]+)\)\|',line)
    if mm: rows.append([Paragraph(L(mm.group(1),mm.group(6)),C),mm.group(2),mm.group(3),mm.group(4),mm.group(5)])
st+=[PageBreak(),Paragraph(f'D. {len(rows)} further benchmarks and datasets cited in the text of the paper',H2),tbl(['Dataset','Venue','Year','What it tests','Cited in'],rows,[W*.18,W*.3,W*.06,W*.28,W*.18])]
nc=ref[ref.CitedInPaper!='yes'].sort_values(['Year','Title'],ascending=[False,True])
st+=[PageBreak(),Paragraph(f'E. The {len(nc)} works not included in the paper (page limit)',H2),tbl(['#','Title','Venue','Year'],[[i,Paragraph(L(x.Title,x.Link),C),x.Venue,x.Year] for i,x in enumerate(nc.itertuples(),1)],[W*.05,W*.55,W*.32,W*.08])]
aux=open('data/paper_reference_numbers.csv').read().splitlines()[1:]
num=[(int(l.split(',')[1]),l.split(',')[0]) for l in aux]
st+=[PageBreak(),Paragraph('F. The 217 references, numbered as in the paper',H2),tbl(['No.','Title','Venue','Year'],[[f'[{n}]',Paragraph(L(R.loc[k].Title,R.loc[k].Link),C),R.loc[k].Venue,R.loc[k].Year] for n,k in sorted(num)],[W*.06,W*.54,W*.32,W*.08])]
sc=pd.read_csv('data/scores.csv',dtype=str,keep_default_na=False)
st+=[PageBreak(),Paragraph('G. Every reported score with its source table (paper Table 9)',H2),tbl(['Method','Values as reported','Source table','Paper'],[[x.Method,x.Values,x.iloc[2],Paragraph(L('paper',Lk.get(x.Key)) if x.Key in Lk else '-',C)] for _,x in sc.iterrows()],[W*.18,W*.47,W*.25,W*.1])]
def foot(c,dd):
    c.saveState(); c.setFont('Helvetica',7); c.drawString(1.4*cm,0.8*cm,'Supplementary lists · cut-off 24 September 2026 · authors TBD'); c.drawRightString(landscape(A4)[0]-1.4*cm,0.8*cm,f'page {dd.page}'); c.restoreState()
SimpleDocTemplate('supplementary/Supplementary_Lists.pdf',pagesize=landscape(A4),leftMargin=1.4*cm,rightMargin=1.4*cm,topMargin=1.2*cm,bottomMargin=1.3*cm,title='Supplementary lists: '+TITLE,author='TBD').build(st,onFirstPage=foot,onLaterPages=foot)
print('ok')

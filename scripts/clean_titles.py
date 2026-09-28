"""Turn LaTeX markup that some publishers leave in titles (M$^{3}$D, $\\tau$-bench) into plain Unicode for display."""
import re
SUP=str.maketrans('0123456789+-=()nkiT','⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿᵏⁱᵀ')
SUB=str.maketrans('0123456789+-=()','₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎')
GREEK={'alpha':'α','beta':'β','gamma':'γ','delta':'δ','epsilon':'ε','lambda':'λ','mu':'μ','pi':'π','sigma':'σ','tau':'τ','theta':'θ','phi':'φ','omega':'ω','Delta':'Δ','Sigma':'Σ','Omega':'Ω','Pi':'Π','infty':'∞','times':'×','cdot':'·','rightarrow':'→','leftarrow':'←','star':'⋆','ast':'*'}
def clean(t):
    if not re.search(r'[\\$^_{}]',t): return t
    s=t
    for _ in range(3):
        s=re.sub(r'\\(?:textit|textbf|mathbf|mathrm|mathcal|mathit|underline|emph|text|textsc|mathbb|operatorname|boldsymbol)\s*\{([^{}]*)\}',r'\1',s)
    s=re.sub(r'\\([A-Za-z]+)',lambda m:GREEK.get(m.group(1),m.group(1) if m.group(1) not in('left','right','mathrm') else ''),s)
    s=re.sub(r'\^\{([^{}]*)\}',lambda m:m.group(1).translate(SUP) if all(ch in '0123456789+-=()nkiT' for ch in m.group(1)) else '^'+m.group(1),s)
    s=re.sub(r'\^([0-9nkiT])',lambda m:m.group(1).translate(SUP),s)
    s=re.sub(r'_\{([^{}]*)\}',lambda m:m.group(1).translate(SUB) if all(ch in '0123456789+-=()' for ch in m.group(1)) else '_'+m.group(1),s)
    s=re.sub(r'_([0-9])',lambda m:m.group(1).translate(SUB),s)
    s=s.replace('$','').replace('{','').replace('}','').replace('\\','')
    return re.sub(r'\s+',' ',s).strip()
if __name__=='__main__':
    import pandas as pd,glob
    n=0
    for f in glob.glob('data/venues/*/*.csv')+['data/references.csv']:
        d=pd.read_csv(f,dtype=str,keep_default_na=False)
        if 'Title' not in d: continue
        new=d.Title.map(clean); ch=(new!=d.Title).sum()
        if ch: d['Title']=new; d.to_csv(f,index=False); n+=ch
    print('titles cleaned',n)

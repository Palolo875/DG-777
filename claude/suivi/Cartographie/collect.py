import subprocess, re, json, os, sys
os.chdir('/home/user/design-governance')
SP='/tmp/claude-0/-home-user-DG-777/a53d38a4-2da0-5e06-9ee2-c76fc7c01b1f/scratchpad/'
files=subprocess.check_output(['git','ls-files']).decode().split('\n'); files=[f for f in files if f]
TRUNK=['ACTION/RUN-DIRECTION','DIRECTION/CREATIVE-BOOT','DIRECTION/VISUAL_TARGET','DIRECTION/FIRST-OBJECT','SAVOIR/TYPE','ACTION/FIRST-RENDER','ACTION/GATE-A/CONTROLES','BIBLIOTHEQUE/SEQUENCE']
ESQ=['BIBLIOTHEQUE/TENSION','BIBLIOTHEQUE/SUPPORT','BIBLIOTHEQUE/GRID','BIBLIOTHEQUE/SCENE','BIBLIOTHEQUE/SIGNATURE','SAVOIR/STYLE','SAVOIR/CRAFT/CFT-02']
CON=['SAVOIR/STATE','SAVOIR/CRAFT/CFT-05','SAVOIR/CRAFT/CFT-03','BIBLIOTHEQUE/OBJECT','BIBLIOTHEQUE/SECTIONS']
# part utile au rendu, estimée lors de la lecture (fichier -> %)
UTILE={'SKILL.md':10,'design/savoir/qualite-creative.md':50,'design/savoir/composition.md':55,'design/savoir/typographie.md':60,
'design/savoir/identite.md':85,'design/savoir/contexte.md':75,'design/savoir/images-et-sources.md':55,'design/savoir/gout-et-tendances.md':60,
'design/savoir/techniques.md':45,'design/savoir/fondements.md':40,'design/savoir/styles.md':30,'design/savoir/connexions.md':10,
'design/savoir/systeme-de-design.md':20,'design/formes/choisir.md':30,'design/formes/catalogue.md':35,'design/direction/diriger.md':40,
'design/direction/standard.md':30,'design/direction/boucle.md':50,'design/direction/cadrer.md':45,'design/direction/premier-objet.md':35,
'design/produit/finition.md':65,'design/produit/plancher.md':40,'design/produit/interface.md':40,'design/produit/premier-rendu.md':40,
'design/produit/preuve-visuelle.md':20,'references/recettes.md':80,'agent/chemins.md':5,'agent/repondre.md':15,
'gouvernance/travail.md':2,'gouvernance/verification.md':5,'gouvernance/pipeline.md':10,'gouvernance/cloture.md':3,'gouvernance/structure.md':5,
'gouvernance/integrite.md':10,'gouvernance/statuts.md':0,'gouvernance/principes.md':0}
def first_line(path):
    try: t=open(path,encoding='utf-8').read()
    except Exception: return ''
    if path.endswith('.py'):
        m=re.search(r'"""(.+?)(\n|""")',t,re.S); return m.group(1).strip() if m else ''
    for l in t.split('\n'):
        l=l.strip()
        if not l or l.startswith('#') or l.startswith('<!--') or l.startswith('---') or l.startswith('>'): continue
        return re.sub(r'[`*\[\]]','',l)[:180]
    return ''
def kind(f):
    e=os.path.splitext(f)[1].lower()
    if e=='.md': return 'texte'
    if e in ('.py','.sh','.yml'): return 'code'
    if e in ('.png','.svg'): return 'image'
    if e in ('.ttf','.woff2'): return 'police'
    if e in ('.json','.cff','.txt') : return 'données' if 'LICENSE' not in f and 'OFL' not in f else 'licence'
    if e=='.html': return 'page'
    if f.startswith('LICENSE'): return 'licence'
    return 'autre'
def audience(f):
    if f=='SKILL.md': return ('agent','toujours')
    if f.startswith('design/principes/'): return ('agent','au signal')
    if f.startswith(('design/','agent/')) and f.endswith('.md') and not f.endswith('README.md'): return ('agent','par route')
    if f.startswith('references/') and not f.endswith('README.md'): return ('agent','par outil' if 'recettes' in f else 'au signal')
    if f.startswith('gouvernance/') and f.endswith('.md') and not f.endswith('README.md'): return ('agent','trace complète')
    if f.startswith('gouvernance/'): return ('atelier','trace complète')
    if f.startswith('scripts/'):
        b=os.path.basename(f)
        if b in ('parcours.py','planche.py','regard.py','check_render.py','read_route.py','journal_mobilisation.py'): return ('agent','outil')
        return ('atelier','maintenance')
    if f.startswith('maintenance/'): return ('atelier','maintenance')
    if f.startswith('supports/') and (f.endswith('.py') or f.endswith('.json') or 'template' in f or 'fonts/' in f): return ('atelier','maintenance')
    return ('humain','lecture')
out=[]
for f in files:
    b=os.path.getsize(f)
    try: lines=sum(1 for _ in open(f,encoding='utf-8'))
    except Exception: lines=None
    a=audience(f)
    out.append(dict(p=f,d=f.split('/')[0] if '/' in f else '(racine)',b=b,l=lines,k=kind(f),a=a[0],m=a[1],r=first_line(f) if kind(f) in('texte','code') else '',u=UTILE.get(f)))
# routes
s=subprocess.check_output(['python3','scripts/read_route.py','--sommaire']).decode()
routes=[];cur=None
for line in s.split('\n'):
    if re.match(r'^[\w./-]+\.md$',line.strip()): cur=line.strip(); continue
    m=re.match(r'^([A-Z][A-Z0-9_/-]+)\s+([\d.]+) k\s+(\d+) s\.-s\.\s+(.*)$',line.strip())
    if m:
        c=m.group(1); st='tronc' if c in TRUNK else 'esquisses' if c in ESQ else 'construction' if c in CON else 'au signal'
        routes.append(dict(c=c,f=cur,k=float(m.group(2)),s=int(m.group(3)),r=m.group(4)[:160],st=st))
# core sections
t=open('SKILL.md',encoding='utf-8').read(); idx=[m.start() for m in re.finditer(r'^### ',t,re.M)]+[len(t)]
core=[dict(t=t[idx[i]:].split('\n')[0][4:],b=len(t[idx[i]:idx[i+1]].encode())) for i in range(len(idx)-1)]
# recipes
t=open('references/recettes.md',encoding='utf-8').read(); parts=re.split(r'^## ',t,flags=re.M)[1:]
rec=[]
for p in parts:
    name=p.split('\n')[0].strip(); m=re.search(r'\*\*Problème\.\*\*\s*(.+)',p)
    rec.append(dict(n=name,b=len(p.encode()),r=(m.group(1)[:150] if m else '')))
# commands
h=subprocess.check_output(['python3','scripts/parcours.py','--help']).decode()
cmds=[]
for m in re.finditer(r'^    (\w+)\s{2,}(.+?)(?=^    \w+\s{2,}|\Z)',h,re.M|re.S):
    cmds.append(dict(n=m.group(1),r=' '.join(m.group(2).split())))
# tests count
tests=0
for f in files:
    if re.search(r'scripts/test_.*\.py$',f): tests+=len(re.findall(r'^\s*def (test|cas)_',open(f).read(),re.M))
data=dict(files=out,routes=routes,core=core,rec=rec,cmds=cmds,
  trunks={'LITE':8013,'ITER':5593,'STANDARD':7082,'DIRECTION':35438,'SYSTÈME':7803},
  stages={'ESQUISSES':31158,'CONSTRUCTION':38259},core_budget=33000,core_size=os.path.getsize('SKILL.md'))
json.dump(data,open(SP+'carte/data.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(out),len(routes),len(core),len(rec),len(cmds),tests,os.path.getsize(SP+'carte/data.json'))

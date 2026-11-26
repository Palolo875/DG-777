"""Décomposition de décisions mesurables d'une page (rétro-ingénierie, option 2). Outil de suivi, hors paquet."""
import json, sys
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np, io

JS = r"""(L) => {
  const vis = e => { const r = e.getBoundingClientRect(), s = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05; };
  const textes = [...document.querySelectorAll('body *')].filter(e => vis(e) &&
    [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1));
  const tailles = {}, familles = new Set(), graisses = new Set(), couleurs = new Set();
  let premierMots = 0;
  for (const e of textes) {
    const s = getComputedStyle(e), r = e.getBoundingClientRect();
    const t = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join(' ').trim();
    const n = t.split(/\s+/).length;
    const fs = Math.round(parseFloat(s.fontSize));
    tailles[fs] = (tailles[fs] || 0) + t.length;
    familles.add(s.fontFamily.split(',')[0].replace(/["']/g, '').trim());
    graisses.add(s.fontWeight); couleurs.add(s.color);
    if (r.top + scrollY < innerHeight && r.bottom > 0) premierMots += n;
  }
  const tri = Object.entries(tailles).map(([k, v]) => [+k, v]).sort((a, b) => b[1] - a[1]);
  const courant = tri.length ? tri[0][0] : 16;
  const significatives = tri.filter(([k, v]) => v >= 20).map(([k]) => k).sort((a, b) => a - b);
  const plusGrand = significatives.length ? significatives[significatives.length - 1] : courant;
  // longueur de ligne : paragraphes de 120 caractères ou plus
  const ps = textes.filter(e => e.textContent.trim().length > 120 && ['P','LI','DD','DIV'].includes(e.tagName));
  const ch = ps.map(e => e.getBoundingClientRect().width / (parseFloat(getComputedStyle(e).fontSize) * 0.5));
  const lignes = ch.length ? ch.sort((a,b)=>a-b)[Math.floor(ch.length/2)] : 0;
  const gauche = textes.map(e => Math.round(e.getBoundingClientRect().left)).filter(x => x >= 0);
  const marge = gauche.length ? Math.min(...gauche) : 0;
  const cols = {}; gauche.forEach(x => { const k = Math.round(x / 8) * 8; cols[k] = (cols[k] || 0) + 1; });
  const colonnes = Object.values(cols).filter(v => v >= 3).length;
  const fonds = new Set([...document.querySelectorAll('body, body *')].filter(vis).map(e => getComputedStyle(e).backgroundColor).filter(c => c !== 'rgba(0, 0, 0, 0)'));
  const rayons = new Set([...document.querySelectorAll('body *')].filter(vis).map(e => getComputedStyle(e).borderRadius).filter(r => r !== '0px'));
  const ombres = [...document.querySelectorAll('body *')].filter(vis).filter(e => getComputedStyle(e).boxShadow !== 'none').length;
  return {hauteur: document.documentElement.scrollHeight, courant, plus_grand: plusGrand, echelle: +(plusGrand / courant).toFixed(1),
    tailles: significatives.length, familles: familles.size, graisses: graisses.size, couleurs_texte: couleurs.size,
    fonds: fonds.size, rayons: rayons.size, ombres, ligne_ch: Math.round(lignes), marge_gauche: marge, alignements: colonnes,
    mots_premier_ecran: premierMots};
}"""

def vide(png):
    im = np.asarray(Image.open(io.BytesIO(png)).convert('L').resize((360, 225)), dtype=float)
    fond = np.median(im)
    return round(float((np.abs(im - fond) < 6).mean()) * 100)

def mesurer(url):
    out = {}
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for L, H in ((1440, 900), (390, 844)):
            pg = nav.new_page(viewport={'width': L, 'height': H})
            try:
                pg.goto(url, timeout=45000, wait_until='load'); pg.wait_for_timeout(1500)
                m = pg.evaluate(JS, L); m['vide_premier_ecran'] = vide(pg.screenshot())
                out[L] = m
            except Exception as e:
                out[L] = {'erreur': str(e)[:120]}
            pg.close()
        nav.close()
    return out

if __name__ == '__main__':
    res = {}
    for u in sys.argv[1:]:
        res[u] = mesurer(u); print(u, json.dumps(res[u].get(1440), ensure_ascii=False), flush=True)
    json.dump(res, open(sys.argv[0].replace('.py', '.json'), 'w'), ensure_ascii=False, indent=1)

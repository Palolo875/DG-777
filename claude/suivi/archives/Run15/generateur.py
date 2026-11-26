#!/usr/bin/env python3
"""Génère la page des Lueurs (run 15). Données d'exemple cohérentes : durées sommées, heures de fin calculées."""
import base64, pathlib, sys

ICI = pathlib.Path(__file__).parent
AUTONOME = "--autonome" in sys.argv

SOIREES = [
    ("jeudi", 8, "En famille", "Dès 6 ans. Des films courts, drôles ou tendres, pour commencer tôt et rentrer avant minuit.", [
        ("Le Renard et la lanterne", "animation", "France", 7), ("Mamie déménage", "fiction", "France", 12),
        ("Le Grand Saut", "animation", "Belgique", 5), ("Petit Orage", "animation", "Suisse", 8),
        ("Les Cerises de Lou", "fiction", "France", 14), ("Oiseau de nuit", "animation", "Canada", 6),
        ("La Cabane", "fiction", "France", 11), ("Plouf", "animation", "Pays-Bas", 4),
        ("Le Facteur des cimes", "documentaire", "France", 13), ("Bonne nuit, la lune", "animation", "Japon", 9)]),
    ("vendredi", 9, "D'ici", "Des films tournés dans nos vallées, ou par des gens qui en viennent.", [
        ("Transhumance", "documentaire", "France", 16), ("La Dernière Fromagère", "documentaire", "France", 12),
        ("Neige de juin", "fiction", "France", 9), ("Le Col", "fiction", "Italie", 15),
        ("Écho", "expérimental", "France", 4), ("Ceux du haut", "documentaire", "Suisse", 11),
        ("Pente douce", "fiction", "France", 8), ("Le Bal du 14", "fiction", "France", 13),
        ("Racines", "animation", "France", 6), ("Brouillard", "fiction", "Autriche", 10)]),
    ("samedi", 10, "La nuit la plus longue", "La compétition. Dix fictions venues de loin ; vous votez pour le prix du public en sortant.", [
        ("Les Heures creuses", "fiction", "Portugal", 14), ("Ana, en août", "fiction", "Espagne", 17),
        ("Station 9", "fiction", "Corée du Sud", 12), ("Le Poids du ciel", "fiction", "Sénégal", 15),
        ("Retour de flamme", "fiction", "France", 9), ("Petites Mains", "fiction", "Mexique", 11),
        ("Le Silence d'Oslo", "fiction", "Norvège", 13), ("Après la pluie", "fiction", "Tunisie", 10),
        ("Deux Rives", "fiction", "Géorgie", 16), ("Fin de saison", "fiction", "Québec", 8)]),
    ("dimanche", 11, "Clôture", "Le palmarès, puis une carte blanche aux films qui ont fait rire le verger les années passées.", [
        ("Prix du public 2027", "annoncé le soir même", "—", 15), ("Le Chien de Paulette", "fiction", "France", 6),
        ("Vélo", "animation", "Danemark", 4), ("La Noce", "fiction", "Grèce", 12),
        ("Tondre", "fiction", "Irlande", 7), ("Mise à feu", "animation", "France", 5),
        ("Le Dernier Bus", "fiction", "Belgique", 10), ("Comme un dimanche", "fiction", "France", 9),
        ("Les Pommes", "animation", "Pologne", 8), ("Clap", "expérimental", "France", 3)]),
]
DEBUT = 22 * 60 + 15  # premier film à la nuit tombée

def hm(m):
    h = (m // 60) % 24
    return f"{h} h {m % 60:02d}" if m % 60 else f"{h} h"

def src(nom):
    if not AUTONOME:
        return nom
    data = (ICI / nom).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()

total_films = sum(len(s[4]) for s in SOIREES)
assert total_films == 40

def soiree_html(jour, n, theme, chapo, films):
    duree = sum(f[3] for f in films)
    fin = DEBUT + duree
    lignes = "\n".join(
        f'<tr><td class="t">{t}</td><td class="g">{g}<span>, {p}</span></td><td class="d" data-min="{d}">{d} min</td></tr>'
        for t, g, p, d in films)
    return f'''<article class="soir" id="soir-{n}" aria-labelledby="h-{n}" data-duree="{duree}">
  <header><p class="jour">{jour}</p><h3 id="h-{n}"><span class="num">{n}</span> juillet</h3><p class="theme">{theme}</p></header>
  <p class="chapo">{chapo}</p>
  <ol class="horaire"><li><b>20 h</b> le verger ouvre</li><li><b>{hm(DEBUT)}</b> premier film</li><li><b>vers {hm(fin)}</b> fin</li></ol>
  <table><caption class="sr">Films du {jour} {n} juillet</caption><tbody>
{lignes}
  </tbody><tfoot><tr><td>10 films</td><td></td><td class="d" data-somme="{n}">{duree} min</td></tr></tfoot></table>
</article>'''

polices = (ICI / "polices-integrees.css").read_text() if AUTONOME else '<link rel="stylesheet" href="polices.css">'
if AUTONOME:
    polices = f"<style>{polices}</style>"

page = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Les Lueurs — courts-métrages en plein air, 8–11 juillet 2027</title>
<meta name="description" content="Troisième édition des Lueurs : quatre soirées de courts-métrages projetés dans les vergers, du 8 au 11 juillet 2027. Prix libre, apportez votre couverture.">
{polices}
<style>
:root {{
  --papier: #ece0c8;
  --papier-2: #e3d4b8;
  --encre: #1f2d66;
  --encre-2: #3d4a80;
  --rouge: #b9321e;
  --rouge-vif: #e0533b;
  --nuit: #141c3f;
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
body {{ margin: 0; background: var(--papier); color: var(--encre); font: 17px/1.55 "Instrument Sans", system-ui, sans-serif; -webkit-font-smoothing: antialiased; }}
a {{ color: inherit; }}
.sr {{ position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }}
:focus-visible {{ outline: 3px solid var(--encre); outline-offset: 3px; }}
.fin :focus-visible {{ outline-color: #f2e7d0; }}
.fenetre {{ position: absolute; inset: 0; overflow: hidden; }}

/* ——— Premier écran : l'estampe, le nom projeté sur l'écran ——— */
.scene {{ position: relative; overflow: hidden; height: min(56.25vw, 100vh); min-height: 560px; }}
.planche {{ position: absolute; top: 0; left: 50%; height: 100%; aspect-ratio: 16 / 9; transform: translateX(-50%); }}
@media (min-aspect-ratio: 16/9) {{ .planche {{ width: 100%; height: auto; top: 50%; transform: translate(-50%, -50%); }} }}
.planche img {{ position: absolute; inset: 0; width: 100%; height: 100%; display: block; }}
.ecran {{ position: absolute; left: 48.1%; top: 33.9%; width: 26.6%; height: 32.2%; display: grid; place-items: center; text-align: center; container-type: inline-size; }}
.ecran h1 {{ margin: 0; font: 400 17cqi/0.86 "Gloock", Georgia, serif; letter-spacing: -0.01em; color: var(--encre); mix-blend-mode: multiply; }}
.ecran h1 span {{ display: block; }}
@media (prefers-reduced-motion: no-preference) {{
  .ecran h1 {{ animation: projecteur 1.3s steps(1, end) .4s both; }}
  @keyframes projecteur {{ 0% {{ opacity: 0; }} 25% {{ opacity: .45; }} 35% {{ opacity: .1; }} 55% {{ opacity: .8; }} 70% {{ opacity: .55; }} 100% {{ opacity: 1; }} }}
}}
.marque {{ position: absolute; z-index: 2; top: 28px; left: 56px; display: flex; gap: 40px; align-items: baseline; font-weight: 600; }}
.marque nav {{ display: flex; gap: 28px; font-weight: 500; }}
.marque nav a {{ text-decoration: none; }}
.marque nav a:hover {{ text-decoration: underline; text-underline-offset: 4px; }}
.annonce {{ position: absolute; z-index: 2; left: 56px; top: clamp(92px, 9vw, 130px); width: min(31vw, 460px); }}
.surtitre {{ margin: 0 0 18px; font-size: 15px; letter-spacing: .02em; }}
.dates {{ margin: 0; font: 400 clamp(52px, 6.4vw, 104px)/.9 "Gloock", Georgia, serif; letter-spacing: -0.015em; }}
.dates .an {{ display: block; font-size: .42em; letter-spacing: 0; margin-top: .25em; }}
.dates a {{ text-decoration: none; }}
.dates a:hover {{ color: var(--rouge); }}
.promesse {{ margin: 20px 0 0; max-width: 30ch; font-size: 18px; }}
.actions {{ display: flex; flex-wrap: wrap; gap: 14px 22px; align-items: center; margin-top: 26px; }}
.bouton {{ display: inline-block; padding: 14px 22px; background: var(--rouge); color: #fbf3e4; font-weight: 600; text-decoration: none; }}
.bouton:hover {{ background: var(--encre); }}
.lien {{ font-weight: 600; text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 5px; }}
.credit {{ position: absolute; z-index: 2; right: 20px; bottom: 14px; margin: 0; padding: 3px 8px; font-size: 12px; background: var(--papier); }}

/* ——— Programme : la feuille de salle ——— */
.section {{ padding: 112px 56px; }}
.entete {{ display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 4fr); gap: 32px 56px; align-items: end; max-width: 1328px; margin: 0 auto 56px; }}
h2 {{ margin: 0; text-wrap: balance; font: 400 clamp(44px, 5.2vw, 84px)/.95 "Gloock", Georgia, serif; letter-spacing: -0.015em; }}
.entete p {{ margin: 0; max-width: 46ch; }}
.jours-nav {{ display: none; }}
.grille {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); max-width: 1328px; margin: 0 auto; border-top: 3px solid var(--encre); }}
.soir {{ padding: 22px 22px 8px; border-right: 1px solid var(--encre); }}
.soir:first-child {{ padding-left: 0; }}
.soir:last-child {{ border-right: 0; padding-right: 0; }}
.soir header {{ min-height: 168px; }}
.jour {{ margin: 0; font-weight: 600; text-transform: capitalize; }}
.soir h3 {{ margin: 2px 0 6px; font: 400 26px/1 "Gloock", Georgia, serif; }}
.soir h3 .num {{ display: block; font-size: 96px; line-height: .9; color: var(--rouge); }}
.theme {{ margin: 0; font-weight: 600; }}
.chapo {{ margin: 10px 0 16px; font-size: 15px; min-height: 5.5em; }}
.horaire {{ list-style: none; margin: 0 0 16px; padding: 10px 0; border-block: 1px solid var(--encre); font-size: 15px; }}
.horaire li {{ display: flex; gap: 10px; }}
.horaire b {{ min-width: 82px; font-variant-numeric: tabular-nums; }}
table {{ width: 100%; border-collapse: collapse; font-size: 15px; }}
td {{ padding: 7px 0; border-bottom: 1px solid rgba(31, 45, 102, .28); vertical-align: top; }}
td.t {{ font-weight: 600; padding-right: 8px; }}
td.g {{ color: var(--encre-2); padding-right: 8px; font-size: 14px; }}
td.g span {{ display: none; }}
td.d {{ text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }}
tfoot td {{ border-bottom: 0; padding-top: 10px; font-weight: 600; }}
.note {{ max-width: 1328px; margin: 28px auto 0; font-size: 14px; color: var(--encre-2); }}

/* ——— Venir : le détail des couvertures ——— */
.venir {{ background: var(--papier-2); }}
.venir .cadre {{ display: grid; grid-template-columns: minmax(0, 6fr) minmax(0, 5fr); gap: 56px; max-width: 1328px; margin: 0 auto; align-items: start; }}
.detail {{ margin: 0; }}
.detail img {{ width: 100%; height: auto; display: block; aspect-ratio: 900 / 304; object-fit: cover; }}
.detail figcaption {{ margin-top: 10px; font-size: 13px; color: var(--encre-2); }}
.modes {{ margin: 32px 0 0; padding: 0; list-style: none; border-top: 1px solid var(--encre); }}
.modes li {{ display: grid; grid-template-columns: 150px 1fr; gap: 16px; padding: 14px 0; border-bottom: 1px solid var(--encre); }}
.modes b {{ font-weight: 600; }}
.adresse {{ margin: 0 0 6px; font: 400 30px/1.15 "Gloock", Georgia, serif; }}
.sac {{ display: block; margin-top: 88px; padding-top: 28px; border-top: 3px solid var(--encre); }}
.sac h3 {{ margin: 0 0 14px; font: 400 34px/1.05 "Gloock", Georgia, serif; }}
.sac ul {{ margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 22px 40px; }}
.sac li {{ max-width: 34ch; }}
.sac li b {{ display: block; }}
.pluie {{ margin-top: 28px; padding-top: 16px; border-top: 1px solid var(--encre); }}
.ex {{ font-size: 12px; font-weight: 500; padding: 1px 6px; border: 1px solid currentColor; white-space: nowrap; vertical-align: 2px; }}

/* ——— Fin : l'écran seul ——— */
.fin {{ background: var(--nuit); color: #f2e7d0; padding: 0; }}
.fin .cadre {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); align-items: center; max-width: 1440px; margin: 0 auto; }}
.fin .image {{ position: relative; }}
.fin .image img {{ width: 100%; display: block; aspect-ratio: 660 / 480; object-fit: cover; }}
.fin .image p {{ position: absolute; left: 15%; top: 19%; width: 63%; height: 58%; margin: 0; display: grid; place-items: center; text-align: center; font: 400 clamp(26px, 3.4vw, 52px)/1 "Gloock", Georgia, serif; color: var(--encre); mix-blend-mode: multiply; }}
.fin .texte {{ padding: 56px; }}
.fin h2 {{ font-size: clamp(36px, 4vw, 64px); }}
.fin .actions .lien {{ color: #f2e7d0; }}
.fin .bouton:hover {{ background: #f2e7d0; color: var(--nuit); }}
.pied {{ display: flex; flex-wrap: wrap; justify-content: space-between; gap: 20px 40px; max-width: 1328px; margin: 0 auto; padding: 36px 56px 48px; font-size: 14px; color: #c9bfa9; border-top: 1px solid rgba(242, 231, 208, .25); }}
.pied p {{ margin: 0; max-width: 62ch; }}

@media (max-width: 1180px) {{
  .grille {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
  .soir:nth-child(2) {{ border-right: 0; padding-right: 0; }}
  .soir:nth-child(3) {{ padding-left: 0; }}
  .soir:nth-child(n+3) {{ border-top: 3px solid var(--encre); margin-top: 24px; }}
  .annonce {{ width: min(40vw, 460px); }}
}}
/* ——— Téléphone ——— */
@media (max-width: 760px) {{
  body {{ font-size: 16px; }}
  .scene {{ height: auto; min-height: 0; }}
  .fenetre {{ position: relative; height: 460px; }}
  .planche {{ height: 100%; left: 0; transform: translateX(-37%); }}
  .marque {{ top: 14px; left: 14px; font-size: 15px; background: var(--papier); padding: 4px 8px; }}
  .marque nav {{ display: none; }}
  .credit {{ right: 10px; bottom: 8px; font-size: 11px; }}
  .annonce {{ position: static; width: auto; padding: 28px 20px 8px; }}
  .dates {{ font-size: 60px; }}
  .promesse {{ font-size: 17px; }}
  .bouton {{ width: 100%; text-align: center; padding: 16px; }}
  .section {{ padding: 72px 20px; }}
  .entete {{ grid-template-columns: 1fr; margin-bottom: 28px; }}
  .jours-nav {{ display: flex; position: sticky; top: 0; z-index: 3; gap: 0; margin: 0 -20px; padding: 0 20px; background: var(--papier); border-bottom: 1px solid var(--encre); }}
  .jours-nav button {{ flex: 1; padding: 12px 0 10px; border: 0; border-bottom: 3px solid transparent; background: none; color: var(--encre); font: 600 15px/1.2 "Instrument Sans", sans-serif; }}
  .jours-nav button[aria-selected="true"] {{ border-bottom-color: var(--rouge); }}
  .jours-nav button b {{ display: block; font: 400 26px/1 "Gloock", serif; }}
  .grille {{ display: block; border-top: 0; }}
  .soir {{ padding: 24px 0 0; border: 0; }}
  .js .soir:not(.actif) {{ display: none; }}
  .soir header {{ min-height: 0; }}
  .chapo {{ min-height: 0; }}
  td.g span {{ display: inline; }}
  .venir .cadre, .fin .cadre {{ grid-template-columns: 1fr; gap: 32px; }}
  .modes li {{ grid-template-columns: 1fr; gap: 2px; }}
  .sac ul {{ grid-template-columns: 1fr; }}
  .fin .texte {{ padding: 8px 20px 56px; }}
  .pied {{ padding: 28px 20px 40px; }}
}}
</style>
</head>
<body>
<header class="scene" aria-label="Les Lueurs, troisième édition">
  <div class="marque"><span>Les Lueurs <span style="font-weight:400">3<sup>e</sup> édition</span></span>
    <nav aria-label="Sections"><a href="#programme">Programme</a><a href="#venir">Venir</a><a href="#sac">Prix libre</a></nav></div>
  <div class="fenetre"><div class="planche">
    <img src="{src('verger.jpg')}" width="1536" height="864" alt="Estampe en deux encres : un écran blanc tendu entre des pommiers, au-dessus de couvertures posées dans l'herbe ; le projecteur l'éclaire depuis la droite.">
    <div class="ecran"><h1><span>Les</span> <span>Lueurs</span></h1></div>
  </div><p class="credit">Image générée, en attendant l'affiche 2027</p></div>
  <div class="annonce">
    <p class="surtitre">Courts-métrages en plein air, dans les vergers</p>
    <p class="dates"><a href="#soir-8">8</a>–<a href="#soir-11">11 juillet</a><span class="an">2027 · quatre soirs</span></p>
    <div class="actions"><a class="bouton" id="cta-main" href="#programme">Voir le programme</a><a class="lien" href="#venir">Venir au verger</a></div>
  </div>
</header>

<main>
<section class="section" id="programme" aria-labelledby="h-prog">
  <div class="entete"><h2 id="h-prog">Quarante films,<br>quatre soirs</h2>
    <p>Quarante courts-métrages projetés à la nuit tombée, entre les pommiers. Le verger ouvre à 20 h : on s'installe, on pique-nique, la buvette sert le jus des pommes de l'an dernier. Le premier film part quand il fait assez nuit pour l'écran, vers 22 h 15.</p></div>
  <div class="jours-nav" role="tablist" aria-label="Choisir la soirée">
    {''.join(f'<button role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="soir-{s[1]}" data-soir="{s[1]}"><b>{s[1]}</b>{s[0][:3]}.</button>' for i, s in enumerate(SOIREES))}
  </div>
  <div class="grille">
{''.join(soiree_html(*s) for s in SOIREES)}
  </div>
  <p class="note">Programme d'exemple : titres, durées et thèmes seront remplacés par la sélection 2027, annoncée en juin.</p>
</section>

<section class="section venir" id="venir" aria-labelledby="h-venir">
  <div class="cadre">
    <div>
      <h2 id="h-venir">Monter au verger</h2>
      <figure class="detail"><img src="{src('couvertures.jpg')}" width="900" height="304" alt="Détail de l'estampe : des couvertures étalées dans l'herbe."><figcaption>Le pré sous les pommiers, deux cents couvertures environ chaque soir.</figcaption></figure>
    </div>
    <div>
      <p class="adresse">Verger du Pré-Haut,<br>chemin des Vergers, Sauvérac <span class="ex">exemple</span></p>
      <p>À 900 m d'altitude, au-dessus du village. Les voitures restent en bas : la dernière montée se fait à pied, dix minutes sous les arbres.</p>
      <ul class="modes">
        <li><b>En navette</b><span>Depuis la gare de la vallée, départs à 19 h 15 et 20 h 30 ; retour après la dernière séance. Gratuite.</span></li>
        <li><b>En voiture</b><span>Parking du champ de foire, à l'entrée du village, fléché « Les Lueurs ». Pensez au covoiturage : la route est étroite.</span></li>
        <li><b>À pied, à vélo</b><span>Depuis la place de l'église, suivez le chemin des Vergers. Garage à vélos à l'entrée du pré.</span></li>
      </ul>
      <div class="actions"><a class="bouton" href="https://www.openstreetmap.org/search?query=Sauv%C3%A9rac" rel="noopener">Ouvrir l'itinéraire</a><span class="ex">lieu d'exemple</span></div>
    </div>
  </div>
  <div class="cadre sac" id="sac">
    <h3>Dans le sac</h3>
    <ul>
      <li><b>Une couverture</b>On s'assoit dans l'herbe. Quelques transats pour qui en a besoin, à demander à l'entrée.</li>
      <li><b>Une petite laine</b>Il fait souvent 12 °C à minuit, même en juillet.</li>
      <li><b>Le pique-nique</b>Ou la buvette : tartes, fromage du Pré-Haut, jus de pomme.</li>
      <li><b>Une lampe douce</b>Pour le retour. Pendant les films, on l'éteint : l'écran a besoin du noir.</li>
      <li><b>De quoi donner</b>L'entrée est à prix libre. Le chapeau passe à l'entracte ; il paie les films et le projecteur.</li>
      <li><b>Les enfants</b>Bienvenus tous les soirs ; le jeudi est fait pour eux.</li>
    </ul>
    <p class="pluie"><b>S'il pleut</b> : repli à la salle des fêtes du village, annoncé ici le jour même avant 17 h.</p>
  </div>
</section>

<section class="fin" aria-labelledby="h-fin">
  <div class="cadre">
    <div class="image"><img src="{src('ecran.jpg')}" width="660" height="480" alt=""><p>Jeudi 8 juillet,<br>22 h 15</p></div>
    <div class="texte"><h2 id="h-fin">On éteint les lampes,<br>le premier film commence.</h2>
      <div class="actions"><a class="bouton" href="#programme">Voir le programme</a><a class="lien" href="#venir">Venir au verger</a></div></div>
  </div>
  <footer class="pied">
    <p><b>Les Lueurs</b>, festival de courts-métrages en plein air, tenu par une association de bénévoles. Contact : <a href="mailto:bonjour@leslueurs.exemple">bonjour@leslueurs.exemple</a> <span class="ex">exemple</span></p>
    <p>Image : estampe générée par IA (Figma, novembre 2026), illustration et non photo du festival ; elle attend l'affiche 2027. Lieu, programme et horaires sont des exemples. Polices Gloock et Instrument Sans, licence SIL OFL.</p>
  </footer>
</section>
</main>
<script>
document.documentElement.classList.add('js');
const tabs = [...document.querySelectorAll('.jours-nav [role=tab]')];
function choisir(n) {{
  tabs.forEach(t => t.setAttribute('aria-selected', t.dataset.soir === String(n)));
  document.querySelectorAll('.soir').forEach(s => s.classList.toggle('actif', s.id === 'soir-' + n));
}}
tabs.forEach((t, i) => {{
  t.addEventListener('click', () => choisir(t.dataset.soir));
  t.addEventListener('keydown', e => {{
    const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
    if (d) {{ const u = tabs[(i + d + tabs.length) % tabs.length]; u.focus(); choisir(u.dataset.soir); }}
  }});
}});
choisir(8);
document.querySelectorAll('.dates a').forEach(a => a.addEventListener('click', () => choisir(a.getAttribute('href').split('-')[1])));
</script>
</body>
</html>
'''
import re
tete, corps = page.split("<body>", 1)
corps, script = corps.split("<script>", 1)
corps = re.sub(r" ([:;!?»])", "\u202f\\1", corps)
corps = re.sub(r"« ", "«\u202f", corps)
page = tete + "<body>" + corps + "<script>" + script
(ICI / ("les-lueurs.html" if AUTONOME else "page.html")).write_text(page)
print("écrit", "autonome" if AUTONOME else "dev", len(page))

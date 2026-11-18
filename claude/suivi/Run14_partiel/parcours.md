# Parcours — page.html

Mesures et captures en une passe ; rien n'est jugé ici. Chaque signal pose une question : la décision reste au run.

## 1. Défauts bloquants
- **Objet de l’état clé dans son cadre (--in-frame)** : 768 px : #commander : 1 élément(s) sur 1 hors du cadre → ACTION/VISUAL_PROOF

## 2. Réserves à vérifier
- Contraste du texte sur fond uni : aucun texte évalué sous le seuil WCAG 2.2 AA ; 1440 px : 123 texte(s) évalué(s), 133 candidat(s), 4 exclu(s) ; 768 px : 122 texte(s) évalué(s), 133 candidat(s), 3 exclu(s) … (suite dans `recette.json`)
- Nom accessible des contrôles (candidats DOM) : 30 contrôle(s) DOM inspecté(s) ; nom accessible calculé non vérifié ; candidat hors couverture : #p-assiette, #p-bol, #p-tasse, a.marque, button.lien-choix, summary
- Parcours clavier : arrêts et indicateur de focus : 24 arrêt(s) à 1440 px ; 1440 px : page, fin=end, 30 candidat(s) ; 22 arrêt(s) à 768 px ; 768 px : page, fin=end, 28 candidat(s) … (suite dans `recette.json`)

## 3. Signaux et questions
- Marqueur de vague relevé : **serif de caractère ou serif italique** (vague 2). Corrigé, ou gardé par l'atelier : la variante qui le retire, comparée à la vue. En `STANDARD`, une convention attendue se garde sans atelier.
- 1440 px · **Habillage de gabarit** — 3 points médians entre des mots (« Ø 27 · h 2,8 »). Chaque marque encode-t-elle une information du contenu (vraie séquence, rubrique), ou apparaîtrait-elle quel que soit le sujet ? Geste (`SAVOIR/STATE`) : Garder la marque qui encode une information du contenu (une vraie séquence, une rubrique qui situe).
- À regarder, non mesuré : **Partie ordinaire** — navigation, bouton, onglets et pied, logo et titre masqués, appartiennent-ils encore à cette page ? Geste (`SAVOIR/STATE`) : Emprunter à la direction une seule propriété qui ne change pas le comportement : voix typographique, bord dans la logique de l’objet de preuve, couleur par rôle, alignement sur la grille. Sections ordinaires (fonctionnalités, preuve, tarifs, questions, contact, inscription, pied) : `BIBLIOTHEQUE/SECTIONS`.

## 4. Images à regarder
- **D'abord, seule : l'image sans le texte** `/tmp/run14/travail/verif-bureau/regard/sans-texte-1440.png`. Avant d'ouvrir une autre capture et de relire la direction déclarée, écris dans la trace l'idée qui s'y lit en une seconde ; compare ensuite ce nom à la direction. S'ils ne concordent pas, c'est l'idée qui se reprend.
- Ensuite :
  - 1440 px : écran `/tmp/run14/travail/verif-bureau/ecran-1440@2x.png` ; réduite `/tmp/run14/travail/verif-bureau/regard/reduite-1440.png`
- Foyer agrandi : `/tmp/run14/travail/verif-bureau/foyer-1440@2x.png`
- Page entière réduite : `/tmp/run14/travail/verif-bureau/silhouette-1440.png` : le rythme des sections, le second moment, ce qui se répète.
- Mouvement : `/tmp/run14/travail/verif-bureau/mouvement-1440.png` : l'entrée image par image, le défilement et le survol ; le mouvement déclaré se juge ici, pas sur une capture fixe.
- Rendu contre références : `/tmp/run14/travail/verif-bureau/contre-references.png` : le niveau visé se juge ici, à la même hauteur.

## 5. Prochaine commande
- Pendant la boucle, une version à la fois : `python3 scripts/parcours.py captures /tmp/run14/travail/build/page.html --version v2` (premier écran seul, aux mêmes largeurs).
- Regard séparé, si un second agent est possible : `python3 scripts/parcours.py critique /tmp/run14/travail/build/page.html --brief "…"` (images seules et consigne).
- Garder un signal ou un marqueur : construis la variante qui le retire, puis `python3 scripts/planche.py atelier.png /tmp/run14/travail/build/page.html retiree.html --bureau-seul` et compare à la vue.
- Après correction : `python3 scripts/parcours.py verifier /tmp/run14/travail/build/page.html --foyer '.coupe' --action '#commander' --refs /tmp/run14/travail/references`

## 6. Lignes mesurables de la trace légère
- Recette : 1 défaut(s) bloquant(s), 3 réserve(s), largeurs 1440, 768 px, action dans le premier écran vérifiée (`#commander`).
- Marqueurs relevés : serif de caractère ou serif italique.
- Poids : fichier 124 Ko ; images 0 Ko (0) ; polices 4 déclaration(s) @font-face, 66 Ko intégrés ; au-delà de 2 Mo pour la page, 500 Ko pour une image ou 300 Ko de polices, un signal [À ADAPTER].
- Signaux de finition : 1 ; captures : 4 fichiers dans `/tmp/run14/travail/verif-bureau`.
- Mouvement : 9 animation(s) à l'entrée sur 1900 ms, 0 au défilement, 0 liée(s) au défilement, survol de cartes : aucun.


## 7. Limites de la recette
Limites : seules les fautes objectivables sont contrôlées, à l'état et aux largeurs observés. 0 requête(s) externe(s) bloquée(s) : les mesures utilisent alors les polices de repli. Les fonds en dégradé ou en image sont mesurés sur une capture sans texte (pire décile du fond ; quartiles pour un texte tourné) ; les opacités de groupe, le texte rempli par son fond, le texte SVG, le texte natif des contrôles et des pseudo-éléments ne sont pas évalués ; leur présence détectée conserve une réserve. La couverture du contraste est bornée au DOM inspecté ; le contraste non textuel des bordures et des icônes n'est pas mesuré ; celui de l'indicateur de focus ne l'est que pour un contour ou un anneau d'ombre net sur fond uni ; le ratio d'un texte qui passe n'est pas rapporté. L'objet de preuve mesure CSS et rectangle, sans vérifier les pixels ni l'occlusion. Les noms sont des candidats DOM, pas un calcul AccName ; leur présence conserve une réserve. Le clavier porte sur les candidats du périmètre actif et les arrêts observés ; une borne atteinte conserve une réserve. Le mouvement réduit enregistre les animations et transitions démarrées au chargement et au défilement, sur la première largeur ; les animations pilotées par script sans API d'animation du navigateur ne sont pas observées. Les captures montrent l'état observé ; elles ne jugent rien. Le chevauchement de texte est mesuré sur les rectangles de lignes, ramenés à l'interligne, hors calques fixes ou collants ; un texte décoratif superposé (aria-hidden ou très transparent) reste à juger ; il ne voit ni les glyphes ni les recouvrements par une image. Une assertion d'état ne prouve que ce qu'elle exprime, à l'état et aux largeurs observés. Cette recette ne valide ni la direction visuelle, ni le goût, ni l'utilisabilité, ni un verdict global.

## Mesures contre les références

Page entière à 1440 px, comparée aux 3 référence(s) mesurée(s) de `/tmp/run14/travail/references`. Un relevé de niveau, pas une norme : une page plus courte ou plus sobre peut être juste ; l'écart se décide, il ne se subit pas.

La part d'image ou de média compte les images, vidéos, canevas et SVG ; une matière construite en code (dégradés, formes, données en HTML) n'y entre pas.

| | Hauteur | Image ou média (matière codée non comptée) | Sections | Plus grand texte / texte courant |
|---|---|---|---|---|
| Cette page | 5342 px | 14 % | 6 | ×5.9 |
| [1] www.mudaustralia.com | 10328 px | 53 % | 9 | ×2 |
| [2] www.jarsceramistes.com | 900 px | 2 % | 3 | ×1 |
| [3] www.astierdevillatte.com | 6855 px | 34 % | 10 | ×5.8 |
| Médiane des références | 6855 px | 34 % | 9 | ×2.0 |

**Écart de moitié ou plus : image ou média 14 % contre 34 %.** L'objet de preuve déclaré (`.coupe`) est construit en code : il n'entre pas dans la part d'image, et l'écart d'image peut être voulu. La matière se juge sur capture, pas sur ce chiffre.

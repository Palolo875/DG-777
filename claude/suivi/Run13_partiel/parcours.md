# Parcours — planning-kine.html

Mesures et captures en une passe ; rien n'est jugé ici. Chaque signal pose une question : la décision reste au run.

## 1. Défauts bloquants
- **Chevauchement et troncature de texte** : 1440 px : « · Asthme (éducation) » et « En séance » (12×14 px); 1440 px : « · Rééduc. vestibulaire » et « En séance » (16×14 px); 1440 px : « · Asthme (éducation) » et « Vertiges (VPPB) · 12/15 » (21×14 px); 768 px : « libres » et « 1 » (8×16 px); 768 px : « … (suite dans `recette.json`) → SAVOIR/TYPE ; SAVOIR/STATE
- **Objet de l’état clé dans son cadre (--in-frame)** : 768 px : .gap .cand button[data-place] : 5 élément(s) sur 5 hors du cadre; 390 px : .gap .cand button[data-place] : aucun élément visible → ACTION/VISUAL_PROOF
- **Objet de preuve au premier écran (#mapPanel)** : 1440 px : intersection verticale 402.28125 px sur 402.28125, horizontale 1012 px sur 1012; 768 px : intersection verticale 437.96875 px sur 437.96875, horizontale 720 px sur 720; 390 px : objet sans surface visible (0×0) … (suite dans `recette.json`) → DIRECTION/FIRST-OBJECT ; SAVOIR/CRAFT/CFT-04a

## 2. Réserves à vérifier
- Contraste du texte sur fond uni : aucun texte évalué sous le seuil WCAG 2.2 AA ; 1440 px : 506 texte(s) évalué(s), 635 candidat(s), 112 exclu(s) ; 768 px : 505 texte(s) évalué(s), 635 candidat(s), 113 exclu(s) … (suite dans `recette.json`)
- Nom accessible des contrôles (candidats DOM) : 174 contrôle(s) DOM inspecté(s) ; nom accessible calculé non vérifié ; candidat hors couverture : button.mrow.tbc
- Parcours clavier : arrêts et indicateur de focus : 60 arrêt(s) à 1440 px ; 1440 px : page, fin=limit, 174 candidat(s) ; 60 arrêt(s) à 768 px ; 768 px : page, fin=limit, 174 candidat(s) ; 26 arrêt(s) à 390 px ; 390 px : page, fin=end, 26 candidat(s) … (suite dans `recette.json`)

## 3. Signaux et questions
- 1440 px · **Cohérence de rayon** — 4 rayons différents : 3, 6, 8, 10 px (et des pilules). Une seule logique de rayon, ou des rôles distincts nommés ? Geste (`SAVOIR/STATE`) : Pour deux rectangles arrondis à inset uniforme, tester `rayon intérieur = max(0, rayon extérieur − inset)`.
- 1440 px · **Surface** — 8 ombres différentes. Une seule lumière, ou des élévations distinctes et voulues ? Geste (`SAVOIR/STATE`) : Si une matière éclairée par le haut est voulue, tester un liseré clair de **1 px CSS** sur son bord supérieur et atténuer l’ombre opposée.
- 1440 px · **Masse visuelle** — 6 tailles de texte : 12, 13, 14, 15, 16, 21 px. L'échelle a-t-elle des paliers lisibles, ou des tailles proches qui se concurrencent ? Geste (`SAVOIR/STATE`) : Réduire son échelle, sa densité ou son contraste, ou renforcer le foyer par sa position.
- 1440 px · **Accent** — 3 teintes vives distinctes. Chaque couleur a-t-elle un rôle (action, statut, donnée) ? Geste (`SAVOIR/STATE`) : Réaffecter les couleurs par rôles, distinguer action et statut, puis retirer ou réduire seulement les usages parasites.
- 1440 px · **Typographie fine** — 3 × ponctuation haute sans espace insécable (français) (« une barre par praticien et par »). Caractères et espaces typographiques justes, comme sur un produit fini ? En français : `parcours.py typo PAGE --corriger`. Geste (`SAVOIR/STATE`) : Employer `…` et les guillemets du texte (« » en français, “ ” en anglais).
- 1440 px · **Habillage de gabarit** — 134 points médians entre des mots (« Kinésithérapie · 6 praticiens »). Chaque marque encode-t-elle une information du contenu (vraie séquence, rubrique), ou apparaîtrait-elle quel que soit le sujet ? Geste (`SAVOIR/STATE`) : Garder la marque qui encode une information du contenu (une vraie séquence, une rubrique qui situe).
- 390 px · **Typographie fine** — 3 × ponctuation haute sans espace insécable (français) (« une barre par praticien et par »). Caractères et espaces typographiques justes, comme sur un produit fini ? En français : `parcours.py typo PAGE --corriger`. Geste (`SAVOIR/STATE`) : Employer `…` et les guillemets du texte (« » en français, “ ” en anglais).
- 390 px · **Habillage de gabarit** — 132 points médians entre des mots (« Données d’exemple · heure figée mer. 10: »). Chaque marque encode-t-elle une information du contenu (vraie séquence, rubrique), ou apparaîtrait-elle quel que soit le sujet ? Geste (`SAVOIR/STATE`) : Garder la marque qui encode une information du contenu (une vraie séquence, une rubrique qui situe).
- 1440 px · **Mouvement** — rien ne bouge (ni entrée, ni défilement, ni script). Page faite pour se montrer : un seul moment orchestré servirait-il la promesse ? Page d'outil ou de lecture : rien à justifier. Geste (`SAVOIR/STATE`) : Relier le mouvement à un changement d’état ou à un seul moment orchestré (une entrée, une révélation).
- 1440 px · **Silhouette** — 2 sections de même silhouette (« section », « Mercredi 18 novembre »). Quelle section porte le second moment de la page, et laquelle est volontairement plus calme ? Geste (`SAVOIR/STATE`) : Déplacer ou redimensionner une masse, modifier un recadrage ou un contraste pour rendre la priorité perceptible.
- À regarder, non mesuré : **Partie ordinaire** — navigation, bouton, onglets et pied, logo et titre masqués, appartiennent-ils encore à cette page ? Geste (`SAVOIR/STATE`) : Emprunter à la direction une seule propriété qui ne change pas le comportement : voix typographique, bord dans la logique de l’objet de preuve, couleur par rôle, alignement sur la grille. Sections ordinaires (fonctionnalités, preuve, tarifs, questions, contact, inscription, pied) : `BIBLIOTHEQUE/SECTIONS`.

## 4. Images à regarder
- **D'abord, seule : l'image sans le texte** `/tmp/run13/work/parcours-v3/regard/sans-texte-1440.png`. Avant d'ouvrir une autre capture et de relire la direction déclarée, écris dans la trace l'idée qui s'y lit en une seconde ; compare ensuite ce nom à la direction. S'ils ne concordent pas, c'est l'idée qui se reprend.
- Ensuite :
  - 1440 px : écran `/tmp/run13/work/parcours-v3/ecran-1440@2x.png` ; réduite `/tmp/run13/work/parcours-v3/regard/reduite-1440.png`
  - 390 px : écran `/tmp/run13/work/parcours-v3/ecran-390@2x.png` ; réduite `/tmp/run13/work/parcours-v3/regard/reduite-390.png` ; sans le texte `/tmp/run13/work/parcours-v3/regard/sans-texte-390.png` ; sur téléphone émulé (tactile, 3×) `/tmp/run13/work/parcours-v3/ecran-390-telephone.png`
- Foyer agrandi : `/tmp/run13/work/parcours-v3/foyer-1440@2x.png`
- Page entière réduite : `/tmp/run13/work/parcours-v3/silhouette-1440.png` : le rythme des sections, le second moment, ce qui se répète.
- Mouvement : `/tmp/run13/work/parcours-v3/mouvement-1440.png` : l'entrée image par image, le défilement et le survol ; le mouvement déclaré se juge ici, pas sur une capture fixe.
- Sans référence fournie : au niveau haut, regarder deux ou trois références réelles du même type et relancer avec `--refs DOSSIER`.

## 5. Prochaine commande
- Pendant la boucle, une version à la fois : `python3 scripts/parcours.py captures /tmp/run13/livrable/planning-kine.html --version v2` (premier écran seul, aux mêmes largeurs).
- Regard séparé, si un second agent est possible : `python3 scripts/parcours.py critique /tmp/run13/livrable/planning-kine.html --brief "…"` (images seules et consigne).
- Garder un signal ou un marqueur : construis la variante qui le retire, puis `python3 scripts/planche.py atelier.png /tmp/run13/livrable/planning-kine.html retiree.html --bureau-seul` et compare à la vue.
- Après correction : `python3 scripts/parcours.py verifier /tmp/run13/livrable/planning-kine.html --foyer '#mapPanel' --action '.gap .cand button[data-place]'`

## 6. Lignes mesurables de la trace légère
- Recette : 3 défaut(s) bloquant(s), 3 réserve(s), largeurs 1440, 768, 390 px, action dans le premier écran vérifiée (`.gap .cand button[data-place]`).
- Marqueurs relevés : aucun.
- Poids : fichier 171 Ko ; images 0 Ko (0) ; polices 3 déclaration(s) @font-face, 69 Ko intégrés ; au-delà de 2 Mo pour la page, 500 Ko pour une image ou 300 Ko de polices, un signal [À ADAPTER].
- Signaux de finition : 10 ; captures : 8 fichiers dans `/tmp/run13/work/parcours-v3`.
- Mouvement : 0 animation(s) à l'entrée sur 0 ms, 0 au défilement, 0 liée(s) au défilement, survol de cartes : aucun.


## 7. Limites de la recette
Limites : seules les fautes objectivables sont contrôlées, à l'état et aux largeurs observés. 0 requête(s) externe(s) bloquée(s) : les mesures utilisent alors les polices de repli. Les fonds en dégradé ou en image sont mesurés sur une capture sans texte (pire décile du fond ; quartiles pour un texte tourné) ; les opacités de groupe, le texte rempli par son fond, le texte SVG, le texte natif des contrôles et des pseudo-éléments ne sont pas évalués ; leur présence détectée conserve une réserve. La couverture du contraste est bornée au DOM inspecté ; le contraste non textuel des bordures et des icônes n'est pas mesuré ; celui de l'indicateur de focus ne l'est que pour un contour ou un anneau d'ombre net sur fond uni ; le ratio d'un texte qui passe n'est pas rapporté. L'objet de preuve mesure CSS et rectangle, sans vérifier les pixels ni l'occlusion. Les noms sont des candidats DOM, pas un calcul AccName ; leur présence conserve une réserve. Le clavier porte sur les candidats du périmètre actif et les arrêts observés ; une borne atteinte conserve une réserve. Le mouvement réduit enregistre les animations et transitions démarrées au chargement et au défilement, sur la première largeur ; les animations pilotées par script sans API d'animation du navigateur ne sont pas observées. Les captures montrent l'état observé ; elles ne jugent rien. Le chevauchement de texte est mesuré sur les rectangles de lignes, ramenés à l'interligne, hors calques fixes ou collants ; un texte décoratif superposé (aria-hidden ou très transparent) reste à juger ; il ne voit ni les glyphes ni les recouvrements par une image. Une assertion d'état ne prouve que ce qu'elle exprime, à l'état et aux largeurs observés. Cette recette ne valide ni la direction visuelle, ni le goût, ni l'utilisabilité, ni un verdict global.

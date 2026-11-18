# Parcours — index.html

Mesures et captures en une passe ; rien n'est jugé ici. Chaque signal pose une question : la décision reste au run.

## 1. Défauts bloquants
- **Objet de l’état clé dans son cadre (--in-frame)** : 768 px : #affiche .btn.p : 1 élément(s) sur 1 hors du cadre; 390 px : #affiche .btn.p : 1 élément(s) sur 1 hors du cadre → ACTION/VISUAL_PROOF

## 2. Réserves à vérifier
- Chevauchement et troncature de texte : tronqué, à juger : 768 px : « débord 0,9 s », 390 px : « débord 0,9 s » ; texte SVG compris, calques fixes ou collants exclus
- Contraste du texte sur fond uni : aucun texte évalué sous le seuil WCAG 2.2 AA ; 1440 px : 177 texte(s) évalué(s), 184 candidat(s), 0 exclu(s) ; 768 px : 172 texte(s) évalué(s), 184 candidat(s), 5 exclu(s) … (suite dans `recette.json`)
- Objet de preuve au premier écran (#affiche .poster) : 1440 px : intersection verticale 766.265625 px sur 848.5625, horizontale 600 px sur 600; limites : découpe par un ancêtre non évaluée; 768 px : intersection verticale 790.265625 px sur 999.28125, … (suite dans `recette.json`)
- Noms accessibles calculés par le navigateur à 1440 px : 10 contrôle(s), tous nommés ; la réserve de la recette sur ce point est levée.

## 3. Signaux et questions
- Marqueur de vague relevé : **fond beige ou crème** (vague 2). Corrigé, ou gardé par l'atelier : la variante qui le retire, comparée à la vue. En `STANDARD`, une convention attendue se garde sans atelier.
- Marqueur de vague relevé : **orange rouille** (vague 2). Corrigé, ou gardé par l'atelier : la variante qui le retire, comparée à la vue. En `STANDARD`, une convention attendue se garde sans atelier.
- Marqueur de vague relevé : **libellés mono en capitales** (vague 3). Corrigé, ou gardé par l'atelier : la variante qui le retire, comparée à la vue. En `STANDARD`, une convention attendue se garde sans atelier.
- **Cumul : 3 marqueurs sur le premier écran.** S'ils sont gardés, palette et typographie s'éprouvent ensemble à l'atelier, pas marqueur par marqueur.
- 1440 px · **Texte secondaire** — texte courant en police à chasse fixe : « Proposition : nom de domaine, adresse et… ». La chasse fixe sert-elle ce texte long, ou le fatigue-t-elle ? Geste (`SAVOIR/STATE`) : Corriger d’abord le contraste texte/fond selon `ACTION/GATE-A`, puis régler graisse, position ou espacement pour établir la hiérarchie.
- 1440 px · **Masse visuelle** — 23 tailles de texte : 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 34, 44, 51, 66, 68, 69, 89, 103, 115, 130 px. L'échelle a-t-elle des paliers lisibles, ou des tailles proches qui se concurrencent ? Geste (`SAVOIR/STATE`) : Réduire son échelle, sa densité ou son contraste, ou renforcer le foyer par sa position.
- 1440 px · **Alignement optique** — mot seul en fin de titre : « RÉOUVERTURE SAMEDI 3 AVRIL 2027 » : « 2027 » seul. Rééquilibrer les lignes (text-wrap: balance, insécable) ? Geste (`SAVOIR/STATE`) : Comparer les contours visibles et la ligne de base.
- 1440 px · **Texte secondaire** — texte sous 12 px : 10 px « · ancienne halle aux grains ». Lisible à taille réelle et au zoom ? Geste (`SAVOIR/STATE`) : Corriger d’abord le contraste texte/fond selon `ACTION/GATE-A`, puis régler graisse, position ou espacement pour établir la hiérarchie.
- 1440 px · **Texte secondaire** — texte sous 12 px : 10 px « La Halle ». Lisible à taille réelle et au zoom ? Geste (`SAVOIR/STATE`) : Corriger d’abord le contraste texte/fond selon `ACTION/GATE-A`, puis régler graisse, position ou espacement pour établir la hiérarchie.
- 1440 px · **Typographie fine** — 4 × ponctuation haute sans espace insécable (français) (« 14,8 : 1 »). Caractères et espaces typographiques justes, comme sur un produit fini ? En français : `parcours.py typo PAGE --corriger`. Geste (`SAVOIR/STATE`) : Employer `…` et les guillemets du texte (« » en français, “ ” en anglais).
- 1440 px · **Habillage de gabarit** — 17 points médians entre des mots (« Proposition d’identité · saison 2027 ») ; 12 sur-titres en capitales espacées au-dessus d'un titre (« Après deux ans de travaux »). Chaque marque encode-t-elle une information du contenu (vraie séquence, rubrique), ou apparaîtrait-elle quel que soit le sujet ? Geste (`SAVOIR/STATE`) : Garder la marque qui encode une information du contenu (une vraie séquence, une rubrique qui situe).
- 390 px · **Texte secondaire** — texte courant en police à chasse fixe : « Proposition : nom de domaine, adresse et… ». La chasse fixe sert-elle ce texte long, ou le fatigue-t-elle ? Geste (`SAVOIR/STATE`) : Corriger d’abord le contraste texte/fond selon `ACTION/GATE-A`, puis régler graisse, position ou espacement pour établir la hiérarchie.
- 390 px · **Masse visuelle** — 23 tailles de texte : 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 18, 19, 22, 28, 31, 39, 40, 44, 48, 52, 56, 61 px. L'échelle a-t-elle des paliers lisibles, ou des tailles proches qui se concurrencent ? Geste (`SAVOIR/STATE`) : Réduire son échelle, sa densité ou son contraste, ou renforcer le foyer par sa position.
- 390 px · **Alignement optique** — mot seul en fin de titre : « RÉOUVERTURE SAMEDI 3 AVRIL 2027 » : « 2027 » seul. Rééquilibrer les lignes (text-wrap: balance, insécable) ? Geste (`SAVOIR/STATE`) : Comparer les contours visibles et la ligne de base.
- 390 px · **Texte secondaire** — texte sous 12 px : 8 px « Saison 2027 ». Lisible à taille réelle et au zoom ? Geste (`SAVOIR/STATE`) : Corriger d’abord le contraste texte/fond selon `ACTION/GATE-A`, puis régler graisse, position ou espacement pour établir la hiérarchie.
- 390 px · **Texte secondaire** — texte sous 12 px : 8 px « Après deux ans de travaux ». Lisible à taille réelle et au zoom ? Geste (`SAVOIR/STATE`) : Corriger d’abord le contraste texte/fond selon `ACTION/GATE-A`, puis régler graisse, position ou espacement pour établir la hiérarchie.
- 390 px · **Typographie fine** — 4 × ponctuation haute sans espace insécable (français) (« 14,8 : 1 »). Caractères et espaces typographiques justes, comme sur un produit fini ? En français : `parcours.py typo PAGE --corriger`. Geste (`SAVOIR/STATE`) : Employer `…` et les guillemets du texte (« » en français, “ ” en anglais).
- 390 px · **Habillage de gabarit** — 17 points médians entre des mots (« Proposition d’identité · saison 2027 ») ; 12 sur-titres en capitales espacées au-dessus d'un titre (« Après deux ans de travaux »). Chaque marque encode-t-elle une information du contenu (vraie séquence, rubrique), ou apparaîtrait-elle quel que soit le sujet ? Geste (`SAVOIR/STATE`) : Garder la marque qui encode une information du contenu (une vraie séquence, une rubrique qui situe).
- 1440 px · **Mouvement** — rien ne bouge (ni entrée, ni défilement, ni script). Page faite pour se montrer : un seul moment orchestré servirait-il la promesse ? Page d'outil ou de lecture : rien à justifier. Geste (`SAVOIR/STATE`) : Relier le mouvement à un changement d’état ou à un seul moment orchestré (une entrée, une révélation).
- 1440 px · **Silhouette** — 2 sections de même silhouette (« DESSINÉES, PAS RÉDUITES », « CE QUI NE BOUGE PAS »). Quelle section porte le second moment de la page, et laquelle est volontairement plus calme ? Geste (`SAVOIR/STATE`) : Déplacer ou redimensionner une masse, modifier un recadrage ou un contraste pour rendre la priorité perceptible.
- À regarder, non mesuré : **Partie ordinaire** — navigation, bouton, onglets et pied, logo et titre masqués, appartiennent-ils encore à cette page ? Geste (`SAVOIR/STATE`) : Emprunter à la direction une seule propriété qui ne change pas le comportement : voix typographique, bord dans la logique de l’objet de preuve, couleur par rôle, alignement sur la grille. Sections ordinaires (fonctionnalités, preuve, tarifs, questions, contact, inscription, pied) : `BIBLIOTHEQUE/SECTIONS`.

## 4. Images à regarder
- **D'abord, seule : l'image sans le texte** `/tmp/run12/livrable/parcours-index/regard/sans-texte-1440.png`. Avant d'ouvrir une autre capture et de relire la direction déclarée, écris dans la trace l'idée qui s'y lit en une seconde ; compare ensuite ce nom à la direction. S'ils ne concordent pas, c'est l'idée qui se reprend.
- Ensuite :
  - 1440 px : écran `/tmp/run12/livrable/parcours-index/ecran-1440@2x.png` ; réduite `/tmp/run12/livrable/parcours-index/regard/reduite-1440.png`
  - 390 px : écran `/tmp/run12/livrable/parcours-index/ecran-390@2x.png` ; réduite `/tmp/run12/livrable/parcours-index/regard/reduite-390.png` ; sans le texte `/tmp/run12/livrable/parcours-index/regard/sans-texte-390.png` ; sur téléphone émulé (tactile, 3×) `/tmp/run12/livrable/parcours-index/ecran-390-telephone.png`
- Foyer agrandi : `/tmp/run12/livrable/parcours-index/foyer-1440@2x.png`
- Page entière réduite : `/tmp/run12/livrable/parcours-index/silhouette-1440.png` : le rythme des sections, le second moment, ce qui se répète.
- Mouvement : `/tmp/run12/livrable/parcours-index/mouvement-1440.png` : l'entrée image par image, le défilement et le survol ; le mouvement déclaré se juge ici, pas sur une capture fixe.
- Sans référence fournie : au niveau haut, regarder deux ou trois références réelles du même type et relancer avec `--refs DOSSIER`.

## 5. Prochaine commande
- Pendant la boucle, une version à la fois : `python3 scripts/parcours.py captures /tmp/run12/livrable/index.html --version v2` (premier écran seul, aux mêmes largeurs).
- Regard séparé, si un second agent est possible : `python3 scripts/parcours.py critique /tmp/run12/livrable/index.html --brief "…"` (images seules et consigne).
- Garder un signal ou un marqueur : construis la variante qui le retire, puis `python3 scripts/planche.py atelier.png /tmp/run12/livrable/index.html retiree.html --bureau-seul` et compare à la vue.
- Après correction : `python3 scripts/parcours.py verifier /tmp/run12/livrable/index.html --foyer '#affiche .poster' --action '#affiche .btn.p'`

## 6. Lignes mesurables de la trace légère
- Recette : 1 défaut(s) bloquant(s), 3 réserve(s), largeurs 1440, 768, 390 px, action dans le premier écran vérifiée (`#affiche .btn.p`).
- Marqueurs relevés : fond beige ou crème, orange rouille, libellés mono en capitales.
- Poids : fichier 347 Ko ; images 0 Ko (0) ; polices 16 déclaration(s) @font-face, 210 Ko intégrés ; au-delà de 2 Mo pour la page, 500 Ko pour une image ou 300 Ko de polices, un signal [À ADAPTER].
- Signaux de finition : 16 ; captures : 9 fichiers dans `/tmp/run12/livrable/parcours-index`.
- Mouvement : 0 animation(s) à l'entrée sur 0 ms, 0 au défilement, 0 liée(s) au défilement, survol de cartes : aucun.


## 7. Limites de la recette
Limites : seules les fautes objectivables sont contrôlées, à l'état et aux largeurs observés. 0 requête(s) externe(s) bloquée(s) : les mesures utilisent alors les polices de repli. Les fonds en dégradé ou en image sont mesurés sur une capture sans texte (pire décile du fond ; quartiles pour un texte tourné) ; les opacités de groupe, le texte rempli par son fond, le texte SVG, le texte natif des contrôles et des pseudo-éléments ne sont pas évalués ; leur présence détectée conserve une réserve. La couverture du contraste est bornée au DOM inspecté ; le contraste non textuel des bordures et des icônes n'est pas mesuré ; celui de l'indicateur de focus ne l'est que pour un contour ou un anneau d'ombre net sur fond uni ; le ratio d'un texte qui passe n'est pas rapporté. L'objet de preuve mesure CSS et rectangle, sans vérifier les pixels ni l'occlusion. Les noms sont des candidats DOM, pas un calcul AccName ; leur présence conserve une réserve. Le clavier porte sur les candidats du périmètre actif et les arrêts observés ; une borne atteinte conserve une réserve. Le mouvement réduit enregistre les animations et transitions démarrées au chargement et au défilement, sur la première largeur ; les animations pilotées par script sans API d'animation du navigateur ne sont pas observées. Les captures montrent l'état observé ; elles ne jugent rien. Le chevauchement de texte est mesuré sur les rectangles de lignes, ramenés à l'interligne, hors calques fixes ou collants ; un texte décoratif superposé (aria-hidden ou très transparent) reste à juger ; il ne voit ni les glyphes ni les recouvrements par une image. Une assertion d'état ne prouve que ce qu'elle exprime, à l'état et aux largeurs observés. Cette recette ne valide ni la direction visuelle, ni le goût, ni l'utilisabilité, ni un verdict global.

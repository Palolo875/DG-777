# 14 — SAVOIR/STATE (reste) et SAVOIR/TECH

Lecture du 19 novembre 2026. Tailles des routes :
- `SAVOIR/STATE` : 17,0 k caractères ;
- `SAVOIR/TECH` : 13,2 k.

## 1. Ce que les runs en ont fait (journaux des runs 9 à 16)

| Route | Lue | Proposée par un outil |
|---|---|---|
| SAVOIR/STATE | 3 runs (9, 13, 16) | **19 fois** |
| SAVOIR/TECH | 0 | 1 |

STATE est la route de savoir **la plus proposée** du paquet : la passe de finition et Gate C y renvoient. Les agents la lisent pourtant dans moins d'un cas sur six.

## 2. STATE : ce qu'elle contient

- **Le jugement visuel situé.** Il distingue six lentilles : direction artistique, craft, polish, créativité, goût et spécificité. Il les ordonne en trois niveaux : correction, puis précision, puis intention. La question du niveau 3 : « Quel choix résulte d'un jugement délibéré, serait absent d'une version par défaut, et quelle contrainte sert-il ? »
- **Une table de 18 gestes** (symptôme → geste → réinspection) :
  - rayons, masse, vide, silhouette, surface, chiffres, accent ;
  - détail révélateur, texte secondaire, états, alignement optique, image, mouvement ;
  - **élément de caractère**, **partie ordinaire**, **habillage de gabarit** ;
  - typographie fine.
  Trois de ces gestes ont leur planche avant/après en PNG.
- **Les états pertinents** et la récupération après erreur.

**C'est une table de réparation, pas de direction.** Elle part d'un symptôme observé sur un rendu. Elle améliore ce qui existe ; elle ne choisit pas ce qui doit exister. Trois lignes visent pourtant directement le générique :
- « élément de caractère » : une seule touche tirée du sujet, posée sur une limite ;
- « partie ordinaire » : emprunter à la direction une propriété pour la navigation ou le bouton ;
- « habillage de gabarit » : sur-titres en capitales espacées, numéros 01, 02, 03, mot coloré dans un titre…

**Outillage, vérifié.** L'habillage de gabarit est **déjà détecté** par `parcours.py verifier` (lignes 332 à 499 : surtitres, numéros, flèches, points médians, libellés, tirets ; seuil de 2). `regard.py` mesure de son côté les douze marqueurs de vague (violet, Inter, halo dégradé, fond crème, mono en capitales…).

## 3. TECH : ce qu'elle contient

- **Un ordre d'examen.** P0 : direction, hiérarchie, composition, typographie, matière. Puis P1 : plancher d'usage et d'accessibilité. Puis P2 : traduction dans le runtime.
- **Socle et amélioration progressive** (`[VEILLE 2026-10]`) : `corner-shape`, les animations pilotées par le défilement et `grid-lanes` passent sous `@supports`, avec un repli.
- **« Chercher une méthode »**, avant de coder une technique incertaine (grain sans escalier, texte évidé, graphique), dans cet ordre :
  1. le savoir du système ;
  2. la source primaire datée ;
  3. un exemple ouvert, à adapter ;
  4. **un essai isolé** et capturé avant intégration.
  C'est une bonne pratique pour la qualité d'exécution, et aucun run ne l'a lue.
- **Transitions interactives** (FLIP, View Transitions, interruptions), **mobile**, et **médiums non web** (cinq responsabilités de preuve).
- **Hors périmètre déclaré** : l'e-mail et le parcours d'achat.

## 4. Recherches à côté (Exa et WebSearch)

| Source | Ce qu'elle dit | Ce que ça touche |
|---|---|---|
| Reber, Schwarz & Winkielman 2004, *PSPR* 8(4) | Le plaisir esthétique suit la **fluidité de traitement**. Le contraste figure/fond, la symétrie, la clarté et la prototypicalité rendent un objet plus facile à traiter, donc plus beau. L'effet du contraste **disparaît à 10 s d'exposition**. Il est neutralisé si la personne attribue la facilité à une autre cause. | Explique pourquoi la finition (alignement, contraste, rythme, groupement) augmente la beauté perçue : elle augmente la fluidité. Cela touche surtout la dimension **classique** (note 13), pas l'expressive. |
| Listes de « tells » de l'IA (Impeccable : 59 règles ; guides anti-slop ; Gigazine sur Show HN ; BuiltIn) | Elles nomment le kicker au-dessus du titre, les numéros 01, 02, 03, les capitales espacées, le mot accentué, les sections de même hauteur et Inter par défaut. 10,5 % des sites de Show HN mettent leurs libellés en capitales (chiffre non vérifié). | **Le système est déjà aligné** et outillé (`verifier`, `regard`). Ce sont des avis de praticiens convergents, pas des études. Retirer ces tells enlève le générique visible, mais n'apporte pas de caractère. |

## 5. Constats

**Certain**
- STATE est proposée 19 fois et lue 3 fois. TECH n'a jamais été lue.
- Les marques de gabarit sont déjà détectées par `verifier`. Le paquet n'a pas de manque de détection sur ce point.

**Probable**
- La finition et l'anti-slop agissent sur le plancher : moins de défauts, plus de fluidité, plus de beauté classique. Ils n'agissent pas sur le plafond : présence, caractère, point de vue. C'est cohérent avec ce que Junior a jugé (« générique, cheap » malgré des corrections). Le plafond dépend de la direction (READ, leviers par caractère) et de la sélection (choix externe).
- La proposition d'une route ne suffit pas à la faire lire (19 contre 3). Cela confirme la piste « servir les lignes, pas la route » (notes 12 et 13).

**À vérifier**
- Si les gestes de STATE servis au bon moment changent visiblement le rendu. Avec 3 lectures, rien n'est mesurable. Il faudrait comparer deux rendus d'un même brief, avec et sans service des lignes.

## 6. Pistes (non intégrées, règle 1)

1. **Servir les lignes de STATE qui correspondent aux signaux relevés.** Quand `verifier` relève un signal, il afficherait directement le geste correspondant (une ligne de la table), au lieu de renvoyer à la route. C'est le même principe qu'un registre consultable.
2. **Distinguer plancher et plafond dans le vocabulaire du système.** Finition et anti-slop forment le plancher ; direction, leviers de caractère et sélection forment le plafond. Cela éviterait qu'un rendu « sans tells » passe pour un rendu réussi. C'est une phrase de doctrine, à discuter.
3. **Servir l'essai isolé de TECH dans la fiche `verifier`** quand le rendu contient une technique fragile (grain, trame, texte sur image). Le coût est faible.
4. **Laisser le reste de TECH en l'état** : transitions, mobile et médiums non web sont hors de la série esthétique actuelle.

## Sources
- Reber, Schwarz & Winkielman 2004 (PDF) : https://dornsife.usc.edu/norbert-schwarz/wp-content/uploads/sites/231/2023/11/04_pspr_reber_et_al_beauty.pdf
- Reber et al. (PubMed) : https://pubmed.ncbi.nlm.nih.gov/15582859
- Impeccable, 59 tells : https://botmonster.com/web-dev/impeccable-design-detector-rules-59-ai-design-tells/
- Liste anti-slop (wiki ux-skill) : https://github.com/Laith0003/ux-skill/wiki/Anti-AI-slop-ban-list
- Gigazine, design slop : https://www.gigazine.net/gsc_news/en/20260423-design-slop
- BuiltIn, « AI Makes Bad Design Look Good Enough » : https://builtin.com/articles/ai-design-slop-era
- Corriger le slop, tell par tell : https://capitalandcompute.net/blog/fix-ai-slop-design/

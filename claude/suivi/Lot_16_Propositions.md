# Lot 16 — Propositions : des esquisses à armes égales

Rédigé le 25 novembre 2026, après le run 22. Base : V1.3.0 (`R2026-11-25e`, `master` `54fa7a0`). Aucun run. Règle 1 : rien n'est intégré sans décision ; « D'accord » vaut pour les options A partout.

## 0. Mesure (vérifiée dans les fichiers et le journal du run 22)

| Constat | Preuve |
|---|---|
| **Les références viennent de la catégorie, avant les directions** | Run 22 : galeries de céramique, cartons d'exposition, photos « stoneware glaze », toutes cherchées entre 17 h 39 et 17 h 41 ; planche des esquisses à 17 h 42. |
| **Ce sont les mêmes d'un run à l'autre** (remarque de Junior) | Carton « Frames » de Fonts In Use : 17k et 22e. « Merveilles » de Sèvres : 17k, 19x et 22e. Galerie Lefebvre : 17k et 22e. Requêtes « galerie céramique… grès émaillé… vernissage » : 17k et 17l. |
| **Le système les place là** | Ligne `ANCRE` du noyau : « Avant le premier build […], regarde en image deux ou trois références réelles au niveau visé ». Le détail (`DIRECTION/STANDARD`) dit « du même type d'objet ou du monde du sujet ». Une seule recherche sert donc à la fois à calibrer le niveau et à trouver l'idée. |
| **Les esquisses ne sont pas au même niveau d'investissement** | Planche du run 22 : A a reçu matière, voix et références ; B (cartel) est presque vide ; C (calendrier) a une idée, mais l'exécution d'un tableau de bord. Code : A 2 585 octets et 5 effets ou polices ; B 1 623 et 3 ; C 1 856 et 1. |
| **Rien ne demande l'égalité** | `DIRECTION/DIVERGENCE`, étape 2 : « même contenu », défauts de mise en page corrigés avant de juger, modale « au même niveau ». Rien n'exige que chaque esquisse reçoive son geste, sa voix et sa source, et rien ne le vérifie. |
| **Le rang déclaré (15b) se trompe** | L'idée que les quatre runs ont produite est déclarée « rang 3, ~5 % ». |

Noyau : 31 921 octets sur 33 000 (marge 1 079).

## 1. Sous-lot 16a — Deux usages des références

- **A (recommandée).** Séparer deux usages des références :
  - **Calibrer le niveau** : la recherche faite aujourd'hui (même type d'objet, au niveau visé) reste avant le premier build. Elle est dite pour ce qu'elle est : « elles calibrent le niveau ; elles ne donnent pas l'idée ».
  - **Nourrir une piste** : après avoir écrit les directions, une recherche par direction gardée, partie de son fait de l'inventaire et non de la catégorie. Au moins une recherche se fait **hors du domaine**, dans le monde du fait : pour la céramique, une feuille de cuisson, un four, un registre d'atelier, plutôt qu'une galerie.
  - Chaque esquisse dit sa source dans la trace. `parcours.py references` sert déjà ; rien de nouveau à coder.
- **B.** Déplacer toutes les références après les directions. Je ne la recommande pas : on perdrait la calibration du niveau avant les esquisses, qui a fait progresser les rendus.

## 2. Sous-lot 16b — Des esquisses à armes égales

- **A (recommandée).**
  - **La règle.** Avant la planche, chaque esquisse, la modale comprise, reçoit ce que la gardée reçoit : sa source (16a), l'élément qui porte son idée poussé au niveau d'expression déclaré, sa voix typographique, et sa matière si elle en a une.
  - **Une phrase** : « Une esquisse qui perd faute d'avoir été poussée n'a pas été éprouvée : pousse-la, ou dis pourquoi elle ne peut pas l'être. »
  - **Un signal sur la planche** (`planche.py`). Il relève une esquisse nettement plus plate que les autres : peu de contrastes, de formes ou de textures mesurés sur son image, comparés à ceux de ses voisines. Le message est une question, pas un verdict : « B paraît à plat à côté des autres : poussée au même niveau ? ». Sur la planche du run 22, je m'attends à ce qu'il relève B. À vérifier en l'écrivant.
- **B.** La règle seule, sans signal. Moins de code, mais la consigne « au même niveau » existe déjà pour la modale et n'a pas suffi.

## 3. Sous-lot 16c — Le rang (15b)

- **A (recommandée).** Garder le rang comme incitation à chercher plus loin, mais **ne plus en attendre la diversité**. Le signal de `trace` reste ; une phrase de `DIRECTION/DIVERGENCE` dit que le rang déclaré n'est pas une mesure. Pas d'autre changement avant des runs sur d'autres briefs.
- **B.** Une mémoire des idées déjà vues par catégorie, comme la liste des polices trop vues (`SAVOIR/TOOLS/CONVERGENCE`). Je ne la recommande pas maintenant : un seul cas observé ferait une liste d'interdits, pas un savoir.

## 4. Coût et budget

- **Noyau** : environ 180 octets.
  - Ligne « Diverger sur image » : « chaque esquisse poussée, avec sa source ».
  - Ligne `ANCRE` : « elles calibrent le niveau, pas l'idée ».
  - Noyau prévu : environ 32 100 octets sur 33 000.
- **Par run** :
  - trois recherches et quelques images de plus ;
  - des esquisses plus travaillées, donc plus de tours avant la planche (probable : +10 à +20 tours, non mesuré).
  - Ce coût sert la qualité, comme tu l'as demandé pour l'optimisation : on ne retire pas ce qui est utile.

## 5. Gardes et tests (mutation rouge, échec nommé)

- **CORE-01** : les deux formulations nouvelles du noyau.
- **Signal de planche** : une page d'essai plate à côté de pages travaillées est relevée ; quatre pages travaillées, rien. Mutation : le signal n'est plus émis, et le test doit échouer.

## 6. Ce que le lot ne prouvera pas

- **Que les alternatives deviennent aussi fortes** que la gardée : seule une planche jugée par toi le dira.
- **Que la convergence recule.** Des références par piste peuvent converger à leur tour, si tous les agents tirent les mêmes pistes du même inventaire.
- **Que le signal de planche mesure l'investissement.** Il mesure une platitude visuelle. Une esquisse sobre par choix peut être relevée à tort : c'est pour cela que c'est une question.

## 7. Ordre proposé et vérification

1. **16a et 16b ensemble** (elles se tiennent), plus la phrase de 16c : révision `R2026-11-25f` et publication V1.4.0. Si tu préfères garder les numéros pour des changements plus gros, une V1.3.1.
2. **Puis un run**, sur ta décision, sur un brief neuf d'une ligne. Le juge principal sera la planche des esquisses : sont-elles à armes égales ?

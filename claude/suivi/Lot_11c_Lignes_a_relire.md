# Lot 11c — Les lignes d'invariant, à relire avant intégration

Rédigé le 21 novembre 2026. Base : `R2026-11-15s` (`master` `8a222f6`). **Rien n'est intégré** : ce document est à relire par Junior. Aucun run.

## 0. Ce que j'ai mesuré sur une copie jetable

J'ai retiré du noyau les 16 blocs prévus, sur une copie, sans lignes de remplacement, puis lancé les validations et les tests.

| Mesure | Avant (`s`) | Copie sans les blocs | Avec les lignes (estimation) |
|---|---|---|---|
| Noyau `SKILL.md` | 48 173 octets | 24 674 octets | **≈ 30 300 octets** |
| Tronc DIRECTION | 31 398 caractères | 35 129 caractères | 35 129 caractères |
| Lecture fixe d'un run DIRECTION (noyau + tronc) | ≈ 77 800 caractères | — | **≈ 64 400 caractères (−17 %)** |
| Lecture fixe d'un run LITE, ITER ou STANDARD | noyau entier | — | **≈ −37 %** sur le noyau |

**Deux écarts à la proposition, que je signale.**

1. **La cible de 25 000 octets n'est pas tenable en 11c.** Les lignes ajoutent environ 4 400 octets, et trois petits blocs d'obligation restent (voir § 2). On arrive vers 30 300. La suite de la baisse viendra de 11d (réécriture courte des blocs gardés).
2. **En DIRECTION, le gain est plus faible que prévu** (−17 % au lieu de −28 %). La raison : `DIRECTION/DIVERGENCE`, `DIRECTION/CREATIVE-BOOT` et `DIRECTION/STANDARD` font partie du tronc DIRECTION. Tant que leurs blocs étaient au noyau, le tronc les repliait ; une fois retirés du noyau, ils reviennent dans le tronc. **C'est sain** : un run DIRECTION lit toujours la procédure entière, une fois ; les autres modes ne la lisent plus.
   - Conséquence : le tronc DIRECTION dépasse son budget (35 129 sur 35 000).

## 1. Comment les lignes vivent dans les sources

- Chaque ligne est un **petit bloc du noyau**, écrit dans le même fichier, **juste avant le bloc qu'elle résume**. Le bloc complet passe en « différé », servi par sa route.
- La ligne et son bloc restent donc côte à côte : qui modifie l'un voit l'autre.
- Les obligations `[REQUIS]` passent à la forme « ligne » de 11a (étiquette et route sur la même ligne, texte complet dans la route).

## 2. Ce qui reste au noyau tel quel

Trois blocs d'obligation sont déjà courts. Les remplacer par une ligne ne gagnerait presque rien et ferait perdre la formulation exacte :
- `COMP-TYPO` (213 octets), `COMP-CONTROLES` (476), `COMP-COULEUR` (532).

## 3. Les lignes, à relire

Pour chacune : le bloc remplacé, sa taille, et la ligne qui le remplace. Le texte complet du bloc reste servi par la route nommée en fin de ligne.

### L1 — remplace `DIR-LEVIERS` (4 973 octets) · ligne de 595 octets

> [REQUIS PAR LE MODULE — premier écran, identité ou scène d’une surface `DIRECTION` dont la décision visuelle est ouverte ; pas pour un correctif local] **Diverger sur image**, avant le premier build : cinq directions avec leur probabilité, dont la modale (ta première idée astucieuse est la modale au second degré) ; trois esquisses moins probables en premier écran complet, aussi à 390 px pour un produit d’abord mobile ; choix sur la planche, face à la modale ; puis atelier et `verifier`. Décision étroite : trois directions, une esquisse. Détail : `DIRECTION/DIVERGENCE`.

### L2 — remplace `DIR-DECLARATION` (2 897 octets) · ligne de 564 octets

> [REQUIS PAR LE MODULE — surface `DIRECTION`, ou surface `STANDARD` ou `ITER` dont la décision visuelle est ouverte] **Déclarer la direction** avant de construire la suite : `DIRECTION`, `VISION`, `REGISTRE` (une base et un modificateur pris dans deux dimensions du registre : composition, matière, représentation, époque et culture, densité, interaction, voix), `NIVEAU`, `ASSET`, `COMPOSANT`, `FINITION`, `MOUVEMENT`, `MOBILE`, en mots qui se vérifient sur capture. Après la capture, chaque ligne est vue ou se corrige. Détail : `DIRECTION/DIVERGENCE`.

### L3 — remplace `MOY-PLAFOND` (3 444 octets) · ligne de 422 octets

> **Atteindre avant de déclarer.** Sur une décision visuelle ouverte, le niveau visé est haut. Un plafond ne se déclare qu’après un essai par couche qui porte la thèse, écrit dans la trace : atteinte, échec ou interdite. Ce qui est codable se code ; un sujet figuratif ne se dessine pas de mémoire. Génération d’image et outil branché attendent l’accord de la personne. Détail : `DIRECTION/CREATIVE-BOOT`.

### L4 — remplace `ANCRE` (2 078 octets) · ligne de 425 octets

> [REQUIS PAR LE MODULE — surface `DIRECTION`] **Ancre et calibration.** Accepter une direction identitaire exige une ancre ; sans elle, la direction reste `EXPLORATORY`. Avant le premier build d’une décision visuelle ouverte, regarde en image deux ou trois références réelles au niveau visé, avec leur provenance et une ligne de jugement chacune ; sans accès, dis-le. Détail : `DIRECTION/STANDARD`, `SAVOIR/SOURCE`.

### L5 — remplace `BOUCLE-ATELIER` (3 904 octets) · ligne de 408 octets

> **Atelier sur capture.** Sur une surface `DIRECTION`, après la première capture, au moins un tour, même en trace légère : lecture sans le texte, test de retrait, défaut dominant corrigé et recapturé ; il est requis dans le scope de B1b. Avant de livrer, la passe de finition, par lots, jusqu’à ce que `verifier` ne laisse aucun signal sans correction ni raison. Détail : `ACTION/ATELIER-EDITION`.

### L6 — remplace `BOUCLE-CAPTURE` (569 octets) · ligne de 323 octets

> **Revue sur capture** : quatre questions vérifiables sur l’image de la page entière (où va l’œil ; le plus grand élément l’est-il à juste titre ; quelle section s’échangerait ; qu’enlèverait un directeur artistique). Une faiblesse de craft ouvre Gate C (`ACTION/GATE-C`). Détail : `SAVOIR/CRAFT/CFT-00`.

### L7 — remplace `STRUCT-TRAME` (703 octets) · ligne de 277 octets

> **Test de trame.** Avant de fixer la structure, écris en une ligne l’ordre de sections que toute IA produirait pour ce brief, puis romps-le ou garde-le par ce que la personne doit voir, comprendre ou faire d’abord ; renommer ne suffit pas. Détail : `BIBLIOTHEQUE/SELECT`.

### L8 — remplace `COMP-SINGULARITE` (633 octets) · ligne de 256 octets

> **Singularité.** Sans logo ni nom, qu’est-ce qui reste propre au produit ? Le genre se reconnaît au premier regard ; la singularité se joue d’abord dans l’objet, la donnée, la voix, la matière ou le détail. Détail : `SAVOIR/FRAME/SINGULARITE`.

### L9 — remplace `COMP-CONVERGENCE` (846 octets) · ligne de 341 octets

> **Question de convergence.** Si la palette et la police de titre sont celles que le modèle prendrait sans brief, nomme ce qui les justifie dans le produit, ou prélève-les sur le sujet ; compare deux voix sur le vrai titre (`SAVOIR/TYPE-VOIX`). Un choix convergent reste valide s’il tient sur la planche. Détail : `SAVOIR/CRAFT/CFT-05`.

### L10 — remplace `COMP-TITRE` (957 octets) · ligne de 225 octets

> **Équilibre d’un titre** qui porte la scène : réglé sur le vrai texte, puis corrigé sur capture, en desktop et en mobile (coupes qui gardent le sens, lignes équilibrées, écart d’échelle). Détail : `SAVOIR/TYPE`.

### L11 — remplace `VER-SCENE + VER-AUDIENCE` (802 octets) · ligne de 359 octets

> **Vérité de la scène.** Un marquage local près du claim ou de l’objet : `OBSERVED` ou `ILLUSTRATIVE` (la fiction l’emporte), plus `MECHANISM` s’il y a lieu. Les labels `TRUTH/*` restent internes ; un artefact fictif le dit visiblement, en langage produit (« données d’exemple », « image générée »). Détail : `DIRECTION/DIRECTION-ATELIER`.

### L12 — remplace `REGISTRES` (456 octets) · ligne de 228 octets

> **Listes closes.** Modes, gates, axes `V/U/A/T`, états, verdicts, statuts et champs de `RUN_CARD` ne prennent que les valeurs de leurs sections propriétaires ; aucune vue ni aucun outil n’en crée. Détail : `ACTION/STATUS`.

**Total des lignes** : 4 423 octets pour 13 blocs qui en font 22 262.

## 4. Gardes et tests qui cassent, et ce que je propose

Sur la copie sans les blocs, 18 tests échouent. Je les reprendrai un par un à l'intégration. Le rapport dira, pour chacun, s'il est gardé, adapté ou déplacé vers la route.

| Garde ou test | Pourquoi il casse | Proposition |
|---|---|---|
| `REQ-01` : 6 planchers en forme « bloc au noyau » | Les blocs quittent le noyau | Passage en forme « ligne » (11a), pour `DIR-LEVIERS`, `DIR-DECLARATION` et `ANCRE` |
| `CORE-01` : 5 phrases exigées au noyau (revue sur capture en quatre questions, activation de Gate C, esquisses aussi en mobile, planchers couleur et typographie) | Leur texte part avec les blocs | Les lignes L1 et L6 les portent ; les planchers couleur et typographie restent au noyau (§ 2) |
| `REG-01` : liste des dimensions du registre au noyau | Elle était dans `DIR-LEVIERS` | La ligne L2 la porte |
| `CHG-10` et 5 tests de `read_route` : budget du tronc DIRECTION | +3 731 caractères | **A** : budget du tronc à 36 000 caractères ; **B** : réduire le tronc ailleurs |
| 7 autres tests de `test_audit_regressions` (relais de ressources, contrôles A du tronc, séquence, trace) | Ils lisent un texte qui vivait dans les blocs | Revue une par une : adapter le test à la route quand l'obligation y reste servie |

## 5. Décisions demandées

1. **Les lignes** : à valider, corriger ou réécrire. Ce sont elles que tout agent lira.
2. **La cible de 11c** : **A (recommandée)** : budget du noyau à 31 000 octets en 11c, puis la suite de la baisse en 11d ; **B** : tenir 25 000 dès 11c, avec des lignes beaucoup plus courtes, au risque de perdre des nuances.
3. **Le tronc DIRECTION** : **A (recommandée)** : budget à 36 000 caractères, puisqu'il reprend un texte que le noyau portait ; **B** : le réduire ailleurs.

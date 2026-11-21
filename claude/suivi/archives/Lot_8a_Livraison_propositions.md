# Lot 8 — Passe de livraison : propositions (partie a)

18 novembre 2026. Révision de départ : `R2026-11-15i`. Document hors du paquet. Rien n'est intégré.

## 0. Je signale un lot surdimensionné

Le lot 8 réunit deux travaux de nature différente :
- **8a — les constats restants.** Treize constats précis et deux questions reportées des lots 4 bis et 7. Ce document les traite.
- **8b — la passe des sept critères de livraison** (plan, § 1 bis). Elle commence par des mesures : point d'entrée, un lieu par sujet, aucun reste, lisibilité, langue, charge de procédure, prêt à l'usage. Les corrections viennent ensuite. Elle mérite ses propres propositions, chiffres à l'appui.

Je propose de livrer 8a, puis 8b, chacun avec sa révision. Trois constats ne se jugent bien qu'avec les mesures de 8b : ils y passent (§ 4).

## 1. Déjà corrigés

| Constat | Corrigé au lot | Vérifié aujourd'hui |
|---|---|---|
| A-22 — restes de l'ancien rangement | S et 2 | Le dossier `sections/` et les tables « Document » n'existent plus |
| D-09 — une cellule de 3 842 caractères dans le README des scripts | 2 | La plus longue cellule fait 561 caractères |
| F-11 — cellules illisibles dans la fiche de version | 6 | La table est sortie ; la plus longue cellule fait 426 caractères |

## 2. Corrections sans choix

### F-09 — une note mal alignée sur la carte, en mobile

**Vérifié à 390 px.** Sous « Les responsabilités reliées », la note « Carte de responsabilités, pas un ordre fixe d'exécution » est centrée dans une boîte de 176 px, en retrait du titre.

**Changement.** En mobile, la note s'aligne à gauche, sous le titre. Les cartes sont régénérées par leur générateur (`supports/generer.py`), puis la fraîcheur est contrôlée.

### E-09 — une liste de principes de plus dans l'intégrité

**Vérifié.** `SAVOIR/INTEGRITY` porte « Règles d'or — lecture rapide » : huit règles dont chacune a déjà son propriétaire (classement, cadrage, preuves, override). La section se décrit elle-même comme « pas une procédure ».

**Changement.**
- « Règles d'or » est retirée : chaque règle reste chez son propriétaire, rien ne se perd.
- « REPASSE — méthodologie studio », appelée par la table des signaux, reste. Elle prend un titre qui dit ce qu'elle contient : « REPASSE — repasse ciblée, selon le mode ».

### E-04 — 113 étiquettes en capitales

**Vérifié.**
- Les règles comptent 211 codes en capitales distincts : modes, statuts, champs.
- Ce sont des codes lus par les validateurs et par la fiche `RUN_CARD`. Les traduire casserait les schémas.
- Vous avez fixé le critère « Langue » : un mot français pour chaque notion qu'une personne rencontre ; les codes restent là où une machine les lit.
- Les guides et le README en citent 18. Un seul manque au glossaire : `CORRECTION`.

**Changement.**
- `CORRECTION` entre au glossaire.
- Une garde vérifie que tout code en capitales cité dans les guides ou le README a sa ligne au glossaire.
- Les codes restent dans les règles.

### D-13 — un budget en octets, l'autre en caractères

**Vérifié.** Le noyau se compte en octets (46 000) : c'est le poids du fichier chargé par l'hôte de la skill. Le tronc se compte en caractères (35 000) : c'est ce que l'agent lit. Les deux unités sont justes, mais rien ne le dit.

**Changement.** Une phrase dans les « Contrats de maintenance » de `maintenance/evolution.md` dit pourquoi chaque budget a son unité.

### D-18 — des archives datées de 1970

**Vérifié.** Pour que les archives soient reproductibles, le build date tous les fichiers de l'origine du calendrier informatique, faute de date donnée (`SOURCE_DATE_EPOCH` vaut 0). Une fois décompressés, les fichiers affichent le 1er janvier 1970.

**Changement.** La date par défaut devient celle du dernier commit (`git log -1 --format=%ct`). Les archives restent reproductibles pour un même commit et portent une date vraie. Hors dépôt git, la date reste fixe et se déclare.

## 3. Corrections avec un choix

### E-11 — trois routes sans rapport de moment dans un même fichier

**Vérifié.** `gouvernance/travail.md` (37 k) porte trois routes :
- `ACTION/PRECONDITION` : conditions avant d'agir ;
- `ACTION/RUN_CARD` : fiche de travail ;
- `ACTION/PIPELINE-DIRECTION` : déroulé de fabrication, huit étapes.

| Option | Changement |
|---|---|
| **A (recommandée)** | `ACTION/PIPELINE-DIRECTION` part dans un fichier à lui, `gouvernance/pipeline.md` (environ 12 k). `travail.md` garde les conditions et la fiche, ce que dit son titre. Le lecteur retrouve la route par son code, sans rien changer ailleurs ; seuls les liens des guides vers l'ancien fichier sont mis à jour, et le test de déplacement les nomme. |
| B | Ne rien déplacer. |

### E-12 — une « vue d'exécution » sans usage

**Vérifié.** Dans `ACTION/RUN_CARD`, « Vue d'exécution dérivée » ajoute un gabarit de douze champs (`EXECUTION-SNAPSHOT`). Aucun autre fichier, schéma ni outil ne l'emploie. Les quatre paragraphes qui suivent disent en revanche des règles de reprise utiles : relation ouverte, effet attendu, réexamen après un changement. La condition de façade LCF-54 les garde.

| Option | Changement |
|---|---|
| **A (recommandée)** | Retirer le gabarit de douze champs et le nom `EXECUTION-SNAPSHOT`. Garder les paragraphes de reprise, sous le titre « Reprendre un run ». LCF-54 suit le nouveau titre. |
| B | Tout garder. |

### F-10 — des exemples qui montrent surtout des traces complètes

**Vérifié.** Sur les cinq exemples de `references/examples.md`, un seul montre une trace légère. Les quatre autres montrent une trace complète, dont trois avec verdict. Or la trace légère est celle par défaut, et c'est celle que les runs produisent.

| Option | Changement |
|---|---|
| **A (recommandée)** | « DIRECTION — première scène identitaire » et « DIRECTION + STYLE » passent en trace légère, aux six lignes que la commande `parcours.py trace` contrôle ; un test vérifie que la commande les accepte. La forme courte LITE et le composant partagé SYSTÈME gardent leur trace complète : c'est leur cas réel (clôture, run partagé). On a alors trois traces légères pour deux complètes. |
| B | Ne rien changer. |

### Typographie de lecture : quel propriétaire ? (question du lot 4 bis)

**Vérifié.** Le corps de 16 px, l'interligne et la mesure de 45 à 80 signes sont dans `SAVOIR/CONTEXT`. `SAVOIR/TYPE` n'en dit rien.

| Option | Changement |
|---|---|
| **A (recommandée)** | Le corps, l'interligne et la mesure passent dans `SAVOIR/TYPE`, propriétaire de la typographie. `SAVOIR/CONTEXT` garde ce qui relève de l'accessibilité (espacement agrandi, 320 px, texte en image) et renvoie à `SAVOIR/TYPE` pour le reste. Coût : environ 250 caractères au tronc `DIRECTION`, sur 3 840 de marge. |
| B | Laisser où c'est, avec un renvoi depuis `SAVOIR/TYPE`. |

### B-20 — 30 gabarits de formulaire

**Vérifié.**
- Les 30 blocs font 13 k en tout. Chacun n'est lu que par sa route.
- Ils mêlent deux séparateurs : « CHAMP — description » et « CHAMP: valeur ».
- Plusieurs validateurs et la commande `trace` lisent les lignes `CHAMP:` des traces produites.

| Option | Changement |
|---|---|
| **A (recommandée)** | Écarter, avec raison. Unifier les séparateurs changerait ce que lisent les validateurs et les traces des agents, sans gain pour un lecteur, qui ouvre ces gabarits un à un. |
| B | Unifier le séparateur des gabarits à remplir sur « — » et réserver « : » aux exemples remplis, en adaptant les validateurs. |

## 4. Passent à 8b

| Constat | Pourquoi là |
|---|---|
| F-06 — 69 k de guides et de glossaire qui redisent le système | C'est le critère « un lieu par sujet ». La mesure dira quelles redites retirer, et chaque retrait vous sera montré. |
| F-13 — installation « vérifiée le 14 octobre » | C'est le critère « prêt à l'usage » : je rejouerai l'installation depuis une copie propre, puis la date sera mise à jour ou la phrase corrigée. |
| Le reste des sept critères | Mesures d'abord, propositions ensuite. |

## 5. Vérification prévue (8a)

1. Branche `livraison-a`.
2. Tests :
   - la garde du glossaire, avec sa mutation rouge (un code absent) ;
   - la date des archives, non nulle et identique sur deux builds du même commit ;
   - selon les options : `parcours.py trace` accepte les deux nouveaux exemples, et la route du déroulé est servie depuis son nouveau fichier ;
   - planchers de trouvabilité, troncs et noyau mesurés avant et après.
3. Capture de la carte corrigée à 390 px, jointe au rapport.
4. Validation complète avec navigateur, révision `R2026-11-15j`.

**Critère d'arrêt.** Si le déplacement du déroulé casse un lien que le test de déplacement ne nomme pas, je m'arrête et je vous le montre.

## 6. Ce qu'il faut me dire

« D'accord, options A partout » suffit, avec ou sans le découpage 8a puis 8b.

# Lot 3 — Une seule voix : propositions

15 novembre 2026. Révision de départ : `R2026-11-15a`. Document hors du paquet. Rien n'est intégré.

Ce lot ne change pas ce que le système demande. Il fait en sorte que chaque chose soit dite une fois, ou que ses formes multiples soient reliées et hiérarchisées. J'ai relu les 13 constats dans les fichiers actuels. Il y a les 12 constats du plan, plus la partie d'E-05 laissée au lot 2 : la table des conditions de départ est une troisième table « par mode ».

| Sort | Constats |
|---|---|
| Déjà corrigé | D-06 (lot 1). A-12 en partie (lot S). |
| À corriger, sans choix à faire | A-02, A-03 avec B-10, A-12, B-05, B-07, B-11 |
| À corriger, avec un choix | D-03, A-15 avec D-12, F-05, E-05 (table) |

**Ce que cela coûte.** Aucune correction ne touche le noyau compilé ni un tronc. Aucune ne touche une règle absolue. Ce sont des tables complétées, des phrases de rattachement et deux retraits de doublons. Le choix A-15 / D-12 touche aussi le code des outils.

---

## 1. Déjà corrigé

| Constat | Ce que j'ai vérifié |
|---|---|
| D-06 — les marqueurs de vague vivent en trois endroits | Depuis le lot 1, une seule fonction lit la liste datée. Le validateur échoue si un marqueur listé n'est ni protégé ni déclaré (VAG-01). L'outil de regard affiche « non mesuré » pour un marqueur qu'il ne sait pas relever. Une quatrième vague ne passerait donc plus inaperçue. Les trois listes existent toujours, mais elles sont tenues par la liste datée. |
| A-12, en partie | Trois des six lieux qui disaient quoi charger ont disparu avec `sections/`. Le reste est traité au § 2. |

---

## 2. Corrections sans choix

### A-02 — la déclaration manque à la table des cadres

**Constat vérifié.** `DIRECTION/CADRES` réconcilie six vues d'une même direction : cible, cadrage du noyau, Creative Boot, atelier, trace légère, `RUN_CARD`. La déclaration en neuf lignes, pourtant exigée à chaque run où la décision visuelle est ouverte et la seule que les runs écrivent, n'y figure pas.

**Changement.**
- Ajouter une colonne « Déclaration » et la remplir : Promesse et objet de preuve → `VISION` ; Ancre et moyens → `ASSET`.
- Ajouter cinq lignes pour ce que seule la déclaration porte : Registre (`REGISTRE`), Niveau visé (`NIVEAU`), Composants et finition (`COMPOSANT`, `FINITION`), Mouvement (`MOUVEMENT`), Mobile (`MOBILE`). Les autres vues y indiquent leur équivalent quand il existe, par exemple la question « Mouvement » de la revue créative.
- Ajouter une phrase : « La déclaration est la vue écrite à chaque run où la décision visuelle est ouverte ; les autres ne se remplissent que lorsque leur moment ou leur niveau de trace le demande. »
- `RUN-PRIORITY` n'est pas un cadre mais un ordre de priorité : il est traité avec B-11.

**Ce que je ne fais pas ici.** Décider que le Creative Boot et la cible deviennent des vues de trace complète. C'est le constat A-01, au lot 4, parce que cela change ce qui arrive à l'agent.

### A-03 et B-10 — trois systèmes d'axes, sans ordre entre eux

**Constat vérifié.** Trois systèmes coexistent :
- les **axes d'expression** de `CFT-02` (12) ;
- les **axes de tension** de `BIBLIOTHEQUE/TENSION` (7) ;
- les **dimensions du registre** (7), au noyau et dans la taxonomie de `SAVOIR/STYLE`.

Les deux premiers sont reliés par le texte (l'expression d'un côté, la structure de l'autre). Les dimensions du registre ne sont reliées à aucun des deux, alors qu'elles recouvrent sept axes de `CFT-02` sous d'autres noms. `DIVERGENCE` dit de situer l'idée sur `CFT-02` et le noyau de diverger par le registre ; rien ne dit lequel prime.

**Changement.**
1. Dans la taxonomie de `SAVOIR/STYLE`, une colonne « Axes de `CFT-02` » donne la correspondance :

| Dimension du registre | Axes de `CFT-02` |
|---|---|
| Composition | Structure, Rythme |
| Matière et rendu | Matière |
| Représentation | Matière, Texte / image |
| Époque et culture | Temporalité |
| Densité et énergie | Densité, Intensité émotionnelle |
| Interaction et temps | Mouvement |
| Voix et comportement | Voix, Formalité |

2. Une phrase dans `DIRECTION/DIVERGENCE`, là où l'on situe l'idée, dit l'usage de chacun : « Pour diverger et nommer le registre, les dimensions du registre ; pour une alternative située, les axes de `CFT-02`, dont elles regroupent sept ; pour la structure, les axes de tension. »
3. `CFT-02` (« la seule liste d'axes d'expression ») ajoute que les dimensions du registre y renvoient.
4. Les listes partielles du noyau (cinq axes de tension) et de `DIVERGENCE` (six axes d'expression) sont des exemples : `DIVERGENCE` dit « notamment ». Le noyau ne change pas.

Le noyau garde ses sept dimensions.

### A-12 — « zéro à deux routes », contre un tronc de huit

**Constat vérifié.** `SAVOIR/READ` dit : « Charge typiquement zéro à deux routes ». Le tronc du mode DIRECTION en charge huit, par conception. Les runs en ouvrent sept à treize.

**Changement.**
- « Charge typiquement zéro à deux routes » devient « Au-delà du tronc de ton mode, charge typiquement zéro à deux routes de SAVOIR ».
- La dernière phrase de la route (« Les anciens identifiants de section… ») est retirée. C'est le même reste que la phrase retirée au lot 2 ; je l'avais manquée.

### B-05 — sept grilles pour juger un rendu

**Constat vérifié.** La table « Rattachement des grilles » de `SAVOIR/CRAFT` relie quatre grilles : revue créative, `CFT-00`, contrat du premier objet, Gate C. Trois en sont absentes :
- la **revue sur capture** en quatre questions, alors que c'est la grille de travail en trace légère ;
- le **jugement visuel situé** de `SAVOIR/STATE` ;
- le **premium perçu** de `SAVOIR/FRAME`.

De plus, Gate C se dit « obligatoire en `DIRECTION` », puis applicable sans verdict en trace légère : les deux phrases sont à vingt lignes l'une de l'autre.

**Changement.**
- Une colonne « Revue sur capture » en tête de la table, qui rattache chacune de ses quatre questions aux lignes.
- Une phrase qui situe les deux autres grilles. Le jugement visuel situé est la grille des gestes de finition, ouverte sur un défaut de finesse. Le premium perçu est la traduction du mot « premium » en relations, ouverte quand un brief l'emploie.
- Gate C commence par : « En trace complète, il est obligatoire en `DIRECTION` […] ; en trace légère, voir la fin de la route. »
- Que les six critères de Gate C n'arrivent pas au noyau relève du lot 4.

### B-07 — trois listes de rôles d'asset

**Constat vérifié.** `SAVOIR/SOURCE` porte trois listes de rôles d'asset qui ne se recouvrent pas :
- une liste de six rôles (« photo du sujet, texture, lumière… ») ;
- une table de huit rôles, « Routes par rôle » ;
- une liste de onze rôles fonctionnels dans l'atlas (« preuve produit, contenu, identité, orientation… »).

La table renvoie à l'atlas, mais leurs vocabulaires diffèrent.

**Changement.**
- **L'atlas devient le seul vocabulaire.** Chaque ligne de la table nomme entre parenthèses le rôle de l'atlas qu'elle sert ; certaines le font déjà. Par exemple, Personne → contenu, preuve produit ; Objet → preuve produit, contexte ; Illustration → contenu, atmosphère.
- **Une ligne explicite pour les trois rôles sans route.** Pour orientation, média temporel et modèle spatial, la route se décide dans `DIRECTION/ASSET-ROUTE`, selon le médium (`SAVOIR/TECH`). Je n'invente pas d'ordre de routes pour eux.
- **La liste de six rôles est retirée.** Elle devient « Pars du rôle de la matière (« Routes par rôle », ci-dessous) ».

### B-11 — cinq ordres de construction ou de jugement

**Constat vérifié.** Cinq ordres coexistent, et deux seulement sont reliés entre eux :

| Ordre | Ce qu'il dit | Où |
|---|---|---|
| Ordre de décision | JTBD → structure → hiérarchie → lisibilité → accessibilité → système visuel → polish | `SAVOIR/FRAME` |
| Compilation de la cible | contexte réel → promesse → tension → … → premier rendu jugeable | `DIRECTION/VISUAL_TARGET` |
| Séquence de composition | intention → tension → foyer → … → retenue | `SAVOIR/FRAME` |
| Ordre de jugement | `P0` → `P3` | `SAVOIR/TECH` |
| `RUN-PRIORITY` | TRUTH → DIRECTION → FIRST-OBJECT → FINISH | `DIRECTION/EXTERNAL-START` |

**Changement.** Une phrase, sous l'ordre de décision de `SAVOIR/FRAME`, donne le rôle de chacun : « Cet ordre dit ce qui prime quand deux exigences se contredisent. Il ne dit ni dans quel ordre construire (la compilation de `DIRECTION/VISUAL_TARGET`, puis la séquence de composition ci-dessous), ni dans quel ordre examiner un rendu (`P0` à `P3`, `SAVOIR/TECH`), ni dans quel ordre corriger une démonstration sur brief vague (`RUN-PRIORITY`, `DIRECTION/EXTERNAL-START`). » `RUN-PRIORITY` et `P0–P3` reçoivent un renvoi vers cette phrase.

---

## 3. Corrections avec un choix

### D-03 — trois tables de renvoi échappent à la garde « une seule table de signaux »

**Constat vérifié.** La garde SIG-01 reconnaît une table de signaux à son en-tête (« Signal », « Situation »… puis « Route »). Trois tables renvoient pourtant vers des routes sous un autre en-tête :
- les critères de Gate C (« Geste si absent (route à charger) ») ;
- le vocabulaire de `SAVOIR/STATE` (« savoir à approfondir ») ;
- les familles de l'atlas (« Route approfondie »).

Elles sont lues pendant leur route, et non au départ d'un run : elles envoient d'un critère vers son propriétaire.

| Option | Changement |
|---|---|
| **A (recommandée)** | Écrire le principe : seules `DIRECTION/CHARGE` et la table des signaux du noyau disent quoi charger au départ ; une table qui, dans une route, renvoie d'un critère à son propriétaire est un renvoi local. La garde SIG-01 reconnaît désormais toute table dont une colonne nomme une route à charger ou à approfondir. Les trois tables actuelles sont déclarées, chacune avec sa raison ; une nouvelle table de ce genre échoue tant qu'elle n'est ni retirée ni déclarée. Le message de succès dit « une table de signaux, trois renvois locaux déclarés ». |
| B | Retirer la colonne de route des trois tables, en mettant le renvoi dans le texte. Les tables perdent une information utile à l'agent pendant la lecture. |

### A-15 et D-12 — 66 blocs marqués « noyau », dont 31 n'y sont pas

**Constat vérifié.** Dans les fichiers de règles, 66 blocs sont encadrés par `<!-- noyau:début … -->` :
- 35 sont compilés dans le noyau ;
- 31 sont seulement servis par leur route : ce sont les blocs « différés », que `build_core.py` vérifie servis en entier et activés par un renvoi.

Le nom de la balise trompe le mainteneur.

| Option | Changement |
|---|---|
| **A (recommandée)** | Les blocs différés prennent la balise `<!-- différé:début ID -->`. `build_core.py`, le lecteur et les validateurs suivent. Une garde nouvelle vérifie que la balise d'un bloc correspond à son registre : un bloc `noyau` est compilé, un bloc `différé` est servi par sa route. Changement mécanique, sans effet sur le texte servi ni sur le noyau. |
| B | Garder les balises et l'expliquer dans la maintenance. |

### F-05 — trois tables d'orientation dans les guides, dont une affichée à l'agent

**Constat vérifié.** Le niveau 2 des guides porte la carte des sujets, les combinaisons et les angles. Ces tables sont écrites pour les personnes. La carte des sujets apparaît pourtant à l'agent, en tête d'une recherche `--trouver` qui nomme un sujet : elle sert à classer le propriétaire du sujet en premier.

| Option | Changement |
|---|---|
| **A (recommandée)** | Garder ce fonctionnement et le dire là où l'agent lit le lecteur (`DIRECTION/CHARGE`, « Retrouver un savoir ») : la ligne « SUJET » de `--trouver` oriente vers le propriétaire ; elle n'ajoute aucune lecture au-delà de la règle de `SAVOIR/READ`. Les combinaisons et les angles restent pour les personnes. Ce constat est écarté avec cette raison. |
| B | Retirer la ligne « SUJET » de la sortie de `--trouver`. On perd le classement par propriétaire, qui fait monter la bonne route sur les termes larges ; un test de trouvabilité le protège. |

### E-05 (table) — une troisième table « par mode »

**Constat vérifié.** La table des conditions de départ (`ACTION/PRECONDITION`) décrit, par mode, ce qu'une trace complète doit établir. Le paquet de clôture (`ACTION/CLOSE-PACKAGE`) décrit ce qu'elle livre, et ses lignes recouvrent presque toutes celles de la première. Ce qui ne figure que dans la table des conditions est déjà dans les lignes de `DIRECTION/CHARGE` et dans le déroulé `DIRECTION` : JTBD et arbitrage en STANDARD, alternative et comparaison en DIRECTION.

| Option | Changement |
|---|---|
| **A (recommandée)** | Retirer la table. À sa place : « Ce qu'un mode charge est dans la ligne de `DIRECTION/CHARGE` ; ce qu'il doit établir et livrer en trace complète, dans le paquet de clôture (`ACTION/CLOSE-PACKAGE`). » La phrase ajoutée au lot 2 part avec la table. La règle `N/A-JUSTIFIED` / `NOT-VERIFIED` (concept HON-06) qui la suit reste. Le libellé de la condition LCF-39, qui cite cette route, est mis à jour. |
| B | Garder la table, déjà réservée à la trace complète depuis le lot 2. |

---

## 4. Vérification prévue

1. Branche `voix`.
2. Tests existants, plus :
   - SIG-01 élargie, avec sa mutation rouge (une table de renvoi non déclarée échoue) ;
   - si A-15 option A : la garde de correspondance entre balise et registre, avec sa mutation rouge ;
   - la correspondance entre dimensions du registre et `CFT-02`, contrôlée : chaque dimension nommée au noyau a sa ligne dans la table de `SAVOIR/STYLE`.
3. Noyau compilé identique octet par octet ; troncs inchangés.
4. Validation complète avec navigateur, archives régénérées, révision `R2026-11-15b`.
5. Registre : chaque constat passe à « corrigé », « déjà corrigé » ou « écarté, avec raison ».

**Critère d'arrêt.** Si une correction demande de toucher au noyau ou à un tronc, je m'arrête et vous la montre.

## 5. Ce qu'il faut me dire

« D'accord, options A partout » suffit. Sinon : les corrections du § 2 à écarter, et l'option choisie pour D-03, A-15 / D-12, F-05 et E-05 (table).

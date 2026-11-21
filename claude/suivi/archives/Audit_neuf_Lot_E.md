# Audit neuf — Lot E : la gouvernance

13 novembre 2026. Révision auditée : `R2026-11-13c`. Document hors du paquet. Rien n'est intégré.

**Lus en entier (8 fichiers, 102 k).** `gouvernance/README.md`, `principes.md`, `statuts.md`, `travail.md`, `verification.md`, `cloture.md`, `structure.md`, `integrite.md`. Écart déclaré : les lignes de plus de 430 à 900 caractères ont été lues coupées.

**Exécutés et analysés par programme (34 fichiers, 110 k).** Les 4 schémas, les 4 exemples et les 26 fichiers de test : chacun passé au validateur, message et code relevés ; champs des schémas comptés.

**Exécutés, lus par extraits (2 fichiers, 96 k).** `gouvernance/outils/validate_run_card.py` (inventaire des fonctions, contrat sémantique lu en entier) et `validate_contracts.py` (inventaire). Ils ne comptent pas comme « lus en entier ».

**Recoupé hors paquet.** Les quatre fiches de mobilisation et les traces des runs de phase 6 (SOM-3, FIN-3, FTX-1, IDT-1).

**Statuts.** Certain : lu ou mesuré. Probable : cohérent avec plusieurs observations. À vérifier : non établi. **Poids.** Bloquant, important ou mineur.

**Points de vue.** A agent, P personne, I ingénieur, M mainteneur, T intégrité, V preuve.

---

## 1. Verdict du lot

La gouvernance est cohérente, honnête sur ce qu'elle atteste, et bien outillée. Elle n'a servi dans aucun des quatre runs de la phase 6.

1. **Le module tient debout** (certain). Les deux validateurs passent, chaque fichier de test invalide est refusé pour le motif que son nom annonce, et le texte sépare partout « non applicable », « non vérifié » et « non observé ».
2. **Aucune route de gouvernance n'a été lue en phase 6** (certain). Treize routes, 100 k de texte, zéro lecture sur quatre runs. Aucune fiche de travail n'a été produite. Les quatre sorties sont en trace légère.
3. **Le contrôle est placé là où rien ne passe** (certain). La trace complète a un schéma de 145 champs et un validateur de 1 099 lignes. La trace légère, seule produite, n'a aucun contrôle.
4. **Le vocabulaire est lourd** (certain pour le compte) : 113 étiquettes en capitales, presque toutes en anglais, pour 14 400 mots.

Aucun constat bloquant. Le constat E-03 est celui qui pèse le plus sur la suite : dans votre protocole de test, la trace complète ne peut pas se déclencher.

---

## 2. Ce qui tient

| Vérification | Résultat |
|---|---|
| `validate_run_card.py` | 93 cas unitaires sur 93, 12 locators stricts sur 12, témoin de schéma refusé |
| `validate_contracts.py` | 29 cas sur 29, 3 cas de cardinalité, clés répétées refusées |
| 23 fichiers de test invalides | tous refusés, code 1, chacun pour le motif de son nom |
| 3 fichiers de test valides et l'exemple | tous acceptés |

Ce qui est bien fait, lu dans le texte.

- **La gouvernance se dit proportionnée** (`README.md:3-12`). « Pas un formulaire à remplir systématiquement » ; « alléger la formalité ne supprime aucune preuve applicable ».
- **La frontière de validation est écrite sans détour** (`travail.md:183-186`). Une fiche validée atteste une forme ; elle n'atteste ni que les observations ont eu lieu, ni la justesse des jugements, ni la qualité perçue.
- **Une preuve manquante ne devient jamais un succès** (`travail.md:19`, `cloture.md:20, 76`). La règle est tenue dans le texte et dans le code (`validate_run_card.py:487-560`).
- **L'auto-comparaison est nommée pour ce qu'elle est** (`verification.md:131, 148`). Une seconde session du même auteur n'est jamais un regard externe.
- **Le premier rendu vaut point d'arrêt** (`travail.md:261-264`). Construire, montrer, laisser la personne valider, réorienter ou arrêter. Valider n'est pas accepter.
- **Le test de non-récitation** (`integrite.md:10, 15`) : « quelle décision concrète a changé grâce à ce module ? ». Appliqué à ce module, il donne le constat E-01.

---

## 3. Constats importants

### E-01 — Aucune route de gouvernance n'a été lue dans les runs de la phase 6

**Lieu.** Les sept fichiers de texte de `gouvernance/`. **Points de vue.** V, A. **Statut.** Certain pour la phase 6 ; pour les phases antérieures, à vérifier au lot G.

Les sept fichiers portent treize routes.

| Fichier | Taille | Routes | Lues en phase 6 |
|---|---|---|---|
| `travail.md` | 38 k | conditions de départ, fiche de travail, déroulé de direction | 0 |
| `verification.md` | 19 k | contrats de preuve, Gate B, dérogation | 0 |
| `structure.md` | 12 k | contrat de route, contrôle structurel | 0 |
| `cloture.md` | 12 k | dossier de clôture, test de sortie, lecture instrumentée | 0 |
| `integrite.md` | 9 k | intégrité | 0 |
| `statuts.md` | 7 k | statuts | 0 |
| `principes.md` | 2 k | portée d'action, frontière du service | 0 |

Les fiches de mobilisation se trompent sur les lectures partielles (D-01), mais une route qui n'y figure pas n'a pas été servie du tout : l'absence est fiable. Cinq passages de ces fichiers atteignent quand même l'agent, par le noyau : listes closes, point d'arrêt, faux asset, récitation, limites.

Le déroulé de direction (`travail.md:195-285`) est cité dans la ligne DIRECTION comme lecture « pendant la fabrication ». Il confirme A-04 par un autre chemin : huit étapes numérotées, jamais lues.

### E-02 — L'effort de contrôle est à l'inverse de l'usage

**Lieu.** `gouvernance/schemas/`, `gouvernance/outils/` ; `agent/repondre.md:42`. **Points de vue.** V, I. **Statut.** Certain.

| | Trace complète | Trace légère |
|---|---|---|
| Forme | fiche de travail, 145 champs déclarés, 12 requis à la racine | six lignes au plus |
| Contrôle | validateur de 1 099 lignes, 93 cas, 26 fichiers de test, profil strict | aucun |
| Produite en phase 6 | 0 fois | 4 fois sur 4 |

Rien ne vérifie qu'une trace légère porte ses six lignes, ni que la ligne « défaut dominant » décrit un geste appliqué plutôt qu'envisagé. Le parcours affiche des « lignes mesurables de la trace légère » ; il ne lit pas la trace écrite.

### E-03 — Dans le protocole de test, la trace complète ne peut pas se déclencher

**Lieu.** `travail.md:264` ; `agent/repondre.md:42` ; `verification.md:115`. **Points de vue.** A, V. **Statut.** Certain pour le mécanisme.

Le passage en trace complète demande que la personne veuille « retenir la direction pour un produit réel », ou que le run soit persistant, partagé ou audité. Un run de test part d'un dossier vide et s'arrête à la première proposition. Conséquences, toutes prévues par le texte :

- la comparaison sur capture d'une décision principale (B1b) « ne s'applique pas » (`travail.md:205`) ;
- Gate B et le dossier de clôture ne sont pas chargés ;
- aucun verdict n'est rendu : toute sortie reste « exploratoire ».

La moitié « preuve » du système n'est donc pas mesurable par les runs tels qu'ils sont menés. Ce n'est pas un défaut du texte. C'est une limite de ce que la phase 6 peut dire de lui.

### E-04 — 113 étiquettes en capitales pour 14 400 mots

**Lieu.** Les sept fichiers de texte. **Points de vue.** P, A, M. **Statut.** Certain pour le compte ; gêne pour un agent : probable.

| Famille | Valeurs |
|---|---|
| États du run | 7 |
| Issues | 6 |
| Verdicts par axe | 5 |
| Verdicts globaux | 6 |
| Statuts de direction | 4 |
| Conséquence décisionnelle | 5 |
| Résultats locaux de comparaison | 3 |
| Statuts de source | 3 |
| Routes de production d'un asset | 5 |
| Types d'ancre | 3 |
| Catégories de lecture | 4 |
| Relation et exposition d'un relecteur | 4 et 5 |

S'y ajoutent une quarantaine de noms de champs (`NEXT-PROOF`, `EXIT-CONDITION`, `REVIEW-DATE`…). Le texte passe une part visible de sa longueur à empêcher ces familles de se confondre (`statuts.md:43-45`, `travail.md:119, 178`, `structure.md:59-61, 82-84`). Presque tout est en anglais dans un système écrit en français.

### E-05 — La table des conditions de départ ignore le niveau de trace

**Lieu.** `travail.md:10-16`. **Points de vue.** A, M. **Statut.** Certain, lu.

La ligne DIRECTION y exige « capture, comparaison, gates A/B/C, trace locale des assets, statut de direction et V/U/A/T », sans réserve. Trois autres passages disent que Gate B, B1b et le verdict ne valent qu'en trace complète (`travail.md:205, 264` ; ligne DIRECTION de la table de chargement). Le fichier ne nomme la trace légère qu'à sa ligne 205.

C'est aussi une troisième table « par mode », après la table de chargement et celle du dossier de clôture (`cloture.md:10-16`). La garde qui interdit une seconde table de chargement reconnaît un en-tête précis ; ces deux-là portent un autre en-tête. Ce constat prolonge A-12 et D-03.

### E-06 — Le regard externe du texte et votre règle 7

**Lieu.** `verification.md:146-169` ; `cloture.md:82` ; `verification.md:20`. **Points de vue.** T. **Statut.** Question, pas défaut.

Le texte prévoit un regard externe, décrit comment le qualifier d'« indépendant » ou d'« aveugle », recommande « plusieurs évaluateurs » pour une décision importante, et mesure la méthode par « la perception de qualité par plusieurs regards situés ». Votre règle de travail dit : pas de juge externe aveugle, le juge des rendus c'est vous.

Les deux ne se contredisent pas à la lettre : la règle vise vos tests, le texte vise un run chez un tiers. Mais le système décrit un appareil de preuve que son propre auteur a décidé de ne pas employer pour l'éprouver.

### E-07 — Deux instruments de lecture qui ne se connaissent pas

**Lieu.** `cloture.md:85-94` ; `scripts/journal_mobilisation.py`. **Points de vue.** M, V. **Statut.** Certain.

La gouvernance définit quatre catégories de lecture pour un run instrumenté (`STARTUP-NOMINAL`, `CONDITIONAL-READ`, `AUDIT-READ`, `ACTUAL-READ`). Le journal de mobilisation, arrivé depuis, a son propre vocabulaire (« consultée », « proposée, non lue », « lecture partielle »). Aucun fichier de gouvernance ne cite le journal ; la fiche du journal ne cite aucune des quatre catégories.

---

## 4. Constats mineurs

| N° | Lieu | Constat | Vue | Statut |
|---|---|---|---|---|
| E-08 | `statuts.md:59-61` | Un « principe positif de qualité » est rangé dans la section des statuts. | M | certain |
| E-09 | `integrite.md:78-110` | Huit « règles d'or » et une « méthodologie studio » : une liste de principes de plus, dans la section d'intégrité. Prolonge A-02. | A, M | certain |
| E-10 | `integrite.md:87` | Règle d'or 6 : « la spec est toujours requise » sur une surface de direction. Aucune trace de phase 6 ne nomme une spec. | A | à vérifier au lot G |
| E-11 | `travail.md` | Un seul fichier de 38 k porte trois routes sans rapport de moment : conditions avant d'agir, format de fiche, déroulé de fabrication. | M | certain |
| E-12 | `travail.md:145-170` | La « vue d'exécution » ajoute douze champs et un paragraphe sur les « relations ouvertes » dont je n'ai trouvé aucun usage. | M | certain pour le texte ; usage : à vérifier |
| E-13 | `validate_contracts.py:468-511` | Message final en anglais dans un outil en français. | P | certain |
| E-14 | `validate_all.py:236-241` | La validation d'ensemble nomme 4 des 23 fichiers invalides ; les autres sont éprouvés par la table interne du validateur de fiches. Deux lieux pour la même liste. | M | certain |

---

## 5. Propositions (non intégrées)

Chacune se décide à part.

1. **E-01, E-03.** Décider ce que vous voulez savoir de la gouvernance. Soit un run mené jusqu'à « retenir pour un produit réel », pour voir la trace complète fonctionner une fois. Soit acter qu'elle est hors du champ de la mesure, et le dire dans le suivi.
2. **E-02.** Un contrôle court de la trace légère : six lignes présentes, geste appliqué nommé. C'est le seul document que les runs produisent.
3. **E-04.** À discuter : ce qui, dans ces familles, sert un run sans fiche de travail. Le reste pourrait vivre avec le schéma plutôt que dans le texte lu.
4. **E-05.** Faire dire à la table des conditions de départ ce qui ne vaut qu'en trace complète, ou la fondre dans la table de chargement.
5. **E-06.** Votre décision : garder le regard externe comme possibilité pour d'autres, ou l'aligner sur votre pratique.
6. **E-07.** Rattacher le journal aux catégories de lecture, ou retirer les catégories.

---

## 6. Ce que ce lot n'a pas vérifié

- Les deux validateurs n'ont pas été lus ligne à ligne : 1 610 lignes, dont j'ai lu l'inventaire et le contrat sémantique.
- Les schémas, exemples et fichiers de test ont été exécutés et comptés, pas lus un à un.
- Je n'ai pas cherché de fiche de travail dans les phases antérieures à la phase 6 ; « jamais produite » n'est établi que pour la phase 6.
- Je n'ai pas fabriqué de fiche trompeuse pour éprouver le validateur ; le texte déclare lui-même qu'il n'atteste qu'une forme.
- Le comptage des étiquettes est fait par motif ; quelques noms de champs y sont comptés avec les statuts.

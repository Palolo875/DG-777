# Audit neuf — Lot D : navigation, validation, livraison

13 novembre 2026. Révision auditée : `R2026-11-13c`. Document hors du paquet. Rien n'est intégré.

**Lus en entier (11 fichiers, 290 k).** `scripts/read_route.py`, `build_core.py`, `journal_mobilisation.py`, `validate_structure.py`, `validate_reading_map.py`, `validate_design_governance.py`, `validate_all.py`, `validate_supports.py`, `preparer_livraison.py`, `build_distributions.sh`, `README.md`. Écart déclaré : dans les trois grands validateurs, les lignes de plus de 175 à 250 caractères ont été lues coupées.

**Analysé par programme (1 fichier, 12 k).** `scripts/package_manifest.json` : listes comparées entre elles et au dépôt, poids par catégorie.

**Exécutés, lus par extraits seulement (5 fichiers, 113 k).** `test_read_route.py`, `test_audit_regressions.py`, `test_core_budget.py`, `test_journal_mobilisation.py`, `test_preparer_livraison.py`. Ils ne comptent pas comme « lus en entier » au registre.

**Exécuté.** Les cinq suites de tests ; la validation complète avec navigateur sur une copie ; neuf essais du journal de mobilisation ; deux injections dans une copie pour éprouver les gardes ; un relevé des tables qui mènent à des routes.

**Statuts.** Certain : lu ou mesuré. Probable : cohérent avec plusieurs observations. Hypothèse : plausible, non mesuré. **Poids.** Bloquant, important ou mineur.

**Points de vue.** A agent, P personne, I ingénieur, M mainteneur, T intégrité, V preuve.

---

## 1. Verdict du lot

La mécanique est solide : le lecteur, la compilation du noyau et la construction des archives font ce qu'ils annoncent. Deux choses sont moins sûres qu'elles n'en ont l'air.

1. **Le code tient** (certain). 241 cas de test passent, plus 231 sous-tests. Le manifeste et le dépôt coïncident à l'unité près.
2. **Le journal de mobilisation n'est pas fiable sur la lecture** (certain, reproduit). Il déclare « lecture partielle » une route lue en entier, « consultée » une route coupée, et « consultée » un tronc écrit dans un fichier que personne n'a ouvert. C'est l'instrument qui sert de preuve aux runs.
3. **Les validateurs prouvent que le paquet s'accorde avec lui-même, sur des formulations connues** (certain). Environ 180 phrases sont épinglées une à une. Une formulation nouvelle du même défaut passe : deux injections l'ont montré.
4. **Trois gardes annoncent plus qu'elles ne contrôlent** (certain) : « une seule table de signaux », « planchers d'obligation », « vouvoiement des façades ».

Aucun constat bloquant dans ce lot. Le constat D-01 pèse sur le lot G : les fiches de mobilisation des runs ne peuvent pas servir seules de preuve de lecture.

---

## 2. Ce qui tient

| Vérification | Résultat |
|---|---|
| `test_read_route.py` | 103 cas, tous verts |
| `test_audit_regressions.py` | 98 cas et 231 sous-tests, tous verts |
| `test_core_budget.py` | 18 cas, tous verts |
| `test_journal_mobilisation.py` | 12 cas, tous verts |
| `test_preparer_livraison.py` | 10 cas, tous verts |
| Manifeste | 149 fichiers GitHub, 144 Local ; aucun fichier du dépôt hors manifeste ; l'écart entre les deux listes est exactement les 5 fichiers de préparation et d'intégration continue |
| Validation complète avec navigateur | `FULL VALIDATION PASSED`, code 0, 11 min 43 s ; deux constructions identiques |
| Vitesse du lecteur | une route en 0,1 s ; une recherche par phrase en 1,9 s |

Ce qui est bien fait, lu dans le code.

- **Le lecteur refuse plutôt que de deviner** (`read_route.py:447-521`). Locator inconnu, ambigu, en double ou porté par deux fichiers : erreur nommée, jamais de repli silencieux.
- **Un bloc n'est replié que s'il est réellement dans le noyau** (`read_route.py:570-598`). Si `SKILL.md` est périmé ou absent, la route est servie en entier.
- **La recherche dit sa limite** (`read_route.py:1247`) : « ce résultat ne prouve pas l'absence du savoir ».
- **Le noyau ne peut pas perdre un bloc en silence** (`build_core.py:204, 233-235`). Tout bloc est soit compilé, soit servi par une route dont on vérifie qu'elle le contient en entier.
- **La construction est transactionnelle** (`build_distributions.sh:218-265`). Verrou, sauvegarde, restauration en cas d'échec, contrôle des membres de chaque archive contre le manifeste, archives reproductibles.
- **Les contrôles disent ce qu'ils n'attestent pas.** « Rendu non évalué », « build et reproductibilité NOT-VERIFIED », « cette préparation ne certifie aucun rendu ni résultat d'usage ».
- **Un déplacement de texte est éprouvé pour de bon** (`validate_all.py:114-185`) : sur une copie, une route change de fichier ; avec la table des lieux à jour tout reste vert, sans elle l'erreur est détectée.

---

## 3. Constats importants

### D-01 — Le journal se trompe dans les deux sens sur la lecture partielle

**Lieu.** `scripts/journal_mobilisation.py:92-109` (fonction `extraction`). **Points de vue.** I, V. **Statut.** Certain, reproduit.

Le journal lit la ligne de commande du shell parent, cherche la première occurrence de `read_route.py`, et y cherche un filtre (`| head`, `| grep`…). Il ne regarde pas ce qui a été réellement coupé.

| Commande lancée | Ce qui s'est passé | Ce que dit la fiche |
|---|---|---|
| `read_route.py A \| head -3 ; read_route.py B` | A coupée, B entière | A et B « lecture partielle » |
| `read_route.py A ; read_route.py B \| head -3` | A entière, B coupée | A et B « consultée » |
| `read_route.py A \| wc -l` | rien de lu, un nombre affiché | « consultée » |
| `read_route.py A \| head -200` sur une route de 65 lignes | route entière | « lecture partielle » |
| plusieurs commandes dans un même script | une route coupée à 3 lignes | « consultée » |

Un agent enchaîne presque toujours plusieurs commandes sur une ligne. Les fiches de SOM-3 et d'IDT-1 portent déjà un faux « Tronc non consulté ». Le test existant (`test_journal_mobilisation.py:88`) ne couvre que le cas simple d'une seule commande.

### D-02 — « Consultée » veut dire « servie », pas « lue »

**Lieu.** `journal_mobilisation.py:70, 187` ; `read_route.py:1166-1175`. **Points de vue.** V, T. **Statut.** Certain, reproduit.

Avec `--tronc DIRECTION --fichier chemin`, le lecteur écrit le tronc dans un fichier et affiche huit lignes d'en-tête. Le journal relève ces huit lignes et la fiche déclare huit routes « consultées ». Dans l'essai, le fichier n'a jamais été ouvert. Même résultat avec une redirection `> fichier`.

Le docstring le dit honnêtement (« une route lue n'est pas une route appliquée »). Le mot de la fiche dit plus. Or `--fichier` est la forme recommandée pour le tronc : le cas le plus courant est celui où l'instrument ne voit rien.

### D-03 — La garde « une seule table de signaux » laisse passer trois autres tables

**Lieu.** `validate_structure.py:979-999` (garde 21, SIG-01). **Points de vue.** M, A. **Statut.** Certain, relevé par programme.

La garde reconnaît une table à son en-tête : première colonne « Signal », « Situation », « Question » ou « Déclencheur », deuxième « Route ». Trois tables font le même travail sous d'autres en-têtes.

| Lieu | En-tête | Lignes qui mènent à une route |
|---|---|---|
| `design/produit/finition.md:16` | « Critère … Geste si absent (route à charger) » | 6 sur 6 |
| `design/savoir/composition.md:51` | « Terme, Signal à traiter … savoir à approfondir » | 17 sur 17 |
| `design/savoir/images-et-sources.md:141` | « Famille … Route approfondie » | 6 sur 6 |

Le message de succès dit « une table de signaux ». Ce constat rejoint A-12 (six endroits disent quoi charger) par un autre chemin.

### D-04 — « Plancher » et « atteignable » ne disent pas qu'une règle est lue

**Lieu.** `validate_structure.py:865-976` (gardes 19 et 20). **Points de vue.** V, A. **Statut.** Certain pour le mécanisme ; le rapprochement avec les lots A et B est une lecture croisée.

- **Garde 20.** Elle couvre les 13 obligations qui portent l'étiquette `[REQUIS PAR LE MODULE — …]`. Une prescription écrite à l'impératif sans étiquette n'a pas de plancher contrôlé. C'est le cas des routes relevées en A-04 et B-05 (déroulé, preuve visuelle, finition). Onze planchers sur treize sont « dans le noyau », c'est-à-dire présents dans les 44 k de `SKILL.md`.
- **Garde 19.** « Atteignable » veut dire qu'une route sert la ligne. Aucun mode n'est tenu de charger cette route. B-01 a mesuré 11 routes de savoir lues sur 38.

Les deux gardes font ce que leur commentaire décrit. C'est le résumé affiché (« règles atteignables, 13 planchers d'obligation ») qui se lit comme une garantie de lecture.

### D-05 — Les gardes de formulation ne reconnaissent que les phrases déjà rencontrées

**Lieu.** `validate_structure.py:114-299, 383-385, 655-664, 813-825` ; `validate_reading_map.py:237-747`. **Points de vue.** M, V. **Statut.** Certain, deux injections.

| Registre | Entrées |
|---|---|
| Vocabulaire retiré | 42 |
| Résumés fidèles (déclencheur, puis mot attendu) | 65 |
| Conditions de façade | 56 |
| Lignes de table attendues | 11 |
| Phrases que le noyau doit porter | 10 |

Deux phrases ajoutées dans une copie, puis validation relancée :

- un tutoiement dans le guide opérateur (« Tu peux choisir le mode toi-même… ») : validation verte. La garde connaît huit tournures (`validate_structure.py:385`) et annonce « vouvoiement des façades » ;
- une affirmation de mode non datée dans le savoir (« le verre liquide translucide et les dégradés maillés signent les pages de cette année ») : validation verte. La garde connaît dix-huit marqueurs (`validate_reading_map.py:511-513`).

Le docstring l'assume (`validate_structure.py:42-47`, `validate_reading_map.py:13`). Deux conséquences restent. Chaque correction de texte ajoute une ligne de validateur : 184 phrases à tenir en accord avec le corpus. Et une validation verte ne dit rien d'une contradiction nouvelle.

### D-06 — Les marqueurs de mode vivent en trois endroits

**Lieu.** `validate_reading_map.py:511-513` ; `scripts/regard.py:583-595` ; `design/savoir/gout-et-tendances.md`. **Points de vue.** M. **Statut.** Certain.

Le corpus date ses marqueurs par vagues (trois à ce jour). L'outil de regard en mesure douze. Le validateur en refuse dix-huit hors d'un passage daté. Les trois listes sont écrites à la main, séparément. Une quatrième vague ajoutée au corpus ne serait ni mesurée ni protégée. Ce constat complète B-08 et C-05.

### D-07 — Les deux budgets sont au plafond

**Lieu.** `build_core.py:33` ; `read_route.py:612, 1179-1184`. **Points de vue.** M, A. **Statut.** Certain, mesuré.

| Budget | Mesure | Plafond | Marge |
|---|---|---|---|
| `SKILL.md` | 43 984 octets | 46 000 | 2 016 (4 %) |
| Tronc DIRECTION | 34 520 caractères | 35 000 | 480 (1 %) |

Toute règle ajoutée au tronc demande d'en retirer une autre. Effet de bord : à chaque run DIRECTION, le lecteur affiche à l'agent un avertissement destiné au mainteneur (« MARGE FAIBLE — un ajout au tronc se compense par un allègement… »).

---

## 4. Constats mineurs

| N° | Lieu | Constat | Vue | Statut |
|---|---|---|---|---|
| D-08 | `package_manifest.json` (liste `local`) | L'export installé chez l'agent pèse 2,45 Mo en 144 fichiers. Tests : 256 k (10 %). Validateurs et compilation : 189 k (8 %). Un agent en run n'utilise ni les uns ni les autres. | P, A | chiffres certains ; gêne réelle : hypothèse |
| D-09 | `scripts/README.md:10` | La ligne de `parcours.py` est une seule cellule de 3 842 caractères. `preparer_livraison.py` et `build_distributions.sh` n'y figurent pas, alors que la distribution GitHub les livre. | P, M | certain |
| D-10 | `scripts/*.py`, `*.sh`, `gouvernance/outils/*.py` | 32 identifiants d'anciens constats et décisions (« RET-4 », « INV-B2-9 », « F-DIR-005 », « constat C13 »…), 37 occurrences. Aucun ne se résout dans le paquet : l'historique est dehors (règle 3), les renvois sont restés. | M, T | certain |
| D-11 | `build_core.py:37-75, 162-172` | Le registre prévoit des « colonnes gardées » ; les 66 entrées valent toutes `None`. La fonction `project` ne sert pas. | I | certain |
| D-12 | `build_core.py:78-120` | 66 blocs portent la marque « noyau » dans les sources ; 35 sont compilés dans le noyau, 31 sont seulement servis par leur route. Le nom de la marque trompe. | M | certain |
| D-13 | `build_core.py:33` ; `read_route.py:612` | Un budget en octets, l'autre en caractères. | M | certain |
| D-14 | `preparer_livraison.py:43` | Le résumé affiché retient cinq bilans de tests ; ceux du journal, des régressions, du regard et du parcours n'y sont pas. | M | certain |
| D-15 | `build_distributions.sh:52-90, 108-125` | Ajouter un fichier demande trois gestes (copie dans le script, deux listes du manifeste). Le texte du README Local est écrit dans le script de construction, hors du README. | M | certain |
| D-16 | `journal_mobilisation.py:204-215` | « Tronc non consulté » est calculé sur le tronc du paquet présent au moment de la fiche, pas sur celui du run. | V | certain |
| D-17 | `build_distributions.sh:181` ; `validate_all.py:286-290` | La validation complète construit deux fois, et chaque construction relance la validation de l'export Local : les suites sans navigateur tournent trois fois. | I | certain |
| D-18 | `build_distributions.sh:186-187` | Pour être reproductibles, les archives datent tous leurs fichiers de l'origine du calendrier informatique. | P | certain |

---

## 5. Propositions (non intégrées)

Chacune se décide à part.

1. **D-01, D-02.** Faire mesurer au journal ce qui est sorti réellement : le nombre de caractères écrits avant la coupure, comparé à la taille de la route. Renommer « consultée » en « servie ». Pour `--fichier`, dire « écrite dans un fichier, lecture non observée ».
2. **D-03.** Soit élargir la garde aux tables dont une colonne mène à des routes, soit dire dans son message qu'elle contrôle un en-tête.
3. **D-04, D-05.** Reformuler les messages de succès pour qu'ils nomment ce qui est contrôlé : « 13 obligations étiquetées », « 8 tournures de tutoiement », « 18 marqueurs connus ».
4. **D-06.** Une seule liste de marqueurs, lue par le validateur et par l'outil de regard.
5. **D-07.** Retirer l'avertissement de marge de la sortie de l'agent ; le garder dans la validation.
6. **D-08.** À discuter : un export d'usage sans tests ni validateurs.
7. **D-10.** Remplacer chaque identifiant par la raison en clair, ou les retirer.

---

## 6. Ce que ce lot n'a pas vérifié

- Les cinq fichiers de tests n'ont pas été lus ligne à ligne. Je ne sais donc pas si chaque test éprouve ce que son nom promet.
- Les lignes longues des trois grands validateurs ont été lues coupées.
- Les 56 conditions de façade n'ont pas été éprouvées une à une ; deux gardes seulement ont reçu une injection.
- La construction n'a pas été essayée en cas de panne (verrou resté, disque plein).
- Le comportement du journal hors Linux n'a pas été essayé ; le code prévoit de ne rien déduire sans `ps`.

**État de la validation complète.** `validate_all.py --require-browser` sur une copie du dépôt : `FULL VALIDATION PASSED`, code 0, en 11 min 43 s. Un premier lancement avait été interrompu par la coupure de session ; il a été relancé en entier.

# Lot 18 — Propositions : brancher le savoir

Rédigé le 25 novembre 2026, après l'exploration du système (`Exploration_systeme.md`). Base : V1.4.0 (`R2026-11-25f`). Décisions de Junior : « Allons-y » (plan d'action, étape 1 : brancher le savoir existant) ; « Pas de génération d'images pour l'instant ». Aucun run. Règle 1 : « D'accord » vaut pour les options A partout.

## 0. Mesure

| Constat | Preuve |
|---|---|
| **Le tronc est lu à chaque run** : un fichier écrit par un outil, avec une consigne de le lire une fois en entier. | Journaux des runs 21 à 24 : 4 runs sur 4. |
| **Les routes de construction ne sont jamais lues.** | Mêmes journaux : 0 lecture de `BIBLIOTHEQUE/SELECT`, `TENSION`, `SUPPORT`, `GRID`, `SCENE`, `OBJECT`, `SECTIONS`, `SIGNATURE`, ni de `SAVOIR/STATE`, `STYLE`, `CRAFT/CFT-02`, `CFT-03`, `CFT-05`. |
| **La cause est écrite dans le noyau.** La règle de vitesse dit : « Le reste de la ligne se lit quand son signal apparaît. » `agent/chemins.md` ajoute : « Au-delà du tronc de ton mode, charge typiquement zéro à deux routes de SAVOIR. » | `SKILL.md`, ligne 40 ; `agent/chemins.md`, ligne 258. |
| **Le tirage est le levier le plus suivi.** Les esquisses gardées aux runs 23 et 24 viennent de ses pistes. | `Reverse_1_runs_23_24.md`. |
| **Taille des routes à brancher** (caractères servis par `read_route.py`). | `TENSION` 1 857 · `SUPPORT` 3 387 · `GRID` 4 194 · `SCENE` 4 273 · `SIGNATURE` 1 029 · `STYLE` 13 241 · `CFT-02` 4 600 · `SELECT` 13 825 · `STATE` 16 928 · `CFT-05` 7 595 · `CFT-03` 4 153 · `OBJECT` 4 722 · `SECTIONS` 5 637. |

Noyau : 32 004 octets sur 33 000 (marge 996).

## 1. Sous-lot 18a — Deux lectures d'étape, servies comme le tronc

Le tronc marche parce qu'un outil écrit un fichier et que le noyau dit de le lire une fois. On applique le même mécanisme à deux étapes du mode DIRECTION, celles où le savoir sert.

- **A (recommandée).** `read_route.py --etape ESQUISSES|CONSTRUCTION --fichier …`, chaque lecture sous 40 000 caractères, comme un tronc.
  - **ESQUISSES** : avant d'esquisser, une fois les directions écrites. Contenu : `BIBLIOTHEQUE/TENSION`, `SUPPORT`, `GRID`, `SCENE`, `SIGNATURE`, `SAVOIR/STYLE`, `SAVOIR/CRAFT/CFT-02` (environ 32 600 caractères). On y lit les axes de tension, les supports, les grilles, les scènes, la signature, les huit profils de style et les axes de registre : de quoi faire différer les esquisses par la structure et le style, pas seulement par l'idée.
  - **CONSTRUCTION** : avant le premier build de la direction gardée. Contenu : `SAVOIR/STATE` (la table complète des gestes de finition, avec ses planches), `SAVOIR/CRAFT/CFT-05` (couleur, avec ses planches), `CFT-03` (composition, densité, harmonie), `BIBLIOTHEQUE/OBJECT`, `SECTIONS` (environ 39 000 caractères). Les gestes de finition passent de la correction après coup à la **construction**.
  - **Le noyau** dit quand lire, à la place de « quand son signal apparaît » : la ligne « Diverger sur image » commence par « lis d'abord l'étape ESQUISSES » ; la ligne du premier rendu par « avant le premier build, lis l'étape CONSTRUCTION ». Environ 200 octets.
  - **Les étapes s'écrivent dans `DIRECTION/CHARGE`**, comme le tronc (« **Étape ESQUISSES** : … », « **Étape CONSTRUCTION** : … ») : une seule table, aucune liste concurrente.
  - **`chantier`** annonce les deux commandes dans sa suite.
- **B.** Élargir le tronc DIRECTION. Impossible sous le budget (35 177 + 71 600 caractères), et ce serait lu trop tôt, avant que les directions existent.
- **C.** Garder la lecture conditionnelle et seulement la reformuler. Je ne la recommande pas : quatre runs montrent qu'un signal laissé au jugement de l'agent n'est pas suivi.

`SELECT` (13 825 caractères) reste hors des deux étapes : son test de trame est déjà au noyau, et l'étape ESQUISSES couvre le reste.

## 2. Sous-lot 18b — Le tirage tire aussi une structure et un style

- **A (recommandée).** `parcours.py tirage` (et `chantier`) tire, en plus des deux pistes du sujet et de la dimension de registre :
  - **une grille** parmi les six de `BIBLIOTHEQUE/GRID` ;
  - **un profil** parmi les huit de `SAVOIR/STYLE`.

  Ce tirage vaut pour l'esquisse issue du tirage, qui passe le test du lien comme les autres. Les codes sont lus dans les routes, jamais recopiés dans le script (comme les pistes aujourd'hui). La recherche va dans ce sens : un schéma de structure imposé à la génération augmente la diversité visuelle et structurelle (« Mine, Sample, Render », lu dans le résumé).
- **B.** Tirer seulement le profil de style.

## 3. Sous-lot 18c — Choisir par code, et le tracer

- **A (recommandée).** La ligne « modal, trame et parti » nomme, pour la direction gardée, sa **grille** (`GRID/…`), sa **scène** ou son **support** (`SCENE/…`, `SUPPORT/…`) et son **profil** (`STYLE/…`, ou « mélange » avec ses deux dimensions). `parcours.py trace` signale une ligne sans aucun de ces codes : un signal, pas un échec, sans objet hors DIRECTION. Gabarits de trace mis à jour : exemples, guide 3, `chantier`.
- **B.** Rien dans la trace.

## 4. Sous-lot 18d — Accorder les règles de sobriété

- **A (recommandée).** Préciser deux phrases :
  - la règle de vitesse du noyau : « Le reste de la ligne se lit quand son signal apparaît ; en DIRECTION, les deux étapes se lisent toujours » ;
  - `agent/chemins.md` : « au-delà du tronc **et des étapes de ton mode** ».

  Sans cela, les nouvelles lectures contrediraient les anciennes.
- **B.** Ne rien changer : contradiction laissée à l'agent.

## 5. Coût et budget

- **Noyau** : environ 300 octets (sur une marge de 996).
- **Par run DIRECTION** : environ 72 000 caractères lus en plus, soit environ 20 000 jetons, une fois chacun. Relus en cache sur la suite du run, ils ajoutent probablement 5 à 10 % de lecture de cache, plus quelques tours de choix. Ce coût sert la qualité, comme tu l'as demandé ; il sera mesuré au run suivant.

## 6. Gardes et tests (mutation rouge, échec nommé)

- `read_route --etape` :
  - chaque étape sert ses routes, sous le budget ;
  - une étape absente de `DIRECTION/CHARGE` donne une erreur nommée ;
  - une route de l'étape qui disparaît du catalogue est signalée par la validation de structure.
- Plancher : les deux consignes d'étape sont des phrases protégées du noyau (CORE-01).
- `tirage` : une grille et un profil existants sont tirés, lus dans leurs routes.
- `trace` : une ligne sans code de structure ni de profil est signalée.
- Une mutation par garde.

## 7. Ce que le lot ne prouvera pas

- **Que lire ce savoir améliore les rendus.** Composition et composants sont des taxonomies : servis, ils aideront à choisir, pas forcément à construire. C'est précisément ce que le run suivant dira, et ce que le lot de construction traitera ensuite (fiches de composition, détails de composants, techniques, mouvement, échelle typographique).
- **Que la grille tirée donne une bonne esquisse.** Elle peut produire une combinaison forcée ; elle doit passer le test du lien et gagner sur la planche.

## 8. Ordre et vérification

1. 18a à 18d ensemble : révision `R2026-11-25g`, publication V1.5.0.
2. Puis, sur ta décision, un run avec un brief que nous avons déjà, pour comparer à un rendu connu : l'atelier vélo (run 23) ou la page de contact du studio (run 24). On regarde si les étapes ont été lues, si les esquisses diffèrent par la structure et le style, et si le rendu sort du basique.

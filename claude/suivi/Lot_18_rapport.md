# Lot 18 — Rapport : brancher le savoir ; publication V1.5.0

- **Révision** : `R2026-11-25g`, livrée le 26 novembre 2026. Publication **V1.5.0**.
- **Branche** : `lot-18`.
- **Décision** : « Oui » (options A du lot 18) ; « Pas de génération d'images pour l'instant ».
- **Runs** : aucun.

## 1. Ce qui change

| Sous-lot | Où | Changement |
|---|---|---|
| **18a** Deux lectures d'étape | `DIRECTION/CHARGE` (`agent/chemins.md`), `read_route.py --etape NOM [--fichier …]` | **ESQUISSES**, une fois les directions écrites : `BIBLIOTHEQUE/TENSION`, `SUPPORT`, `GRID`, `SCENE`, `SIGNATURE`, `SAVOIR/STYLE`, `SAVOIR/CRAFT/CFT-02` (30 467 caractères). **CONSTRUCTION**, avant le premier build : `SAVOIR/STATE`, `SAVOIR/CRAFT/CFT-05`, `CFT-03`, `BIBLIOTHEQUE/OBJECT`, `SECTIONS` (36 934 caractères). Servies comme le tronc : un fichier, un sommaire, à lire une fois. Le tronc n'a pas changé (35 177). |
| **18a** Quand lire | Noyau, ligne « Diverger sur image » | « puis lis l'étape ESQUISSES (`read_route.py --etape ESQUISSES --fichier esquisses.txt`) » avant les esquisses ; « avant de construire la gardée, lis l'étape CONSTRUCTION ». |
| **18b** Tirage | `parcours.py tirage`, `chantier` | Tire aussi une grille (`BIBLIOTHEQUE/GRID`) et un profil (`SAVOIR/STYLE`), avec leur première phrase, lus à leur lieu (`tirage_structure`). `chantier` annonce les deux étapes, dans son détail et dans sa sortie. |
| **18c** Trace | `parcours.py trace`, gabarit de `chantier`, exemples | En DIRECTION, une ligne « modal, trame et parti » sans structure (`GRID/…`, `SCENE/…`, `SUPPORT/…`) ni profil (`STYLE/…` ou mélange) est signalée (signal, pas échec ; rien hors DIRECTION). Les exemples de `references/examples.md` nomment leurs codes. Le guide 3 n'en a pas : DOC-01 refuse les codes dans une page pour les personnes. |
| **18d** Sobriété | Règle de vitesse (noyau), `agent/chemins.md` | « Le reste de la ligne se lit quand son signal apparaît, sauf ses **étapes** » ; « au-delà du tronc **et des étapes** de ton mode ». |

Noyau : 32 307 octets sur 33 000 (+303).

## 2. Gardes, tests et mutations rouges

- **CHG-11** (`validate_structure.py`) : les étapes ESQUISSES et CONSTRUCTION sont déclarées, lisibles, et chacune reste sous 40 000 caractères.
- **CORE-01** : trois phrases protégées : « puis lis l'étape ESQUISSES », « lis l'étape CONSTRUCTION », « sauf ses **étapes** ».
- **Tests** :
  - `read_route` : étapes servies, budget, fichier, étape inconnue nommée (107 cas) ;
  - `parcours` : grille et profil existants tirés ; `chantier` annonce les étapes ; signal de trace en DIRECTION et rien hors DIRECTION (199 cas).

| Mutation | Résultat |
|---|---|
| L'étape CONSTRUCTION retirée de la ligne DIRECTION | Rouge : CHG-11 et `test_stages_are_served_like_a_trunk` |
| Le signal de trace retiré | Rouge : P92 |
| « lis l'étape CONSTRUCTION » retiré du noyau | Rouge : CORE-01 |

## 3. Préparation et livraison

- **Préparation complète** : réussie en 460 s, le 25 novembre au soir. Comme la date avait changé, la date de publication a été corrigée au 26 novembre (README, notes, fiche, journal des changements, citation) et la préparation relancée : réussie en **481 s**.
- **Tests** : `parcours` 199, `read_route` 107, `regard` 42, `check_render` 265… ; reproductibilité vérifiée.
- **Commits** : `76c3d02` sur `lot-18`, fusionné en `60ab692` sur `master` (`--no-ff`).
- **Archive GitHub** : les 164 fichiers sont identiques au commit.
- **Sortie** :
  - `Design_Governance_V1_GITHUB_R2026-11-25g.zip` (sha256 `caff1313…aa78`) ;
  - dans `claude/livraison/R2026-11-25g/` : archive Local (sha256 `d885f875…465a`) et bundle vérifié.

  La `25f` est retirée de DG-777.

## 4. Ce que le lot ne prouve pas

- **Que l'agent lira les étapes.** C'est probable, puisque le tronc, servi de la même façon, est lu à chaque run ; c'est à vérifier au run suivant, dans le journal.
- **Que les lire améliore les rendus.** Composition et composants restent des taxonomies : ils aident à choisir, peu à construire. Le lot de construction viendra ensuite.
- **Le coût par run** : environ 67 000 caractères lus en plus, non mesuré.

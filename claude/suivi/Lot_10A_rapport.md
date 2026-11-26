# Lot 10A — Rapport (propreté)

- **Révision** : `R2026-11-15p`, livrée le 21 novembre 2026.
- **Branche** : `lot-10a`.
- **Décision** : « À toi le choix, allons-y » (21 novembre). Le périmètre est celui du plan de travail, avec deux choix par défaut :
  - D1 : la ligne de veille est gardée, avec son origine dite ;
  - D3 : on ne garde que les archives `k` et la dernière livrée.
- **Runs** : aucun.

## 1. Ce qui est fait

| Étape | Changement | Garde ou test |
|---|---|---|
| **A1** Fuites du journal | Dans `qualite-creative.md`, les deux citations de runs sont remplacées par des exemples neutres. Dans `test_regard.py`, « Terres lentes » devient « Titre d'essai ». La ligne de veille devient « Convergences relevées lors d'essais du système, sur peu de briefs, à confirmer » (D1). | PRO-01 |
| **A2** Mesure obsolète | Dans `versions.md`, la phrase « un run avec le système coûte plus… » (mesure du 29 octobre) est remplacée par la mesure actuelle, datée, sans comparaison : 116 à 208 tours, 22 à 46 millions de jetons relus en cache, 14 à 27 minutes. | — |
| **A3** Garde PRO-01 | `validate_structure.py` refuse, en mot entier, tout nom tiré des runs. La liste (`.claude/suivi/noms_interdits.txt`, hors paquet) est passée par `preparer_livraison.py` (variable `DG_NOMS_INTERDITS`). Sans liste, la préparation affiche « NOT-VERIFIED ». | 3 cas dans `test_audit_regressions.py` |
| **A5** Journal optionnel | Les 5 outils de production (`check_render`, `parcours`, `planche`, `regard`, `read_route`) tournent sans `journal_mobilisation.py`. **Vérifié en vrai** dans une copie sans le module. | 1 cas (5 sous-cas) |
| **A7** Date juste | La ligne de révision porte la date réelle (21 novembre). L'étape 6 du déroulé d'un lot le dit dans `CLAUDE.md`. | — |
| **A8** Suivi | `suivi/INDEX.md` liste les documents vivants. Audits, lots S à 9e, runs 9 à 16 et notes de lecture vont dans `suivi/archives/`, sans suppression. Dans DG-777, les archives `l`, `m` et `n` sont retirées (D3) ; `k` et `o` restent, plus `p` à cette livraison. | — |

## 2. Ce qui est reporté, et pourquoi (changement de périmètre annoncé)

**A4 (archive « skill » sans l'atelier) et A6 (route d'instrumentation sortie de la skill)** passent au lot 12. Le relevé des dépendances le montre :
- `maintenance/README.md` est cité 29 fois, y compris par le noyau et le README ;
- les validateurs de la gouvernance sont cités par les guides ;
- `validate_all.py` lance les tests ;
- `parcours.py` a besoin de `supports/fonts/manrope.ttf`.

Les retirer casserait des liens et des commandes documentées. La séparation se fera **avec** la refonte de la documentation, qui réécrit ces renvois. Le relevé fichier par fichier est dans la conversation du 21 novembre ; il est à refaire à l'ouverture du lot 12.

## 3. Mutations rouges

| Mutation | Résultat |
|---|---|
| Mot entier cassé dans PRO-01 (simple sous-chaîne) | Rouge : `test_nom_refuse_en_mot_entier` |
| PRO-01 non appelée par la validation | Rouge : `test_la_garde_tourne_dans_la_validation` |
| Une citation de run remise dans le paquet | Rouge : la validation échoue (PRO-01) |
| Import du journal non protégé dans `planche.py` | Rouge : `test_import_protege` (outil `planche`) |

**Erreur en cours de route.** La garde PRO-01 a d'abord attrapé **mon propre test**, qui citait les vrais noms de briefs. Le test utilise maintenant des noms fictifs.

## 4. Préparation et livraison

- **Préparation complète** : `--require-browser --empreintes`, réussie du premier coup.
  - Garde PRO-01 **active** (liste du suivi).
  - Tests : régressions d'audit 159, `parcours` 170, `regard` 41, `read_route` 106, journal 19, `check_render` A, B et C.
  - Validations complète et locale : PASSED.
- **Commits** : `2cff357` sur `lot-10a`, fusionné en `b541344` sur `master` (`--no-ff`).
- **Archive GitHub** : les 151 fichiers sont identiques au commit.
- **Sortie** :
  - `Design_Governance_V1_GITHUB_R2026-11-15p.zip` (sha256 `90e6b35b…9540`), à la racine de DG-777, à côté de la `k` ;
  - dans `claude/livraison/R2026-11-15p/` : archive Local (sha256 `12829f88…55c1`) et bundle `--branches`, vérifié.
  - La `o` est retirée de DG-777 (D3 : seules `k` et la dernière livrée restent). Elle reste dans l'historique git et dans le bundle.

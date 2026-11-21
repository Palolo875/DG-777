# Lot 11d — Rapport : un seul agent, même sans outils

- **Révision** : `R2026-11-15u`, livrée le 21 novembre 2026.
- **Branche** : `lot-11d`.
- **Décision** : « Oui » à `Lot_11d_Propositions.md`, options A : D1, D2 et D3 A (pas de réécriture).
- **Runs** : aucun.

## 1. Ce qui change

| Proposition | Changement |
|---|---|
| **D1** Sans outils | Un bloc `SANS-OUTILS` au noyau, section « Classer, puis charger » (`agent/chemins.md`, servi aussi par `DIRECTION/CHARGE`), au texte proposé. 555 octets. |
| **D2** Un seul agent | Garde **SUB-01** (`validate_structure.py`, garde 27) : une phrase du noyau compilé qui parle d'un sous-agent, d'un second ou autre agent, d'agents séparés ou d'un travail en parallèle est refusée, sauf si elle le dit facultatif ou soumis à l'environnement. Le noyau actuel la passe. |
| **D3** Pas de réécriture | Les 23 blocs gardés sont inchangés. Budget du noyau à **31 500 octets** (31 057 aujourd'hui). |

## 2. Tests et mutations rouges

5 cas dans `test_audit_regressions.py` (classe `UnSeulAgent`) : le noyau réel passe ; « second agent » et « en parallèle » sont refusés ; la même phrase dite facultative ou soumise à l'environnement passe ; « l'agent » seul passe.

| Mutation | Résultat |
|---|---|
| La garde ne relève plus rien | Rouge : `test_second_agent_refuse`, `test_parallele_refuse` |
| « en parallèle » retiré de la liste | Rouge : `test_parallele_refuse` |
| L'exception « facultatif / si l'environnement » supprimée | Rouge : `test_facultatif_admis` |

## 3. Préparation et livraison

- **Préparation complète** : `--require-browser --empreintes`, réussie du premier coup.
  - Tests : régressions d'audit 173 (168 + 5), budget 19, `parcours` 176, `read_route` 106, `regard` 41, journal 19, `check_render` A, B et C.
  - Validations de structure, de carte de lecture, complète et locale : PASSED. Garde PRO-01 active.
- **Commits** : `01284d5` sur `lot-11d`, fusionné en `3705d62` sur `master` (`--no-ff`).
- **Archive GitHub** : les 151 fichiers sont identiques au commit.
- **Sortie** :
  - `Design_Governance_V1_GITHUB_R2026-11-15u.zip` (sha256 `82ad4bed…bd64`), à côté de la `k` ;
  - `claude/livraison/R2026-11-15u/` : archive Local (sha256 `bbeb3311…9d0b`) et bundle vérifié.
  - La `t` est retirée de DG-777. Elle reste dans l'historique et dans le bundle.

## 4. Bilan du lot 11

| Mesure | Avant le lot 11 (`q`) | Après (`u`) |
|---|---|---|
| Noyau | 45 876 octets | **31 057 octets (−32 %)** |
| Routes indexées au noyau | 34 sur 85 | **85 sur 85** |
| Obligations `[REQUIS]` tenues | 13 (11 par un bloc, 2 par un tronc) | 13 (8 par un bloc, 3 par une ligne, 2 par un tronc) |
| Lecture fixe d'un run DIRECTION (noyau + tronc) | ≈ 77 000 caractères | ≈ 65 000 (−16 %) |
| Lecture fixe des autres modes | noyau entier | ≈ −15 000 caractères de noyau |
| Gardes nouvelles | — | REQ-01 « ligne », IDX-01, SUB-01 |

## 5. Ce que ce lot ne prouve pas

- Qu'un agent sans outils suit le passage : il faudrait un run en profil E2.
- Que les lignes d'invariant et l'index suffisent pour que les modes courts ouvrent la bonne route : seul un run le dira (lot 13).
- Que SUB-01 attrape toutes les formulations : c'est une liste close.

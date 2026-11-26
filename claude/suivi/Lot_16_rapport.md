# Lot 16 — Rapport : des esquisses à armes égales ; publication V1.4.0

- **Révision** : `R2026-11-25f`, 25 novembre 2026. Publication **V1.4.0**.
- **Branche** : `lot-16`.
- **Décision** : « Ça me va » (options A, V1.4.0).
- **Runs** : aucun.

## 1. Ce qui change

| Sous-lot | Où | Changement |
|---|---|---|
| **16a** Deux usages des références | Noyau (ligne `ANCRE`) ; `DIRECTION/STANDARD` (« Calibrer le niveau ») ; `DIRECTION/DIVERGENCE` (« Une source par piste ») | Les références vues avant le premier build « calibrent le niveau, pas l'idée ». Après les directions, chaque direction gardée cherche ses propres références à partir de son fait, et non de la catégorie, dont une hors du domaine. |
| **16b** Esquisses à armes égales | Noyau (« chacune poussée avec sa propre source ») ; `DIRECTION/DIVERGENCE`, étape 2 ; `planche.py` | Avant la planche, chaque esquisse, la modale comprise, reçoit sa source, son geste poussé, sa voix et sa matière. « Une esquisse qui perd faute d'avoir été poussée n'a pas été éprouvée. » La planche signale une page nettement plus plate que les autres. |
| **16c** Le rang | `DIRECTION/DIVERGENCE` | « Le rang du fait dit d'où vient l'idée, mais ne mesure pas non plus sa rareté : un agent ne voit pas sa propre modale. » |

- **Trace** : la ligne « modal, trame et parti » nomme aussi la source de chaque esquisse (gabarit de `chantier` mis à jour).
- **Signal de planche** :
  - **Mesure.** Densité de bords de chaque premier écran, c'est-à-dire la part des pixels voisins dont la luminance diffère nettement, comparée à la médiane des autres pages.
  - **Seuil.** Une page est signalée sous 0,55 de la médiane (`[À ADAPTER]`), à chaque format capturé, et seulement dès trois pages.
  - **Essai sur la planche du run 22.** Il relève B (cartel) à 0,48, et rien d'autre ; C, le calendrier, est à 0,72.
  - **Marge.** Elle est étroite : un seuil à 0,45 n'aurait rien relevé.
- **Noyau** : 32 004 octets sur 33 000 (+83). Deux phrases protégées (CORE-01).

## 2. Tests et mutations rouges

| Mutation | Résultat |
|---|---|
| Le signal de page plate n'est plus émis | Rouge : R42 |
| « elles calibrent le niveau, pas l'idée » retiré du noyau | Rouge : CORE-01 |

## 3. V1.4.0

Manifeste, titres des README, notes et fiche de version, citation (1.4.0), cartes régénérées ; entrée V1.4.0 au journal des changements.

## 4. Préparation et livraison

- **Préparation complète** : réussie au premier passage, en **447 s**. Tests : `parcours` 196, `regard` 42, `check_render` 265, `read_route` 106… ; reproductibilité vérifiée.
- **Commits** : `18ccb96` sur `lot-16`, fusionné en `324d722` sur `master` (`--no-ff`).
- **Archive GitHub** : les 164 fichiers sont identiques au commit.
- **Sortie** : `Design_Governance_V1_GITHUB_R2026-11-25f.zip` (sha256 `1fc93948…f224`) ; `claude/livraison/R2026-11-25f/` : archive Local (sha256 `041dd419…c12c`) et bundle vérifié. La `25e` est retirée de DG-777.

## 5. Ce que ce lot ne prouve pas

- Que les alternatives deviennent aussi fortes que la gardée : seule ta lecture d'une planche le dira.
- Que la convergence recule : des sources par piste peuvent converger si les pistes convergent.
- Que le signal mesure l'investissement : il mesure une platitude visuelle. Une esquisse sobre par choix peut être relevée ; c'est pourquoi il pose une question.

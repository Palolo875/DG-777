# Lot 9e — Rapport (clôture du lot 9)

- **Révision** : `R2026-11-15o`.
- **Branche** : `lot-9e`, fusionnée dans `master` avec `--no-ff`.
- **Décision** : « Vas y » au document de propositions (`Lot_9e_Propositions.md`). Les options A s'appliquent partout.
- **Runs** : aucun.

## 1. Ce qui est intégré

| Proposition | Ce qui change | Garde |
|---|---|---|
| **P1** Références sans jugement (B-3) | `parcours.py verifier` compte les lignes « Change : … ; ne se transfère pas : … » de `refs.md` restées au gabarit. Il cherche dans `--refs`, ou sinon dans le dossier de la page et son parent, sur trois niveaux au plus, sans le dossier de la skill. Le résultat est une ligne de la fiche : un signal, pas un échec. **Essai sur les vrais runs du PILOT** : 13, 3, 4 et 5 lignes relevées (17k, 17l, 18k, 18l). | P26 |
| **P2** Référence de niveau (B-1, B-2) | Dans `SAVOIR/TOOLS/MOYENS`, « Références à observer » : une référence au moins est du même type d'objet et vient d'une source éditée ; un site d'information du sujet calibre le contenu, pas le niveau. Dans le bloc `ANCRE` du noyau, « au niveau de finition visé » devient « au niveau visé (ligne `NIVEAU`) ». | P27 |

Sont aussi mis à jour : `maintenance/evolution.md` (deux lignes) et la fiche de version.

**Noyau** : 45 810 octets sur 46 000.

## 2. Mutations rouges

Les cinq mutations rouges échouent chacune avec un échec nommé :
- gabarit mal reconnu ;
- dossier de la skill non exclu ;
- ligne de la fiche retirée ;
- renvoi à `NIVEAU` retiré ;
- phrase « source éditée » retirée.

**Correction en cours de route.** La première mutation restait **verte**. Mon test fabriquait son exemple avec la même constante que le code, si bien qu'une mutation de la constante se compensait elle-même. Le test écrit maintenant le gabarit tel que `references` l'écrit, en clair. La mutation est devenue rouge.

**Avant la préparation** : une cellule de `scripts/README.md` dépassait 500 signes (LIS-01). J'ai retiré mon ajout dans cette cellule, et la description reste dans `maintenance/evolution.md`.

## 3. Constats clos sans changement

A-1, A-2, A-3, A-4, B-6, C-3, C-4, D-1, E-3 et E-4 sont clos pour les raisons données dans `Lot_9e_Propositions.md`, section 0. A-2 reste suivi au carnet de goût ; A-4 reste une décision de Junior (génération d'images).

## 4. Préparation et livraison

À compléter.

## 5. Bilan du lot 9

Tous les constats du lot 9 sont traités ou clos. Les lots 9b à 9e ont produit les révisions `l`, `m`, `n` et `o`, sans run après le PILOT. Restent hors du lot :
- les deux pistes de `CLAUDE.md` (observer la modale par une recherche d'images ; accord pour la génération d'images) ;
- le test de convergence et la reprise de la série esthétique, quand Junior demandera un run.

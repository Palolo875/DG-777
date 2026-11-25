# Lot 14b — Rapport : oser

- **Révision** : `R2026-11-25a` (nouvelle série, accord de Junior : « Ça me va »), livrée le 25 novembre 2026. Version publique toujours V1.1.1 ; V1.2.0 à la fin du lot 14.
- **Branche** : `lot-14b`.
- **Décisions** : « D'accord, on lance » (options A du lot 14) ; budget du noyau à **33 000 octets** (« 33 000 ça me va »). Textes préparés dans `Lot_14b_textes.md`, intégrés tels quels, avec deux ajustements signalés au § 2.
- **Runs** : aucun.

## 1. Ce qui change

| Proposition | Changement |
|---|---|
| **N** Atelier symétrique | Route `ACTION/ATELIER-EDITION` : la variante qui intensifie l'élément porteur se fait **toujours** (échelle, contraste, position, fond perdu, matière ou cadrage, « poussés d'un cran net ») ; les trois versions (actuelle, retrait, intensification) se comparent sur une planche ; on garde la plus forte à la vue, avec sa raison ; garder l'actuelle reste valide ; l'intensification ne gagne que si l'idée s'y lit mieux, au niveau d'expression déclaré, sans que la tâche y perde. Ligne du noyau et étape 3 de la divergence : « test de retrait et d'intensification ». |
| **O** Expression déclarée | Ligne `NIVEAU` de la déclaration : « et l'expression attendue : sobre, affirmée ou expressive, déduite du sujet, du public et de la destination ». Ligne du noyau : `NIVEAU` (avec l'expression attendue). Règle « Classique et expressif » : « l'expression attendue […] dit jusqu'où l'écart se pousse ; elle se déduit du sujet et de la destination, jamais d'un goût par défaut. » |
| | Trace légère : la ligne de direction nomme l'expression ; `parcours.py trace` **signale** (sans refuser) une ligne de direction sans « sobre », « affirmée » ou « expressive ». Gabarits de trace (exemples, `chantier`) et exemple du guide 3 mis à jour. |
| **Q** Ambition | Bloc `POSTURE` du noyau : « **Pousser le geste.** Le plancher protège ; il ne suffit pas. Le geste qui porte l'idée se pousse jusqu'au bout, au niveau d'expression déclaré ; la retenue porte sur le reste, pas sur lui. » |
| Budget | `CORE_BUDGET_BYTES` 31 500 → **33 000** (build, maintenance, notes de version). Noyau : 31 358 → **31 699 octets**. |

## 2. Ajustements faits en route

- La garde CORE-01 posée en 14a protégeait « test de retrait, où l'élément qui porte l'idée ne part pas » ; N a changé la phrase. Elle protège maintenant « où l'élément qui porte l'idée ne part pas », qui reste.
- L'exemple de trace du guide 3 dit « expression : affirmée », pour rester un exemple sans signal.

## 3. Tests et mutations rouges

- `parcours` : 181 cas (+1) : ligne de direction sans expression signalée, sans échec ; avec « affirmée », aucun signal.
- CORE-01 : trois formulations nouvelles protégées (atelier symétrique, expression déclarée, « Pousser le geste »).

| Mutation | Résultat |
|---|---|
| Le signal d'expression n'est plus émis | Rouge : test « ligne de direction sans expression » |
| Le motif d'expression accepte tout | Rouge : même test |
| « Pousser le geste » retiré du noyau | Rouge : CORE-01 |

## 4. Préparation et livraison

À compléter.

## 5. Ce que ce sous-lot ne prouve pas

- Que les rendus deviennent plus affirmés tout en restant justes : seul un run jugé par Junior le dira.
- Le risque d'excès : surveillé par la planche à trois et le niveau d'expression ; non mesuré.
- Coût : une variante de plus par run à l'atelier ; non mesuré.

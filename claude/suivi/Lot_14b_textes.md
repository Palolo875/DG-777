# Lot 14b — Oser : les textes, avant intégration

Préparé le 25 novembre 2026, pendant la préparation de 14a. Base : `Lot_14_Propositions.md` (options A approuvées : « D'accord, on lance »). **Rien n'est intégré** : j'intègre après la livraison de 14a, sauf avis contraire de Junior. Les mots en gras sont les ajouts.

## N — Un atelier symétrique

**Route `ACTION/ATELIER-EDITION`**, phrase actuelle :
> Une variante qui **intensifie** la décision principale (échelle, contraste, position, fond perdu) ne se construit que si la capture la montre timide : l'idée ne se lit pas en une seconde, ou l'objet de preuve ne domine pas.

devient :
> **Fais aussi, toujours, la variante qui intensifie l'élément qui porte l'idée**, au même niveau de finition : échelle, contraste, position, fond perdu, matière ou cadrage, poussés d'un cran net. **Compare les trois sur une planche** (`planche.py`) : la version actuelle, le retrait, l'intensification. **Garde la plus forte à la vue, et dis pourquoi** ; garder l'actuelle reste un résultat valide. L'intensification ne gagne pas parce qu'elle est plus forte, mais parce que l'idée s'y lit mieux, au niveau d'expression déclaré (ligne `NIVEAU`), sans que la tâche y perde.

**Ligne du noyau (atelier)** : « test de retrait, où l'élément qui porte l'idée ne part pas » devient « **test de retrait et d'intensification**, où l'élément qui porte l'idée ne part pas, **comparés à la version sur une planche** ».

**Route `DIRECTION/DIVERGENCE`, étape 3** : « lecture sans le texte, test de retrait, défaut dominant » devient « lecture sans le texte, **test de retrait et d'intensification**, défaut dominant ».

## O — Le niveau d'expression déclaré

**Déclaration (`DIRECTION/DIVERGENCE`)**, ligne actuelle :
> NIVEAU — le niveau visé, en un test vérifiable sur capture (« qu'on la prenne pour la capture réelle d'une marque soignée »).

devient :
> NIVEAU — le niveau visé, en un test vérifiable sur capture (« qu'on la prenne pour la capture réelle d'une marque soignée »), **et l'expression attendue : sobre, affirmée ou expressive, déduite du sujet, du public et de la destination (une invitation de galerie n'appelle pas ce qu'appelle un outil de marées)**.

**Ligne du noyau (déclarer la direction)** : « `NIVEAU`, » devient « `NIVEAU` **(avec l'expression attendue : sobre, affirmée ou expressive)**, ».

**`SAVOIR/FRAME`, « Classique et expressif »**, une phrase ajoutée à la fin :
> **L'expression attendue, déclarée à la ligne `NIVEAU`, dit jusqu'où l'écart se pousse ; elle se déduit du sujet et de la destination, jamais d'un goût par défaut.**

**Trace légère** : la ligne « DIRECTION DÉCLARÉE ET THÈSE » nomme l'expression (« nom, registre, **expression**, mouvement, vision »). `parcours.py trace` signale une ligne de direction sans « sobre », « affirmée » ou « expressive », comme il signale déjà un choix sans « choisi par » : un **signal**, pas un refus.

## Q — Une ambition au-delà du plancher

**Bloc `POSTURE` du noyau**, un paragraphe ajouté après « Piège de conformité » :
> **Pousser le geste.** Le plancher protège ; il ne suffit pas. Le geste qui porte l'idée se pousse jusqu'au bout, au niveau d'expression déclaré ; la retenue porte sur le reste, pas sur lui.

## Coût et budget

| Changement | Octets au noyau (estimation) |
|---|---|
| Ligne d'atelier (N) | + 70 |
| Ligne de déclaration (O) | + 75 |
| Pousser le geste (Q) | + 220 |
| **Total** | **≈ + 365**, pour une marge de 142 (31 358 sur 31 500) |

**Proposition** : budget du noyau à **32 000 octets**. Alternative : financer en raccourcissant la ligne « Vérité de la scène » (≈ 340 octets, son détail reste dans sa route) ; je la déconseille, c'est une ligne de vérité.

Coût par run : une variante de plus à l'atelier (l'intensification), soit quelques tours.

## Gardes et tests prévus

- CORE-01 protège « test de retrait et d'intensification », « l'expression attendue : sobre, affirmée ou expressive » et « Pousser le geste ».
- `parcours.py trace` : le signal « expression non déclarée » apparaît sans sobre/affirmée/expressive, et disparaît avec ; l'exemple de trace livré (`references/examples.md`) est mis à jour et passe sans signal. Mutation rouge sur chaque.

## Ce que je surveillerai

- **Le risque d'excès** : un atelier qui intensifie toujours peut tirer vers le bruyant. La planche à trois et « garder l'actuelle reste valide » sont la parade ; le niveau d'expression déclaré la borne.
- **Le widget de marées aurait dû rester sobre** : l'expression « sobre » doit y donner une intensification de la lisibilité (une seule réponse, énorme), pas plus de couleurs.

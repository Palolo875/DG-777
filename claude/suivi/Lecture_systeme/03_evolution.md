# Lecture du système, étape 3 : maintenance/evolution.md (19 novembre 2026)

Lu : lignes 29 à 139 (promotion, cycle de vie, retrait). Les lignes 1 à 28 (recette documentaire) et 140 à 152 (contrats de maintenance) ne sont pas lues à cette étape.

## Ce qu'il dit
- **Une route devient durable** après « plusieurs usages contrastés documentés », un contrat complet, une maintenance assumée, des rendus qui **ne s'homogénéisent pas**, et un **gain réel observé ou mesuré, avec une base de comparaison, un contexte et une limite**. Elle ne se valide jamais « par beauté, fréquence ou capture unique ».
- **Le contrat de gain réel** demande : TASK, BASELINE, OBSERVATION ou MEASURE, CONTEXT, LIMIT, OWNER, NEXT-REVIEW.
- **Le cycle de vie :** SEED (le socle, sans gain mesuré), PILOT (au plus 5 à la fois), ADOPTED, DEPRECATED, ABANDONED. Le passage de SEED à ADOPTED exige le contrat de gain réel.
- **Une table de retrait** (lignes 107 à 138) : une trentaine d'entrées « versées au socle », chacune avec ce qu'elle apporte, sa limite et sa procédure de retrait. Presque toutes finissent par « Ne garantit pas le niveau ».

## Ce que j'y trouve
1. **Le système grandit par inclusion.** Les essais versés au socle y entrent avec le statut SEED, c'est-à-dire canoniques, sans gain mesuré. Aucun n'est ADOPTED, puisqu'aucun n'a de base de comparaison. Cela rejoint ce que relevait l'audit du 13 novembre : « Le système grossit plus vite qu'il n'est jugé ». **Probable**, d'après la table et les audits ; je n'ai pas relu chaque décision de versement.
2. **Une limite est déjà écrite noir sur blanc** (ligne 128) : la modale au second degré « agit à l'intérieur d'un run, pas d'un run à l'autre ». Le système sait donc qu'il ne voit pas une convergence d'un run à l'autre, et c'est exactement le cas du diagramme vu de dessus, aux runs 9, 10, 14 et 16.
3. **Les recettes de code existent déjà** (ligne 137, `references/recettes.md`, 175 lignes). Il y en a cinq : graphique, grand chiffre, moment orchestré, focus, contrôles. Elles contiennent du code. Mais elles règlent **« un comportement, jamais une apparence »**, et la règle dit : « si deux rendus en sortent avec la même apparence, elle impose un style : elle se réécrit ou se retire ». **Elles ont servi trois fois en six runs** : 2 fois au run 11, 1 fois au run 14, jamais ailleurs.
4. **Le système refuse volontairement les exemples d'apparence**, pour éviter que les rendus se ressemblent (critère de « non-homogénéisation »). C'est un choix délibéré, et il contredit ma proposition de « spécimens » visuels, que j'avais présentée comme une idée neuve. Je ne l'avais pas vu.
5. **Pour STANDARD, « la convention bien exécutée » existe déjà** (ligne 132) : rayons emboîtés, gris hiérarchisés, un accent par rôle, chiffres alignés, états vrais. Le point « convention exécutée à haut niveau » n'est donc pas absent ; il est écrit comme une liste de finition, et les runs ne le montrent pas tenu.

## Recherche faite à côté : exemples ou consignes ?
- *Teach Better or Show Smarter?* (https://arxiv.org/abs/2406.15708, 2024) : choisir de bons exemples améliore davantage le résultat qu'optimiser les consignes. « Même des consignes détaillées ne règlent pas le comportement aussi bien que des exemples, qui permettent l'imitation. » Ces tâches sont du raisonnement, pas du design.
- *Show and Tell* (https://arxiv.org/abs/2511.13972, 2025), sur le contrôle du style dans du code généré : **la combinaison de consignes et d'exemples donne le meilleur contrôle**. Les consignes seules tiennent mieux que les exemples seuls quand le code s'étend sur plusieurs tours. Les exemples seuls aident surtout la forme initiale.
- Deux autres travaux trouvent un effet variable des exemples, et parfois nul ou négatif (INSTRUCTEVAL, https://arxiv.org/pdf/2306.04757 ; *The Atomic Instruction Gap*, https://arxiv.org/pdf/2510.17388).
- **Correction de mon affirmation d'avant :** « des spécimens plutôt que des règles » était trop fort. Les études soutiennent plutôt **des contraintes courtes accompagnées d'exemples**, avec des effets qui dépendent de la tâche.

## Ce que ça change pour la suite
- Il y a une vraie tension à trancher : **des exemples d'exécution font monter le plancher, mais risquent d'uniformiser les rendus**, ce que le système refuse.
- **Piste créative, à discuter :** des « triptyques » plutôt que des spécimens. Une même convention, par exemple la grille d'un billet, exécutée au plus haut niveau dans **trois registres très différents**. On montre ce qui reste constant (la qualité d'exécution) et non une apparence à copier, ce qui respecte le critère de non-homogénéisation.
- **Le cadre PILOT, avec son contrat de gain réel, est le bon véhicule** pour essayer le kit : une base de comparaison (avec et sans), une observation, une limite, et au plus cinq essais à la fois.

## Suite proposée
Lire `references/recettes.md` en entier, puis `design/README.md` (le cœur du système, auquel renvoie la section « Fonctionnement » du README).

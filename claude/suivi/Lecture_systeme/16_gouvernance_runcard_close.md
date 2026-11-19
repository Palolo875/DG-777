# 16 — Gouvernance : README, RUN_CARD, CLOSE-PACKAGE

Lecture du 19 novembre 2026. Ce qui a été lu :
- `gouvernance/README.md` (2,8 k) ;
- `ACTION/RUN_CARD` (18,0 k), survolée ;
- `ACTION/CLOSE-PACKAGE` (7,2 k).

## 1. Ce que les runs en ont fait

- Aucun run n'a lu `RUN_CARD` ni `CLOSE-PACKAGE` (journaux des runs 9 à 16).
- C'est cohérent : tous les runs de la série étaient en trace légère. Le README de la gouvernance le dit lui-même : « Proposition exploratoire : trace légère, limites visibles ; pas de RUN_CARD ni d'acceptation implicite. »

## 2. Ce que contient la gouvernance

- **Son rôle (README).** « Vérifier une affirmation, protéger un risque, permettre une reprise ou préparer une acceptation. » Elle n'est « pas un formulaire à remplir systématiquement », et « montrer une proposition ne vaut pas accepter un produit ».
- **RUN_CARD.**
  - Des champs minimaux : ID, owner, mode, état, issue, verdict, statut de direction…
  - Un profil de capacités : disponible, indisponible ou non requis.
  - Un tableau **« Mode agent seul et preuve dégradée »**. Avec le rendu et la capture mais sans second regard, l'agent peut construire, comparer et corriger. Il ne peut pas conclure seul à une revue indépendante, ni calibrer une décision d'identité importante.
  - Une **frontière de validation** : une RUN_CARD validée atteste la forme de la trace, **jamais la qualité visuelle** ni la préférence.
- **CLOSE-PACKAGE.**
  - Un paquet minimal par mode. En DIRECTION, il comprend un « creative close » : présence, signature, détail de craft, défaut dominant, prochaine action.
  - La fraîcheur de la preuve : un verdict expire après un changement.
  - Le cycle de vie des réserves, l'owner final et les droits.
  - **Une condition d'arrêt du polish** : il s'arrête quand plus rien ne promet de changer une relation visible.

## 3. Ce que la gouvernance fait et ne fait pas pour le goût

- **Elle protège contre les fausses affirmations**, pas contre la médiocrité. Tout y est construit pour qu'un manque de preuve ne soit pas rédigé comme une réussite. Le système le dit lui-même (frontière de validation).
- **Pour la série esthétique**, en trace légère, elle se réduit à « proposition exploratoire, limites visibles ». Elle ne coûte presque rien dans les runs, et ne les aide presque pas.
- **Son coût réel se trouve dans le noyau.** Le vocabulaire de preuve et de trace y occupe une place notable : `trace` 31 fois, `preuve` 29, `Gate` 14, `verdict` 7, et `NOT-VERIFIED`, `N/A-JUSTIFIED` et `EXPLORATORY` 4 fois chacun. Je n'ai pas mesuré la part en octets.

## 4. Recherches à côté (Exa et WebSearch)

| Source | Ce qu'elle dit | Ce que ça touche |
|---|---|---|
| Tam et al., *Let Me Speak Freely?* (EMNLP 2024 Industry) | Imposer un format strict (JSON, XML) **dégrade le raisonnement**, d'autant plus que la contrainte est stricte. Les tâches de classification, elles, peuvent s'améliorer. | Une trace très formatée pendant la création pourrait coûter de la qualité. |
| Réponse de .txt (dottxt), *Say What You Mean* ; mise à jour des auteurs (GitHub, décembre 2024) | La réponse attribue la baisse à des prompts différents entre les deux conditions. À prompts égaux, la génération structurée fait aussi bien ou mieux. Les auteurs maintiennent l'écart en moyenne sur 9 prompts, avec une forte variance. | **Résultat contesté.** On ne peut pas affirmer que la trace nuit à la création. En revanche, la charge d'instructions qui s'accumulent (IFScale, ManyIFEval, déjà notés) reste un mécanisme mieux établi. |

## 5. Constats

**Certain**
- La gouvernance est explicitement allégée en trace légère. Elle ne prétend pas juger la qualité visuelle, et l'auto-jugement y est borné, comme dans GATE-B.
- Rien dans la gouvernance ne cause directement les rendus « génériques ».

**Probable**
- Son effet sur le goût est **indirect** : elle prend une part du budget d'attention du noyau. C'est le même mécanisme que pour toutes les instructions qui s'accumulent.

**À vérifier**
- La part réelle du noyau consacrée à la preuve et à la trace, et si l'on peut la déplacer sans perdre les gardes. Le budget est de 46 000 octets, le noyau en fait 45 250 : il n'y a presque plus de marge pour ajouter du savoir de goût sans en retirer.

## 6. Pistes (non intégrées, règle 1)

1. **Mesurer la part du noyau par fonction** : direction, goût, preuve, trace, outils. C'est un simple relevé par bloc `NOYAU`, sans rien changer. Ce serait la base pour libérer de la place, si Junior veut servir des lignes de goût dans le noyau.
2. **Ne rien ajouter à la gouvernance pour la série esthétique.** Le seul ajout utile est la ligne « choix : auto-jugé / Junior / absent » (note 15), qui reprend une règle existante.

## Sources
- Tam et al. 2024 (ACL Anthology) : https://aclanthology.org/2024.emnlp-industry.91/
- Tam et al. 2024 (arXiv) : https://arxiv.org/abs/2408.02442
- Réponse de .txt : https://blog.dottxt.ai/say-what-you-mean.html
- Mise à jour des auteurs : https://github.com/appier-research/structure-gen/blob/main/updates.md

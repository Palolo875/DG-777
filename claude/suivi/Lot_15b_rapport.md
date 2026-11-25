# Lot 15b — Rapport : l'idée propre au sujet ; publication V1.3.0

- **Révision** : `R2026-11-25e`, 25 novembre 2026. Fin du lot 15 : publication **V1.3.0**.
- **Branche** : `lot-15b`.
- **Décisions** : « Ça me va » (options A du lot 15) ; « Oui » pour lancer 15b et corriger le mode rapide.
- **Runs** : aucun.

## 1. Ce qui change

| Piste | Où | Changement |
|---|---|---|
| **I et M** : idée tirée d'un fait de deuxième rang | Noyau (ligne « Diverger sur image ») ; `DIRECTION/DIVERGENCE` ; `SAVOIR/CRAFT/CFT-01` (paragraphe « Classer ») | L'inventaire du sujet se classe du plus évident au moins évident. Le premier rang est ce que tout agent prendrait. Les trois esquisses viennent d'un fait de deuxième rang ou au-delà ; le premier rang ne gagne que sur la planche. Sur un brief vague, l'inventaire supposé est écrit dans la trace, pour que la personne puisse le corriger. |
| **J** : rareté | `DIRECTION/DIVERGENCE` ; trace | Les probabilités restent, comme ordre de grandeur pour diversifier. Ce qui se vérifie, c'est le rang du fait. La trace dit de quel rang vient l'idée gardée ; `parcours.py trace` signale une ligne « modal » sans rang (signal, pas échec ; sans objet en décision étroite). |
| **Q1-2** : plaider pour la modale | Noyau ; `DIRECTION/DIVERGENCE` | Avant de juger, la modale est défendue en une ligne (ce qu'elle ferait de mieux pour ce sujet) et esquissée sous cet angle. Une esquisse ne l'emporte que si elle bat la modale ainsi défendue. Même règle pour une voix typographique jugée modale : elle part en perdant sur la planche, pas sur son étiquette. |
| **Mode rapide** | `validate_all.py --rapide` | Il transmet maintenant, comme la préparation complète, la liste des noms tirés des runs (garde PRO-01). |

- **Gabarits de trace** : les trois exemples de `references/examples.md`, le guide 3 et le gabarit de `chantier` disent le rang (et la défense de la modale dans le gabarit).
- **Noyau** : 31 921 octets sur 33 000 (+222). Deux phrases protégées (CORE-01) : « tirées d'un fait de deuxième rang ou au-delà » et « face à la modale défendue en une ligne ».

## 2. Tests et mutations rouges

| Mutation | Résultat |
|---|---|
| Le signal « sans rang » n'est plus émis | Rouge : P89 |
| La défense de la modale retirée du noyau | Rouge : CORE-01 |
| Le mode rapide n'active plus PRO-01 | Rouge : `test_rapide_active_pro01` |

## 3. V1.3.0

- **Version publique V1.3.0** : manifeste, titres des README (français et anglais), notes de version, fiche de version, citation (1.3.0), quatre cartes régénérées.
- **Journal des changements** : entrée V1.3.0 (cinq recettes, matière observée, idée de deuxième rang, modale défendue).

## 4. Préparation et livraison

_à compléter_

## 5. Ce que ce sous-lot ne prouve pas

- **La convergence.** Rien ne dit qu'elle recule. Des agents du même modèle dressent le même inventaire, et le classent sans doute dans le même ordre : le deuxième rang peut converger à son tour. Seule une campagne de runs le dira. Le vrai remède reste le contenu réel du client.
- **Les rangs que donne l'agent.** Le système les relève sans les vérifier : c'est une déclaration.
- **La modale défendue** peut se défendre sans conviction. La planche et ton regard restent juges.

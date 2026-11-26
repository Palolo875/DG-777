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

- **Préparation complète** : réussie au premier passage, en **479 s**. Tests : `parcours` 196, audit 198, `check_render` 265, `regard` 41, `read_route` 106… ; reproductibilité vérifiée.
- **Un faux pas à la livraison** : mon `git add` a refusé le dossier ignoré `dist`, et le commit n'a pas eu lieu. La comparaison de l'archive l'a montré (fichiers différents de l'ancien `master`). Après le commit, l'archive est identique.
- **Commits** : `83b4a79` sur `lot-15b`, fusionné en `54fa7a0` sur `master` (`--no-ff`).
- **Archive GitHub** : les 164 fichiers sont identiques au commit.
- **Sortie** : `Design_Governance_V1_GITHUB_R2026-11-25e.zip` (sha256 `5baceb2b…ccfd`) ; `claude/livraison/R2026-11-25e/` : archive Local (sha256 `fb9c4b04…cfdb`) et bundle vérifié. La `25d` est retirée de DG-777.

## 4 bis. Discussion après livraison : l'optimisation

Junior : ne pas optimiser à tout prix ; références, recherches, captures et tours d'atelier servent la qualité. **Décision : rien ne change pour l'instant.** Piste notée : mesurer le seul gaspillage pur (route relue, page réécrite pour une retouche, commande relancée sans raison) sur le journal du Run 21, si le coût devient un frein.

## 5. Ce que ce sous-lot ne prouve pas

- **La convergence.** Rien ne dit qu'elle recule. Des agents du même modèle dressent le même inventaire, et le classent sans doute dans le même ordre : le deuxième rang peut converger à son tour. Seule une campagne de runs le dira. Le vrai remède reste le contenu réel du client.
- **Les rangs que donne l'agent.** Le système les relève sans les vérifier : c'est une déclaration.
- **La modale défendue** peut se défendre sans conviction. La planche et ton regard restent juges.

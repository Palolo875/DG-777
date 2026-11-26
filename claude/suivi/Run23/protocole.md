# Run 23 — V1.4.0, brief d'une ligne : les esquisses à armes égales ?

- **Lancé le** 25 novembre 2026. **Décision** de Junior : « Allons-y » (après le rapport du lot 16, qui proposait ce run).
- **But** : savoir si, avec la V1.4.0, les esquisses arrivent **à armes égales** sur la planche (chacune avec sa source, son geste poussé, sa voix, sa matière), et si les sources par piste sortent de la catégorie. Secondairement : la qualité du rendu sur un brief vague, et le coût.

## Conditions

- Paquet : `R2026-11-25f` (V1.4.0), installé depuis l'archive Local livrée, dans `/tmp/run23f/.claude/skills/design-governance-practice`.
- Un agent neuf (sous-agent `general-purpose`, modèle de la session, effort par défaut), dossier vide, `DG_JOURNAL` activé.
- Le prompt des runs 17 à 22, au brief et aux livrables près (une page de site : captures à 1440 et 390 px).
- **Brief d'une ligne, choisi par Claude** : « Fais la page d'accueil du site d'un petit atelier de réparation de vélos à Bordeaux. » Aucun nom, aucune donnée : l'agent doit poser ses hypothèses.
- Ressources : Internet gratuit et sans compte ; ni génération d'images, ni outil branché, ni service payant.

## Ce qui se relève

- La planche des esquisses : sont-elles à armes égales (jugement de Junior) ? Le signal de page plate s'est-il déclenché, et qu'en a fait l'agent ?
- Les recherches : avant les directions (calibration), puis par piste ; une recherche hors du domaine ?
- L'idée gardée, son rang, la modale défendue.
- Le coût (`cout_des_runs.py`).

## Limite

Un run montre une tendance, il ne prouve rien. Aucun point de comparaison sans système sur ce brief.

## Résultats (relevés par Claude ; le jugement est celui de Junior)

- **Idée gardée** : « Départs » : la page est une affiche jaune des départs de gare ; chaque réparation a son heure de départ et son prix ; un billet calcule l'heure et le total à partir de cases cochées (geste repris de l'esquisse C). Titre : « Déposé le matin, reparti le soir. »
- **Planche** (`livrable/planche-esquisses.png`) : quatre esquisses, toutes poussées.
  - **Modale** : vraie photo libre d'un mécanicien, cartes de services.
  - **A, Départs** : tableau jaune.
  - **B, Pierre blonde** : enseigne « CYCLES » peinte sur fond de pierre.
  - **C, Fiche** : étiquette kraft à cocher, tampon « Prêt ce soir 17 h ».
  - **Lecture de Claude** : nettement plus égales qu'au run 22 ; C est une vraie concurrente. Code des esquisses : 3,1 à 4,0 ko, contre 1,6 à 2,6 au run 22.
  - **Signal de page plate** : non déclenché.
- **Références** :
  - calibration d'abord (sites d'ateliers vélo, 20 h 24) ;
  - puis recherches par piste avant la planche : façade en pierre calcaire de Bordeaux, étiquette de réparation, liste de prix à la craie (20 h 28–29), dont une partie hors du domaine ;
  - la source de A (affiches de gare) est nommée dans la trace, sans recherche relevée au journal.
- **Trace** : modale ~55 %, rang 1, défendue (« la photo rassure en une seconde ») ; A ~7 %, rang 6, issue du tirage, source nommée ; B ~5 %, rang 7 ; C ~10 %, rang 5.
- **Coût** : 151 tours, cache lu 32,6 M, 23 images, 21 minutes. Moins que le run 22 (174 tours, 38,4 M) et proche du run 19x (141, 33,5 M).

## Jugement de Junior

« Je partage ton avis » : rendu solide et professionnel, idée propre au sujet et exécution nette ; il lui manque la chaleur et la matière de l'atelier (le geste de l'esquisse C repris, sa matière perdue) ; tableau absent du premier écran mobile ; frise « Arrivées » faible. Constats pour le système, à vérifier : la fusion de deux esquisses garde le geste et perd la matière ; la survie de l'idée au premier écran mobile n'a pas bloqué.

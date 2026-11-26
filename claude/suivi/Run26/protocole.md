# Run 26 — V1.8.0, un objet qui n'est pas un site : l'écran d'accueil d'une application

- **Lancé le** 26 novembre 2026. **Décision** de Junior : « Ça me va » (run proposé sur un objet qui n'est pas un site).
- **Choix de Claude** : une application mobile, le terrain des références de Junior (interfaces de produit), presque jamais éprouvé par le système.
- **Brief d'une ligne, choisi par Claude** : « Conçois l'écran d'accueil d'une application mobile de suivi de dépenses pour un jeune couple. »
- **But** : après les lots 18 à 20, le rendu passe-t-il pour un produit fini de son genre (« soigné, fini, abouti, le visuel global ») ? Sinon, qu'est-ce qui fait encore démo ou basique ? Relevés :
  - étapes lues ;
  - recettes appelées (grille, détails de composants, données, mouvement) ;
  - signaux de retenue ;
  - coût.
- **Conditions** : paquet `R2026-11-25k` (V1.8.0) depuis l'archive Local ; agent neuf (sous-agent `general-purpose`, modèle de la session, effort par défaut) ; dossier vide ; `DG_JOURNAL` ; prompt des runs précédents, au brief et aux livrables près (écran à 390 px, et à 1440 px si l'agent le juge utile) ; Internet gratuit sans compte ; ni génération d'images, ni outil branché, ni service payant.
- **Jugement** : Junior.
- **Limite** : un run montre une tendance.

## Résultats (relevés par Claude ; le jugement est celui de Junior)

- **Étapes lues au bon moment** : ESQUISSES avant les esquisses (07 h 04), CONSTRUCTION après le choix (07 h 10). `DIRECTION/STANDARD` (« Un vrai produit d'abord ») lu aussi.
- **Recettes appelées** : `details-composants` seulement. La grille tirée (`GRID/RADIAL`, avec sa recette annoncée) a donné l'esquisse B, un cadran, sans que la recette soit ouverte.
- **Planche** (`livrable/planche-esquisses-390.png`) : quatre esquisses poussées, à armes égales.
  - Modale : carte violette « reste à dépenser », anneau par catégorie, bouton flottant.
  - A, « La ligne de partage » : fond papier, serif, une ligne de budget partagée.
  - B : cadran sombre.
  - C : fil de messages.
- **Idée gardée** : A. En tête, une phrase (« En novembre, Léa a avancé 1 328 €, Malik 374 € ») et une ligne de budget avec le repère « Votre partage 58 / 42 » et la part avancée en trop hachurée. Puis l'écart à régler (« Malik verse 341,09 € à Léa »), « Régler la différence », « Voir le calcul », le rythme du mois, les dernières dépenses, l'ajout dans la zone du pouce, la barre d'onglets. États vide et « quittes » ; ajout de dépense fonctionnel ; erreur près du champ ; montants vérifiés (9 assertions).
- **Lecture de Claude** :
  - **Plus de gadget** : c'est une vraie application. Conventions tenues, l'idée vit dans un détail de données (la ligne et son repère), le texte est simple.
  - **Mais le profil « éditorial » revient** : fond papier, serif, filets, boutons cerclés, aucune profondeur. L'agent le dit lui-même (« deux choix très répandus en ce moment »).
  - La modale, plus proche des références de Junior (interfaces de produit soignées), a perdu.
- **Coût** : 197 tours, cache lu 47,8 M, 21 images, 20 minutes (run 25 : 202 tours et 53,1 M).

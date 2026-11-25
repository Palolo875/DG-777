# Run 21 — capacité esthétique : section héro (V1.1.1)

- **Lancé le** 25 novembre 2026. **Décision** de Junior : « on va faire une héro section pour évaluer la capacité esthétique […], c'est un run. Pas de run avec ou sans le système pour l'instant. » Brief et effort choisis par Junior parmi mes options.
- **But** : évaluer la capacité esthétique de la V1.1.1 sur un premier écran, seul (aucune comparaison).
- **Paquet** : `R2026-11-15y` (V1.1.1), archive Local livrée.
- **Agent** : sous-agent `general-purpose` neuf, modèle `claude-opus-5-5`, effort high, dossier vide `/tmp/run21y`.
- **Prompt** : le prompt type de la série (ressources gratuites, ni génération ni connecteur ni service payant ; « Je ne serai pas disponible »), mode laissé à l'agent.
- **Brief** : section héro du site d'une fonderie typographique indépendante inventée (« Contrepoinçon », Nantes) qui lance une famille inventée (« Marnière ») : serif d'édition, 8 graisses et italiques, variable, latin étendu ; essai gratuit, licences dès 60 € par style ; belle au bureau et sur téléphone.
- **Difficulté assumée** : la famille n'existe pas ; l'agent doit la montrer avec une police libre de remplacement, et le dire.
- **Livrables** : HTML autonome ; premier écran à 1440 px et à 390 px ×2 ; détails ×2 ; trace.
- **Jugement** : Junior seul, sur le rendu.

## Déroulé (25 novembre 2026)

- **Mode** : DIRECTION, choisi par l'agent. Direction déclarée « Bon à tirer » : la famille jugée comme un livre, sur une double page (texte annoté à gauche, page de titre réglable à droite).
- **Procédure suivie** : modale nommée, 4 pistes dont 3 esquissées et comparées sur planche (`planche-divergence.png`), atelier avec test de retrait (`atelier-test-de-retrait.png`), `verifier` à 1440, 768 et 390 px, mouvement vérifié en réduit.
- **Vérité** : Marnière figurée par Literata (OFL), dit en note visible ; textes, liens et année marqués comme exemples.
- **Coût** : 153 tours, sortie 198 k, cache lu 32,4 M, contexte max 297 k, 26 images, 90 appels d'outils, 17 min.
- **Livrables** : `Run21/livrable/` (copie). Noms du brief ajoutés à `noms_interdits.txt`.
- **Jugement de Junior** : à venir.

## Avis de Claude (25 novembre 2026), à garder en tête (décision de Junior)

- Réussi : idée juste pour le public (le caractère jugé sur une page de texte), finition professionnelle, retenue, curseur de graisse, honnêteté sur le remplaçant.
- Faible : (1) au bureau, l'idée « livre » se lit moins que dans l'esquisse (cadre sombre retiré par le test de retrait) ; (2) à 390 px, le premier écran est presque la modale, l'idée n'arrive qu'en défilant ; (3) page de droite chargée ; (4) notes de marge collées au bord à 1440 px.
- Hypothèses pour le système, **non intégrées** : le test de retrait protège ce qui porte l'idée ; une lecture sans le texte aussi sur le premier écran mobile.

## Question 1 discutée (25 novembre 2026), mise de côté par Junior

Le système fait suivre la procédure ; ce qui échappe est le jugement visuel (l'agent juge son propre travail). Pistes notées, non intégrées : (1) comparer chaque version à l'esquisse choisie, à même échelle, bureau et mobile ; (2) plaider pour la modale avant de l'écarter ; (3) le goût par l'exemple (paires jugées).

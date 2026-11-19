# Lecture du système, étape 1 : README.md (19 novembre 2026)

Paquet `R2026-11-15k`. Le fichier lu est `README.md` en entier (132 lignes). Les mesures et les recherches sont faites à côté de la lecture.

## Ce que dit le README
- **Promesse :** des pages, écrans et identités « qui ont une vraie direction, réellement construits et soignés dès la première proposition », puis améliorés en regardant le rendu.
- **Objectif :** « obtenir un niveau élevé plus régulièrement, avec moins d'oublis, de tâtonnements et de reprises inutiles ». C'est déclaré comme une **hypothèse à éprouver**, renvoyée au « cap » de `maintenance/versions.md`.
- **Périmètre :** « éprouvé sur le Web » ; l'identité est moins éprouvée.
- **Fonctionnement :** deux boucles, créer puis apprendre. La boucle « créer » comprend une étape « calibrer le niveau sur des références réelles ».
- **Cinq règles essentielles :** direction visible, ancre, vérifications, déclarer avant d'agir, réel et beau ensemble.
- **Limites :** l'efficacité n'est pas vérifiée ; « séduisant n'est pas prouvé, conforme n'est pas réussi » ; « une étape ou une référence qui ne change rien est retirée » ; le niveau dépend des moyens atteints.

## Mesures
- `SKILL.md` : 244 lignes, 6 719 mots, 45 250 caractères.
- Tronc `DIRECTION`, lu en plus au démarrage : 5 180 mots, 35 882 caractères.

## Recherches faites à côté
1. **La spécification Agent Skills** (https://agentskills.io/specification) recommande moins de 5 000 jetons pour le corps de `SKILL.md`, et moins de 500 lignes. Le guide d'Anthropic (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) dit la même chose : « Concise is key… Only add context Claude doesn't already have ». Un guide d'un tiers rappelle que ces limites sont des repères, pas des plafonds stricts.
   - **Constat** (l'estimation des jetons est approximative : il y a plus d'un jeton par mot en français) : le noyau tient sous les 500 lignes, mais avec des lignes très longues. En jetons, il dépasse probablement **deux fois** la recommandation. En ajoutant le tronc, un run `DIRECTION` charge probablement **trois à quatre fois** ce budget avant le premier pixel.
2. **Le suivi de nombreuses consignes à la fois.**
   - IFScale (https://arxiv.org/abs/2507.11538, NeurIPS 2025) : la précision baisse quand le nombre de consignes simultanées augmente. Même les meilleurs modèles n'atteignent que 68 % à 500 consignes. Les modèles favorisent les **premières** consignes, et les modèles qui raisonnent tiennent jusqu'à environ 100 à 250 consignes avant de décrocher.
   - ManyIFEval (EMNLP 2025, https://doi.org/10.18653/v1/2025.findings-emnlp.896) : la performance baisse dès 6 à 10 consignes simultanées.
   - **Limite :** ces études portent sur des consignes simples (des mots-clés, du format), pas sur des consignes de design. Elles ne prouvent rien pour la skill ; elles rendent seulement plausible le risque qu'une consigne de goût se perde au milieu de nombreuses consignes de procédure.

## Ce que j'en retiens
- **Le cap prévoit un témoin qu'on n'a pas fait.** `maintenance/versions.md` (ligne 22) dit : « Chaque question se juge par comparaison avec un travail fait sans lui, sur des demandes comparables ». Aucun run sans la skill n'a encore été fait. **Le critère du système lui-même demande ce run témoin.**
- **Les règles disent surtout comment travailler, pas la qualité visée.** Quatre des cinq règles portent sur le processus et la preuve (ancre, vérifications, déclaration, réel et beau ensemble). Seule la première parle du résultat visible, et aucune ne parle de l'exécution au détail. C'est cohérent avec ce que montrent les runs : la vérité et la conformité sont tenues, le goût l'est moins.
- **Le README fixe lui-même un principe d'économie :** « une étape ou une référence qui ne change rien est retirée ». Il justifie déjà d'alléger ce qui ne change pas le rendu, comme les probabilités chiffrées ou certains formulaires. C'est à vérifier étape par étape, pas à affirmer.
- **Deux formulations se contredisent :** « éprouvé sur le Web » d'un côté, « efficacité non vérifiée » de l'autre. « Éprouvé » semble vouloir dire « essayé en runs », pas « prouvé efficace ». La formulation peut induire en erreur.

## Suite proposée
Lire `maintenance/versions.md` : le cap, puis « ce qui est vérifié, ce qui ne l'est pas ». Le README y renvoie pour juger l'hypothèse.

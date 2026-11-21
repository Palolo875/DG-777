# Lot 10 — Propositions : meilleur, plus rapide, moins coûteux, sans perte de qualité

Rédigé le 21 novembre 2026. Base : `R2026-11-15o` (`master` `03cdd00`). Aucun run pour cette rédaction.

Règle 1 : rien n'est intégré sans décision. « D'accord » vaut pour les options A partout.

## 0. Mesure : où partent réellement le coût et le temps d'un run

**Méthode.**
- Dépouillement par script des transcriptions des quatre agents du PILOT (17k, 17l, 18k, 18l) : jetons déclarés à chaque tour, appels d'outils, taille du texte renvoyé, images reçues.
- Le script est dans le scratchpad. Il ne lit aucun contenu, il compte.

| Run | Tours | Contexte maximal | Lecture de cache cumulée | Écriture de cache | Sortie | Images lues | Durée |
|---|---|---|---|---|---|---|---|
| 17k | 203 | 320 k | **46,4 M** | 0,80 M | 267 k | 28 | 27 min |
| 17l | 163 | 308 k | **36,6 M** | 0,55 M | 190 k | 29 | 22 min |
| 18k | 116 | 254 k | **21,9 M** | 0,35 M | 132 k | 13 | 14 min |
| 18l | 208 | 316 k | **45,3 M** | 0,64 M | 300 k | 24 | 21 min |

### Correction d'une erreur de ma part

J'ai annoncé partout environ 275 à 330 k jetons par run : dans le registre, dans le protocole du PILOT et dans mes avis. **Ce chiffre est la taille finale du contexte, pas le coût.** À chaque tour, l'agent relit tout son contexte, généralement depuis le cache. Le volume réel traité par run est de **22 à 46 millions de jetons lus en cache**, plus 130 à 300 k jetons de sortie.

### Où va le coût

Le calcul utilise les tarifs relatifs publiés : lecture de cache entre 0,05 et 0,1 fois le prix d'entrée selon le modèle, écriture de cache 1,25 fois, sortie environ 5 fois.

| Poste | Part estimée |
|---|---|
| Contexte relu à chaque tour (lecture et écriture de cache) | **70 à 80 %** |
| Sortie (réflexion, HTML, commandes) | 20 à 30 % |

**Le coût suit donc presque le produit du nombre de tours par la taille moyenne du contexte.** C'est le levier principal, devant la longueur du noyau prise seule.

### Ce qui remplit le contexte (texte renvoyé à l'agent, par run)

- **Images** : 13 à 29 captures lues, avec un plafond d'environ 1 600 jetons chacune, soit 20 à 45 k jetons qui restent là jusqu'à la fin.
- **Lecture du noyau et du tronc** : environ 80 k caractères, soit environ 22 k jetons, présents dans tous les tours.
- **Sorties de `read_route`** : 10 à 53 k caractères.
- **Sorties de `verifier`** : 12 à 18 k caractères. 17k l'a lancé **11 fois**.
- **Commandes diverses** (`ls`, `cat`, scripts ponctuels) : 33 à 63 k caractères, en 21 à 36 appels.
- **Recherches web, lecture du HTML produit** : 8 à 35 k caractères chacune.

### Le même levier joue sur la qualité

- Les modèles se dégradent quand le contexte s'allonge, même sur des tâches simples, et davantage quand on ajoute du contenu non pertinent (Chroma, *Context Rot*, 2025, 18 modèles).
- C'est cohérent avec la dégradation quand les instructions s'accumulent (IFScale, ManyIFEval, notes 01 à 03).
- **Alléger le contexte n'oppose donc pas coût et qualité.** C'est probablement bon pour les deux, mais à vérifier par run.

## 1. Propositions

### A. Propreté : sortir de la skill ce qui n'est pas la skill

**A1 — Les fuites du journal de Junior (vérifiées dans les 151 fichiers).**
- Les deux citations de runs dans `qualite-creative.md` (« Le dessin est fixé », « le 3 avril tombe un samedi ») et « Terres lentes » dans `test_regard.py` sont remplacées par des exemples neutres.
- La phrase de coût obsolète de `versions.md` (« un run avec le système coûte plus de jetons et de temps… », tirée de la mesure du 29 octobre) est remplacée par la mesure actuelle, datée, sans comparaison.
- La ligne « Convergences relevées avec le système » de la veille dit qu'elle vient d'essais sur peu de briefs. **À trancher par Junior : la garder ainsi, ou la sortir vers le suivi.**
- Une garde refuse dans le paquet les noms de briefs, de lieux et de titres des runs. La liste est tenue hors du paquet et passée au validateur. Test avec mutation rouge.

**A2 — Séparer la skill de l'atelier.**
- Une troisième distribution, « skill », contient seulement ce qu'un agent et une personne utilisent.
- Elle exclut : tests, validateurs, fixtures, compilation, préparation, CI, maintenance, génération des supports, `journal_mobilisation.py`. Cela fait 55 fichiers sur 151.
- Les outils de production n'importent le journal que s'il est présent.
- La route `DIRECTION/LECTURE-INSTRUMENTEE` part à l'atelier.
- Les distributions GitHub et Local restent, pour le développement.
- Le README dit quelle archive installer.

### B. Moins de tours et un contexte plus léger, avec les mêmes contrôles

Chaque mesure garde les contrôles existants ; seule la façon de les servir change.

**B1 — Des images qui coûtent moins.**
- Pendant la boucle, `parcours.py captures --version` produit **une seule planche** : premier écran au bureau et en mobile, côte à côte, en 1×. Elle remplace les captures séparées.
- Le ×2 sert seulement au zoom sur un détail, et à la livraison.
- `verifier` désigne **une** image à regarder d'abord (la lecture sans texte) et liste les autres sans les imposer.
- **Cible** : diviser par deux les images lues (de 13–29 à 6–12).

**B2 — `verifier` ne répète pas ce qui n'a pas changé.**
- Dès le deuxième appel sur une même page, il affiche seulement ce qui a changé : défauts et signaux apparus ou disparus. La fiche complète reste dans `parcours.md`.
- **Cible** : diviser par deux à quatre le texte de `verifier` dans le contexte.

**B3 — Le chantier en une commande.**
- `parcours.py chantier "brief court" --poles a,b` fait en **un seul appel** ce que les runs font en 10 à 20 tours au démarrage :
  - dossiers de travail ;
  - `tirage` ;
  - `leviers` ;
  - le gabarit de la trace légère ;
  - la commande de `references` à compléter.
- Il n'écrit aucune décision. Il prépare le terrain et renvoie une sortie courte.

**B4 — Le tronc DIRECTION lu sous une forme utile.**
- `read_route --tronc DIRECTION` produit déjà le fichier, et l'agent le lit en entier (35 k caractères).
- Proposition : le tronc s'ouvre par un **sommaire d'une page**. Pour chaque route : quand la lire, et la ligne-clé. Le corps reste dans le fichier, lu à la demande.
- C'est une mesure, pas une réécriture du savoir.

**B5 — Trois consignes de travail au noyau, à coût nul.**
- Grouper les commandes dans un même appel.
- Écrire le HTML une fois, puis le corriger par retouches, sans le réécrire.
- Lancer `verifier` seulement après un changement qui peut modifier un défaut.
- Environ 200 octets ; il en reste 190, donc il faut retirer une redite. Elle est à trouver au moment de l'intégration.

### C. Plus tard : l'architecture « outils d'abord » (cartographie, section 3)

Un noyau court, les outils comme interface principale, et une bibliothèque lue par les outils. C'est un lot à part, et c'est le plus gros gain potentiel. **Il ne se décide qu'après la mesure de B.**

## 2. Comment on saura que la qualité n'a pas baissé

- **Mesure du coût** : le même script de dépouillement, gardé dans le suivi et hors du paquet, sur chaque run. Indicateurs : tours, contexte maximal, lecture de cache cumulée, sortie, images, durée.
- **Mesure de la qualité** : un PILOT comme le 9b. Deux objets ; pour chacun, deux agents neufs, l'un en `o` et l'autre avec le lot 10. Junior juge **à l'aveugle, par paires**.
- **Règle de décision proposée** :
  - on garde B si Junior ne préfère pas `o` sur la majorité des objets, **et** si le coût baisse d'au moins 30 % ;
  - si la qualité baisse sur un objet, on regarde quelle mesure en est la cause avant de conclure.
- **Les runs ne partent qu'avec l'accord de Junior.**

## 3. Ordre proposé

1. Décision de Junior sur A1 (dont la question de la veille), A2 et B1 à B5.
2. Intégration de A et B sur une branche, tests avec mutation rouge, préparation complète, puis révision `R2026-11-15p`.
3. PILOT de mesure, coût et qualité, quand Junior le décide.
4. Selon le résultat, le lot C.

## Sources

- Chroma, *Context Rot: How Increasing Input Tokens Impacts LLM Performance* (2025) : https://www.trychroma.com/research/context-rot
- Anthropic, tarifs et prompt caching (multiplicateurs de lecture et d'écriture du cache) : https://platform.claude.com/docs/en/about-claude/pricing et https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching

> **Remplacé** par `Plan_de_travail_publication.md` (21 novembre). Gardé pour mémoire.

# Feuille de route — un système de niveau publication

Rédigé le 21 novembre 2026. Base : `R2026-11-15o`.

**Demande de Junior.** Un système très bon à l'intérieur comme à l'extérieur : navigation, utilisation, compréhension, présentation. Rien d'inutile ni d'obsolète. Utilisable par le public, des personnes ou des experts, au niveau de ce que publient Anthropic, Google ou Artificial Analysis. **Les runs à la fin**, parce qu'ils coûtent cher.

Règle 1 : chaque lot passe par propositions puis décision.

**Règle 10, rappelée** : une route qu'aucun run n'a ouverte n'est pas « en trop ». On retire l'**obsolète** (mesure périmée, veille échue, redite, matériau de test), pas le non-lu.

## 1. Les critères (ce que « niveau publication » veut dire ici)

| Axe | Critère vérifiable | État en `o` |
|---|---|---|
| **Navigation** | Une entrée d'une page. La documentation est rangée en quatre types, selon le cadre Diátaxis : tutoriel, guides pratiques, référence, explication. Toute page est à deux clics au plus de l'entrée. | Guides par niveau ; pas de tutoriel guidé ; la référence est mêlée aux règles |
| **Utilisation** | Installation en une commande, dépendances comprises. Une archive « skill » sans l'atelier. Des messages d'erreur qui disent quoi faire. Un mode dégradé sans navigateur. | Dépendances à la main ; 55 fichiers d'atelier livrés |
| **Compréhension** | Les textes pour les personnes parlent en mots ; les codes vivent dans la référence. Un schéma public. Un glossaire tiré des sources. | 62 codes dans le noyau ; glossaire écrit à la main |
| **Présentation** | Licence ; journal des changements ; versions datées juste ; page de méthode ; page « Fondements et sources » ; positionnement en une phrase ; langue décidée. | Pas de licence ; date de révision figée au 15 novembre |
| **Propreté** | Aucun matériau de test ni mesure périmée dans la skill. Une garde l'empêche à l'avenir. | 4 fuites ; une phrase de coût obsolète |
| **Qualité interne** | Une architecture lisible (noyau court, une commande par étape). Un guide de contribution. Un code homogène. Des tests avec mutation rouge (déjà en place). | Noyau à 49 % de procédure ; contrôle plus lourd que la production |
| **Preuve** | Coût par run mesuré correctement (tours × contexte). Comparaison avec et sans système à l'aveugle. Résultats publiés avec leurs limites. | Aucune comparaison pour la version actuelle ; coût mal annoncé jusqu'ici |

## 2. Les lots, dans l'ordre (aucun run avant le dernier)

| Lot | Contenu | Pourquoi à ce rang |
|---|---|---|
| **10A — Propreté** | Fuites du journal de Junior, phrase de coût obsolète, garde contre les noms de runs ; distribution « skill » sans l'atelier ; journal de mobilisation optionnel ; date de révision juste | On ne construit pas sur du matériau à retirer |
| **10B — Outils plus sobres** | Planches à 1× pendant la boucle ; `verifier` qui n'affiche que les changements ; `chantier` en un appel ; sommaire du tronc ; trois consignes de travail au noyau | Premier pas vers l'architecture, et gain de coût mesurable ensuite |
| **11 — Outils d'abord** | Une commande par étape (`diverger`, `declarer`, `atelier`, `livrer`) ; la procédure sort du noyau à mesure ; noyau ramené vers environ 5 000 tokens ; gouvernance en module optionnel ; mode dégradé en texte | La documentation doit décrire l'architecture finale, pas l'actuelle |
| **12 — Documentation de publication** | README d'une page ; tutoriel « premier rendu en 10 minutes » ; guides pratiques ; référence générée (commandes, routes, codes, statuts) ; explication (fondements et sources, méthode) ; schéma public ; journal des changements ; licence ; fichier de citation ; guide de contribution ; langue | Elle se rédige une fois l'architecture stable |
| **13 — Évaluation finale (runs)** | Le même protocole que le PILOT 9b, sur 3 ou 4 objets : **sans système**, **`o`** et **final**, jugés à l'aveugle par Junior ; coût mesuré par le script ; résultats publiés avec leurs limites | Les runs coûtent cher : un seul passage, à la fin, qui mesure tout |

**Garde-fou sans run entre deux lots.** Les tests, la préparation complète et le script de coût sur un **run rejoué** ne lancent aucun agent. À défaut, on se contente d'une estimation du contexte lu, et chaque rapport dit ce qui n'a pas été mesuré.

## 3. Décisions qui reviennent à Junior

1. **La licence** : par exemple MIT pour le code et CC BY 4.0 pour les textes, ou une autre.
2. **La langue** : français seul, français et anglais, ou anglais avec un français tenu à jour. Les publications citées comme modèles sont en anglais.
3. **Le nom** : « Design Governance » peut évoquer la gouvernance d'un design system plutôt que la direction artistique.
4. **La ligne de veille « Convergences relevées avec le système »**, qui vient de ses essais : la garder en précisant son origine, ou la sortir vers le suivi.
5. **Les juges de l'évaluation finale** : Junior seul (règle 7), ou avec deux ou trois designers en plus, à l'aveugle.
6. **La visibilité de DG-777** : si le dépôt est public, son journal l'est aussi.

## 4. Ce qui sera retiré comme obsolète (inventaire à finir au lot 10A)

Il ne sera retiré qu'après vérification dans les fichiers :
- la mesure du 29 octobre (déjà corrigée dans le suivi ; reste dans `versions.md`) ;
- les citations de runs et les titres de briefs ;
- les veilles dont l'échéance est passée au moment de la livraison ;
- les redites relevées par la cartographie : les quatre « ordres » ;
- les archives et bundles des révisions intermédiaires (`l` à `n`) dans DG-777, une fois la version finale livrée.

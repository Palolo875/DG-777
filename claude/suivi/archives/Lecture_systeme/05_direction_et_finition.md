# Lecture du système, étape 5 : design/direction/README.md et design/produit/finition.md (19 novembre 2026)

Les deux fichiers sont lus en entier (13 et 52 lignes).

## direction/README.md
C'est un sommaire de cinq fichiers : `cadrer.md`, `diriger.md`, `premier-objet.md`, `boucle.md` et `standard.md`. Il ne contient aucune règle.

## produit/finition.md
- **`ACTION/GATE-C`, le contrôle du « craft » sur le rendu réel :** six critères, de C1 à C6 (stratégie de surface, typographie choisie, composition intentionnelle, densité optique, profondeur, résolution située). Pour chacun : ce qui le rend présent, ce qui déclenche un retour, et le geste à faire s'il manque. C2 demande déjà de « fixer deux ou trois rôles et une échelle contrastée ».
- **Mais Gate C n'écrit un verdict qu'en trace complète.** En trace légère, le mode par défaut de tous nos runs, *« un critère absent déclenche son geste… aucun verdict n'est écrit »*. **Aucune trace des runs 9 à 16 ne mentionne Gate C ni ses critères** (vérifié par une recherche dans les traces). Le meilleur outil de jugement du craft ne laisse donc aucune trace dans les runs réels.
- **C1 fait revenir le travail quand un aplat est « gardé sans essai de matière ».** C'est probablement ce qui pousse les agents à essayer du grain, qu'ils retirent ensuite (runs 10, 12 et 16). Le résultat est juste, mais il coûte des allers-retours.
- **`ACTION/ATELIER-EDITION` :** c'est le texte du noyau, déjà lu à l'étape précédente. Une seule bonne garde existe contre le comparatif truqué, et elle ne vise que la typographie : *« la variante essaie une autre voix qui a du caractère, pas une voix neutre facile à battre »*. Rien d'équivalent ne protège la modale esquissée sur la planche.
- **Le regard séparé, « si l'environnement permet un second agent » :** il n'a jamais été fait. Les traces disent « pas de second agent » et « non fait ». Le script `parcours.py critique` (ligne 1612) interdit d'ailleurs au critique de « lancer un sous-agent ». Dans nos runs, la seule vérification extérieure prévue n'a donc jamais eu lieu.

## Recherche faite à côté : un modèle peut-il corriger son propre travail ?
- Huang et al., *LLMs Cannot Self-Correct Reasoning Yet* (https://arxiv.org/abs/2310.01798, ICLR 2024) : sans retour extérieur, la performance **baisse** après autocorrection. Le modèle change plus souvent une bonne réponse en mauvaise que l'inverse, parce qu'il « ne juge pas correctement » sa propre sortie.
- Kamoi et al., revue critique publiée dans TACL en 2024 (https://aclanthology.org/2024.tacl-1.78/) : aucune étude ne montre une autocorrection réussie avec le retour d'un modèle qu'on interroge, sauf pour des tâches qui s'y prêtent exceptionnellement. **L'autocorrection marche quand un retour extérieur fiable existe.**
- CRITIC (https://arxiv.org/pdf/2305.11738) : l'autovérification est « remarquablement peu fiable » sans outil extérieur.
- *The Mirror Loop* (https://arxiv.org/abs/2510.21861, 2025) : une autocritique répétée sans contact extérieur tend à reformuler plutôt qu'à progresser. Une seule étape de vérification extérieure relance le changement.
- **Limite :** toutes ces études portent sur le raisonnement et le texte. Aucune ne porte sur la critique de son propre design visuel.

## Ce que ça explique dans nos runs (probable)
- **Les fautes objectives sont bien corrigées,** parce qu'elles ont un retour extérieur fiable : `check_render` et `verifier` mesurent le débordement, le contraste, le focus.
- **Le goût ne progresse pas après la première planche,** parce qu'il n'a **aucun retour extérieur fiable**. L'atelier, le test de retrait et la lecture sans le texte sont des autocritiques de l'agent, et le regard séparé n'a jamais eu lieu.
- **C'est le mécanisme le plus solide trouvé jusqu'ici** pour expliquer le constat central : des rendus propres mais génériques.

## Ce que ça oriente (à discuter, pas à intégrer)
Pour améliorer le goût, il faut **un retour extérieur fiable sur le goût**. Plus d'étapes d'autocritique n'y suffiront pas. Par ordre de fiabilité :
1. **Le jugement de Junior,** en paires à l'aveugle, et ses verdicts conservés comme exemples (le carnet de goût).
2. **La comparaison chiffrée avec des références réelles** de son top 20 : rapport d'échelle, nombre d'encres, densité. Ce sont des mesures, donc un retour extérieur, même partiel.
3. **La modale observée** (des captures réelles du genre) plutôt que la modale esquissée par l'agent.
4. **Un critique modèle sur images seules,** seulement pour écarter les écarts nets (environ 59 % d'accord avec les humains sur des paires proches, d'après l'étape 4).

## Suite proposée
Lire `design/direction/boucle.md` (créer puis apprendre), puis `design/savoir/qualite-creative.md` (le jugement créatif et les CFT).

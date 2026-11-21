# Lecture du système, étape 9 : savoir/gout-et-tendances.md, « Goût, références et tendances », CONVERGENCE et MOYENS (19 novembre 2026)

Lu : des lignes 37 à 102. Vérifié dans `scripts/regard.py` : les lignes 579 à 590 (la table des marqueurs mesurés).

## Ce qu'il dit
- « Le goût n'est pas un canon de marques… Observe une référence pour extraire une **relation**, non une surface à copier. »
- **La liste datée des marqueurs** ([VEILLE 2026-10], « à revoir avant 2027-01 ») : vague 1 (violet, Inter…), vague 2 (crème, serif de caractère…), vague 3 (dithering, hachures de plan, libellés mono…).
- **Une ligne « Convergences relevées avec le système » existe déjà.** Elle cite :
  - « une donnée calculée devenue l'image principale » ;
  - la grotesque condensée en titre ;
  - la didone sur fond crème pour « haut de gamme » ;
  - la fiche de données en petit tableau à filets ;
  - « d'un run à l'autre sur un même brief, même objet central et même grotesque de titre ».
- **La carte des moyens contient une liste de « Références à observer » :** Siteinspire, Godly, Fonts In Use, Letterform Archive. Elle précise : « une image sans auteur ni source (tableau d'épingles, flux de réseau social) n'est pas une référence ».

## Corrections de mes affirmations d'avant
1. J'avais dit que la liste « suit les modes du marché, pas les réflexes propres au système ». **C'est faux :** une ligne de convergences propres au système existe. Elle nomme déjà « une donnée calculée devenue l'image principale », qui est proche du diagramme. Elle ne nomme pas le **plan, la coupe ou le schéma pris comme objet principal sur un sujet sans mécanisme**, qui est le cas des runs 10, 14 et 16.
2. J'avais présenté une « liste de sources de calibration » comme une idée neuve. **Elle existe** (Siteinspire, Godly, Fonts In Use, Letterform Archive). Elle n'est pas rangée par type d'objet, et les agents ne la suivent qu'en partie : le run 16 a pris Fonts In Use, mais le run 10 a pris des sites de festivals locaux.

## Vérifié dans regard.py
- Le script mesure **12 marqueurs**, tous des vagues du marché : violet, Inter, halo, cartes, crème, brun, serif de titre, rouille, bandeau, ASCII, bleu Klein, mono en capitales.
- **Aucune convergence propre au système n'est mesurée.** La donnée devenue image, l'objet central répété et la didone sont rangés parmi les « non mesurés, à regarder ». Leur repérage repose donc sur l'œil de l'agent, c'est-à-dire sur l'autocritique (voir l'étape 5).

## Un point sur ta collection (le top 20)
La règle « une image sans auteur ni source (flux de réseau social) n'est pas une référence » s'applique à une partie de ton corpus, qui vient de carrousels et de flux. Cela rejoint la colonne « Source » de la grille v2 : une pièce sans source vérifiée peut servir d'exemple de goût, pas de référence au sens du système.

## Recherche faite à côté : les modèles convergent-ils d'un run à l'autre ?
- Doshi et Hauser, *Science Advances* (2024, https://www.science.org/doi/10.1126/sciadv.adn5290) : les idées de l'IA rendent chaque histoire plus créative, mais **les histoires se ressemblent davantage entre elles**. C'est un gain individuel et une perte collective.
- *The Hidden Cost of AI-Assisted Creativity* (Doshi, Boussioux et al., https://discovery.ucl.ac.uk/id/eprint/10232647/) : **une IA qui génère les idées réduit la diversité ; une IA qui aide seulement à choisir la préserve.**
- Wenger et Kenett (2025, https://arxiv.org/abs/2501.19361) : les réponses de modèles différents se ressemblent bien plus entre elles que celles des humains, et **demander au modèle d'être plus créatif n'augmente que légèrement la variété**.
- Jiang et al. (2025, « Artificial Hivemind », cité par la recherche, non relu) : les modèles s'effondrent sur un espace de sorties étroit.
- **Limite :** ces études portent sur le texte. Aucune ne porte sur le design visuel.

## Ce que ça change (à discuter)
1. **La convergence d'un run à l'autre est une propriété des modèles, pas un défaut d'un run.** Une consigne de type « sois original » n'y suffit pas (Wenger et Kenett). Le système a déjà deux bonnes réponses : le **tirage au sort** (`parcours.py tirage`) et la ligne des **convergences propres au système**. Ce qui manque :
   - **mesurer** ces convergences, au lieu de les laisser à l'œil de l'agent ;
   - **tenir la ligne à jour avec les runs**, en y ajoutant par exemple « plan, coupe ou schéma vu de dessus comme objet principal sur un sujet sans mécanisme ».
2. **Une piste qui s'inverse :** puisque l'IA qui choisit préserve la diversité mieux que l'IA qui génère, l'apport extérieur le plus utile au départ est **humain ou réel** (ton brief, tes références, tes images, le tirage). L'agent sert alors à construire et à choisir, plutôt qu'à inventer seul la direction. C'est cohérent avec l'étape 5 : il faut un retour extérieur.
3. **Une piste mesurable :** l'empreinte d'un run (teinte dominante, paire de polices, objet principal) existe déjà dans `regard.py --antecedent`. Si on la consignait pour chaque run dans un registre commun, on mesurerait la convergence de la **série**, pas seulement d'un projet. Cela comblerait la limite de REUSE (étape 8).

## Suite proposée
Lire `DIRECTION/CREATIVE-BOOT` et `DIRECTION/DIVERGENCE` dans `design/direction/diriger.md` (le boot, les cinq directions et la planche), pour finir le tour de la séquence `DIRECTION` dans les sources.

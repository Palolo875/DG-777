# Lecture du système, étape 6 : direction/boucle.md et savoir/qualite-creative.md (19 novembre 2026)

Lu : `boucle.md` en entier (82 lignes) et `qualite-creative.md` des lignes 1 à 139 (CFT-00 et CFT-01). La suite (CFT-02 à CFT-06) n'est pas encore lue.

## direction/boucle.md
- **Le premier rendu doit déjà être « beau, composé, crédible, spécifique et suffisamment résolu »** (ligne 11). C'est l'exigence, mais le texte ne donne aucun moyen extérieur de vérifier « beau ».
- **Un run peut s'arrêter tôt** (ligne 19) « si la qualité initiale attendue est atteinte ». C'est l'agent qui en juge seul.
- **La réouverture de la direction existe** (table du diagnostic, ligne 37, et signaux de réouverture, lignes 49 à 58) : « direction faible, interchangeable ou contradictoire → rouvrir la direction » ; « la signature devient générique ». **Aucun run n'a jamais rouvert sa direction.** Une recherche dans les traces ne trouve que le nom d'une esquisse (« On rouvre », run 12). C'est cohérent avec l'étape 5 : le signal est laissé à l'appréciation de l'agent.
- **« Observe à taille réelle et au zoom, pas seulement en vignette »** est inscrit au noyau, mais le choix de direction se fait sur une planche en vignettes.
- **Les signaux d'apprentissage** (ligne 82) servent à « améliorer V1 au niveau de la série de runs ». Rien ne transmet pourtant ce qu'un run a appris au run suivant, sauf une nouvelle révision du paquet.

## savoir/qualite-creative.md (CFT-00 et CFT-01)
- **CFT-00, la qualité créative :** huit dimensions (présence, point de vue, culture visuelle, spécificité, composition, désirabilité, résolution, retenue), avec une question de critique pour chacune. C'est une bonne grille de lecture. Elle est explicitement « ni un score, ni un verdict », et seule la **revue sur capture en quatre questions** sert en trace légère.
- **CFT-01, la phrase d'idée :** « Sur cette page, [un élément de l'inventaire] devient [le dispositif que la composition appelle]. Le dispositif est une scène, un geste ou un objet de preuve, non un effet. » L'inventaire comprend « les nombres du brief (places…) », « son lieu », « les objets imprimés de son monde ». S'y ajoute **« Une chose vivante »** : « choisir un bois et voir la chaise ; régler un prêt et lire la mensualité ».
- **Hypothèse sur l'origine du diagramme et des gadgets** (probable, non prouvée, car les traces légères ne gardent pas la phrase d'idée) : la chaîne du noyau « promesse → objet de preuve → geste », ajoutée à cette phrase d'idée qui change le lieu ou les nombres du sujet en « dispositif », et à l'injonction d'« une chose vivante », pousse vers un plan ou une coupe interactifs. C'est exactement ce que montrent les runs 9 (plan de l'appartement), 10 (plan du verger), 14 (coupe cotée avec composition du service) et 16 (plan de la salle avec le siège allumé).
- **Le système limite les variantes** (ligne 138) : « Ne crée ni quota de variantes ni obligation de nouveauté. Une variation est recevable seulement si une différence de tâche, donnée, contexte, preuve ou registre la rend nécessaire. » **Cela contredit ma piste « varier beaucoup ».**

## Recherche faite à côté
- **Le prototypage en parallèle.** Dow et al., *Parallel prototyping leads to better design results* (ACM TOCHI, 2010, https://dl.acm.org/doi/10.1145/1879831.1879836) : à nombre de prototypes, retours et temps égaux, produire plusieurs prototypes **en parallèle** avant le retour donne de meilleures publicités, que ce soit au taux de clic ou selon l'avis d'experts (24,4 contre 21,7), plus de divergence entre les idées et plus de confiance chez les designers. Le travail en série fixe la personne sur une seule option.
- **La fixation sur les exemples.**
  - Jansson et Smith, *Design fixation* (1991, https://cecas.clemson.edu/cedar/wp-content/uploads/2016/07/9-JanssonAndSmith1991.pdf) : un exemple montré avec le problème est copié, **même ses défauts**.
  - Wadinambiarachchi et al. (CHI 2024, https://arxiv.org/html/2403.11164) : les images générées par IA, **et dans une moindre mesure la recherche d'images**, augmentent la fixation sur l'exemple et diminuent la variété et l'originalité.
  - Les mesures qui atténuent la fixation (des consignes de « défixation », des heuristiques de design) ne sont soutenues que par des preuves indirectes.

## Ce que ça change (à discuter)
1. **Le refus des exemples d'apparence par le système est justifié par la recherche sur la fixation.** Ma piste des « triptyques » et même les références de calibration comportent ce risque. Il faudrait les montrer **après** la première divergence, et non avant, ou les accompagner d'une consigne explicite de défixation. Hypothèse à tester, pas à affirmer.
2. **« Varier beaucoup » est soutenu, mais dans une forme précise :** des variantes **en parallèle, avant tout retour**, puis un choix. Le système fait déjà trois esquisses en parallèle. Il limite ensuite les variantes à celles qui sont « nécessaires ». La recherche donne plutôt raison au parallèle qu'au volume en soi.
3. **La source probable du diagramme et des gadgets se trouve au cœur de la méthode** (la phrase d'idée, l'objet de preuve, la chose vivante), pas dans une règle accessoire. C'est la piste la plus importante, et la plus délicate, puisque ces règles produisent aussi les meilleures idées des runs. Exemple : le plan du run 9, qui convenait à son brief.
4. **Même la recherche d'images pour observer la modale** peut fixer l'agent sur ce qu'il voit. Il faut la présenter comme une contre-référence explicite, et c'est à tester.

## Suite proposée
Lire `qualite-creative.md` de la ligne 140 à la fin (CFT-02 à CFT-06), puis `design/direction/premier-objet.md` pour vérifier l'hypothèse sur l'objet de preuve.

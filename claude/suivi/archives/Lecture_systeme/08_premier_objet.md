# Lecture du système, étape 8 : design/direction/premier-objet.md (19 novembre 2026)

Le fichier est lu en entier (77 lignes).

## Le constat central, vérifié par les balises du fichier
- **La ligne qui pousse vers l'objet de preuve est dans le noyau.** Le bloc `<!-- noyau:début PREMIER-OBJET -->` (ligne 11) dit : « convertis le brief vague avec la chaîne **promesse → objet de preuve → geste**. L'objet passe avant les listes de bénéfices et **rend le mécanisme plus clair** que le texte seul. »
- **La ligne qui l'équilibre n'y est pas.** Elle est dans un bloc `<!-- différé:début PREMIER-OBJET-SUITE -->` (ligne 14) : « Au premier regard, **l'objet ou le geste peut ouvrir, selon le contexte (CFT-04a)**. » Elle n'est donc pas lue à chaque run.
- **Cette même ligne différée renforce d'ailleurs la poussée :** l'objet est « de préférence **codé** (composant, donnée, état ou interaction du produit) ». Pour un sujet sans image, « codé » mène tout droit au plan, à la coupe ou au schéma.
- **Le mot « mécanisme » revient deux fois** : à la ligne 11, puis dans la ligne « Intégration » du contrat. Il convient à un produit qui *fonctionne* (une application, un calculateur). Un festival, une céramique ou un billet n'ont pas de « mécanisme » à rendre clair. Le noyau leur en fait chercher un, et l'agent l'invente sous forme de diagramme.

## Ce que confirment les runs
- Run 9 (une application de partage de charges) : il y a un vrai mécanisme, le plan de l'appartement est juste. **C'est le cas pour lequel la règle est faite.**
- Runs 10 (festival), 14 (céramique) et 16 (billet) : il n'y a pas de mécanisme, et pourtant un plan ou une coupe a été choisi comme « objet de preuve ». **Ce sont les cas où la règle déborde.**

## Le reste du fichier
- **`DIRECTION/GROUNDING` :** rendre contestable un refus de vérifier un fait. Sans lien avec le goût.
- **`DIRECTION/REUSE` :** compare un run à ses **antécédents** sur six champs, dont l'objet de preuve et la thèse. C'est exactement l'outil qui pourrait attraper le réflexe du diagramme d'un run à l'autre. **Mais il ne se déclenche que s'il existe un run précédent du même projet.** Un agent neuf dans un dossier vide n'en a jamais, et un vrai utilisateur qui change de projet non plus. C'est la même limite que celle de la ligne 128 d'`evolution.md` (« pas d'un run à l'autre »).

## Recherche faite à côté : l'image qui informe ou l'image qui décore
- NN/g, *Photos as Web Content* (oculométrie, https://www.nngroup.com/articles/photos-as-web-content/, revu en août 2026) : les utilisateurs **examinent les images qui portent une information utile** (produits, vraies personnes) et **ignorent les grandes images décoratives** et les photos de banque d'images.
- NN/g, *Using Imagery in Visual Design* (2023, https://www.nngroup.com/articles/imagery-in-visual-design/) : il faut privilégier les images qui informent ; les images décoratives peuvent porter le ton, sans écraser les premières.
- **Ce que ça dit :** la doctrine de l'objet de preuve est **fondée** (une image qui informe vaut mieux qu'un décor). Mais pour un événement ou un objet artisanal, ce qui informe, c'est **le lieu, l'ambiance, les gens, la pièce elle-même**, pas un mécanisme. Le noyau traduit « qui informe » par « mécanisme » et « codé ». C'est vrai pour un produit numérique, et trop étroit ailleurs.

## Ce que ça précise (à discuter)
1. **La cause du diagramme est maintenant localisée avec précision :** le bloc `PREMIER-OBJET` du noyau, son vocabulaire du « mécanisme », et l'absence au noyau de son contrepoids (CFT-04a). C'est vérifié dans les fichiers. Le lien de cause à effet avec les rendus reste une hypothèse, à tester.
2. **Une correction minimale testable :** faire monter dans le noyau la phrase déjà écrite « l'objet ou le geste peut ouvrir, selon le contexte », et remplacer « mécanisme » par une formule qui couvre aussi le lieu, la pièce et l'ambiance (par exemple « rend la promesse plus tangible que le texte seul »). On la teste en `PILOT` sur deux briefs sans mécanisme (le festival, le billet), avec et sans le changement, à l'aveugle.
3. **REUSE ne peut pas servir de garde entre runs dans l'usage réel.** Le seul moyen d'attraper les réflexes propres au système est de les **nommer** dans la liste des marqueurs, à partir de ce que les runs ont produit. C'est la piste « nommer le diagramme parmi les marqueurs ».

## Suite proposée
Lire `SAVOIR/TOOLS/CONVERGENCE` en entier (`design/savoir/gout-et-tendances.md`, section des marqueurs), pour voir comment la liste des marqueurs est tenue et datée, et où y ajouter les réflexes du système.

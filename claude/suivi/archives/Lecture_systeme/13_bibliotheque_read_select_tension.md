# 13 — BIBLIOTHEQUE/READ, /SELECT, /TENSION

Lecture du 19 novembre 2026, avec `read_route.py`. Tailles :
- READ : 11,8 k caractères ;
- SELECT : 12,9 k ;
- TENSION : 1,9 k.

## 1. Ce que les runs en ont fait (journaux des runs 9 à 16, routes lues comparées aux routes proposées)

| Route | Lue | Proposée par un outil |
|---|---|---|
| BIBLIOTHEQUE/SEQUENCE | 6 runs (9, 10, 12, 14, 15, 16) | 1 |
| BIBLIOTHEQUE/MICRO | 2 runs (11, 13) | 2 |
| BIBLIOTHEQUE/SELECT | 1 run (13) | 1 |
| BIBLIOTHEQUE/READ | 0 | 1 |
| BIBLIOTHEQUE/TENSION | 0 | 0 |

Les agents lisent ce qui ordonne une page en sections (SEQUENCE). Ils ne lisent jamais ce qui traduit un caractère en leviers (READ).

## 2. READ : la découverte principale

READ contient une table **« Traduire un caractère en leviers »**. C'est, de tout ce que j'ai lu jusqu'ici, le savoir esthétique **le plus concret** du paquet. Elle donne douze caractères :
- calme, tension ;
- intimité, monumentalité ;
- précision, spontanéité ;
- continuité, rupture ;
- collection, instrument ;
- retenue, intensité.

Chacun a des leviers de départ chiffrés et un **piège réflexe** :

- **Calme** : écart titre/texte d'environ ×2 à ×2,5, un seul foyer. Piège : « page grise sans foyer ».
- **Tension** : écart de ×4 ou plus, masse décentrée, une rupture de grille contrôlée. Piège : « tout décalé, désordre sans axe ».
- **Monumentalité** : un élément sur environ la moitié de la largeur. Piège : « titre géant sur fond sombre et dégradé ».
- **Retenue** : une ou deux teintes et des neutres teintés. Piège : « neutre interchangeable propre et moderne ».
- **Intensité** : couleur saturée **en surface étendue, pas seulement en accent**. Piège : « néon d'une vague datée ».

La méthode est saine : un pôle par paire utile, deux paires au plus, deux ou trois leviers, puis un jugement sur capture. Le texte dit lui-même « points de départ, non des mesures ».

Ces pièges correspondent exactement à ce que Junior a reproché aux rendus : « générique, cheap » pour le neutre interchangeable, « gadget » pour les signes techniques posés en décor.

READ contient aussi :
- **le caractère perceptuel** à nommer quand une décision esthétique est active ;
- **la thèse structurelle** et le « premier objet habitable » ;
- **les types de preuve** : PERCEPTUAL, EXPERT, TECHNICAL, USER/TASK.

## 3. SELECT et TENSION

- **SELECT** :
  - un filtre avant le catalogue : quelle décision, quel niveau minimal, quel premier objet, quelle preuve de sortie ;
  - une table « relation recherchée → route → premier levier → observation » ;
  - une sélection par mode ;
  - un garde-fou de dérivation ;
  - des **signaux de convergence structurelle**, dont « grain, trame d'impression ou texture repris d'un brief à l'autre ». C'est une convergence propre au système, déjà nommée.
  - En revanche, **le diagramme comme objet principal n'y figure pas** (constat A-3) : la piste « nommer le diagramme » s'insérerait ici.
- **TENSION** : sept axes (densité, foyer, position de la preuve, temporalité, matière du champ, navigation, action). En trace légère, « l'axe retenu se lit dans l'artefact », ce qui ne demande rien d'écrit. La route est courte et abstraite, avec moins de prise que la table de READ.

## 4. Recherches à côté (Exa et WebSearch)

| Source | Ce qu'elle dit | Ce que ça touche |
|---|---|---|
| Tuch et al. 2012, *IJHCS* 70(11) | 119 sites d'entreprises jugés par des non-designers en 17 à 1 000 ms. **Une faible complexité visuelle et une forte prototypicalité** (le site ressemble à ce qu'on attend de sa catégorie) donnent la meilleure beauté perçue. L'effet de prototypicalité est fort (d ≈ 1,8 à 2,0 à complexité basse ou moyenne). | **Contrepoids important.** Au premier regard d'un public, l'écart au modal peut coûter. Cela soutient ce que dit déjà SINGULARITE (« la convergence de genre est légitime ») et le pôle « calme ». Limites : des non-designers, des sites d'entreprise, une vue passive. |
| Lavie & Tractinsky 2004, *IJHCS* 60(3) | La beauté perçue d'un site a deux dimensions distinctes : **classique** (ordre, clarté, proche de l'utilisabilité) et **expressive** (créativité, originalité, rupture des conventions). | Les deux ne s'opposent pas : on peut les viser ensemble. Hypothèse : garder une structure prototypique et porter l'écart sur la matière, le type et la couleur. Je n'ai lu que des résumés (la page de l'échelle d'Aalto). |
| Ratios d'échelle typographique | Je n'ai trouvé **aucune étude contrôlée**, seulement des règles de praticiens (titre deux à trois fois le texte, ratios modulaires). | Les chiffres ×2,5 et ×4 de READ sont des conventions de métier, pas des mesures. Le texte le dit déjà (« non des mesures »). |

## 5. Constats

**Certain**
- La table caractère → leviers de READ existe, elle est concrète, et aucun run ne l'a lue.
- Le diagramme comme objet principal n'est pas parmi les signaux de convergence de SELECT.

**Probable**
- C'est le levier le plus direct contre le « générique » et le « cheap ». Il donne au modèle des relations de forme (échelle, surface de couleur, masse) plutôt que des adjectifs. Cela va dans le sens de PRISM (note 12) : le style textuel abstrait ne suffit pas.

**À vérifier**
- La recherche (Tuch) dit qu'au premier regard, le prototypique et le peu complexe plaisent le plus au grand public. Le système pousse vers la singularité et l'écart au modal. Pour un objet d'identité jugé par un designer exigeant (Junior), c'est la dimension expressive qui compte. Pour un public, c'est la dimension classique. Le système ne dit pas laquelle prime selon le cas, ou le dit dans FRAME, une route jamais lue.

## 6. Pistes (non intégrées, règle 1)

1. **Servir la table de READ au bon moment, pas toute la route.** Une fois le registre déclaré, la fiche `verifier` (ou une option de `parcours.py`) servirait les deux lignes des pôles choisis, avec leurs pièges réflexes. Coût : 300 à 500 caractères au lieu de 11,8 k. C'est le même principe que le registre consultable de la note 12.
2. **Ajouter le diagramme aux signaux de convergence** de SELECT, à côté du grain repris. Formulation à discuter.
3. **Écrire la tension classique / expressive en une phrase.** Garder la structure lisible et prototypique, porter l'écart sur une ou deux dimensions expressives. C'est conforme à SINGULARITE et à la recherche, mais c'est une décision de doctrine, à discuter.
4. **Ne rien faire de TENSION pour l'instant.** C'est la route la moins utile des trois en trace légère.

## Sources
- Tuch et al. 2012 (PDF) : https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38315.pdf
- Tuch et al. 2012 (DOI) : https://doi.org/10.1016/j.ijhcs.2012.06.003
- Lavie & Tractinsky 2004, échelle : https://experience.aalto.fi/aesthetics-scale/
- Tractinsky, recherche sur l'esthétique : https://www.ise.bgu.ac.il/faculty/noam/research/aesthetics.html
- Ratios typographiques (praticiens) : https://blakecrosley.com/en/blog/typography-systems et https://design.tutsplus.com/articles/understanding-typographic-hierarchy--webdesign-11636

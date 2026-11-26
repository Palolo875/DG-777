# Lecture du système, étape 10 : design/direction/diriger.md (19 novembre 2026)

Lu : les lignes 113 à 249 (ASSET-ROUTE, ANCHOR-RESERVE, DIRECTION-ATELIER, DIVERGENCE, déclaration). Les lignes 1 à 112 (CREATIVE-BOOT, VISUAL_TARGET) avaient été lues dans le tronc au run 15.

## Ce que dit le fichier, et ce qui corrige mes affirmations d'avant
1. **La règle contre la modale esquissée pour perdre existe déjà :** « la modale, esquissée **au même niveau que les trois autres** » (ligne 210, au noyau). Les runs 10 et 12 l'ont enfreinte (étape de vérification sur la modale). **Le problème n'est donc pas l'absence de la règle, mais qu'elle repose sur l'autocontrôle de l'agent.**
2. **Une garde contre la donnée devenue image existe aussi au noyau :** « Une donnée calculée devenue image est une piste parmi d'autres, pas le défaut » (ligne 209). Mais les pistes proposées juste au-dessus (« **son lieu** », « **sa forme**… devenue la structure ») sont précisément celles que les agents ont rendues en plan ou en coupe. La garde vise la donnée, pas le dessin technique du lieu ou de la forme.
3. **Correction importante : les cinq directions avec leurs probabilités ne sont pas une décoration.** J'avais écrit que ces probabilités étaient « inventées » et ne donnaient « qu'une apparence de rigueur ». C'est en fait la technique du **Verbalized Sampling** : demander plusieurs réponses avec leur probabilité, puis choisir dans la **traîne** de la distribution. Elle est publiée et mesurée (voir la recherche ci-dessous). Que les directions gardées aient une probabilité de 0,05 à 0,08 correspond exactement au réglage recommandé (moins de 0,10). Ma critique était fausse sur le principe.
4. **Le choix sur la planche appartient à l'agent :** « il choisit une branche, il ne prouve rien ». Le regard humain est prévu après coup : « la planche est jointe à la réponse : la personne… peut réorienter ». Dans nos runs autonomes, personne ne regarde au moment du choix.
5. **Ce qui reste hors du noyau et n'est donc probablement pas lu :** « La direction retenue ne l'emporte que si son avantage est formulé en une phrase vérifiable reliant la position à un effet attendu » (ligne 243). Le module `DIRECTION-ATELIER` est « activable, jamais automatique ».
6. **Le coût de la génération est dit honnêtement** (ligne 115) : l'accord se demande à la prise de brief, en annonçant trois ou quatre générations par image retenue.

## Recherche faite à côté
- **Verbalized Sampling** (Zhang et al., ICML 2026, https://proceedings.mlr.press/v306/zhang26hy.html ; code : https://github.com/CHATS-lab/verbalized-sampling) :
  - l'alignement des modèles produit un « effondrement de mode », causé en partie par un **biais de typicité** chez les annotateurs, qui préfèrent ce qui est familier ;
  - demander au modèle une distribution de réponses avec leurs probabilités **multiplie la diversité par 1,6 à 2,1** en écriture créative, sans perte de qualité mesurée ;
  - **les modèles les plus capables en profitent le plus** ;
  - la consigne recommandée : « échantillonne dans les traînes, chaque probabilité sous 0,10 ».
- **Limite :** les études portent sur le texte (poèmes, histoires, blagues). Elles mesurent la **diversité**, pas la qualité visuelle d'un rendu.

## Ce que ça change (à discuter)
1. **L'étape « Échantillonner » est le mécanisme le mieux fondé de toute la séquence.** Elle produit de la diversité, et c'est sans doute pour cela que les directions gardées sont originales. **Il faut la garder.**
2. **Le point faible est ailleurs : dans le choix.** On échantillonne bien la traîne, puis c'est l'agent qui choisit seul, en vignette, une option qu'il a souvent esquissée lui-même. Or la recherche (étapes 4 et 5) dit qu'un modèle juge mal entre options proches, et ne se corrige pas sans retour extérieur. **La diversité est bien produite ; la sélection n'est pas fiable.**
3. **Cela précise la piste la plus prometteuse :** garder l'échantillonnage tel quel, et rendre le **choix** extérieur. Les moyens possibles :
   - ton jugement sur la planche, quand tu es là ;
   - sinon, une comparaison mesurée avec des références réelles ;
   - et une esquisse de la modale faite autrement que par l'agent, par exemple des captures réelles du genre.
4. **Diversité et qualité sont deux buts différents.** Verbalized Sampling ne promet que la première. Un choix dans la traîne donne de l'original, pas forcément du beau. C'est cohérent avec ce que tu as vu : les runs sont originaux, mais gadget ou génériques.

## Bilan de la séquence DIRECTION lue dans les sources
La séquence est riche et souvent bien fondée : l'échantillonnage dans la traîne, les recettes, Gate C, CFT-04a, la couleur située, l'échelle et le champ calme. Ses deux faiblesses principales, vérifiées dans les fichiers et les journaux :
1. **La place des textes.** Le noyau pousse vers l'objet de preuve et le « mécanisme ». Les contrepoids et le savoir du goût sont dans des routes que les runs n'ouvrent pas.
2. **L'absence de retour extérieur sur le goût.** Le choix, l'atelier, le retrait, la réouverture et la finition reposent tous sur l'autocritique de l'agent. Le seul regard extérieur prévu (le regard séparé, la personne) n'a jamais eu lieu dans nos runs.

## Suite proposée
Rédiger une **synthèse de lecture** (une page) qui croise les étapes 1 à 10 avec les recherches, puis en tirer, si tu le décides, le document de propositions du lot 9b, avec un protocole de test `PILOT` à l'aveugle.

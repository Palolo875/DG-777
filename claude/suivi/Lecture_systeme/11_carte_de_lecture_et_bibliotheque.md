# Lecture du système, étape 11 : carte de ce qui est lu, puis BIBLIOTHEQUE/SECTIONS et BIBLIOTHEQUE/COMPONENTS (19 novembre 2026)

## Carte : ce que les runs lisent réellement
Méthode : `read_route.py --sommaire` (85 routes, avec leur taille), croisé avec les journaux de 8 runs (9 à 16, le run 15 compris). Est comptée comme lue toute route affichée par le lecteur, ou écrite dans le fichier du tronc.

| Famille | Routes | Taille | Lues dans au moins un run |
|---|---|---|---|
| ACTION | 29 | 123,9 k car. | 6 (27,1 k) |
| BIBLIOTHEQUE | 19 | 84,2 k | 3 (20,9 k) |
| DIRECTION | 20 | 106,4 k | 5 (26,1 k) |
| SAVOIR | 17 | 176,5 k | 6 (60,1 k) |
| **Total** | **85** | **491 k** | **20 routes (134 k, soit 27 %)** |

- **Lues dans tous les runs ou presque :** `ACTION/GATE-A/CONTROLES` et `DIRECTION/START/TREE` (8 sur 8), `DIRECTION/FIRST-OBJECT` (7 sur 8), puis le tronc `DIRECTION` (6 sur 8).
- **Les plus grosses routes jamais ouvertes :** `SAVOIR/CRAFT` (44 k, mais certaines de ses sous-routes CFT ont été lues), `DIRECTION/STANDARD` (18,5 k), `ACTION/RUN_CARD` (17,3 k), `SAVOIR/TOOLS` (14,5 k), `ACTION/PIPELINE-DIRECTION`, `SAVOIR/STYLE`, `SAVOIR/TECH`, `SAVOIR/FRAME`, `BIBLIOTHEQUE/READ`…
- **Limites :**
  - une route parente comptée comme jamais lue peut avoir eu des sous-routes lues ;
  - une partie du contenu de ces routes atteint quand même l'agent par les blocs compilés dans le noyau ;
  - le journal ne voit pas les fichiers ouverts directement.
- **Ce que ça dit :** environ les trois quarts du paquet, en volume, ne sont jamais ouverts pendant un run de création. Ils servent la gouvernance, la trace complète et la maintenance, ou attendent un signal qui ne vient pas.

## BIBLIOTHEQUE/SECTIONS (lue en entier)
- **Elle répond directement au constat A-2, le générique sous le premier écran.** Pour chaque section ordinaire (fonctionnalités, preuve, tarifs, questions, contact et accès, inscription, pied de page), elle dit ce que la personne cherche, la forme réflexe, les leviers propres au sujet et ce qu'on vérifie sur capture. C'est clair et utile.
- **Elle n'a été ouverte dans aucun run.** Le tronc `DIRECTION` (`BIBLIOTHEQUE/SEQUENCE`) y renvoie (« Section par section, la forme réflexe et ses leviers : `BIBLIOTHEQUE/SECTIONS` »), mais c'est un renvoi de second niveau, et aucun outil ne l'a proposée.
- **Ses leviers sont surtout d'usage et d'honnêteté** (l'ordre, la preuve, les vraies questions, l'adresse en texte), **peu d'exécution visuelle.** Pour l'aspect, elle renvoie à « une propriété empruntée à la direction ». Même lue, elle corrigerait la structure plus que la finition.

## BIBLIOTHEQUE/COMPONENTS (lue en entier)
- C'est surtout de l'**architecture et de la gouvernance** : six couches (tokens, grammaire de marque, primitives, objets, scènes, gabarits), un contrat de composant partagé en 13 champs, une déclaration de grammaire de marque en 15 champs, un graphe de dépendances.
- **La partie utile au goût tient en un paragraphe, « Parties ordinaires » :** la navigation, les boutons et le pied de page empruntent **une** propriété de la direction (voix typographique, bord, couleur par rôle, alignement, mots du sujet), sans ornement. Le test : « logo et titre masqués, la navigation, le bouton et le pied appartiennent-ils encore à cette page ? » Ce paragraphe a un équivalent dans le noyau.

## Recherche (déjà vérifiée à l'étape 1)
- Le guide d'Anthropic sur l'écriture des skills (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) le dit : « Avoid deeply nested references… Claude might partially read files when they're referenced from other referenced files… Keep references one level deep from SKILL.md ». `BIBLIOTHEQUE/SECTIONS` est exactement dans ce cas : elle est citée par une route du tronc, pas par le noyau.
- Vercel (étape 7) : ce qui est disponible à la demande n'est souvent pas chargé.

## Ce que ça change (à discuter)
1. **Le paquet est surtout du savoir dormant.** Plus de lecture ne fera pas mieux. Ce qui compte, c'est **ce qui est servi au bon moment**. Les routes qui traitent directement les défauts observés (`BIBLIOTHEQUE/SECTIONS`, CFT-03, CFT-04a, CFT-05) existent, mais dorment.
2. **Une piste simple et peu coûteuse, à tester :** quand `verifier` voit une section ordinaire (une grille de cartes, un tableau, un accordéon, un pied de page), il affiche **dans sa fiche les trois lignes utiles** de la route correspondante (le réflexe, un levier, la vérification), au lieu de simplement nommer la route.

## Plan de lecture pour la suite (taille, et ce que j'en attends)
| Ordre | Partie | Taille | Pourquoi |
|---|---|---|---|
| 1 | `SAVOIR/FRAME` et `SAVOIR/STYLE` | 24,5 k | La composition et les styles : le cœur du goût, jamais lu |
| 2 | `BIBLIOTHEQUE/READ`, `/SELECT`, `/TENSION` | environ 20 k | La traduction d'un caractère en leviers concrets |
| 3 | `SAVOIR/STATE` (déjà lu en partie) et `SAVOIR/TECH` | environ 29 k | La finition et les techniques |
| 4 | ACTION : `GATE-B`, `PIPELINE-DIRECTION`, `STATUS` | environ 28 k | Ce que le système appelle « preuve » et « acceptation » |
| 5 | `gouvernance/README.md`, puis survol de `RUN_CARD`, `CLOSE-PACKAGE` | environ 30 k | Le poids de la gouvernance dans le coût |

Ordre de grandeur : 130 k caractères à lire, soit **4 ou 5 étapes comme celle-ci.**

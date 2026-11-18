# Lot 4 bis, sous-lot 2 — Sections ordinaires : rapport

15 novembre 2026. Révision livrée : `R2026-11-15g` (commit `b6853df`, fusionné dans master en `b7b9860`). Document hors du paquet.

Le texte proposé a été intégré tel quel. La validation complète avec navigateur passe, et l'archive GitHub est identique au commit, fichier par fichier.

## 1. Ce qui a changé

| Où | Changement |
|---|---|
| `design/formes/catalogue.md` | Nouvelle route `BIBLIOTHEQUE/SECTIONS`, juste après `BIBLIOTHEQUE/SEQUENCE` : le texte des propositions, sans modification. |
| `BIBLIOTHEQUE/SEQUENCE`, « Trame sur toute la page » (tronc `DIRECTION`) | « Section par section, la forme réflexe et ses leviers : `BIBLIOTHEQUE/SECTIONS`. » |
| Portée du catalogue (`BIBLIOTHEQUE/SCENE`) | Pour un commerce local, une boutique, une lecture ou un événement, le catalogue renvoie aussi aux sections ordinaires. |
| Fiche de `parcours.py verifier` | Le rappel « Partie ordinaire » cite `BIBLIOTHEQUE/SECTIONS`. |
| Fiche de version | Les formes comptent désormais les sections ordinaires. |

## 2. Écart avec ce que j'avais annoncé

**La recherche de « témoignages » ne mène pas à la nouvelle route.** Elle mène à `SAVOIR/SOURCE` et à `SAVOIR/CRAFT/CFT-06`, qui portent la règle d'honnêteté sur les témoignages. Le texte dit « avis » et « citations », pas « témoignages ». J'ai essayé d'ajouter le mot au titre de la section : cela ne changeait pas le classement, je suis donc revenu au texte que vous aviez approuvé.

« Tarifs », « questions fréquentes » et « horaires » mènent bien à la route en premier, et « pied de page » en deuxième.

## 3. Vérification

| Contrôle | Résultat |
|---|---|
| Noyau | identique (44 994 / 46 000 octets) |
| Tronc `DIRECTION` | +80 caractères, soit 34 595 sur 35 000 ; marge de 405 |
| Autres troncs | identiques |
| Régressions d'audit | 138 cas, dont 3 nouveaux : sept sections servies, renvoi au tronc, trouvabilité par le nom |
| Lecteur | 105 cas ; planchers de trouvabilité tenus |
| Recette, regard, parcours | A 118, C 65, B 81 / 39 / 150 cas |
| Autres contrôles (journal, budget, préparation, déplacement, craft, supports, export Local, reproductibilité) | passés |
| Durée de préparation | 12 min 04 s |

Empreintes :
- GitHub `4e118de9…3e6dfd`
- Local `14bf62a6…78b7e9`

## 4. Suite

Le sous-lot 3, B-03, porte sur les planches de principes. Il demande votre regard sur des images : au plus six planches, chacune en avant/après d'un mécanisme sur un même contenu neutre, dessinées par du code du paquet.

Ses propositions contiendront :
- la liste des mécanismes retenus ;
- les planches elles-mêmes, rendues, pour que vous les jugiez à la vue avant toute intégration.

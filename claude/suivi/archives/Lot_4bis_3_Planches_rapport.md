# Lot 4 bis, sous-lot 3 — Planches de principes : rapport

15 novembre 2026. Révision livrée : `R2026-11-15h` (commit `ee7bc36`, fusionné dans master en `7537daa`). Document hors du paquet.

Les six planches que vous avez validées sont intégrées. Les fichiers livrés sont **identiques pixel pour pixel** aux planches que vous avez vues ; seul l'encodage du PNG diffère. La validation complète avec navigateur passe, et l'archive GitHub est identique au commit. Le lot 4 bis est terminé.

## 1. Ce qui a changé

| Où | Changement |
|---|---|
| `design/principes/` | Les six planches, au format 1600 × 900, 163 Ko au total |
| `scripts/principes.py` | Le générateur ; distribution GitHub seulement |
| `SAVOIR/CRAFT/CFT-05` | « Fonds voisins » et « Accent de marque et accent de foyer » citent chacun leur planche |
| `SAVOIR/TYPE`, « Réglage d'un grand texte » | Cite sa planche |
| `SAVOIR/STATE`, sous la table des gestes | Une ligne cite les trois planches : masse visuelle, cohérence de rayon, chiffres |
| Guide de niveau 2 | Un paragraphe présente les planches : un mécanisme, jamais un style à reprendre ; la section propriétaire fait foi |
| Fiche de version, README des scripts, manifeste | Mis à jour |

**Garde PLA-01.** Chaque planche citée existe, chaque fichier de `design/principes/` est cité par une route, et chacun garde le format 1600 × 900.

## 2. Écart

Dans le guide, j'avais prévu un lien vers le dossier. Le contrôle des liens n'accepte que des liens vers des fichiers : le dossier est donc nommé en clair, `design/principes/`.

## 3. Vérification

| Contrôle | Résultat |
|---|---|
| Noyau | identique (44 994 / 46 000 octets) |
| Tronc `DIRECTION` | +82 caractères, soit 34 677 sur 35 000 ; marge de 323 |
| Régressions d'audit | 141 cas, dont 3 nouveaux : planches citées et au format, planche orpheline refusée, planche absente ou hors format refusée |
| Parcours (navigateur) | 151 cas, dont le générateur, qui réécrit les six planches au format |
| Recette, regard, lecteur | A 118, C 65, B 81 / 39 / 105 cas |
| Autres contrôles | passés |
| Taille des archives | GitHub 1,12 Mo ; Local 1,11 Mo, soit environ 160 Ko de plus |
| Durée de préparation | 11 min 43 s |

Empreintes :
- GitHub `c095e6ab…28f702`
- Local `8800a898…16a0e`

## 4. Bilan du lot 4 bis

Trois révisions, une par constat, chacune approuvée avant d'être intégrée :

| Révision | Constat | Ce qui a été ajouté |
|---|---|---|
| `R2026-11-15f` | B-09 | Accessibilité et performance |
| `R2026-11-15g` | B-04 | Sections ordinaires |
| `R2026-11-15h` | B-03 | Planches de principes |

Le noyau n'a pas bougé de tout le lot. Le tronc `DIRECTION` a pris 162 caractères ; il lui reste 323 de marge. Cette marge sera à regarder au lot 7 (poids et coût), qui est le prochain lot du plan.

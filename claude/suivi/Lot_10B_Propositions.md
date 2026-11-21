# Lot 10B — Propositions : des outils plus sobres

Rédigé le 21 novembre 2026. Base : `R2026-11-15p` (`master` `b541344`). Aucun run.

Règle 1 : rien n'est intégré sans décision. « D'accord » vaut pour les options A partout.

## 0. Mesure (sur la révision `p`, sans run)

**Pages de test** : l'invitation du PILOT (`Pilot_9b/objet1/Y`), et les transcriptions des quatre agents du PILOT.

| Mesure | Valeur | Source |
|---|---|---|
| Sortie écran de `verifier`, 1er appel | 3 659 caractères | Mesure du jour |
| Sortie écran de `verifier`, 2e appel, page inchangée | **3 659 caractères, identique** | Mesure du jour |
| Durée d'un appel à `verifier` | environ 50 s | Mesure du jour |
| Appels à `verifier` par run | 3 à 11 | Transcriptions |
| Images produites par `captures --version` | 2 (une par largeur) | Mesure du jour |
| Images lues par run | 13 à 29 | Transcriptions |
| Appels d'outils avant le premier HTML | **31 à 38**, soit environ un tiers du run (dont 4 à 6 `read_route` et 5 à 27 lectures) | Transcriptions |
| Tronc DIRECTION lu en entier | 31 398 caractères | `read_route` |
| Marge du noyau | 190 octets | `build_core` |

**Rappel du coût.** Il suit le nombre de tours multiplié par la taille du contexte (lot 10, mesure). Chaque appel et chaque image restent dans le contexte jusqu'à la fin.

## 1. Propositions

Chacune garde **les mêmes contrôles**. Elle change seulement la façon de les servir.

### B1 — Une seule image par version pendant la boucle

- **A (recommandée).** `parcours.py captures --version vN` écrit **une** planche : premier écran au bureau et en mobile, côte à côte, en 1×.
  - Les captures par largeur restent disponibles (`--separees`).
  - Le ×2 reste au zoom (`--foyer`) et à la livraison (`--pleine`).
  - `verifier` désigne une seule image à ouvrir d'abord (la lecture sans texte).
  - **Cible** : 1 image par version, au lieu de 2.
- **B.** Rien. Le gain viendrait seulement de la consigne au noyau (B5).

### B2 — `verifier` ne répète pas ce qui n'a pas changé

- **A (recommandée).**
  - Dès le 2e appel sur une même page, la sortie écran ne montre que **les défauts et signaux apparus ou disparus**, plus **le nombre** de ceux qui restent, pour qu'un défaut persistant ne soit jamais oublié.
  - `parcours.md` reste complet.
  - `--complet` réaffiche tout.
  - **Cible** : sortie du 2e appel divisée au moins par 3 quand rien n'a changé.
- **B.** Seulement un message « rien n'a changé depuis l'appel précédent », quand c'est le cas.

### B3 — `parcours.py chantier` : le démarrage en un appel

- **A (recommandée).** En un appel :
  - crée les dossiers (`travail/`, `livrable/`, `references/`) ;
  - lance `tirage` ;
  - lance `leviers` si des pôles sont donnés ;
  - écrit le gabarit de la trace légère, avec ses six lignes ;
  - affiche la commande `references` à compléter et la commande `polices --catalogue`.
  - Sortie de 1 500 caractères au plus. Le détail va dans `travail/chantier.md`.
  - **Il n'écrit aucune décision** : ni direction, ni registre, ni choix.
  - **Cible** : une part des 31 à 38 appels de démarrage. L'effet réel ne se mesurera qu'en run.
- **B.** Pas de nouvelle commande ; un paragraphe du noyau liste l'ordre des commandes de démarrage.

### B4 — Le tronc s'ouvre par un sommaire

- **A (recommandée).**
  - `read_route --tronc MODE --fichier` écrit en tête un **sommaire** : une ligne par route du tronc (son rôle, quand la relire, sa phrase-clé, lue à son lieu). Le corps suit, inchangé.
  - Le noyau dit de lire d'abord le sommaire, puis chaque route au moment où elle sert.
  - **Cible** : 4 000 caractères au plus pour le sommaire.
  - **Limite** : rien n'empêche l'agent de lire tout le fichier, et c'est permis.
- **B.** Rien.

### B5 — Trois consignes de travail au noyau

- **A (recommandée).** Une phrase au bloc `BOUCLE` du noyau : « Grouper les commandes ; écrire le HTML une fois puis le retoucher ; ne relancer `verifier` qu'après un changement qui peut modifier un défaut. »
  - Environ 200 octets, financés par une redite du noyau à retirer.
  - Je montrerai la redite choisie dans le rapport, avec l'endroit où son contenu reste servi.
- **B.** La consigne seulement dans `scripts/README.md`, hors du noyau.

## 2. Gardes et tests (mutation rouge, échec nommé)

- **B1** : `captures --version` produit exactement une image, aux deux largeurs côte à côte.
- **B2** :
  - un défaut corrigé disparaît de la sortie et un nouveau y apparaît ;
  - le compte des défauts persistants est affiché ;
  - le 2e appel sur une page inchangée est au moins 3 fois plus court.
- **B3** : `chantier` crée les dossiers et le gabarit de trace (qui passe `parcours.py trace` comme forme à remplir), n'écrit aucune ligne de décision, et respecte son plafond de sortie.
- **B4** : le sommaire cite chaque route du tronc et tient sous 4 000 caractères.
- **B5** : la phrase est au noyau, et le budget reste à 46 000 octets au plus.

## 3. Ce que le lot ne prouvera pas

- Que les agents utiliseront `chantier` ou liront le sommaire plutôt que tout le tronc.
- **La baisse réelle du coût et la qualité ne se mesurent qu'en run** (lot 13, ou la mesure sobre si Junior la décide).

Le rapport donnera les mesures hors run avant et après, et dira ce qui n'est pas mesuré.

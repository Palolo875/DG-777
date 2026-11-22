# Lot 12b — Rapport : une référence générée et une carte de lecture

- **Révision** : `R2026-11-15w`, livrée le 22 novembre 2026.
- **Branche** : `lot-12b`.
- **Décision** : « D'accord » au lot 12 (E2 et E9, options A), puis « Oui » pour 12b.
- **Runs** : aucun.

## 1. Ce qui change

| Proposition | Changement |
|---|---|
| **E2** Référence générée | `guides/reference.md` (≈ 22 000 caractères), écrite par `scripts/reference.py` : l'aide des 5 outils et des 15 commandes de `parcours.py`, puis les 85 sections servies par le lecteur, rangées par famille, avec leur sujet. Reliée depuis le README (« Retrouver une commande ou une section ») et le README des guides. |
| | Garde **DOC-03** (garde 30) : la page est identique à sa génération. La procédure « Ajouter ou modifier une règle » gagne une étape « Référence ». |
| **E9** Carte « Comment l'agent lit » | Quatrième carte des supports (`supports/lecture.*`), produite par le générateur existant, en clair et en sombre : six étapes (noyau, classer, tronc, au signal, outils, sans outils), trois encadrés (budgets, la section fait foi, un seul agent), un pied (« Ce qui n'a pas été vu se déclare »). Reliée depuis le README et le README des supports. |
| **Garde nouvelle des supports** | Une ligne de carte plus large que son encadré est refusée (voir § 3). |
| Fait corrigé en passant | `scripts/README.md` disait « quatorze sous-commandes » : il y en a quinze depuis `chantier` (lot 10B). |

## 2. Deux choix faits en route

1. **La référence donne le sujet de chaque section, pas sa première phrase.** Les premières phrases sont écrites pour l'agent (tutoiement, vocabulaire interne) ; copiées dans une page pour les personnes, elles déclenchaient à juste titre les gardes de registre (VOU-01) et de langue (LAN-01). Le sujet vient du titre de la section, après son code.
   - Sept titres ne conviennent pas tels quels : cinq ne portent que leur code (`ACTION/RUN-*`), deux gardent un mot réservé à l'agent (« gate », « tokens »). Une petite table, `SUJETS`, les dit pour les personnes, sans renommer les titres (leurs ancres restent valides).
   - Le générateur s'arrête si une section nouvelle n'a pas de sujet.
2. **La référence ne nomme pas le fichier d'une section.** Une section déplacée avec son titre ne la rend pas fausse : le contrôle de déplacement existant reste vert.

## 3. Un défaut que la recette ne voyait pas

Sur la capture de la nouvelle carte, deux lignes débordaient de leur encadré. La recette de rendu (`check_render.py`) ne l'a pas relevé : le texte est dans un SVG, et elle ne mesure pas un texte contre son cadre.

- **Correction** : les deux lignes sont raccourcies.
- **Garde ajoutée** dans `validate_supports.py` : chaque ligne d'une carte de séquence est mesurée avec les métriques de la police livrée (lues avec la bibliothèque standard, comme le promet le contrôle des supports), puis comparée à la place de son encadré (bord moins 12 px).
- **Calibrage** : facteur par graisse mesuré dans le navigateur sur 133 textes des cartes (1,02 à 1,04 pour le texte courant, 1,06 à 1,11 pour les titres), majoré.
- Les trois cartes existantes la passent.

## 4. Mutations rouges

| Garde | Mutation | Résultat |
|---|---|---|
| DOC-03 | L'écart n'est plus relevé | Rouge : `test_page_retouchee_refusee` |
| DOC-03 | Un titre sans sujet ne bloque plus la génération | Rouge : `test_titre_sans_sujet_arrete_la_generation` (après correction d'un plantage en échec nommé) |
| DOC-03 | Seules 3 commandes de `parcours` sont générées | Rouge : `test_chaque_section_et_commande`, `test_page_reelle_identique` |
| DOC-03 | Une erreur de génération (code porté par deux titres) n'est plus rattrapée | Rouge : `test_code_ambigu_nomme_sans_planter` |
| Débordement | La garde ne relève plus rien | Rouge : `test_ligne_trop_large_relevee` |
| Débordement | Place des encadrés portée à 400 px | Rouge : `test_ligne_trop_large_relevee` |

Un test existant comptait 6 SVG de supports ; il en compte 8.

**Trouvé par la première préparation complète.** Le contrôle de déplacement (cas « doublon » : le même code sous deux titres) a fait planter la génération de la référence dans la validation de structure. DOC-03 rattrape maintenant l'erreur et la nomme (« référence non générée »), comme les autres gardes ; un test et sa mutation le protègent.

## 5. Préparation et livraison

À compléter.

## 6. Ce que ce sous-lot ne prouve pas

- Que la carte et la référence aident un lecteur neuf : seule une lecture extérieure le dira.
- La garde de débordement porte sur les cartes de séquence ; la carte du système a son propre dessin, non mesuré.

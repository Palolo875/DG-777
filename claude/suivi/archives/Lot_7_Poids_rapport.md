# Lot 7 — Poids et coût : rapport

18 novembre 2026. Révision livrée : `R2026-11-15i` (commit `339d109`, fusionné dans master en `876e99b`). Document hors du paquet.

Les options A ont été appliquées partout. La validation complète avec navigateur passe, et l'archive GitHub est identique au commit, fichier par fichier.

## 1. Avant et après

| Mesure | Avant | Après |
|---|---|---|
| Tronc `DIRECTION` | 34 677 caractères (marge 323) | **31 160** (marge 3 840) |
| Tronc LITE / ITER / STANDARD / SYSTÈME | 11 530 / 9 110 / 10 599 / 11 320 | **8 013 / 5 593 / 7 082 / 7 803** |
| Sortie de la recette, sur une même page | 5 113 caractères | **3 344** |
| Noyau (`SKILL.md`) | 44 994 octets (marge 1 006) | 45 210 (marge 790) |
| Avertissement « marge faible » dans le tronc lu par l'agent | oui | non ; la validation de structure le donne au mainteneur |
| Bruit dans la sortie de la préparation | requêtes de test, « journal introuvable », résumés unittest | aucun |

## 2. Ce qui a changé

| Constat | Changement |
|---|---|
| D-07, A-25 | « Contrôles applicables » devient la sous-route `ACTION/GATE-A/CONTROLES`, la seule que servent les cinq troncs. Une phrase en tête de cette sous-route dit où lire le reste : le contrat de portée, les familles de méthodes et l'adéquation des preuves se lisent en trace complète, à l'acceptation, ou quand l'accessibilité ou la conformité est dans le périmètre. Le plancher REQ-01 (« contrôle applicable dans ACTION ») est porté par la sous-route. |
| D-07 (effet de bord) | Le lecteur ne montre plus la consigne de marge à l'agent ; `validate_structure.py` l'affiche au mainteneur. |
| C-08 | La recette n'affiche plus qu'une ligne de limites par appel. Le détail complet sort avec `--limites` ; il figure aussi dans le JSON et dans une section 7 de la fiche du parcours. |
| A-09 | Le coût est rendu visible, sans plafond. La réponse visible gagne une ligne « Coût » : passes de `verifier`, générations d'image, références capturées. L'absolu 4 le dit, et l'exemple de la skill la montre. |
| B-22 | `DIRECTION/ASSET-ROUTE` : « L'accord demandé dit le coût : trois ou quatre générations par image retenue. » |
| A-13 | Les quatre paragraphes du noyau deviennent une phrase d'ouverture et une liste, avec les mêmes mots. Les phrases de moins de 80 caractères restent jointes à leur voisine. |
| Bruit | Le serveur de test ne journalise plus ses requêtes. Le « journal introuvable », un échec attendu, est capté par son test. La préparation ne relaie plus le résumé ordinaire de unittest. |

## 3. Écarts et points à relire

1. **Le noyau prend 216 octets, et non 100.** Les listes en coûtent 74. La ligne « Coût » de la réponse visible et la mention « et une ligne de coût » coûtent le reste. Il reste une marge de 790 octets.
2. **Deux outils lisaient le texte reformaté :**
   - `parcours.py tirage` cherchait les pistes du sujet sur une seule ligne. Je l'ai adapté à la liste ; les tests l'ont attrapé.
   - Le test de trouvabilité compte désormais une sous-route comme sa route : `ACTION/GATE-A/CONTROLES` répond à `ACTION/GATE-A`. Les scores restent inchangés : 18 sur 30 et 9 sur 15, comme sur master.
3. **Le bruit avait une troisième source.** Le résumé de unittest part sur la sortie d'erreur, et la préparation le relayait comme un signal. Il est maintenant filtré ; une vraie sortie d'erreur reste affichée.
4. **Hors périmètre annoncé :**
   - la garde de chargement (CHG-04) accepte la sous-route de Gate A ;
   - un test du journal utilisait l'ancienne liste du tronc ITER : il a été mis à jour.

## 4. Vérification

| Contrôle | Résultat |
|---|---|
| Régressions d'audit | 146 cas, dont 5 nouveaux : sous-route seule dans les troncs, reste de Gate A toujours servi, pas d'avertissement à l'agent, coût visible, coût d'une génération à l'accord |
| Recette | A 119, dont un nouveau cas : une ligne par défaut, le détail avec `--limites` et dans le JSON ; C 65 ; B 81 |
| Parcours, regard, lecteur, journal, budget, préparation | 151, 39, 105, 18, 19, 10 cas |
| Déplacement, craft, supports, export Local, reproductibilité | passés |
| Durée de préparation | 11 min 17 s |

Empreintes :
- GitHub `f24298bf…20ada9`
- Local `49d63f52…ae5962`

## 5. Suite

Le prochain lot est le **lot 8, la passe de livraison**. Il porte sur l'organisation, la navigation, les noms, les guides, le glossaire et la fiche lisible, ainsi que sur les sept critères de livraison. Y entrent aussi B-20 (présentation des gabarits) et la question laissée au sous-lot 1 du lot 4 bis : quel propriétaire pour la typographie de lecture.

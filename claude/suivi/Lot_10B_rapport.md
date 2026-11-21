# Lot 10B — Rapport : des outils plus sobres

- **Révision** : `R2026-11-15q`, livrée le 21 novembre 2026.
- **Branche** : `lot-10b`.
- **Décision** : « Oui » au document de propositions (`Lot_10B_Propositions.md`). Les options A s'appliquent partout.
- **Runs** : aucun.

## 1. Ce qui change, et la mesure avant et après (hors run)

| Proposition | Changement | Avant (`p`) | Après (`q`) |
|---|---|---|---|
| **B1** Une image par version | `captures --version vN` écrit **une** planche, `vN.png` : premiers écrans côte à côte, à 1×. `--separees` garde une image par largeur ; `--pleine` reste pour la livraison. | 2 images | **1 image** |
| **B2** `verifier` différentiel | Dès le 2e appel, seulement les défauts et signaux apparus ou disparus, plus le **nombre** de ceux qui restent. `--complet` réaffiche tout ; la fiche reste complète. | 2e appel sur la page du PILOT : 3 659 caractères | **347 caractères (÷ 10,5)** |
| **B3** `chantier` | Le démarrage en un appel : dossiers, `tirage`, `leviers` des pôles donnés, gabarit de trace légère (six lignes, forme conforme, **aucune décision**). | 31 à 38 appels avant le premier HTML (PILOT) | **1 appel** pour cette part du démarrage ; l'effet sur un run réel n'est pas mesuré |
| **B4** Sommaire du tronc | Le fichier `--tronc` s'ouvre par un sommaire : une ligne par route, avec sa phrase porteuse, lue à son lieu. | Aucun sommaire | 1 246 caractères pour le tronc DIRECTION |
| **B5** Sobriété au noyau | Le bloc `BOUCLE` dit : grouper les commandes ; écrire le HTML une fois puis le retoucher ; une version en une image ; `verifier` seulement après un changement qui peut modifier un défaut. | — | Noyau : 45 810 → **45 876 octets** sur 46 000 |

**Financement de B5.** La phrase longue sur `check_render.py` (aux largeurs courantes, ne juge ni la direction ni l'usage) est raccourcie. Sa recette complète reste dans `ACTION/RECETTE-RENDU` et dans `verifier`, qui la lance. La garde CORE-01 (blocage des ressources externes « sauf avec `--allow-external` ») est tenue.

## 2. Écart par rapport à la proposition B4, que je signale

J'avais proposé que l'agent lise **d'abord le sommaire**, puis chaque route au moment où elle sert. Un test existant m'a rappelé une décision antérieure : la **règle de vitesse** du noyau demande de lire le tronc **une fois, en entier**, pour éviter les relectures qui s'accumulent dans le contexte. Je l'ai gardée.

Le sommaire sert donc à **s'orienter** dans le fichier, pas à éviter de le lire. B4 ne réduit pas la lecture. Si Junior veut tester l'autre façon, cela demande une mesure en run.

## 3. Un bogue trouvé par les tests

`planche_version` ne créait pas le dossier de sortie, alors que Playwright le faisait de lui-même pour les captures séparées. Le test avec navigateur l'a fait planter sur la copie intacte. C'est corrigé : le dossier est créé.

## 4. Mutations rouges

| Mutation | Résultat |
|---|---|
| Écart faux dans `verifier` (tout est « apparu ») | Rouge : P28 |
| `chantier` écrit une décision dans la trace | Rouge : P29 |
| Une route absente du sommaire | Rouge : P30 |
| Consigne de sobriété retirée du noyau | Rouge : P31 |
| B1 : captures toujours séparées (copie mutée, navigateur) | Rouge : P135 |
| B2 : `verifier` sans différentiel (copie mutée, navigateur) | Rouge : P147 (2 050 → 2 050 caractères) |

La copie intacte passe les 176 cas avec navigateur.

## 5. Préparation et livraison

À compléter.

## 6. Ce que ce lot ne prouve pas

- Que les agents utiliseront `chantier`, la planche et le différentiel.
- La baisse réelle du coût d'un run, qui se mesure en tours multipliés par le contexte : seul un run le dira.
- Que la qualité n'a pas bougé : les contrôles sont les mêmes, mais aucun rendu n'a été produit.

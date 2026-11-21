# Lot 4 — Ce qui doit arriver à l'agent : rapport

15 novembre 2026. Révision de départ : `R2026-11-15b`. Révision livrée : `R2026-11-15c`. Document hors du paquet.

**Décision appliquée.** « Allons-y, à toi le choix. » Vous m'avez laissé les choix de ce lot. Je les ai faits avec trois règles :
- ne rien retirer de ce que l'agent lit sans une preuve que c'est inutile ;
- n'ajouter au noyau que ce que le système désigne déjà comme travail de l'agent ;
- reporter ce qui demande du contenu nouveau ou votre jugement de designer.

Chaque choix est motivé ci-dessous. Vous pouvez revenir sur n'importe lequel.

## 1. D'abord, la carte des déclencheurs

Elle est livrée à part (`Carte_des_declencheurs_Design_Governance.md`), calculée depuis les fichiers.

- **Les 84 routes ont toutes un chemin d'arrivée.** 14 sont dans un tronc, 41 s'ouvrent sur un signal (ligne d'un mode ou table des signaux), 29 par le renvoi d'une autre route. Aucune n'est atteignable par la seule recherche.
- **Les routes jamais lues en phase 6 (B-01) sont toutes « sur signal » ou « par renvoi ».** La carte donne, pour chacune, ce qui l'ouvre. C'est votre remarque du 14 novembre, mesurée : leur non-lecture dit qu'elles n'ont pas été éprouvées, pas qu'elles sont de trop.
- **Le run de contrôle (lot 9) peut s'en servir.** Choisir un brief qui fait apparaître un déclencheur dit si l'agent le suit.

## 2. Le sort de chaque constat

| Constat | Sort | Choix et raison |
|---|---|---|
| A-01 — Creative Boot et cible, 24 % du tronc, peu visibles dans les traces | **Reporté au run de contrôle** | Ne rien retirer. La trace légère n'oblige pas à écrire ces champs : qu'ils n'y figurent pas ne prouve pas qu'ils ne servent pas. Les retirer du tronc changerait ce que lit chaque run DIRECTION sans preuve. Le run de contrôle comparera. |
| A-04 — trois routes prescrites sans condition pendant la fabrication, jamais lues | **Corrigé** | La ligne DIRECTION de `DIRECTION/CHARGE` les conditionne. Gate C s'ouvre quand la revue sur capture révèle une faiblesse de craft. `PIPELINE-DIRECTION` et `VISUAL_PROOF` s'ouvrent en trace complète, ou quand leur ligne de la table des signaux apparaît ; ces deux routes portent surtout des verdicts et des axes, c'est-à-dire de la trace complète. Les contrôles A restent dus. |
| A-10, C-18 — la direction se choisit au bureau, même pour une application | **Corrigé** (noyau) | Pour un produit d'abord mobile, les trois esquisses se rendent aussi à 390 px, et la planche montre le mobile (sans `--bureau-seul`). Pour un produit d'abord au bureau, rien ne change. La planche savait déjà le faire ; aucun code n'a changé, sauf l'aide de l'option. |
| A-11 — le choix de la direction n'a qu'un juge | **Corrigé** | La planche est jointe à la réponse. La personne voit les directions écartées et peut réorienter, sans tour d'échange en plus. Le choix reste celui de l'agent tant qu'elle ne le fait pas. |
| A-24 — la section 5 du noyau promet plus qu'elle ne contient | **Corrigé** (noyau) | Elle s'appelle désormais « Avant de construire — le test de trame », ce qu'elle contient. |
| B-02 — la grille de travail de l'agent n'est pas au noyau | **Corrigé** (noyau) | La revue sur capture en quatre questions devient un bloc compilé (`BOUCLE-CAPTURE`), dans la boucle d'édition. Elle était désignée comme grille de travail en trace légère, mais l'agent ne la voyait jamais. |
| B-05 (suite) — les critères de Gate C n'arrivent pas au noyau | **Corrigé autrement** | Je ne compile pas les six critères : ils recoupent les contrôles du noyau et coûteraient près de 2 000 octets. La revue sur capture, désormais au noyau, ouvre Gate C sur une faiblesse de craft, critère par critère. |
| B-01 — le meilleur savoir de construction n'est pas lu | **Reporté au run de contrôle** | La carte des déclencheurs dit ce qui l'ouvre ; le run dira si l'agent suit. |
| B-03 — le savoir ne se voit jamais (aucune image) | **Reporté** à un lot de savoir nouveau | Il demande de créer du contenu : planches, repères visuels. Votre jugement de designer est en jeu, ainsi que la règle 6 sur les sources, encore ouverte (B-12). |
| B-04 — les sections ordinaires ont peu de savoir | **Reporté**, même lot | Même raison : il s'agit d'écrire du savoir, pas de corriger. |
| B-09 — performance et accessibilité, peu de repères | **Reporté**, même lot | Même raison. La mesure du poids de page existe depuis le lot 1 (`parcours.py verifier`, à titre d'information). |

**Je signale un lot surdimensionné.** B-03, B-04 et B-09 forment à eux trois un chantier de rédaction du savoir, avec recherche et décisions de designer. Je vous propose d'en faire un lot à part, « 4 bis — savoir à écrire ». Il viendrait après le lot 6, qui tranchera la règle 6.

## 3. Ce qui change pour l'agent

| Où | Avant | Après |
|---|---|---|
| Noyau, boucle d'édition | La revue sur capture n'y est citée que comme repli du regard séparé | Ses quatre questions sont au noyau ; une faiblesse de craft ouvre Gate C |
| Noyau, « Diverger sur image » | Esquisses et planche au bureau seulement | Aussi en mobile pour un produit d'abord mobile ; planche jointe à la réponse |
| Noyau, section 5 | « situer l'interface et son caractère » | « le test de trame » |
| Ligne DIRECTION de `CHARGE` | Pipeline, preuve visuelle et Gate C sans condition | Gate C sur faiblesse de craft ; pipeline et preuve visuelle en trace complète ou sur leur signal |

## 4. Les gardes ajoutées

Trois planchers du noyau (`CORE-01`) empêchent ces apports d'en ressortir sans qu'on le voie :
- les quatre questions ;
- l'ouverture de Gate C par la revue ;
- les esquisses en mobile pour un produit d'abord mobile.

Chacun a son test, qui le fait échouer quand on retire le texte (`AgentLotFourTests`).

## 5. Ce qui a été vérifié

| Contrôle | Résultat |
|---|---|
| Noyau compilé | Trois changements, ceux du § 3. `SKILL.md` : **44 891 / 46 000 octets**, soit 864 de plus. La marge tombe à 1 109 octets : le lot 7 (poids et coût) devra la regarder. |
| Troncs des cinq modes | **Identiques**. DIRECTION reste à 34 515 / 35 000. |
| Trouvabilité | 18/30 et 10/15, inchangés. |
| Tests | Lecteur 105, régressions d'audit 116, budget 19, préparation 10, journal 18. |
| Validation complète avec navigateur, archives | Passe du premier coup (`preparer_livraison.py --require-browser`, code 0) : recette 79 cas navigateur, regard 39, parcours 141, cartes du système, build reproductible, export Local validé seul. |

## 6. Livraison

- Dépôt : commit `267d661` sur la branche `agent`, fusionné dans `master`. Le contenu de l'archive GitHub est identique à ce commit.
- Dossier `R2026-11-15c/` : archives GitHub (sha256 `edf1fb2c…`) et Local (sha256 `baaee27b…`), et le dépôt.

## 7. La suite

Le lot 5, garanties vraies : gardes, messages et contrôle de la trace légère. Puis le lot 6, adoption des essais, qui tranchera la règle 6. Le lot « 4 bis — savoir à écrire » attend votre accord sur son principe.

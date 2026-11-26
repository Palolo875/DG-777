# Lot 7 — Poids et coût : propositions

15 novembre 2026. Révision de départ : `R2026-11-15h`. Document hors du paquet. Rien n'est intégré.

Le principe du lot : ce que l'agent lit à chaque run, et ce que ses outils lui affichent, ne doit coûter que ce qui sert. J'ai relu et mesuré les neuf constats dans l'état actuel, ainsi que le bruit de la préparation, noté depuis le lot S.

| Sort | Constats |
|---|---|
| À corriger, sans choix | C-08, B-22, A-13, avertissement de marge (D-07), bruit de la préparation |
| À corriger, avec un choix | D-07 et A-25 (tronc), A-09 (coût d'un run) |
| À écarter, avec raison | D-08, F-08 (poids de l'export Local) |
| Reporté au lot 8 | B-20 (forme des gabarits) |

---

## 1. Mesures actuelles

| Mesure | Valeur |
|---|---|
| Noyau (`SKILL.md`) | 44 994 / 46 000 octets, marge de 1 006 (2 %) |
| Tronc `DIRECTION` | 34 677 / 35 000 caractères, marge de 323 (moins de 1 %) |
| Troncs des autres modes | ITER 9 110, STANDARD 10 599, SYSTÈME 11 320, LITE 11 530 |
| Ce qui pèse le plus dans le tronc `DIRECTION` | `ACTION/GATE-A` : 8 074 caractères |
| Sortie d'un appel de la recette de rendu | 5 113 caractères, dont un paragraphe de limites de 1 813, répété à chaque appel |
| Export Local | 2,67 Mo, dont `scripts/` 892 k (tests 297 k) et `supports/` 629 k |

## 2. Corrections sans choix

### C-08 — la recette répète ses limites à chaque appel

**Constat vérifié.** Chaque appel affiche le même paragraphe de limites, soit 1 813 caractères sur 5 113. Un agent qui appelle la recette cinq fois dans un run en lit 9 000 pour rien.

**Changement.**
- La sortie par défaut garde une seule ligne : « Limites : fautes objectivables seulement, à l'état et aux largeurs observés ; détail : `--limites` ».
- Le paragraphe complet reste disponible avec `--limites`, et il reste dans le JSON et dans la fiche du parcours.

Gain : environ 1 700 caractères par appel. Aucun statut ne change.

### Avertissement de marge (D-07, effet de bord)

**Constat vérifié.** À chaque run `DIRECTION`, le lecteur affiche à l'agent une consigne destinée au mainteneur : « MARGE FAIBLE — un ajout au tronc se compense par un allègement… ».

**Changement.** L'agent voit seulement la taille du tronc. L'avertissement passe à la validation de structure, que lit le mainteneur.

### B-22 — le coût d'une image générée n'est pas dit au moment de l'accord

**Constat vérifié.**
- La méthode demande trois ou quatre variantes par image générée (`SAVOIR/SOURCE`, « Diriger une génération »).
- L'accord est demandé en tête de `DIRECTION/ASSET-ROUTE`, mais ce coût n'y est pas dit.

**Changement.** Une phrase dans `DIRECTION/ASSET-ROUTE`, servi hors tronc : « L'accord demandé dit le coût : trois ou quatre générations par image retenue. »

### A-13 — quatre paragraphes du noyau d'un seul tenant

**Constat vérifié.** Ce sont les paragraphes « Prise de brief », « Atteindre avant de déclarer », « Échantillonner » et « Trace légère par défaut ». Ils font 1 273 à 2 135 caractères chacun, 7 100 octets en tout (17 % du noyau), avec 12 à 21 propositions enchaînées.

**Changement.** Chacun devient une phrase d'ouverture suivie d'une courte liste.
- **Les mots restent les mêmes.** Aucune phrase n'est ni retirée ni réécrite.
- **Coût :** environ 60 à 100 octets pour les marques de liste, pris sur la marge de 1 006.
- **Contrôle :** les gardes de fidélité et de plancher vérifient que rien ne s'est perdu.

### Bruit de la préparation

**Constat vérifié.** Le journal de préparation contient trois lignes de serveur de test (`"GET /propre.html HTTP/1.1" 200`) et deux fois « journal introuvable : /chemin/inexistant.jsonl ». Ces sorties viennent de cas de test qui échouent exprès, et elles se lisent comme des erreurs.

**Changement.**
- Le serveur de test ne journalise plus ses requêtes.
- Les échecs attendus sont captés par leur test au lieu d'aller sur la sortie d'erreur.

## 3. Corrections avec un choix

### D-07 et A-25 — le tronc `DIRECTION` est au plafond

**Constat vérifié.** `ACTION/GATE-A` est servi en entier dans les troncs LITE, ITER, DIRECTION et SYSTÈME, alors que les lignes de mode ne demandent que ses « contrôles applicables ». Il compte quatre sous-sections :

| Sous-section | Taille | Sert à |
|---|---|---|
| Contrat de portée (bloc `MEDIUM…NEXT-PROOF`) | 1 439 | Déclarer le périmètre quand l'accessibilité ou la conformité est dans le périmètre |
| Familles de méthodes, et provenance d'un verdict accepté | 1 488 | La trace complète et l'acceptation |
| Adéquation des preuves | 735 | La trace complète |
| **Contrôles applicables** (table et profils de surface) | 4 250 | **Chaque run** |

Aucune de ces sous-sections ne porte d'obligation `[REQUIS]`.

| Option | Changement |
|---|---|
| **A (recommandée)** | La sous-section « Contrôles applicables » reçoit un sous-code (`ACTION/GATE-A/CONTROLES`). Les troncs servent ce sous-code seulement. Les trois autres sous-sections restent dans `ACTION/GATE-A`, servies quand leur signal apparaît : trace complète, acceptation demandée, ou conformité dans le périmètre. La ligne de chaque mode le dit. **Gain : environ 3 800 caractères par tronc** dans quatre modes ; la marge du tronc `DIRECTION` passe de 323 à environ 4 100. La garde de chargement vérifie la nouvelle lecture. |
| B | Ne rien changer : le tronc `DIRECTION` reste à 99 %, et tout ajout futur y coûtera un retrait. |

**Critère d'arrêt pour A.** Si une garde de plancher (REQ-01) ou de chargement montre qu'un contenu des trois sous-sections est requis à chaque run, je ne le déplace pas : je vous le montre.

### A-09 — aucune borne de coût

**Constat vérifié.**
- L'absolu 4 définit le budget comme « une suite de jalons, pas un nombre d'appels d'outil ».
- La recette de maintenance interdit qu'un quota d'itérations, de variantes ou d'appels gouverne la qualité.
- Une borne chiffrée contredirait donc une règle du système. Pourtant, le coût d'un run reste invisible pour la personne.

| Option | Changement |
|---|---|
| **A (recommandée)** | Rendre le coût visible sans le plafonner. La ligne `RUN` de la trace annonce les jalons prévus. La réponse finit par une ligne de coût réel : passes de `verifier`, générations d'image, références capturées. La personne voit ce que le run a coûté et peut dire « moins » la prochaine fois. Aucun quota n'est ajouté. |
| B | Des plafonds par mode `[À ADAPTER]`, par exemple deux passes de `verifier` avant de montrer. Cela contredit la règle sur les quotas, qu'il faudrait alors changer. |
| C | Ne rien changer. |

## 4. À écarter, avec raison

**D-08 et F-08 — poids de l'export Local (2,67 Mo).**
- **Un poids sur disque, pas un coût de run.** Ce poids n'entre pas dans le contexte de l'agent : le run lit le noyau, puis son tronc et les routes servies, jamais l'export entier.
- **Les tests servent.** Ils permettent à la personne de vérifier son installation (`validate_all.py` dans l'export Local).
- **La police n'est pas superflue.** `manrope.ttf`, la plus grosse pièce de `supports/`, sert aussi à `parcours.py` en run, pour les étiquettes des planches.
- **Décision antérieure.** Le 14 novembre, vous avez décidé l'export Local « tel quel ».

Retirer les cartes SVG et les générateurs des supports gagnerait environ 200 Ko, soit 8 %, au prix d'un export Local qui ne se valide plus entièrement lui-même.

## 5. Reporté au lot 8

**B-20 — 30 gabarits de formulaire en bloc de texte** (13 k en tout). Ils ne pèsent presque rien et ne sont lus que par leur route ; avec l'option A du § 3, le seul gabarit présent dans un tronc (`MEDIUM…NEXT-PROOF`, dans Gate A) en sort. La question qu'ils posent est celle de leur présentation, homogène ou non : c'est la passe de livraison.

## 6. Vérification prévue

1. Branche `poids`.
2. Tests :
   - la recette, sans `--limites`, n'affiche qu'une ligne de limites ; avec `--limites`, le paragraphe complet ;
   - le lecteur n'affiche plus l'avertissement de marge à l'agent, et la validation le donne au mainteneur ;
   - selon l'option, le tronc sert `ACTION/GATE-A/CONTROLES` et les planchers REQ-01 tiennent ;
   - le noyau garde toutes ses phrases (gardes de fidélité et de plancher) ;
   - le journal de préparation ne contient plus ni requête de serveur de test ni « journal introuvable ».
3. Tailles avant et après : noyau, cinq troncs, sortie de la recette.
4. Validation complète avec navigateur, révision `R2026-11-15i`.

## 7. Ce qu'il faut me dire

« D'accord, options A partout » suffit. Sinon : les corrections du § 2 à écarter, l'option choisie pour le tronc et pour le coût, et si vous préférez alléger quand même l'export Local.

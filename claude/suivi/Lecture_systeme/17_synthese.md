# 17 — Synthèse de la lecture du système (notes 01 à 16)

Synthèse du 19 novembre 2026.

Les preuves viennent de quatre sources :
- les fichiers du paquet `R2026-11-15k` ;
- les journaux des runs 9 à 16 ;
- les verdicts de Junior ;
- des recherches doubles (Exa et WebSearch).

La question de départ : obtenir des rendus de haute qualité plus souvent, avec moins de coût, de temps et de complexité.

## 1. Le diagnostic en une phrase

**Le système sait beaucoup de choses sur le goût, mais il les range là où les agents ne vont pas. Il fait ensuite juger le résultat par l'auteur lui-même.**

## 2. Constats

### Certain (vérifié dans les fichiers et les journaux)

| # | Constat | Où |
|---|---|---|
| C1 | En 8 runs, 20 routes sur 85 ont été lues. Celles qui portent le goût ne l'ont jamais été : FRAME (ordre de composition), READ (« caractère → leviers » avec ses pièges réflexes), CFT-03 (champ calme), CFT-05 (couleur située), CFT-04a (contrepoids à l'objet de preuve), GATE-B (B1b, B3), PIPELINE-DIRECTION (§4, §6). | Notes 09 à 15 |
| C2 | Une route proposée n'est pas une route lue : STATE a été proposée 19 fois et lue 3 fois ; VISUAL_PROOF, proposée 9 fois, n'a jamais été lue. | Notes 14 et 15 |
| C3 | Le noyau pousse vers « objet de preuve » et « mécanisme » (le bloc PREMIER-OBJET), alors que son contrepoids est dans un bloc différé. On retrouve le diagramme comme objet principal aux runs 9, 10, 14 et 16. | Notes 07 et 08 |
| C4 | Le système dit déjà que l'auto-jugement ne vaut pas revue. Une décision d'identité demande un contrepoint externe. Des ancres seulement générées interdisent l'acceptation. En trace légère, la proposition reste exploratoire jusqu'à ce que la personne décide. **La règle 7 est donc cohérente avec le système.** | Notes 15 et 16 |
| C5 | La divergence est bien produite (directions avec probabilités, Verbalized Sampling). La sélection, elle, est faite par l'agent, sur vignette, contre une modale parfois caricaturée (runs 10 et 12) ; la modale de second degré n'a jamais été esquissée. | Notes 08 et 10 |
| C6 | Le gabarit et les marqueurs de vague sont **déjà détectés** (`verifier`, `regard.py`). La détection n'est pas ce qui manque. | Note 14 |
| C7 | Le noyau fait 45 250 octets pour un plafond de 46 000. On ne peut rien y ajouter sans retirer autre chose. | Note 16 |
| C8 | Le 29 octobre, Junior a préféré le rendu **sans** système dans 3 briefs sur 4, et ce rendu sans système coûtait 1,7 fois moins de jetons. | Note 03 |

### Probable (appuyé par la recherche, non mesuré ici)

| # | Constat | Appui |
|---|---|---|
| P1 | Servir deux ou trois lignes au bon moment vaut mieux que renvoyer à une route ou en accumuler dans le noyau. | Vercel (une skill n'est pas chargée dans 56 % des cas) ; IFScale et ManyIFEval (dégradation avec le nombre d'instructions) ; registre consultable à 95 % contre des instructions seules (ACM 2026). |
| P2 | Des relations de forme concrètes (échelle, surface de couleur, masse) orientent mieux qu'adjectifs ou profils textuels. | PRISM (le style textuel des modèles est trop général) ; praticiens des briefs. |
| P3 | La finition et l'anti-slop relèvent le **plancher** (fluidité, beauté classique), pas le **plafond** (caractère, point de vue). | Reber et al. 2004 ; Lavie & Tractinsky 2004. |
| P4 | Un modèle juge mal ses propres rendus : il les préfère, et départage mal deux UI proches. | Panickssery et al. 2024 ; *MLLM as a UI Judge* (environ 59 %) ; Huang et al. et Kamoi et al. sur l'autocorrection. |
| P5 | Choisir entre deux options est plus fiable que noter. | Préprints sur l'esthétique (W de Kendall ≈ 0,8) ; Pérez-Ortiz & Mantiuk. |

### À vérifier

- **V1.** Au premier regard d'un public, le **prototypique et peu complexe** plaît le plus (Tuch 2012). Le système pousse vers l'écart au modal. Laquelle des deux beautés doit primer, selon l'objet ?
- **V2.** Les lignes servies changent-elles vraiment le rendu ? Rien n'est mesuré.
- **V3.** Quelle part du noyau sert la preuve et la trace, et quelle part le goût ?

## 3. Pistes, rangées par coût (aucune n'est intégrée, règle 1)

**Coût faible : des outils, sans toucher au noyau**

| Piste | Ce qu'elle fait | Notes |
|---|---|---|
| A1 | Servir **avant le build** les lignes de direction : ordre de composition, leviers et piège des pôles déclarés (READ), essai isolé (TECH) pour une technique fragile. *Correction : le geste STATE du signal relevé est déjà servi par `verifier` (lot 9b, §0).* | 12 à 14 |
| A2 | Une ligne en trace légère : « choix : auto-jugé / Junior / absent ». | 15 |
| A3 | Ajouter le diagramme comme objet principal aux signaux de convergence (SELECT, ou un marqueur `regard`). | 13 |
| A4 | Relever les mots creux sans conséquence (« premium », « moderne »…) dans la thèse. | 12 |

**Coût moyen : la méthode de run**

| Piste | Ce qu'elle fait | Notes |
|---|---|---|
| B1 | **Jugement par paires** : deux candidats finis, l'ordre est masqué, Junior choisit, puis on révèle. Environ un rendu de plus par run. | 15 |
| B2 | **Carnet de goût** : chaque choix de Junior est noté avec sa raison en une phrase, ce qui donne des spécimens réels plutôt que des règles. | 15 |
| B3 | Des références réelles attachées au registre déclaré, montrées **après** la divergence, contre la fixation. | 12 |
| B4 | Relever la part du noyau par fonction, puis échanger des lignes (le contrepoids CFT-04a contre une redite de preuve). | 08 et 16 |

**Doctrine : décisions de Junior**

- **D1.** Plancher et plafond : un rendu sans tells n'est pas un rendu réussi.
- **D2.** Une structure lisible et prototypique, l'écart porté sur une ou deux dimensions expressives.
- **D3.** La portée de FND-01 (« retenue », « cohérence avant créativité ») pour un objet d'identité.
- **D4.** La règle 7 et un relecteur séparé dans un run : le système l'admet, mais pas sous le nom d'« indépendant ».

## 4. Ce que je recommande

1. **Commencer par A1 et A2**, puis **B1 et B2** dans les prochains runs de la série. Ils ne touchent pas au noyau, coûtent peu et sont réversibles.
2. **Mesurer avant d'étendre (PILOT).**
   - Un même petit objet est fait par deux agents neufs : paquet actuel, ou paquet avec A1.
   - Junior compare les deux rendus **par paires, sans savoir lequel vient de quelle condition**. Ce n'est pas un juge externe à l'aveugle : c'est Junior qui juge sans connaître la condition, donc la règle 7 tient.
   - Trois à cinq objets. La limite est déclarée : c'est un petit échantillon, qui sert à décider de la suite, pas à prouver.
3. **Trancher D1 à D4 avant de rédiger le lot 9b**, puisque ces décisions orientent la rédaction des propositions.

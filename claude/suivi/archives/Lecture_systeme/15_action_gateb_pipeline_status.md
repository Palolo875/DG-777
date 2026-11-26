# 15 — ACTION : GATE-B, PIPELINE-DIRECTION, STATUS

Lecture du 19 novembre 2026. Taille des routes :
- `GATE-B` : 9,5 k caractères ;
- `PIPELINE-DIRECTION` : 12,9 k ;
- `STATUS` : 6,4 k.

## 1. Ce que les runs en ont fait (journaux des runs 9 à 16)

Routes ACTION **lues**, en nombre de lectures :

| Route | Lectures |
|---|---|
| GATE-A/CONTROLES | 8 |
| RUN-DIRECTION | 6 |
| FIRST-RENDER | 6 |
| UI-UX-REALITY | 3 |
| RUN-STANDARD | 2 |
| GATE-B/B2 | 2 |
| RECETTE-RENDU | 2 |
| HANDOFF | 1 |

**Jamais lues** : GATE-B dans son ensemble (B1b sur la paire, B3 sur le regard externe), PIPELINE-DIRECTION et STATUS.

Proposées sans être lues : VISUAL_PROOF (9 fois) et ATELIER-EDITION (1 fois ; son essentiel est déjà dans le noyau).

Les agents lisent ce qui contrôle (accessibilité, premier rendu). Ils ne lisent pas ce qui encadre le jugement et la sélection.

## 2. Ce que disent les trois routes

### GATE-B
- **B1, comparaison relationnelle.** En DIRECTION, le build se compare à l'ancre (la référence) sur les axes concernés : « quel résultat porte mieux l'intention ».
- **B1b, discrimination sur capture.** Une paire de captures réelles : l'initiale, puis une édition réversible d'**une seule** décision principale. Elle est requise pour accorder un V positif en trace complète.
- **B1b fait par l'auteur = auto-comparaison.** Elle « peut soutenir une correction de craft, mais ne satisfait jamais un claim de revue indépendante ». Une décision d'identité qui demande un contrepoint externe « reste avec réserve ou prochaine preuve tant que ce regard n'existe pas ».
- **B3, regard externe.** Une seconde session du même auteur est une « auto-comparaison différée ». Le label « indépendant » exige un relecteur non impliqué ou externe, avec son exposition déclarée (aveugle, code vu, prompt vu…). « L'absence de regard indépendant ne devient jamais une validation implicite. »

### PIPELINE-DIRECTION
- **§1** : sur une décision visuelle ouverte, les positions se comparent **sur image**, avec la modale en référence.
- **§4** : si l'enjeu d'identité est élevé et que **toutes** les ancres sont générées, la calibration vaut `generated_only_reserved`, ce qui **interdit `ACCEPTED`**. Une revue indépendante n'est pas une base de calibration.
- **§6, « Sélectionner contre la facilité »** : « La faisabilité immédiate n'est pas une preuve d'appropriation. »
- **§7** : en trace légère, la proposition reste `EXPLORATORY`, jusqu'à ce que la personne demande de retenir la direction.
- **Passe créative** : « Plus beau, plus premium, ressemble à la référence » ne sont pas des observations.

### STATUS
- **Vocabulaire clos** : états, issues, verdicts V/U/A/T, statut de direction et verdict global.
- **`HELD` ne veut pas dire « beau »** : il signifie fidèle à la direction et approprié. Aucun statut ne dit « au niveau » ou « en dessous du niveau ».

## 3. Recherches à côté (Exa et WebSearch)

| Source | Ce qu'elle dit | Ce que ça touche |
|---|---|---|
| Panickssery, Bowman & Feng, NeurIPS 2024 | Les LLM évaluateurs **reconnaissent et préfèrent leurs propres productions**. La préférence pour soi croît avec la capacité à se reconnaître ; au niveau de chaque exemple, la corrélation va de τ ≈ 0,4 avant ajustement à environ 0,6 après. L'étude porte sur des résumés, pas sur des images. | Elle confirme B1b et B3 : une auto-comparaison ne vaut pas jugement. Un second agent du même modèle reste exposé à ce biais. C'est probable pour les images, mais non mesuré. |
| Comparaison par paires ou notation (préprint arXiv 2605.19776 et autres ; Pérez-Ortiz & Mantiuk) | Les préférences par paires donnent un **accord entre experts plus élevé** que les notes (W de Kendall ≈ 0,8). Les échelles de notation dérivent d'une personne à l'autre. Le choix forcé entre deux options évite cette dérive. | Elle soutient la forme « paire » de B1b, et un jugement de Junior par paires plutôt que par note. Ce sont surtout des préprints. |

## 4. Constats

**Certain**
- Le système dit déjà, dans GATE-B et PIPELINE-DIRECTION, tout ce que la recherche confirme :
  - l'auto-jugement ne vaut pas revue ;
  - une décision d'identité demande un contrepoint externe ;
  - un enjeu d'identité élevé avec des ancres seulement générées interdit l'acceptation ;
  - « sélectionner contre la facilité ».
- Aucun run n'a lu ces passages.
- En trace légère, la proposition reste `EXPLORATORY` jusqu'à la décision de la personne. **La règle 7 (Junior juge) est donc cohérente avec le système**, qui réserve l'acceptation à une décision humaine.

**Probable**
- En trace légère, rien ne rend visible que le choix a été **auto-jugé**. La réserve de B3 vit en trace complète. La proposition livrée paraît donc tranchée, alors que le système lui-même la tient pour exploratoire.

**Réponse partielle à la question ouverte (règle 7 et relecteur séparé dans un run)**
- Le système l'admet (B3, « Regard séparé » de l'atelier), mais il doit être nommé selon sa relation réelle.
- Un agent du même modèle qui ne voit que les images est « impliqué » ou d'une relation incertaine. Il ne peut pas être appelé « indépendant ».
- La recherche sur la préférence pour soi va dans ce sens.
- La décision reste à Junior.

## 5. Pistes (non intégrées, règle 1)

1. **Une ligne de regard en trace légère** : « choix : auto-jugé / Junior / absent ». C'est la réserve de B3 rendue visible, sans trace complète. Coût minimal.
2. **Jugement de Junior par paires.** Le run livre deux candidats finis : la direction retenue et la meilleure alternative, toutes deux au même niveau de finition, dans un ordre masqué. Junior choisit, puis on révèle. Cela s'appuie sur B1b, sur la recherche (accord plus élevé par paires) et sur la règle 7. Le coût est d'environ un rendu de plus par run.
3. **Carnet de goût.** Chaque choix de Junior entre deux candidats est noté avec sa raison en une phrase. Au bout de plusieurs runs, on obtient des spécimens réels de ce qu'il préfère, dans l'esprit de PRISM (note 12), plutôt que des règles.
4. **Servir §6, « sélectionner contre la facilité », et la phrase de §4 sur les ancres générées** dans la fiche `verifier`, quand l'enjeu d'identité est élevé.

## Sources
- Panickssery et al. 2024 : https://arxiv.org/abs/2404.13076
- Panickssery et al. 2024 (actes NeurIPS) : https://proceedings.neurips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html
- Préférences ou notes en esthétique (préprint) : https://arxiv.org/pdf/2605.19776
- Pérez-Ortiz & Mantiuk, guide de la comparaison par paires : https://arxiv.org/pdf/1712.03686
- Évaluation perceptuelle du transfert de style (choix forcé) : https://arxiv.org/pdf/2610.10003

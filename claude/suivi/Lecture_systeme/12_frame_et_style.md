# 12 — SAVOIR/FRAME et SAVOIR/STYLE

Lecture du 19 novembre 2026. Routes lues avec `read_route.py` :
- `SAVOIR/FRAME`, dont le propriétaire est `design/savoir/fondements.md`, 12,1 k caractères ;
- `SAVOIR/STYLE`, 12,5 k caractères.

## 1. Ce que les runs en ont fait (vérifié dans les journaux)

- **FRAME.** Aucun run ne l'a lue, et aucun outil ne l'a proposée (`grep` sur les journaux des runs 9 à 16).
- **STYLE.** Elle a été proposée une seule fois (run 11, `read_route --trouver graphique`) et n'a jamais été lue.
- **La porte d'entrée existe pourtant.** Gate C, critère C3 (« Composition intentionnelle »), renvoie à `SAVOIR/FRAME/COMPOSITION`. Mais en trace légère, Gate C n'écrit pas de verdict, et aucun run n'a suivi ce renvoi.

## 2. FRAME : ce qu'elle contient

| Bloc | Contenu | Remarque |
|---|---|---|
| FND-01 | Trois lois : intention avant décoration, retenue avant accumulation, cohérence systémique avant créativité locale. Le défaut raisonnable est le retrait. | L'ordre est conservateur ; il est écrit pour une interface produit. |
| Premium perçu | Relation entre clarté, cohérence, précision, singularité maîtrisée, confiance et désirabilité. Le texte précise que ce n'est pas un score. | Il interdit de déduire le premium du sombre, du minimal ou de la grande typographie : c'est juste. |
| Comprendre, ouvrir, converger, prouver | « La sélection fait partie du craft. » Chaque référence est annotée par la décision qu'elle peut modifier. | C'est la bonne méthode, mais elle reste invisible tant que la route n'est pas lue. |
| COMPOSITION | Ordre de construction : intention → tension → foyer → masse → rythme → matière et type → contenu réel → états → résolution → retenue. | C'est la grammaire positive qui manquait dans les runs, alors qu'elle existe. |
| Pluralité esthétique | Aucun canon unique. Sur un enjeu identitaire, chercher un contrepoint (utilisateur, expert, autre designer). | Elle appuie la piste d'un choix externe. |
| FND-02 | Format de compromis : décision, risque résiduel, réversibilité, owner. | Utile. |
| FND-03 | Cadrage (qui, pourquoi, quelle décision, quelle preuve, quelles contraintes) et nature des hypothèses. | Il recoupe largement le noyau, qui en reprend la ligne. |

## 3. STYLE : ce qu'elle contient

- **Règle de sélection.** Un profil n'est retenu que s'il change une décision. Aucun profil par défaut. Le registre se compose en DIRECTION : une base et un modificateur, pris dans deux dimensions différentes.
- **Taxonomie en sept dimensions.** Composition, matière, représentation, époque, densité, interaction, voix. Elles sont reliées à dix des douze axes de CFT-02.
- **Huit profils internes.** RAW_BRUTALISM, EDITORIAL_PRECISION, PICTORIAL_UTILITY, QUIET_SYSTEM, MAXIMAL_EXPRESSION, DIGITAL_MEMORY, TACTILE_VOLUME, COLLAGE_ASSEMBLY. Chacun a une intention, une expression et des contre-indications.
- **Profil externe.** Un profil observé dans une référence réelle peut être préféré au catalogue interne. Le catalogue n'est « ni exhaustif ni prioritaire ».
- **Test de style.** On masque les couleurs, l'image et le logo. Si la différence disparaît, il n'y avait qu'une étiquette.
- **Vocabulaire à rendre observable.** « Premium », « moderne », « beau », « original »… ne valent jamais décision à eux seuls.
- **Coût en trace.** PROFILE-DECISION, DIALS, COUNTERINDICATION, EVIDENCE, puis leur correspondance avec les champs d'ACTION. C'est lourd pour un petit objet.

## 4. Recherches à côté (Exa et WebSearch)

| Source | Ce qu'elle dit | Ce que ça touche |
|---|---|---|
| PRISM (arXiv 2601.11747) | Le savoir de style « pré-entraîné » des VLM est trop général. Exemple : ils associent le minimalisme à l'abstrait, alors que les designers parlent de formes et de couleurs. Un savoir de style tiré de vrais designs regroupés par style l'emporte : rang 1,49 sur 5 en fidélité, préféré pour sa diversité par 66 % de 30 designers. Demander directement au LLM des variantes de style donne la pire fidélité (0,744). | Les profils STYLE sont du texte d'intention, sans spécimen. Probable : ils pèsent moins qu'un savoir ancré dans des exemples réels. Le support est un jeu Crello (posters), pas du HTML. |
| Design-system compliance, ACM 2026 (dl.acm.org/doi/10.1145/3772363.3798616) | Pour respecter un design system, un registre consultable (95 %) bat le contexte (85 %) et les instructions seules (plus bas). | Un savoir servi au bon moment et interrogeable vaut mieux qu'une règle à lire. Je n'ai lu que le résumé. |
| MM-WebAgent (arXiv 2604.15309) | Un plan global (sections, ordre, style de page), puis des plans locaux, puis une réflexion sur capture. Sans plan local, le score passe de 0,75 à 0,69. | Une génération par étapes ordonnées aide. Cela soutient l'ordre de COMPOSITION comme procédure, mais les métriques sont notées par un MLLM : preuve faible. |
| Brief2Design (arXiv 2604.11019) | Six designers interrogés : structurer l'ambigu, explorer élément par élément, puis recombiner. | Cela recoupe « comprendre, ouvrir, converger ». C'est qualitatif. |
| Interrogating Design Homogenization in Web Vibe Coding (Microsoft Research, arXiv 2603.13036, mars 2026) | Prompter un LLM sur un but esthétique tend à réduire la diversité vers un style dominant. Les auteurs proposent une « friction productive ». | Confirme le risque générique déjà noté (Doshi & Hauser). |
| Pratique des briefs (Studio Klara, Metadigital, Business of Home) ; papier d'Aalborg sur le langage des briefs | Les adjectifs comme « moderne » ou « premium » ne disent rien. Mieux vaut des échelles (traditionnel ↔ moderne) et des références avec leur raison. La recherche académique ne tranche pas sur ce qu'est un bon brief. | La table « vocabulaire à rendre observable » et les dials de STYLE vont dans le bon sens. Ce sont des sources de praticiens, pas des études. |

## 5. Constats

**Certain**
- FRAME/COMPOSITION, la sélection comme craft et la pluralité esthétique sont écrites, et n'ont jamais été lues en run.
- STYLE dit elle-même que le catalogue n'est pas prioritaire et qu'un profil observé dans une vraie référence peut être préféré.

**Probable**
- L'absence de grammaire de composition chargée contribue aux rendus « gadget » et « génériques ». Le noyau donne la chaîne « promesse → objet de preuve → geste », mais pas l'ordre « tension → foyer → masse → rythme ».
- Les profils STYLE, s'ils étaient lus, aideraient peu au goût. Ce sont des descriptions textuelles, et la recherche (PRISM) montre que le style textuel des modèles reste générique sans données réelles.

**Hypothèse à vérifier**
- La loi 3 de FND-01 (« cohérence systémique avant créativité locale », retrait par défaut) est pensée pour une interface produit. Sur un petit objet esthétique (billet, affiche), elle pourrait pousser vers la retenue sage. Aucun run ne l'a lue, donc elle n'a pas pu jouer ; c'est une question de rédaction, pas une cause observée.

## 6. Pistes (non intégrées, règle 1)

1. **Servir l'ordre de composition sans lecture de route.** Une ligne dans la fiche `verifier`, ou dans le noyau à la place d'une ligne PREMIER-OBJET : « foyer, masse, rythme, puis matière ». C'est le coût le plus faible.
2. **Spécimens plutôt que profils textuels.** Associer à chaque profil, ou mieux au registre déclaré, deux ou trois références réelles observées, avec la décision qu'elles changent (format déjà prévu par FRAME). Elles seraient montrées **après** la divergence, pour limiter la fixation (Jansson & Smith).
3. **Alléger la trace STYLE en légère.** Une ligne « registre, ce qu'il change, contre-indication » suffit. Les quatre champs et leur correspondance avec ACTION sont réservés à la trace complète.
4. **Contrôle outillé du vocabulaire.** `verifier` relève dans la trace et la thèse les mots « premium », « moderne », « élégant »… sans conséquence nommée. C'est peu coûteux et mesurable.
5. **Question pour Junior.** L'ordre des lois FND-01 vaut-il pour un objet d'identité, ou faut-il une phrase de portée (« sur une surface DIRECTION, la présence prime sur la retenue tant que la lecture tient ») ?

## Sources
- PRISM : https://arxiv.org/html/2601.11747
- Design System-Compliant UI Generation with LLM Agents : https://dl.acm.org/doi/pdf/10.1145/3772363.3798616
- MM-WebAgent : https://arxiv.org/abs/2604.15309
- Brief2Design : https://arxiv.org/abs/2604.11019
- Interrogating Design Homogenization in Web Vibe Coding : https://arxiv.org/abs/2603.13036
- UIDEC (contraintes et diversité) : https://arxiv.org/html/2501.18748v1
- ControlGUI (diversité perçue, plus avec wireframes et flux qu'avec le prompt seul) : https://doi.org/10.48550/arxiv.2502.03330
- Studio Klara, brief : https://kaizen-demo-klara.pages.dev/blog/the-brief-that-actually-works
- Business of Home : https://businessofhome.com/articles/the-client-dictionary-decoding-requests-into-actionable-design-steps
- Aalborg, niveaux d'abstraction des briefs : https://vbn.aau.dk/files/535716738/Decoding_design_briefs_The_role_of_abstraction_levels_in_textual.pdf

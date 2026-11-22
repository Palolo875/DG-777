# Lot 12 — Propositions : la documentation de publication

Rédigé le 22 novembre 2026. Base : `R2026-11-15u` (`master` `3705d62`). Aucun run. Règle 1 : rien n'est intégré sans décision ; « D'accord » vaut pour les options A partout.

## 0. Mesure (révision `u`) : le plan surestimait le chantier

| Critère du plan (§ 1) | Mesure aujourd'hui | Écart |
|---|---|---|
| Toute page à deux clics au plus du README | **63 pages sur 63** : 23 à un clic, 39 à deux | Tenu ; aucune garde ne le protège |
| Pas de code dans les pages pour les personnes | 14 codes : README 3, `2-comprendre` 5, `3-maitriser` 6 ; `1-utiliser` 0 | Petit |
| Licence, journal des changements, citation, contribution | **Aucun** de ces fichiers | À faire, selon D4 et D7 |
| Archive « skill » sans atelier (A4) | Deux archives : GitHub (151 fichiers) et Local (145). L'atelier fait **24 fichiers** (tests, validateurs, `maintenance/README.md` et `evolution.md`, compilation, journal, générateurs des supports) | **35 renvois** depuis 15 pages de la skill vers ces fichiers |
| Route d'instrumentation sortie de la skill (A6) | `DIRECTION/LECTURE-INSTRUMENTEE` : 1 300 caractères, lue seulement sur signal, une ligne d'index | Voir E7 |
| Référence générée depuis les sources | Aucune. Le glossaire (25 900 octets) est écrit à la main | À faire |
| Le README décrit l'architecture finale | Il ne dit rien du noyau-index (lot 11) ni du mode « sans outils » | Petit |
| Schéma public | Trois cartes (`supports/`) : responsabilités, parcours, boucle. Aucune ne montre **comment l'agent lit** | Une carte manque |
| Fait périmé | Glossaire, « Regard séparé » : « une critique faite par un second agent », sans « facultatif » | 1 ligne |

**Conséquence.** La réorganisation de `guides/` en quatre types (`docs/tutoriel`, `docs/guides/`…) prévue au plan n'est pas utile : la navigation tient déjà, et déplacer 63 pages casserait des liens pour un gain faible. Je propose de **compléter**, pas de réorganiser.

## 1. Décisions à prendre d'abord (elles bloquent E5)

| # | Décision | Options | Ma recommandation |
|---|---|---|---|
| D4 | Licence | MIT (code) et CC BY 4.0 (textes) / Apache 2.0 et CC BY 4.0 / autre | **MIT et CC BY 4.0** : les plus connues, compatibles, qui demandent seulement la citation |
| D5 | Langue | Français seul / français et anglais partout / français, avec un README en anglais | **Français, avec un `README.en.md`** court. Traduire toutes les pages (≈ 790 000 octets de Markdown) coûterait plusieurs sessions sans run pour le vérifier |
| D6 | Nom | Garder « Design Governance » / un nom qui dit la direction artistique | **Garder**, avec un sous-titre : « direction artistique et preuve pour agents de design » |
| D7 | Numérotation publique | `R…` seul / `V1.1` publique datée, `R…` en interne | **`V1.1`**, datée, au moment de la livraison du lot 12 ; `R…` reste la référence interne |

## 2. Propositions (A recommandée partout)

### E1 — Le README à jour de l'architecture
- **A.** Ajouter « Comment l'agent lit » en 5 lignes (noyau d'invariants et index des routes, tronc du mode, routes au signal, outils, sans outils), le profil sans exécution, et une ligne « Ce que coûte un run » avec la mesure du PILOT **datée** et le renvoi au lot 13.
  - La **démonstration** (un brief, un rendu, la trace) attend le lot 13 : un rendu des runs passés porterait des noms de briefs (garde PRO-01).
- **B.** Seulement l'architecture, sans la ligne de coût.

### E2 — Une référence générée depuis les sources
- **A.** `guides/reference.md`, **produit par un script** : les commandes et leurs options (aide des 6 outils), les 85 routes avec leur rôle (sommaire de `read_route`), les statuts. Garde **DOC-03** : la page est identique à sa régénération (mutation rouge). Le glossaire reste écrit à la main.
- **B.** Pas de référence ; le README renvoie aux commandes `--help`.

### E3 — Des mots à la place des codes, et un fait corrigé
- **A.** Les 14 codes du README et des guides 2 et 3 deviennent des mots ; ils restent permis dans le glossaire, la référence et les pages pour l'agent. Garde **DOC-01** sur ces pages. « Regard séparé » devient « facultatif, si l'environnement le permet ».
- **B.** Corriger sans garde.

### E4 — Garde de profondeur des liens
- **A.** **DOC-02** : toute page du paquet à deux clics au plus du README (vrai aujourd'hui ; la garde le protège). Mutation rouge.
- **B.** Rien.

### E5 — Les fichiers du projet (après D4 et D7)
- **A.** `LICENSE` (selon D4), `CHANGELOG.md` ouvert à `V1.1` (les notes de version actuelles y passent), `CITATION.cff`, `CONTRIBUTING.md` court qui renvoie à « Ajouter ou modifier une règle ».
- **B.** Seulement `LICENSE`.

### E6 — L'archive « skill » sans l'atelier (A4)
- **A.** Une troisième archive, `Design_Governance_V1_SKILL.zip` : l'archive Local moins les 24 fichiers d'atelier. Les 35 renvois deviennent, dans cette archive seulement, des liens vers le dépôt public (ou une phrase sans lien pour un nom de script). La validation de l'archive « skill » vérifie qu'aucun lien n'est cassé et que les outils de la boucle s'exécutent. `maintenance/versions.md` (la fiche de version) reste dans la skill.
- **B.** Reporter après le lot 13.

### E7 — La route d'instrumentation (A6)
- **A (mon avis : ne pas la déplacer).** Depuis le lot 11, elle ne coûte qu'une ligne d'index et n'est lue que sur son signal. Elle sert aussi à un utilisateur qui audite ses runs. La déplacer casserait l'index complet (garde IDX-01) pour un gain nul.
- **B.** La déplacer vers `maintenance/`, comme prévu au plan.

### E8 — Un guide « sans navigateur ni exécution »
- **A.** Une section courte dans `guides/1-utiliser.md` : ce qui marche sans outils (pour un agent, et pour une personne qui lit le système sans agent), et ce qui devient « non vérifié ».
- **B.** Rien : le passage du noyau suffit.

### E9 — Une carte « Comment l'agent lit »
- **A.** Une quatrième carte dans `supports/`, produite par le générateur existant, en clair et en sombre : noyau (invariants et index), tronc, routes, outils. Elle passe les contrôles des supports.
- **B.** Rien ; la section du README (E1) suffit.

## 3. Ordre proposé (chaque sous-lot est livrable seul)

1. **12a** : E3, E4, E1, E8, et E7 si A. Ne dépend d'aucune décision. Révision `v`.
2. **12b** : E2 (référence générée) et E9 (carte). Révision `w`.
3. **12c** : E6 (archive « skill »). Révision `x`.
4. **12d** : E5 (fichiers du projet), après D4 à D7 ; passage à `V1.1` si D7 A.

## 4. Ce que le lot ne prouvera pas

- Qu'une personne ou une entreprise comprend le système en deux minutes : il faut une lecture extérieure. Junior relit ; un lecteur neuf serait mieux.
- Que l'archive « skill » marche chez un hôte réel : un run (lot 13) l'installera depuis elle.

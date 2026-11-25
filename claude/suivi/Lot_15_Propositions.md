# Lot 15 — Propositions : faire

Rédigé le 25 novembre 2026. Base : V1.2.0 (`R2026-11-25c`, `master` `2b52bf8`). Aucun run. Règle 1 : rien n'est intégré sans décision ; « D'accord » vaut pour les options A partout.

## 0. Mesure (ce qui existe déjà, vérifié dans les fichiers)

| Sujet | Existant | Constat des runs |
|---|---|---|
| **Recettes** | 5 recettes dans `references/recettes.md` (10 321 octets), servies par `parcours.py recette` : graphique, grand chiffre, moment orchestré, focus, contrôles. Forme : problème, quand / pas quand, procédé, code, pièges. | Quand une recette existe, l'agent s'en sert (widget : 3 appels). Sinon il code de mémoire : émail (19x), graisse animée et curseur (21y), réponse par courriel et ajout à l'agenda (19x). |
| **Matière** | `SAVOIR/SOURCE` (« Construire une atmosphère »), planéité choisie contre l'aplat, `parcours.py references` pour chercher des images ouvertes. | 19x : émail codé de mémoire, jugé « artificiel » ; aucune photo d'émail regardée. |
| **Inventaire du sujet** | **Existe déjà** : `SAVOIR/CRAFT/CFT-01` (inventaire de ce qui appartient au sujet, phrase d'idée, test du concurrent) ; la divergence tire ses pistes « d'une piste différente du sujet », dont le « deuxième attribut » (le plus saillant étant déjà modal). | Convergence 3 sur 3 sur les deux briefs du PILOT, **même quand l'inventaire est lu** (19x l'a ouvert). L'inventaire est le même pour tous les agents : le fait le plus évident (le céladon pour la céramique) gagne partout. |
| **Rareté** | Cinq directions avec leur probabilité estimée. | Estimations fausses : 7 à 8 % pour des idées produites 3 fois sur 3. |
| **Modale** | « Une esquisse ne l'emporte que si elle bat la modale à la vue » ; « un choix convergent reste valide s'il tient sur la planche ». | 19x : la police à empattements, jugée « modale », est écartée ; Junior la préférait. |

Noyau : 31 699 octets sur 33 000 (marge 1 301).

## 1. Sous-lot 15a — Les recettes (le levier le plus sûr)

### F — Cinq recettes nouvelles, tirées des besoins réels des runs
- **A (recommandée).** Même forme que les recettes existantes (problème, quand / pas quand, procédé, code court, pièges), sans style imposé :
  1. **matière codée** (grain, papier, émail, verre, lumière) : un procédé par famille, et le piège du dégradé trop lisse et du reflet plaqué ;
  2. **police variable animée** (balayage de graisse, curseur, mouvement réduit) ;
  3. **réponse par courriel préremplie** (lien `mailto:` composé, champs, erreur et confirmation) ;
  4. **ajout à l'agenda** (fichier `.ics` produit dans la page, fuseau horaire) ;
  5. **objet mis en scène** (cadre, fond, ombre portée crédible, recadrage, fond perdu).
  - Garde : chaque recette a ses rubriques et un code qui passe la recette de rendu (test existant sur les recettes, étendu).
- **B.** Seulement les recettes 1 et 5 (matière et mise en scène), les plus liées à la qualité perçue.

### E et D — La matière observée avant d'être codée
- **A (recommandée).** Dans la recette « matière codée » et l'atelier : avant de coder une matière, en regarder deux photos réelles (`parcours.py references`) ; après, une question à l'atelier : « la matière paraît-elle observée ou dessinée ? » (D), en la comparant à la photo, à la même échelle.
- **B.** Un outil dédié (`parcours.py matiere`) qui assemble photo et rendu sur une planche. Plus de code ; je ne le recommande pas avant un run.

## 2. Sous-lot 15b — L'idée propre au sujet

### I et M — L'idée tirée d'un fait de deuxième rang
- **A (recommandée).** L'inventaire existe ; ce qui manque, c'est d'écarter le fait que tout agent prendrait. Après l'inventaire, l'agent **classe les faits du plus évident au moins évident**, et la direction gardée vient d'un fait **de deuxième rang ou au-delà**, sauf si le premier gagne sur la planche. C'est la règle du « deuxième attribut », étendue à tout l'inventaire. Quand le brief est pauvre (M), la ligne d'inventaire s'écrit dans la trace, pour que la personne puisse réorienter.
- **B.** Rien de plus que l'existant.

### J — La rareté
- **A (recommandée).** Garder les probabilités, qui aident à diversifier les propositions, mais **cesser de les traiter comme une mesure** : la trace dit de quel rang de l'inventaire vient l'idée, plutôt que son pourcentage.
- **B.** Retirer les probabilités.

### Q1-2 — Plaider pour la modale
- **A (recommandée).** Avant d'écarter la modale, l'agent écrit en une ligne ce qu'elle ferait de mieux **pour ce sujet** ; elle n'est écartée que si elle perd sur la planche, ainsi défendue. Vaut aussi pour une voix typographique jugée « modale ».
- **B.** Rien.

## 3. Coût et budget

- Recettes : environ 10 000 octets de plus dans `references/recettes.md` ; rien au noyau (la ligne des recettes existe).
- Lignes 15b : environ 350 octets au noyau (sur 1 301 de marge) ; le détail va dans `CFT-01` et `DIRECTION/DIVERGENCE`.
- Coût par run : une recette lue au lieu d'un tâtonnement ; probablement moins de tours. Non mesuré.

## 4. Gardes et tests (mutation rouge, échec nommé)

- Recettes : chacune a ses rubriques ; son code passe la recette de rendu (extension du test existant des recettes).
- 15b : formulations protégées au noyau (CORE-01) ; `trace` signale une ligne de modal sans rang d'inventaire quand l'idée est ouverte (signal, pas refus).

## 5. Ce que le lot ne prouvera pas

- Que l'exécution s'améliore, ni que la convergence recule : seule la campagne de runs le dira.
- **Limite connue** : sans contenu réel du client, des agents du même modèle partagent le même inventaire. Le deuxième rang réduit la convergence ; il ne la supprime pas. Le vrai remède reste le contenu réel, que la prise de brief demande déjà.

## 6. Ordre proposé

1. **15a** (recettes et matière) : révision `R2026-11-25d`.
2. **15b** (idée propre au sujet, rareté, modale) : révision suivante ; publication V1.3.0 à la fin du lot.
3. Puis la campagne de runs, sur décision de Junior, avec les pages HTML jointes sous des noms neutres.

# Carte des déclencheurs — Design Governance V1, `R2026-11-15c`

15 novembre 2026. Document hors du paquet, calculé depuis les fichiers : la ligne de chaque mode (`DIRECTION/CHARGE`), les troncs, la table des signaux du noyau, les blocs compilés et les renvois entre routes. Il sert à concevoir le run de contrôle (lot 9) : pour qu'une route soit éprouvée, il faut un brief qui fasse apparaître son déclencheur.

## Ce que la carte montre

- **Les 84 routes ont toutes un chemin d’arrivée.** 14 sont lues à chaque run d’au moins un mode (tronc), 41 s’ouvrent sur un signal (ligne d’un mode ou table des signaux du noyau), 29 seulement par le renvoi d’une autre route. Aucune n’est atteignable par la seule recherche.
- **Les routes jamais lues par les runs de la phase 6 (constat B-01) sont presque toutes « sur signal » ou « par renvoi ».** Les quatre briefs ne faisaient pas apparaître leurs déclencheurs (structure ouverte, profil de style, contexte d’accessibilité, couleur…). Leur non-lecture ne dit donc pas qu’elles sont de trop ; elle dit qu’elles n’ont pas été éprouvées. C’est votre remarque du 14 novembre, désormais mesurée.
- **Ce que la carte ne dit pas** : si un agent suit le signal quand il apparaît. Seul un run ciblé le montre.

## Routes jamais lues en phase 6, et ce qui les ouvre

| Route | Comment on y arrive | Déclencheur |
|---|---|---|
| `BIBLIOTHEQUE/SUPPORT` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/COMPAT, BIBLIOTHEQUE/SCENE, BIBLIOTHEQUE/SELECT |
| `BIBLIOTHEQUE/GRID` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/COMPAT, BIBLIOTHEQUE/SELECT |
| `BIBLIOTHEQUE/SCENE` | sur signal | signal : Asset, motion, scène ou type spécifique à construire |
| `BIBLIOTHEQUE/OBJECT` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/COMPAT, BIBLIOTHEQUE/SCENE, BIBLIOTHEQUE/SELECT, SAVOIR/IDENTITY |
| `BIBLIOTHEQUE/MICRO` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/COMPAT, BIBLIOTHEQUE/READ, BIBLIOTHEQUE/SCENE, BIBLIOTHEQUE/SELECT |
| `BIBLIOTHEQUE/MODIFIER` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/SELECT, SAVOIR/SOURCE |
| `BIBLIOTHEQUE/COMPONENTS` | sur signal | ligne SYSTÈME ; signal : Token, composant partagé, theming ou blast radius |
| `BIBLIOTHEQUE/COMPAT` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/SELECT |
| `BIBLIOTHEQUE/READ` | sur signal | signal : Structure ouverte |
| `BIBLIOTHEQUE/TENSION` | sur signal | signal : Structure ouverte |
| `BIBLIOTHEQUE/SIGNATURE` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/READ |
| `BIBLIOTHEQUE/SELECT` | sur signal | ligne STANDARD, DIRECTION ; signal : Structure ouverte ; Asset, motion, scène ou type spécifique à construire |
| `BIBLIOTHEQUE/AVANT-SELECTION` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/SELECT |
| `BIBLIOTHEQUE/DERIVE` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/CONTRACTS, BIBLIOTHEQUE/SCENE, BIBLIOTHEQUE/SELECT |
| `SAVOIR/CONTEXT` | sur signal | signal : Cadrage ambigu ; contexte critique, responsive, performance ou mouvem… |
| `SAVOIR/FRAME` | sur signal | ligne STANDARD, DIRECTION ; signal : Composition nouvelle : ordre intention → tension → foyer → masse → ry… ; Cadrage ambigu ; contexte critique, responsive, performance ou mouvem… |
| `SAVOIR/CRAFT` | sur signal | ligne DIRECTION ; signal : Sujet réel et idée encore ouverte ; Plus de deux registres expressifs, ou deux sans lien au produit (sign… ; Motif générique ou réflexe ; Composition nouvelle : ordre intention → tension → foyer → masse → ry… ; Contenu, titre, ordre des sections ou nom des actions ; Couleur, encodage d’une donnée (polarité, grandeur, ordre) ; texte su… ; Revue créative après la première scène et après la repasse ; varier u… ; Détail final susceptible de modifier le caractère, l’état, la hiérarc… |
| `SAVOIR/STYLE` | sur signal | ligne DIRECTION ; signal : Profil de style à retenir, famille de design, technique ou médium |
| `SAVOIR/TECH` | sur signal | signal : Profil de style à retenir, famille de design, technique ou médium ; Technique à coder sans méthode sûre (matière, texte sur image, graphi… |
| `BIBLIOTHEQUE/CONTRACTS` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/COMPAT, BIBLIOTHEQUE/DERIVE, BIBLIOTHEQUE/EVOLUTION, BIBLIOTHEQUE/SELECT |
| `BIBLIOTHEQUE/GATE` | par renvoi d’une autre route | renvoyée par ACTION/GATE-C, BIBLIOTHEQUE/COMPAT, BIBLIOTHEQUE/SUPPORT |
| `BIBLIOTHEQUE/EVOLUTION` | par renvoi d’une autre route | renvoyée par BIBLIOTHEQUE/DERIVE, BIBLIOTHEQUE/MICRO, SAVOIR/CRAFT |

## Les 84 routes

| Route | Fichier | Taille | Tronc | Ligne de mode | Table des signaux | Blocs au noyau | Renvois reçus |
|---|---|---|---|---|---|---|---|
| `DIRECTION/START` | `agent/chemins.md` | 9.0 k | — | LITE, ITER | — | — | 18 |
| `DIRECTION/CHARGE` | `agent/chemins.md` | 14.6 k | — | — | Détail final susceptible de modifier le caractère, l’état, la hiérarc… | CHARGE-DETAILS, CHARGE-FIN, CHARGE-REGLE, CHARGE-TROUVER | 6 |
| `DIRECTION/FAST-PATH` | `agent/chemins.md` | 0.9 k | — | — | — | — | 1 |
| `ACTION/RUN` | `agent/chemins.md` | 0.4 k | — | LITE, ITER, STANDARD, DIRECTION, SYSTÈME | Token, composant partagé, theming ou blast radius | — | 0 |
| `ACTION/RUN-LITE` | `agent/chemins.md` | 0.8 k | LITE | — | — | — | 3 |
| `ACTION/RUN-ITER` | `agent/chemins.md` | 1.0 k | ITER | — | — | — | 4 |
| `ACTION/RUN-STANDARD` | `agent/chemins.md` | 1.3 k | STANDARD | — | — | — | 3 |
| `ACTION/RUN-DIRECTION` | `agent/chemins.md` | 2.0 k | DIRECTION | — | — | — | 3 |
| `ACTION/RUN-SYSTEM` | `agent/chemins.md` | 1.0 k | SYSTÈME | — | Token, composant partagé, theming ou blast radius | — | 6 |
| `ACTION/FAST-PATH` | `agent/chemins.md` | 1.1 k | LITE | — | — | — | 4 |
| `ACTION/ROUTING` | `agent/chemins.md` | 0.8 k | — | DIRECTION | — | — | 1 |
| `SAVOIR/READ` | `agent/chemins.md` | 3.5 k | — | — | — | — | 1 |
| `SAVOIR/JUGEMENT-COURT` | `agent/chemins.md` | 0.3 k | — | — | — | — | 1 |
| `SAVOIR/ROUTING` | `agent/chemins.md` | 0.3 k | — | — | — | — | 1 |
| `ACTION/HANDOFF` | `agent/repondre.md` | 7.6 k | — | STANDARD, DIRECTION | Réponse visible, trace complète, contrats écrits, checkpoint et accep… | — | 11 |
| `DIRECTION/DOUBLE-LOOP` | `design/direction/boucle.md` | 8.9 k | — | DIRECTION | Recette de rendu : options, états, captures, comparaison ; preuve d’é… ; Après observation : défaut local, craft, direction faible, risque cha… | BOUCLE | 5 |
| `DIRECTION/EXTERNAL-START` | `design/direction/cadrer.md` | 5.3 k | — | DIRECTION | Brief vague ; prise de brief, contenus marqués, données d’exemple | BRIEF | 4 |
| `DIRECTION/DOMAIN-FRAME` | `design/direction/cadrer.md` | 2.7 k | — | STANDARD, DIRECTION | — | — | 1 |
| `DIRECTION/CREATIVE-BOOT` | `design/direction/diriger.md` | 5.5 k | DIRECTION | — | — | — | 5 |
| `DIRECTION/VISUAL_TARGET` | `design/direction/diriger.md` | 5.9 k | DIRECTION | — | — | — | 17 |
| `DIRECTION/CADRES` | `design/direction/diriger.md` | 2.7 k | — | — | — | — | 3 |
| `DIRECTION/ASSET-ROUTE` | `design/direction/diriger.md` | 2.9 k | — | — | Ressource à choisir (bibliothèque, police, icônes, texture, données, … | — | 3 |
| `DIRECTION/ANCHOR-RESERVE` | `design/direction/diriger.md` | 0.8 k | — | DIRECTION | — | — | 2 |
| `DIRECTION/DIRECTION-ATELIER` | `design/direction/diriger.md` | 5.3 k | — | DIRECTION | — | VER-AUDIENCE | 3 |
| `DIRECTION/DIVERGENCE` | `design/direction/diriger.md` | 9.2 k | — | — | — | DIR-DECLARATION, DIR-LEVIERS | 6 |
| `DIRECTION/FIRST-OBJECT` | `design/direction/premier-objet.md` | 6.3 k | DIRECTION | — | Brief vague ; prise de brief, contenus marqués, données d’exemple | PREMIER-OBJET | 5 |
| `DIRECTION/GROUNDING` | `design/direction/premier-objet.md` | 0.7 k | — | — | Fait, claim, terme métier, droit ou capacité réelle qui peut modifier… | — | 2 |
| `DIRECTION/REUSE` | `design/direction/premier-objet.md` | 2.1 k | — | — | Ancien projet, préférence ou composant qui peut orienter le brief ; r… | — | 3 |
| `DIRECTION/STANDARD` | `design/direction/standard.md` | 18.4 k | — | — | Direction identitaire à accepter ; ancre | ABSOLUS, POSTURE | 3 |
| `BIBLIOTHEQUE/SUPPORT` | `design/formes/catalogue.md` | 3.1 k | — | — | — | — | 3 |
| `BIBLIOTHEQUE/GRID` | `design/formes/catalogue.md` | 3.9 k | — | — | — | — | 2 |
| `BIBLIOTHEQUE/SCENE` | `design/formes/catalogue.md` | 3.9 k | — | — | Asset, motion, scène ou type spécifique à construire | — | 4 |
| `BIBLIOTHEQUE/SEQUENCE` | `design/formes/catalogue.md` | 4.2 k | DIRECTION | — | — | — | 4 |
| `BIBLIOTHEQUE/OBJECT` | `design/formes/catalogue.md` | 4.4 k | — | — | — | — | 4 |
| `BIBLIOTHEQUE/MICRO` | `design/formes/catalogue.md` | 3.9 k | — | — | — | — | 4 |
| `BIBLIOTHEQUE/MODIFIER` | `design/formes/catalogue.md` | 1.5 k | — | — | — | — | 2 |
| `BIBLIOTHEQUE/COMPONENTS` | `design/formes/catalogue.md` | 4.4 k | — | SYSTÈME | Token, composant partagé, theming ou blast radius | — | 8 |
| `BIBLIOTHEQUE/COMPAT` | `design/formes/catalogue.md` | 3.5 k | — | — | — | — | 1 |
| `BIBLIOTHEQUE/READ` | `design/formes/choisir.md` | 11.1 k | — | — | Structure ouverte | — | 2 |
| `BIBLIOTHEQUE/TENSION` | `design/formes/choisir.md` | 1.6 k | — | — | Structure ouverte | — | 7 |
| `BIBLIOTHEQUE/SIGNATURE` | `design/formes/choisir.md` | 0.8 k | — | — | — | — | 1 |
| `BIBLIOTHEQUE/SELECT` | `design/formes/choisir.md` | 12.7 k | — | STANDARD, DIRECTION | Structure ouverte ; Asset, motion, scène ou type spécifique à construire | — | 11 |
| `BIBLIOTHEQUE/AVANT-SELECTION` | `design/formes/choisir.md` | 1.4 k | — | — | — | — | 1 |
| `BIBLIOTHEQUE/DERIVE` | `design/formes/choisir.md` | 2.4 k | — | — | — | — | 3 |
| `ACTION/GATE-C` | `design/produit/finition.md` | 4.1 k | — | ITER, DIRECTION | — | — | 4 |
| `ACTION/ANTI-SLOP` | `design/produit/finition.md` | 0.6 k | — | — | Motif générique ou réflexe | — | 3 |
| `ACTION/ATELIER-EDITION` | `design/produit/finition.md` | 3.7 k | — | — | — | BOUCLE-ATELIER | 4 |
| `ACTION/UI-UX-REALITY` | `design/produit/interface.md` | 3.6 k | — | STANDARD, DIRECTION | — | — | 2 |
| `DIRECTION/CAPACITY` | `design/produit/interface.md` | 2.4 k | — | — | Profil de style à retenir, famille de design, technique ou médium | — | 1 |
| `ACTION/GATE-A` | `design/produit/plancher.md` | 8.0 k | LITE, ITER, STANDARD, DIRECTION, SYSTÈME | — | — | — | 6 |
| `ACTION/RECETTE-RENDU` | `design/produit/plancher.md` | 10.2 k | — | — | Recette de rendu : options, états, captures, comparaison ; preuve d’é… | — | 5 |
| `ACTION/POLICIES` | `design/produit/plancher.md` | 2.2 k | — | — | — | — | 1 |
| `ACTION/FIRST-RENDER` | `design/produit/premier-rendu.md` | 1.8 k | DIRECTION | — | — | — | 1 |
| `ACTION/VISUAL_PROOF` | `design/produit/preuve-visuelle.md` | 1.9 k | — | DIRECTION | Recette de rendu : options, états, captures, comparaison ; preuve d’é… | — | 3 |
| `SAVOIR/STATE` | `design/savoir/composition.md` | 16.0 k | — | DIRECTION | Mouvement à déclarer ou à juger ; habillage de gabarit relevé ; Finesse sans geste concret, craft ou états ; Détail final susceptible de modifier le caractère, l’état, la hiérarc… | STATE-PLANCHER | 12 |
| `SAVOIR/CONTEXT` | `design/savoir/contexte.md` | 4.4 k | — | — | Cadrage ambigu ; contexte critique, responsive, performance ou mouvem… | — | 9 |
| `SAVOIR/FRAME` | `design/savoir/fondements.md` | 12.0 k | — | STANDARD, DIRECTION | Composition nouvelle : ordre intention → tension → foyer → masse → ry… ; Cadrage ambigu ; contexte critique, responsive, performance ou mouvem… | COMP-SINGULARITE, FND-CADRAGE | 5 |
| `SAVOIR/TOOLS` | `design/savoir/gout-et-tendances.md` | 15.2 k | — | — | MODAL à nommer ; claim daté ou tendance ; Ressource à choisir (bibliothèque, police, icônes, texture, données, … | — | 13 |
| `SAVOIR/IDENTITY` | `design/savoir/identite.md` | 6.5 k | — | — | — | — | 1 |
| `SAVOIR/SOURCE` | `design/savoir/images-et-sources.md` | 22.6 k | — | DIRECTION | Ressource à choisir (bibliothèque, police, icônes, texture, données, … | — | 8 |
| `SAVOIR/DESIGN-ATLAS` | `design/savoir/images-et-sources.md` | 6.9 k | — | LITE, ITER | Profil de style à retenir, famille de design, technique ou médium | — | 5 |
| `SAVOIR/CRAFT` | `design/savoir/qualite-creative.md` | 44.6 k | — | DIRECTION | Sujet réel et idée encore ouverte ; Plus de deux registres expressifs, ou deux sans lien au produit (sign… ; Motif générique ou réflexe ; Composition nouvelle : ordre intention → tension → foyer → masse → ry… ; Contenu, titre, ordre des sections ou nom des actions ; Couleur, encodage d’une donnée (polarité, grandeur, ordre) ; texte su… ; Revue créative après la première scène et après la repasse ; varier u… ; Détail final susceptible de modifier le caractère, l’état, la hiérarc… | BOUCLE-CAPTURE, COMP-CONTROLES, COMP-CONVERGENCE, COMP-COULEUR | 22 |
| `SAVOIR/STYLE` | `design/savoir/styles.md` | 12.5 k | — | DIRECTION | Profil de style à retenir, famille de design, technique ou médium | — | 9 |
| `SAVOIR/SYSTEM` | `design/savoir/systeme-de-design.md` | 2.1 k | SYSTÈME | — | Token, composant partagé, theming ou blast radius | — | 4 |
| `SAVOIR/TECH` | `design/savoir/techniques.md` | 12.5 k | — | — | Profil de style à retenir, famille de design, technique ou médium ; Technique à coder sans méthode sûre (matière, texte sur image, graphi… | — | 8 |
| `SAVOIR/TYPE` | `design/savoir/typographie.md` | 4.8 k | DIRECTION | — | Typographie ouverte ; grand titre, accroche ou chiffre qui porte la s… | COMP-TYPO | 7 |
| `SAVOIR/TYPE-VOIX` | `design/savoir/typographie.md` | 2.3 k | — | — | Typographie ouverte ; grand titre, accroche ou chiffre qui porte la s… | — | 4 |
| `ACTION/CLOSE-PACKAGE` | `gouvernance/cloture.md` | 6.8 k | — | DIRECTION | — | — | 14 |
| `ACTION/CLOSE-EXIT-CHECK` | `gouvernance/cloture.md` | 3.0 k | — | — | — | — | 2 |
| `DIRECTION/LECTURE-INSTRUMENTEE` | `gouvernance/cloture.md` | 1.0 k | — | — | — | — | 1 |
| `SAVOIR/INTEGRITY` | `gouvernance/integrite.md` | 9.1 k | — | DIRECTION | Détail final susceptible de modifier le caractère, l’état, la hiérarc… ; Doute sur l’application d’une règle ; repasse ; échec connu | INTEG-LIMITES, INTEG-RECITATION | 1 |
| `ACTION/AUTHORITY` | `gouvernance/principes.md` | 0.9 k | — | — | — | — | 1 |
| `DIRECTION/SERVICE-BOUNDARY` | `gouvernance/principes.md` | 1.1 k | — | — | — | — | 1 |
| `ACTION/STATUS` | `gouvernance/statuts.md` | 6.3 k | — | — | — | REGISTRES | 13 |
| `BIBLIOTHEQUE/CONTRACTS` | `gouvernance/structure.md` | 6.8 k | — | — | — | — | 6 |
| `BIBLIOTHEQUE/GATE` | `gouvernance/structure.md` | 4.3 k | — | — | — | — | 3 |
| `ACTION/PRECONDITION` | `gouvernance/travail.md` | 4.0 k | — | — | — | — | 1 |
| `ACTION/RUN_CARD` | `gouvernance/travail.md` | 18.2 k | — | DIRECTION | — | — | 5 |
| `ACTION/PIPELINE-DIRECTION` | `gouvernance/travail.md` | 12.7 k | — | DIRECTION | Réponse visible, trace complète, contrats écrits, checkpoint et accep… | — | 9 |
| `ACTION/STRUCTURED-PROOF` | `gouvernance/verification.md` | 7.1 k | — | — | — | — | 3 |
| `ACTION/GATE-B` | `gouvernance/verification.md` | 9.0 k | — | LITE, ITER, STANDARD, DIRECTION | — | — | 11 |
| `ACTION/OVERRIDE` | `gouvernance/verification.md` | 2.0 k | — | — | Doute sur l’application d’une règle ; repasse ; échec connu | — | 4 |
| `ACTION/MAINTENANCE` | `maintenance/evolution.md` | 1.7 k | — | — | — | — | 2 |
| `BIBLIOTHEQUE/EVOLUTION` | `maintenance/evolution.md` | 5.3 k | — | — | — | — | 3 |

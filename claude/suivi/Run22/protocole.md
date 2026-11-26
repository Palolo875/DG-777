# Run 22 — Campagne V1.3.0, premier run : l'invitation qui avait convergé

- **Lancé le** 25 novembre 2026. **Décision** de Junior : « À toi le choix. Attention à mes limites et usage. »
- **Choix fait** : un seul run d'abord ; la suite (second run sur ce brief, paire « sans système » contre V1.3.0 sur un brief d'une ligne) seulement après le résultat et la décision de Junior.
- **But** : (1) la convergence : l'idée « émail céladon qui s'arrête sur le grès nu » revient-elle, après trois runs sur trois (17k, 17l, 19x) ? (2) les recettes nouvelles (réponse par courriel, agenda, matière) sont-elles servies et tiennent-elles ? (3) le coût.

## Conditions

- Paquet : `R2026-11-25e` (V1.3.0), installé depuis l'archive Local livrée, dans `/tmp/run22e/.claude/skills/design-governance-practice`.
- Un agent neuf (sous-agent `general-purpose`, modèle de la session, effort par défaut, comme 17k, 17l et 19x), dossier vide, `DG_JOURNAL` activé.
- **Le prompt de 19x, mot pour mot**, au chemin du dossier près (brief compris, avec son erreur d'arrondissement).
- Ressources : Internet gratuit et sans compte ; ni génération d'images, ni outil branché, ni service payant.

## Ce qui se relève

- L'idée gardée, en une phrase, et son rang déclaré ; la comparer aux idées de 17k, 17l et 19x (`Convergences_observees.md`). Junior confirme si c'est la même.
- Les directions écrites, leurs probabilités et rangs ; la défense de la modale.
- Les recettes servies (journal) ; la matière regardée en photo ou non.
- Le coût par `Pilot_9b/cout_des_runs.py`, comparé à 19x.

## Jugement

Junior juge seul. Pas d'aveugle pour ce run (il n'y a qu'un rendu) : il voit le rendu à côté de 19x, la planche, et la page HTML.

## Règle de décision

- **Convergence** : si l'idée émail/grès revient, le deuxième rang n'a pas suffi sur ce brief ; on en cherche la cause dans la transcription avant tout autre run.
- **Une idée différente** doit encore appartenir au sujet : une idée arbitraire n'est pas un succès.
- **Limite** : un run montre une tendance, il ne prouve rien.

## Incident

- Le run s'est arrêté sur la limite d'usage de cinq heures du compte, après le choix sur la planche (« A, Pièce trempée ») et pendant la construction de la version finale.
- Il a été repris avec son contexte intact, par un message neutre (« Reprends là où tu t'étais arrêté… termine la demande »). Écart aux conditions de 19x : une interruption, sans consigne nouvelle.

## Résultats (relevés par Claude ; le jugement est celui de Junior)

- **Idée gardée** : « Pièce trempée » : le carton est un grès trempé dans l'émail ; le haut, émail céladon brillant, porte l'envie (titre, artiste, soirée) ; le pied en grès brut porte la pratique (adresse, réponse) ; une ligne de trempage à trois coulures entre les deux.
- **Convergence** : c'est, à mon relevé, **la même idée que 17k, 17l et 19x** (émail céladon qui s'arrête sur le grès nu ; l'envie sur l'émail, la pratique sur la terre). Quatre runs sur quatre, à confirmer par Junior.
- **Ce que la trace déclare** : modale « la pièce » (~45 %, rang 1 : crème, photo de vase, serif italique), défendue (« voir la pièce donne envie ») ; première idée astucieuse « titre émaillé qui coule » (~20 %) ; gardée **A, pièce trempée, ~5 %, rang 3, issue du tirage**. L'agent classe donc comme rare (rang 3, 5 %) l'idée que tous les runs ont produite : **le rang déclaré se trompe comme la probabilité**. C'est la limite écrite dans le rapport 15b (« les rangs que donne l'agent sont une déclaration »), observée dès le premier run.
- **Ce qui a marché** : modale défendue en une ligne et esquissée ; serif d'édition gardée (EB Garamond) après une variante sans empattement jugée à la vue ; matière réglée d'après des photos réelles (Art Institute of Chicago), recette `matiere` servie ; atelier symétrique (retrait, intensification, voix typographique) sur planches ; agenda `.ics` correct (UTC, CRLF) ; réponse par courriel préremplie ; contenus d'exemple marqués.
- **Recettes** : seule `matiere` a été lue ; l'agenda et la réponse sont codés de mémoire, correctement.
- **Coût** (`cout_des_runs.py`) : 174 tours (19x : 141, +23 %) ; cache lu 38,4 M (19x : 33,5 M, +15 %) ; cache écrit 1,27 M (19x : 0,61 M), doublé en partie par l'interruption et la reprise ; 24 images (19x : 22) ; routes lues : 73 k caractères (19x : 6,6 k).

## Jugement de Junior et lecture de la planche

- **Junior** : la convergence peut venir des recherches et références, « quasi les mêmes » d'un run à l'autre ; les autres esquisses de la planche sont moins fortes.
- **Vérifié dans les journaux** : références et requêtes se recoupent (carton « Frames » de Fonts In Use en 17k et 22e ; « Merveilles » de Sèvres en 17k, 19x et 22e ; galerie Lefebvre en 17k et 22e ; requêtes « galerie céramique… grès émaillé… »). Au run 22, elles sont cherchées avant la planche, depuis la catégorie. Causalité probable, non prouvée.
- **Lecture de la planche par Claude** : A nettement la plus forte. Modale générique, avec la photo d'une jarre ancienne de musée qu'on prendrait pour une œuvre exposée. B presque vide, à peine commencée. C, vraie idée (le temps), exécutée comme un tableau de bord.
- **Constat principal** : les esquisses ne sont pas au même niveau d'investissement. A a reçu matière, voix et références ; B et C sont restées à plat. Le duel est inégal, et la planche confirme le premier choix au lieu de l'éprouver.
- **Piste notée, non décidée** : chaque esquisse reçoit sa propre référence et son geste poussé avant la planche ; références cherchées après les directions, une par piste, dont une hors du domaine. Le « deuxième rang » (15b) reste une incitation, sans qu'on en attende la diversité.

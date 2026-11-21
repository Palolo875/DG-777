# Run 15 — notes de Claude (run fait à la main, carte blanche)

18 novembre 2026. Paquet `R2026-11-15k`, installé depuis l'archive livrée dans `/tmp/run15`. Même brief que le run 10 (« Les Lueurs »).

**Biais déclaré.** Ce n'est pas un agent neuf : je connaissais le verdict sur les runs 9 à 14 (le gadget, le générique, les références faibles). La comparaison avec le run 10 n'est donc pas propre. Elle montre ce que le système permet quand on sait où il échoue, pas ce qu'il produit seul.

## Ce qui a fait la différence (par ordre d'effet, à mon avis)

1. **La génération d'images autorisée.** La « carte blanche » valait accord. Trois variantes ont été générées (Figma, gpt-image-2.5-flare) et une estampe a été retenue sur planche. C'est le plus grand levier : sans elle, la route mène à l'atmosphère codée ou au dessin, donc au diagramme (constat A-3). Le noyau ne prévoit pas comment obtenir cet accord quand personne n'est là ; dans les runs d'agent, la route est toujours fermée.
2. **Des références choisies pour leur niveau.** J'ai pris Clermont-Ferrand, Lumière, Visions du Réel et La Villette, puis écrit le jugement de chacune. Les quatre disent la même chose : un premier écran tenu par une seule image forte. Rien dans la skill n'oblige ce niveau (B-1, B-2).
3. **Nommer le diagramme comme modale au second degré.** Le « plan vu de dessus » est écarté d'emblée. Je pouvais le faire parce que j'avais vu les runs ; la skill ne le liste pas parmi les marqueurs de convergence.
4. **Écrire dans la voix du festival, pas du designer** (E-1). Aucune règle ne le demande.

## Ce que les outils ont bien fait

- `verifier` a relevé de vrais défauts que je n'avais pas vus : le débordement à 768 px, le contraste du bouton de fin, le focus à 2,9:1, le mot seul en fin de titre, la définition des images sous 2× et les espaces fines manquantes.
- La planche (modale et trois esquisses) et l'atelier de voix (Gloock contre Anybody) ont tranché vite, à la vue.
- Le marquage « exemple » et « image générée » n'a rien coûté au niveau visuel.

## Frictions

- **Coût de lecture avant le premier pixel.** Il faut lire environ 45 000 caractères de noyau, 36 000 de tronc et 24 000 de `SAVOIR/SOURCE`, soit plus de 100 000 caractères.
- **Fausse alerte du journal (C-1).** Elle revient : j'ai lu le tronc en entier, avec l'outil de lecture, et la fiche le range quand même sous « Manques ».
- **`refs.md`.** Les champs « Change : … » restent des emplacements vides que rien n'oblige à remplir (B-3) ; je les ai remplis à la main.
- **`parcours.py polices`.** Il ne signale pas les axes absents : `font-stretch` n'a aucun effet sur Anybody livré en fichiers fixes, et l'esquisse s'est faite sans le savoir.
- **Réserve « Objet de preuve au premier écran ».** Elle reste avec « découpe par un ancêtre non évaluée », alors que l'objet est entièrement visible.
- **Trace.** Deux lignes dépassaient 600 caractères au premier jet ; l'outil les a signalées et je les ai raccourcies.

## Ce qui reste faible dans le rendu

- La section « Venir » reste la plus ordinaire : une image en bandeau et une liste.
- L'image fait 1 536 px de large (le maximum obtenu), ce qui est sous 2× à 1 440 px. La trame d'impression l'absorbe, mais c'est un plafond.
- L'image est générée. La vraie version demande une affiche commandée à un illustrateur.

## Coût

- 3 générations d'image (crédits IA Figma, sur le plan Starter de Junior).
- 4 références capturées, 1 planche de 4 esquisses, 1 atelier de voix.
- 3 passes de `verifier` et 1 de `check_render`.
- Fichier Figma créé dans les brouillons de Junior : « Run 15 — Les Lueurs (essais d'image) ».

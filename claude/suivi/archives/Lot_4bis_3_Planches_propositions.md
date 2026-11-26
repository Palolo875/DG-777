# Lot 4 bis, sous-lot 3 — Planches de principes : propositions

15 novembre 2026. Révision de départ : `R2026-11-15g`. Document hors du paquet. Rien n'est intégré.

Ce sous-lot traite B-03 : « le savoir ne se voit jamais ». Les six planches sont rendues et jointes à ce document. **C'est à vous de les juger à la vue (votre règle 7) avant toute intégration.**

## 1. Le principe retenu

- Chaque planche montre **un mécanisme déjà écrit dans le savoir**, en avant/après, sur un même contenu neutre : barres grises à la place du texte, titres génériques.
- Seule la variable du mécanisme change d'un panneau à l'autre. Une planche n'est jamais une page à imiter : elle ne propose ni style, ni palette, ni composition à reprendre. C'est la parade au risque de convergence.
- La police est Manrope, déjà livrée avec le paquet pour les supports (licence OFL). Elle ne fait pas partie des marqueurs de vague.
- Chaque planche porte en tête la route qui possède le mécanisme. Chaque panneau a une étiquette et une légende d'une ligne.
- Les planches sont dessinées par du code du paquet : aucune image n'est reprise d'ailleurs.

## 2. Les six planches

| Planche | Mécanisme | Route propriétaire (vérifiée) |
|---|---|---|
| `fonds-voisins.png` | Deux fonds voisins se distinguent par la luminosité, pas par la seule teinte ; le test en niveaux de gris est montré sous chaque panneau | `SAVOIR/CRAFT/CFT-05`, « Fonds voisins » |
| `accent-de-foyer.png` | Un accent qui marque tout ne désigne plus rien | `SAVOIR/CRAFT/CFT-05`, « Accent de marque et accent de foyer » |
| `masse-visuelle.png` | Le décor ne pèse pas plus que la preuve | `SAVOIR/STATE`, geste « Masse visuelle » |
| `grand-titre.png` | Plus un texte grandit, plus il se resserre : interligne près de 1, approche resserrée | `SAVOIR/TYPE`, « Réglage d'un grand texte » |
| `rayons.png` | Rayon intérieur = rayon extérieur − marge, avec un détail agrandi du coin | `SAVOIR/STATE`, geste « Cohérence de rayon » |
| `chiffres.png` | Chiffres tabulaires alignés à droite contre chiffres proportionnels alignés à gauche | `SAVOIR/STATE`, geste « Chiffres » |

**Format.** 1600 × 900 px, en PNG réduit à 128 couleurs sans tramage : environ 23 à 30 Ko par planche, 163 Ko pour les six.

## 3. Intégration proposée

| Où | Changement | Coût |
|---|---|---|
| `design/principes/` | Les six planches | 163 Ko par archive |
| `scripts/principes.py` | Le générateur, joint à ce document, pour refaire ou corriger une planche ; dans la distribution GitHub seulement, comme les autres outils de construction | Environ 9 Ko |
| Routes propriétaires | Une ligne par planche, par exemple : « Planche : `design/principes/fonds-voisins.png` (avant/après, à ouvrir comme image) ». Pour `SAVOIR/STATE`, une seule ligne sous la table des gestes cite les trois planches. | `SAVOIR/TYPE` est dans le tronc `DIRECTION` : environ 75 caractères, sur 405 de marge |
| Guide de niveau 2 (comprendre) | Un court paragraphe qui présente les planches aux personnes | Hors tronc |
| Manifeste | Les six PNG dans les deux distributions ; le générateur dans GitHub seulement | — |

**Garde.** Chaque planche citée existe, et chaque fichier de `design/principes/` est cité par sa route. Un contrôle vérifie aussi leur taille (1600 × 900).

**Ce qui ne change pas.** Le noyau ne change pas. Les planches ne sont jamais chargées d'office : l'agent les ouvre quand sa route les cite.

## 4. Ce que vous jugez

Pour chaque planche, une seule question : **le mécanisme se voit-il d'un coup d'œil, sans lire la légende ?**

Mes propres réserves, pour vous aider à regarder :

1. **Masse visuelle.** Le panneau de gauche, volontairement raté, laisse les barres de texte passer sous le grand disque. Cela peut se lire comme une erreur de mise en page plutôt que comme un défaut de masse.
2. **Chiffres.** Avec des chiffres tabulaires, « 311,10 » prend des espaces visibles autour du « 1 ». C'est le comportement normal de la police, mais un œil non averti peut le prendre pour un défaut.
3. **Rayons.** L'écart en coin se voit surtout dans le détail agrandi. Sur la carte entière, la différence est fine.

Vous pouvez :
- garder ou retirer une planche ;
- en demander une autre, par exemple neutres teintés, texte sur image et zone calme, ou partie ordinaire ;
- demander une correction précise : un panneau, une valeur, une légende.

## 5. Vérification prévue

1. Branche `principes`.
2. Tests :
   - les six planches existent, à 1600 × 900, et chacune est citée par sa route ;
   - un fichier non cité dans `design/principes/` fait échouer la garde (mutation rouge) ;
   - le générateur tourne avec un navigateur et réécrit les six fichiers (test navigateur, `NOT-VERIFIED` sans navigateur).
3. Le noyau reste identique ; le tronc `DIRECTION` reste sous 35 000 caractères.
4. Validation complète avec navigateur, révision `R2026-11-15h`.

**Critère d'arrêt.** Une planche que vous ne validez pas à la vue n'entre pas : je la corrige et vous la remontre, ou je la retire.

## 6. Ce qu'il faut me dire

« D'accord pour les six » suffit. Sinon, dites, planche par planche : gardée, retirée ou à corriger, et quoi.

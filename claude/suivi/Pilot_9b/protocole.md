# PILOT du lot 9b — protocole

- **Lancé le** 20 novembre 2026. **Décision** de Junior : « Deux objets », puis « Vas y ».
- **But** : savoir si le paquet `R2026-11-15l` (lot 9b) donne de meilleurs rendus que `R2026-11-15k`, selon le jugement de Junior.

## Conditions

| Run | Objet | Paquet |
|---|---|---|
| 17k | Objet 1 : carton d'invitation à un vernissage (galerie La Verrière, « Terres lentes ») | `R2026-11-15k` |
| 17l | Objet 1 | `R2026-11-15l` |
| 18k | Objet 2 : widget « marées du jour » d'un club de voile (Perros-Guirec) | `R2026-11-15k` |
| 18l | Objet 2 | `R2026-11-15l` |

**Règles communes à tous les runs :**
- un agent neuf (sous-agent `general-purpose`, modèle de la session, effort par défaut) ;
- un dossier vide, avec le paquet installé depuis l'archive livrée ;
- `DG_JOURNAL` activé ;
- le mode est laissé à l'agent ;
- les consignes de ressources sont celles de la série : Internet gratuit et sans compte ; ni génération d'images, ni outil branché, ni service payant ;
- le prompt est identique à celui du run 16, au brief près ; seul le paquet change d'un run à l'autre.

## Jugement à l'aveugle

- Pour chaque objet, Junior voit deux rendus nommés X et Y et choisit, avec sa raison en une phrase.
- La correspondance entre X/Y et k/l a été tirée au sort **avant** les runs. Seule son empreinte est publiée ici ; le texte est révélé après le jugement.
- Empreinte sha256 de la correspondance : `b98bccd651d7edd8d7ee832ddafaf48b801b970a46c1034f7de87db53cb83603`

## Relevés en plus du jugement

- L'agent `l` a-t-il appelé `leviers` ?
- La question sur le diagramme lui a-t-elle été servie ?
- Sa trace dit-elle qui a choisi ?
- Pour chaque run : coût et mode choisi.

## Limite

Deux paires montrent une tendance ; elles ne prouvent pas un gain. Si les deux paires donnent des résultats opposés, on ne conclut rien.

## Résultats (20 novembre 2026)

| Run | Paquet | Mode | `leviers` | Question du diagramme servie | « Choisi par » | Coût |
|---|---|---|---|---|---|---|
| 17k | k | DIRECTION | — | — | non | ≈323 k jetons, 102 appels, 27 min |
| 17l | l | DIRECTION | 3 appels | oui | oui | ≈310 k jetons, 102 appels, 22 min |
| 18k | k | STANDARD | — | — | non | ≈257 k jetons, 71 appels, 14 min |
| 18l | l | STANDARD | 2 appels | oui | oui | ≈319 k jetons, 101 appels, 21 min |

- **Jugement de Junior** : `l` est préféré sur les deux objets. Le détail est dans le carnet de goût.
- **Convergence** :
  - sur l'objet 1, les deux agents ont trouvé la **même idée** : un émail céladon qui coule et s'arrête sur le grès nu, la pratique écrite sous l'émail ;
  - sur l'objet 2, la **même structure** : le créneau en tête, la courbe avec la ligne du seuil, le phare de Ploumanac'h en fond d'écran.
  - Les différences jugées tiennent à l'exécution (structure, lisibilité, cas limites), pas à la direction.
- **Erreur de brief** : la rue des Tanneurs est dans le 9e arrondissement de Lyon, pas dans le 1er. Les deux runs ont reçu le même brief.

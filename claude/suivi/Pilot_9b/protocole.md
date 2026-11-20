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

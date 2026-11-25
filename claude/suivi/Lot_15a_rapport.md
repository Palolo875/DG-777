# Lot 15a — Rapport : cinq recettes et la matière observée

- **Révision** : `R2026-11-25d`, 25 novembre 2026. La version publique reste V1.2.0 ; V1.3.0 viendra à la fin du lot 15.
- **Branche** : `lot-15a`.
- **Décision** : « Ça me va » (options A du lot 15).
- **Runs** : aucun.

## 1. Ce qui change

**Cinq recettes** dans `references/recettes.md`, servies par `parcours.py recette NOM` (dix en tout) :

| Recette | Ce qu'elle règle | Besoin observé dans les rendus |
|---|---|---|
| `matiere` | Regarder deux photos réelles et écrire trois observations ; coder ensuite en couches (base, variations lentes, grain en image de fond à taille fixe, jamais en filtre, puis l'accident observé) | Émail codé en `feTurbulence` dans les deux invitations du PILOT final ; émail jugé « artificiel » (19x) |
| `police-variable` | Plage déclarée dans `@font-face` ; taille calée sur la graisse la plus forte ; curseur natif nommé qui annonce la graisse en mots ; balayage seulement sans préférence de mouvement réduit, arrêté dès que la personne prend la main | Run 21 (curseur de graisse) ; invitation B du PILOT final (`font-variation-settings`) |
| `reponse-courriel` | Formulaire validé ; message composé et encodé ; la page dit ce qui reste à faire, avec l'adresse en clair et le message à copier ; elle ne dit jamais « envoyé » | `mailto:` composé à la main dans 5 rendus (Runs 9, 14 et 15, invitations A et B du PILOT final) |
| `agenda` | Fichier `.ics` produit dans la page : heure en UTC, texte échappé, lignes pliées à 75 octets, retours CRLF, `UID` et `DTSTAMP` | `.ics` écrit à la main dans les deux invitations du PILOT final |
| `objet-en-scene` | Cadre au rapport fixé qui réserve sa place ; recadrage sur le point d'intérêt à chaque largeur ; deux ombres teintées (contact et portée) ; `drop-shadow` pour un objet détouré | Pistes F et E (objet de preuve posé sur la page) |

- **Règle d'entrée du fichier.** Une phrase de l'en-tête de `recettes.md` change : « un comportement **ou un procédé**, jamais une apparence : … l'**aspect d'une matière** reste à la direction ». Sans cela, la recette `matiere` contredisait l'en-tête.
- **Besoin, pas échec.** Les preuves du tableau montrent un code écrit à la main plusieurs fois. Elles ne montrent pas toujours un échec. L'entrée d'une recette exige que « plusieurs rendus aient achoppé » ; je l'applique ici au sens « plusieurs rendus ont dû le coder de mémoire ». La recette `objet-en-scene` repose sur la piste plus que sur des rendus relevés.

**Matière observée (E et D)** :
- Un paragraphe dans l'atelier (`ACTION/ATELIER-EDITION`, bloc différé, donc 0 octet au noyau) : regarder deux photos réelles avant de coder une matière, puis les comparer côte à côte, à la même échelle, et répondre à « observée ou dessinée ? ». Dessinée, la matière se reprend d'après la photo ou part au test de retrait.
- Une phrase de renvoi dans `SAVOIR/SOURCE`, « Construire une atmosphère ».
- Une ligne dans la table d'évolution (`maintenance/evolution.md`).

Noyau inchangé : 31 699 octets sur 33 000.

## 2. Tests et mutations rouges

10 cas avec navigateur (`parcours` : 195 cas, tous verts). Chaque recette est mise en page, ouverte dans le navigateur et vérifiée sur ce qu'elle promet ; le test d'accès (noms, tabulation, inertie au clavier) est étendu aux trois recettes qui ont des contrôles.

| Mutation (dans la recette) | Résultat |
|---|---|
| Grain mis à l'échelle de l'élément (`20% 20%`) | _à compléter_ |
| Taille non calée sur la graisse la plus forte | _à compléter_ |
| Corps du message non encodé | _à compléter_ |
| Lignes de l'agenda non pliées | _à compléter_ |
| Pas de recadrage mobile | _à compléter_ |

## 3. Préparation et livraison

_à compléter_

## 4. Ce que ce sous-lot ne prouve pas

- Que les rendus s'améliorent : il faut des runs.
- Que la matière codée d'après photo paraisse observée : la question le demande à l'agent, et seul ton regard tranche.
- Les recettes sont vérifiées sur leur comportement (débordement, clavier, encodage, format), pas sur leur beauté.

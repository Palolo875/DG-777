# Lot 4 bis, sous-lot 2 — Sections ordinaires : propositions

15 novembre 2026. Révision de départ : `R2026-11-15f`. Document hors du paquet. Rien n'est intégré.

Ce sous-lot traite B-04. Le texte à intégrer est écrit en entier au § 2 : c'est votre jugement de designer qui est en jeu.

## 1. État vérifié

- **Dans le catalogue**, les sections ordinaires tiennent en trois passages :
  - « Cartes » (`BIBLIOTHEQUE/SEQUENCE`) : une carte marque un objet séparable ; pour des fonctionnalités, préférer une liste, un objet unique ou des onglets ;
  - la ligne « Fin » de la même table : « le pied de page n'est pas qu'une liste de liens » ;
  - « Parties ordinaires » (`BIBLIOTHEQUE/COMPONENTS`) : le comportement conventionnel de la navigation, du bouton, des onglets, du champ et du pied, et une propriété empruntée à la direction.
- **Ailleurs, des règles existent déjà**, et le nouveau texte y renvoie sans les répéter :

| Règle | Propriétaire |
|---|---|
| Pas de preuve inventée (`CNT-01`) | `SAVOIR/CRAFT/CFT-06`, « Preuve sans l'inventer » |
| Boutons nommés par leur objet, formes de titre | `SAVOIR/CRAFT/CFT-06` |
| Pas de motif trompeur dans l'inscription, le paiement ou la résiliation | `ACTION/UI-UX-REALITY`, « Flux d'engagement » |
| Étiquettes et erreurs de formulaire | `SAVOIR/CONTEXT` (sous-lot 1) |
| Le geste à corriger quand une partie est ordinaire | `SAVOIR/STATE`, « Partie ordinaire » |

- **Ce qui manque.** Rien ne dit, section par section, ce que la personne y cherche, la forme réflexe qui la rend ordinaire, et les leviers qui la rendent propre au sujet : fonctionnalités, preuve, tarifs, questions fréquentes, contact et accès, inscription, pied de page.
- **Une portée étroite.** Le catalogue dit lui-même venir « surtout du produit logiciel et du B2B ». Les sections d'un commerce local (horaires, accès, carte) n'y ont pas de place.

## 2. Texte proposé

Une nouvelle route, `BIBLIOTHEQUE/SECTIONS`, placée dans `design/formes/catalogue.md` juste après `BIBLIOTHEQUE/SEQUENCE`. Elle est rédigée dans la voix des autres routes de savoir, qui s'adressent à l'agent.

> ## BIBLIOTHEQUE/SECTIONS — sections ordinaires d'une page
>
> [MÉTHODE] Les sections qui suivent le premier écran sont celles qu'une page livre le plus souvent ordinaires : chacune a une forme réflexe que tout gabarit propose. Pour chacune, voici ce que la personne y cherche, la forme réflexe, les leviers qui la rendent propre au sujet et ce qui se vérifie sur capture. Les règles restent chez leur propriétaire : la preuve jamais inventée (`SAVOIR/CRAFT/CFT-06`, « Preuve sans l'inventer »), les flux d'engagement (`ACTION/UI-UX-REALITY`), les étiquettes de formulaire (`SAVOIR/CONTEXT`) et le comportement des contrôles (`BIBLIOTHEQUE/COMPONENTS`, « Parties ordinaires »). Une forme réflexe n'est pas interdite : elle se garde si elle sert mieux la tâche, et cela se décide comme un marqueur, à l'atelier.
>
> **Fonctionnalités.**
> - **La personne cherche** ce que le produit fait pour elle, et comment.
> - **Réflexe :** trois ou six cartes égales, chacune avec une icône, un titre et deux lignes.
> - **Leviers :**
>   - une fonctionnalité à la fois, avec sa vraie vue et ses états (onglets, défilement pas à pas) ;
>   - une liste dense quand il y en a beaucoup ;
>   - un ordre qui suit la tâche de la personne, pas l'inventaire du produit ;
>   - une seule mise en avant : celle qui porte la thèse.
> - **Sur capture :** sans les icônes, rien ne se perd, sinon c'est qu'elles portaient le sens ; deux fonctionnalités voisines ne se confondent pas.
>
> **Preuve : avis, chiffres, logos.**
> - **La personne cherche** si d'autres, comme elle, y ont trouvé leur compte.
> - **Réflexe :** trois citations en cartes avec portrait rond et cinq étoiles, et une bande de logos grisés.
> - **Leviers :**
>   - la preuve la plus vérifiable d'abord : un chiffre daté avec sa source, une réalisation montrée, une citation avec nom, fonction et contexte ;
>   - une citation longue qui raconte un usage vaut mieux que trois slogans ;
>   - chaque preuve se place près de l'affirmation qu'elle soutient, pas regroupée en fin de page.
> - **Honnêteté :** sans preuve fournie, la section montre la chose elle-même (une réalisation, une vue du produit) ; un avis, un logo ou une note ne s'invente pas.
> - **Sur capture :** chaque preuve dit qui, quoi et quand.
>
> **Tarifs.**
> - **La personne cherche** combien, pour quoi, et ce qui change d'une offre à l'autre.
> - **Réflexe :** trois colonnes, celle du milieu surélevée « la plus populaire », et des listes de coches.
> - **Leviers :**
>   - la différence entre les offres dite en une ligne, puis le détail ;
>   - les coches seulement là où les offres diffèrent ;
>   - le prix réel avec sa période, ses taxes et ce qui n'est pas compris ;
>   - pour un commerce ou un artisan, une carte ou une grille de prestations plutôt que des « offres ».
> - **Honnêteté :** aucun frais révélé plus tard, aucune option présélectionnée, et une résiliation aussi courte que l'inscription.
> - **Sur capture à 390 px :** les offres se comparent sans défilement horizontal.
>
> **Questions fréquentes.**
> - **La personne cherche** la réponse à sa question, vite.
> - **Réflexe :** un accordéon de huit questions génériques en bas de page.
> - **Leviers :**
>   - les vraies questions du sujet (délai, annulation, accès, ce qui est inclus), dans les mots de la personne ;
>   - les trois plus fréquentes ouvertes d'emblée ;
>   - une réponse qui commence par oui, par non ou par le chiffre ;
>   - une question qui revient à chaque brief remonte dans la page, là où elle se pose.
> - **Sur capture :** la réponse se lit sans ouvrir trois panneaux, et l'accordéon s'ouvre au clavier.
>
> **Contact et accès.**
> - **La personne cherche** comment venir, quand, et comment joindre quelqu'un.
> - **Réflexe :** un formulaire « Contactez-nous » et une carte intégrée en pleine largeur.
> - **Leviers :**
>   - pour un lieu : l'adresse, les horaires du jour et l'accès écrits en texte (lisibles sans carte), un lien d'itinéraire, un numéro qui s'appelle d'un geste ;
>   - pour un service : le délai de réponse annoncé, et le canal le plus direct d'abord ;
>   - les horaires exceptionnels visibles.
> - **Sur capture à 390 px :** l'adresse, les horaires et le numéro tiennent dans un écran.
>
> **Inscription ou demande.**
> - **La personne cherche** à s'engager sans surprise.
> - **Réflexe :** un bloc coloré « Prêt à commencer ? » avec un champ e-mail et un bouton.
> - **Leviers :**
>   - ce qui se passe ensuite (ce qu'on reçoit, quand, à quel prix), dit à côté du bouton ;
>   - le moins de champs possible ;
>   - l'action nommée par son objet (« Recevoir le devis ») ;
>   - une fin qui reprend la thèse de l'entrée (`BIBLIOTHEQUE/SEQUENCE`, « Fin »).
> - **Honnêteté :** refuser reste aussi visible qu'accepter, et aucun consentement n'est précoché.
> - **Sur capture :** une erreur s'affiche à côté de son champ.
>
> **Pied de page.**
> - **La personne cherche** ce qu'elle n'a pas trouvé plus haut, et les mentions.
> - **Réflexe :** quatre colonnes de liens, les icônes de réseaux et le copyright.
> - **Leviers :**
>   - le colophon de la fin de séquence : marque, phrase de clôture, coordonnées réelles ;
>   - les liens dont la personne a besoin, pas un plan du site ;
>   - une propriété empruntée à la direction ;
>   - les mentions légales attendues pour le lieu et l'activité.
> - **Sur capture :** aucun lien mort, aucun réseau qui n'existe pas.

**Taille.** Environ 5 200 caractères, servis par la route, hors noyau et hors tronc.

## 3. Comment l'agent y arrive

| Lieu | Ajout | Coût |
|---|---|---|
| `BIBLIOTHEQUE/SEQUENCE`, « Trame sur toute la page » (tronc `DIRECTION`) | « Section par section, la forme réflexe et ses leviers : `BIBLIOTHEQUE/SECTIONS`. » | Environ 85 caractères, sur 485 de marge |
| Fiche de `parcours.py verifier`, rappel « Partie ordinaire » | « sections ordinaires : `BIBLIOTHEQUE/SECTIONS` » | Code seulement |
| Portée du catalogue (`BIBLIOTHEQUE/SCENE`) | Pour un commerce local, une boutique, une lecture ou un événement, renvoi aussi à `BIBLIOTHEQUE/SECTIONS` | Environ 40 caractères, hors tronc |

La recherche (`read_route.py --trouver`) la trouvera sur « tarifs », « questions fréquentes », « témoignages », « pied de page » ou « horaires ».

## 4. Vérification prévue

1. Branche `sections`.
2. Tests :
   - la route est servie par son code et contient les sept sections ;
   - le renvoi est présent au tronc `DIRECTION`, sous le budget ;
   - aucune citation d'auteur (PRO-01) ;
   - la recherche de « tarifs » et de « questions fréquentes » place `BIBLIOTHEQUE/SECTIONS` parmi les trois premières routes ;
   - les planchers de trouvabilité tiennent.
3. Le noyau reste identique.
4. Validation complète avec navigateur, révision `R2026-11-15g`.

**Critère d'arrêt.** Si le renvoi fait passer le tronc `DIRECTION` au-dessus de 35 000 caractères, je ne compense pas en coupant ailleurs sans vous le montrer : je m'arrête.

## 5. Ce qu'il faut me dire

« D'accord » suffit. Pour corriger le texte, citez la section et la ligne, avec ce que vous voulez à la place. Pour retirer une section ou en ajouter une (par exemple une galerie, une équipe ou un blog), dites laquelle.

# Lot 9 — Runs de contrôle : rapport

18 novembre 2026. Paquet testé : `R2026-11-15k` (commit `c1fe44a`), installé depuis l'archive livrée. La validation complète, navigateur compris, passe. L'archive reconstruite est identique à l'archive livrée, fichier par fichier.

## 1. Les deux runs

| | Run 9 | Run 10 |
|---|---|---|
| Brief | Landing « Quote-part » (partage des charges d'une colocation) | Page d'accueil du festival « Les Lueurs » (courts-métrages en plein air) |
| Visée | contrôle du système corrigé | capacité esthétique |
| Agent | non consigné | sous-agent `general-purpose`, sans contexte, modèle de la session, effort par défaut |
| Prompt | non consigné | consigné dans la conversation ; la variable `DG_JOURNAL` y est demandée en clair |
| Mode | `DIRECTION` | `DIRECTION`, choisi par l'agent sans consigne |
| Direction | « Le plan de la coloc » | « Le plan du verger » |
| Coût | non consigné | environ 21 min, 85 appels d'outils, à peu près 300 000 jetons |
| Fichiers | `Run9/` | `Run10/` |

## 2. Verdict de Junior

> « Ça n'a pas un haut niveau comme vrai produit de haute qualité, même si ça contient des exemples ou que ce sont des démos. Certaines parties sont gadget, d'autres génériques, cheap : des interfaces génériques, qu'on les croie faites par une IA ou par un humain. Les références et les recherches obtenues sont aussi de faible qualité, et elles influencent les rendus. »

Ce verdict vaut pour les deux runs. **Le système ne produit pas encore un niveau de produit réel haut de gamme.**

## 3. Constats, vérifiés dans les fichiers

### A. Niveau esthétique

- **A-1. Gadget (certain sur deux runs).** Les deux runs font le même geste : un plan vu de dessus, qui sert à la fois d'image et de preuve. Dans le run 10, ce plan ne répond pas au besoin du brief (l'envie de venir, l'atmosphère) : les couvertures sont des rectangles, les arbres des taches floues. Les deux planches sont bâties de la même façon : la page modale, A le plan, puis B et C.
- **A-2. Générique sous le premier écran (certain sur deux runs).** Après le premier écran, la page redevient une suite de composants standard : onglets, tableau, formulaire, colonnes, pied de page. L'exigence ne tient pas sur toute la page.
- **A-3. Cause probable, à vérifier.** `DIRECTION/EXTERNAL-START` (point 3, `FIRST-OBJECT`) demande « promesse → objet de preuve → geste », et `check_render` signale « Objet de preuve au premier écran ». Ces deux règles poussent vers un objet qui informe. Sur un brief d'ambiance, la seule réponse qu'elles récompensent est un diagramme. Deux runs ne suffisent pas à l'établir.

### B. Références et recherches

- **B-1. Les références ne sont pas au niveau visé (certain).** Le noyau (bloc `ANCRE`, `design/direction/standard.md`) demande « deux ou trois références réelles du même type d'objet […] **ou** du monde du sujet, au niveau de finition visé ».
  - Run 10 : trois sites de petits festivals et cinémas locaux. Courts Circuit 66 a 1 % de surface en image et un texte courant de 11 px.
  - Run 9 : Splitwise et Tricount, c'est-à-dire la page modale de la catégorie, plus un plan de la NASA.
  - Aucune référence ne fixe un niveau haut. Le « ou du monde du sujet » permet de remplir l'exigence avec des sources faibles.
- **B-2. Le niveau visé n'est défini nulle part (certain).** `niveau de finition visé` n'est expliqué ni dans `design/savoir/gout-et-tendances.md` ni dans le reste du savoir. Aucun outil ne le contrôle.
- **B-3. Le jugement des références n'est pas écrit (certain, run 10).** Les cinq entrées de `refs.md` gardent « Change : … ; ne se transfère pas : … » vides. Le noyau demande pourtant une ligne par référence. La trace en donne un résumé court, mais rien ne bloque.
- **B-4. Les sources d'images sont pauvres (certain).** Il n'y a pas de clé Pexels ou Unsplash, Commons n'a rien renvoyé et Poly Haven a été coupé. La génération n'est pas lancée sans accord. Tout est donc construit en code, ce qui alimente A-1.

### C. Journal et trace (candidats déjà notés au lot 9b)

- **C-1. La fausse alerte `--fichier` revient (certain).** La fiche range encore le tronc sous « Manques ».
- **C-2. Nouveau constat (certain).** Au run 10, sept routes ont été redirigées vers un fichier, dont `DIRECTION/START/TREE` et `EXTERNAL-START`, et la fiche les marque « lecture non observée ». Reste à décider si c'est un défaut de l'outil ou de l'agent.
- **C-3. Lignes de trace trop longues : non reproduit.** Au run 10, aucune ligne ne dépasse 600 caractères.
- **C-4. Réserves non nommées : en partie corrigé.** Le run 10 annonce « quatre réserves », mais sans les nommer.

### D. Méthode des runs

- **D-1. Le prompt, l'agent, le modèle et l'effort du run 9 ne sont pas consignés.** Les runs 9 et 10 ne sont donc pas strictement comparables.

## 4. Ce que le lot ne dit pas

- Il ne dit pas que le système dégrade les rendus. Sans skill, on ne sait pas ce que produirait le même agent : aucun run témoin n'a été fait.
- Deux briefs ne suffisent pas à établir A-3.

## 5. Suite

Les propositions du lot 9b porteront d'abord sur B (le niveau des références) et sur A (le gadget et le générique), puis sur C et D.

## 6. Runs 11 à 14 : verdict de Junior

Quatre runs de plus, pour varier les objets : data viz (11), identité et affiche (12), interface d'application (13), fiche produit haut de gamme (14). Détail dans `Registre_des_runs.md`.

> Junior partage l'avis de Claude : classement 12 > 13 > 11 > 14, puis les runs 9 et 10.

Constats ajoutés, sur ces quatre runs :

- **A-3 établi.** Le diagramme sert de héros dans trois runs sur six (9, 10, 14). Quand une image manque, l'agent dessine un objet technique à la place.
- **A-4. Le plafond vient des briefs qui vivent de l'image.** Les objets sans photo (identité, outil, données) donnent les meilleurs rendus. Le festival et la céramique plafonnent.
- **B-5. Pas de calibration en `STANDARD` (certain).** Les runs 11 et 13 n'ont capturé aucune référence, et leur esthétique est la plus générique. L'exigence d'ancre ne vise que les surfaces `DIRECTION`.
- **E-1. La voix du designer passe dans la page (nouveau).** L'agent écrit son raisonnement dans le produit : « Le 3 avril 2027 tombe un samedi », « Le dessin est fixé. Vos pièces restent à tourner. »
- **E-2. Polices libres, sûres et à la mode**, jamais distinctives : Bricolage, Barlow, Big Shoulders, Plex, Young Serif.
- **Méthode.** Les runs 12, 13 et 14 ont été interrompus par la limite d'usage, puis repris par le même agent.

## 7. Série « capacité esthétique » : run 16, le billet de concert

Le protocole : un agent neuf par run, un petit objet entièrement en code, aucun mode imposé. Internet gratuit et sans compte est autorisé ; la génération d'images, les outils branchés et les services payants sont interdits. Le détail est dans `Registre_des_runs.md` et dans `Run16/`.

> Junior reprend l'avis de Claude (« Ajoute »).

**Verdict.** C'est le meilleur des runs sur la fonction, et un résultat moyen sur l'esthétique : la tenue d'un billet d'application bien fait, pas d'un objet qu'on a envie de garder.

Ce qui tient :
- la zone d'entrée (F / 12 / B, les heures, une grille à cases qui reprend la vraie convention Porte / Rang / Place) ;
- des mentions crédibles et justes ;
- aucun marqueur de modèle ;
- une modale bien nommée (la carte Wallet sombre au dégradé violet) et bien évitée.

Constats ajoutés :
- **A-3 (quatrième fois).** Le plan de la salle sert d'objet principal. Il est justifié ici, parce qu'il répond à « où est ma place ? », mais le réflexe est installé. **Piste :** nommer le diagramme comme objet principal parmi les marqueurs de convergence.
- **B-6. Les références ne sont pas transformées.** L'agent a regardé les billets Commodore et Printers' Fair (Fonts In Use), mais rien de leur culture (papier de couleur, trame de sécurité, caractère typographique, numérotation) n'est passé dans le billet. Une ligne « ce qu'elle change » ne suffit pas.
- **E-3. La palette n'est pas justifiée.** Le fond vert d'eau couvre tout le billet, et la trace ne le justifie nulle part : la « Question de convergence » du noyau n'est pas appliquée, et rien ne bloque.
- **E-4. L'accent suit une logique incohérente.** Le rouge marque le siège, une étape, le rang sur le plan et le sceau, au lieu de porter une seule information.
- **E-2 (encore).** Unbounded est une police large très à la mode ; elle donne au billet un air de jeune marque.
- **A-2 (encore).** Le bas du billet est fait de composants d'application standard : tableau, étapes en pastilles, liste à puces.
- **Gadgets :** les demi-cercles de perforation dans un écran (la modale Dribbble) et le sceau en texte circulaire.
- **La planche :** la piste « gaufrier BD », la plus située (Angoulême) et la plus vivante, a été écartée. Une combinaison était possible : la matière de la BD, avec la grille de place pour la fonction.

Erreur du brief : le 14 mars 2027 est un dimanche. L'agent l'a relevée et a gardé le 14.

## 8. Recherche libre et Google Images (19 novembre 2026)

Détail dans `Run16_recherche_libre/recherche.md`.
- **Une recherche web normale** ramène surtout des listes et des concepts génériques. Ce qui a de la valeur vient d'archives spécialisées (Fonts In Use) et des guides des plateformes (Apple Wallet).
- **Google Images (captures de Junior)** montre presque uniquement des modèles à vendre : c'est la **modale observée** du genre. Les rares vrais billets portent les signes d'authenticité que les modèles imitent.
- **Piste pour le lot 9b.** La recherche a deux rôles distincts. **Observer la modale** (ce qu'on évite), par une recherche d'images : aujourd'hui la skill la nomme de mémoire. **Calibrer le niveau** (ce qu'on vise), avec une courte liste de sources par type d'objet. Ces pistes ne sont pas encore des propositions.

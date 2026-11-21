# Lot 4 bis — Savoir à écrire : propositions

15 novembre 2026. Révision de départ : `R2026-11-15e`. Document hors du paquet. Rien n'est intégré.

Vous avez donné votre accord sur le principe du lot : écrire du savoir qui manque, et non plus corriger. J'ai relu les trois constats dans les fichiers actuels.

**Je signale un lot surdimensionné.** B-03, B-04 et B-09 ne demandent pas le même travail :

| Constat | Nature du travail | Part de jugement de designer |
|---|---|---|
| B-09 — accessibilité et performance | Des repères établis (normes, mesures de terrain) traduits en décisions de conception, et un contrôle à ajouter | Faible |
| B-04 — sections ordinaires | Un savoir à écrire, section par section | Forte |
| B-03 — un savoir qui ne se voit pas | Des images à créer, avec un risque propre, la convergence | La plus forte |

Je propose donc **trois sous-lots, une révision chacun, dans cet ordre** : B-09, puis B-04, puis B-03. Ce document vaut **propositions complètes pour B-09** : le texte à intégrer est écrit au § 1. Pour B-04 et B-03, il fixe le principe et la forme (§ 2 et 3) ; leur texte vous sera soumis dans leurs propres propositions.

**Ce que cela coûte.** Le noyau ne change pas. Aucun tronc ne change pour B-09. B-04 ajouterait environ 90 caractères au tronc `DIRECTION`, qui a 485 caractères de marge. Les nouveaux savoirs sont servis par leur route, au signal.

**La règle 6 s'applique.** Les principes sont dits sans leur auteur. Les normes restent nommées (WCAG 2.2), parce qu'elles sont à appliquer. Les repères de terrain sont en `[VEILLE]`, avec leur type de source et leur date.

---

## 1. B-09 — accessibilité et performance (sous-lot 1, texte complet)

### 1.1 État vérifié

- **Savoir (`SAVOIR/CONTEXT`).** L'accessibilité tient en une phrase, une liste de principes. Le responsive et la performance tiennent en deux paragraphes, sans aucun repère.
- **Contrôle (`ACTION/GATE-A`).** Il est déjà complet sur les critères de WCAG 2.2 : cibles, focus non masqué, glisser, aide cohérente, saisie redondante, authentification.
- **Recette de rendu.** Elle mesure le contraste, les noms accessibles, le clavier, les cibles de 24 px avec leur espacement, le focus et le mouvement réduit.
- **Ce qui manque.**
  - **Décisions de maquette.** Rien ne dit ce qui se décide en concevant : taille et longueur de ligne, ordre de lecture, focus dessiné, zoom, espacement du texte, étiquettes de formulaire.
  - **Stabilité.** « Stabilité média » est un contrôle de Gate A, mais aucun outil ne la mesure.
  - **Poids.** `parcours.py verifier` donne le poids de la page « à titre d'information, sans seuil ».

### 1.2 Texte proposé pour `SAVOIR/CONTEXT`

Il s'insère après la phrase des principes de livraison, en deux sous-sections. La sous-section existante « Responsive et performance » garde ses deux paragraphes, et la nouvelle performance les suit.

> ### Accessibilité : ce qui se décide en concevant
>
> La plupart des défauts d'accessibilité se décident dans la maquette, pas dans la correction finale. Le contrôle reste celui d'`ACTION/GATE-A` ; ces repères disent ce qui le rend facile à tenir.
>
> - **Texte.** `[À ADAPTER]` Corps de lecture d'au moins 16 px sur écran, interligne d'environ 1,4 à 1,6 pour un texte courant, lignes de 45 à 80 signes. La page tient quand l'espacement du texte est agrandi (interligne 1,5 ; paragraphes 2 fois la taille ; lettres 0,12 em ; mots 0,16 em) et à 320 px CSS de large sans défilement horizontal, ce qui correspond au zoom à 400 % (WCAG 2.2, 1.4.12 et 1.4.10). Cela exclut une hauteur fixe sur un bloc de texte et un texte rendu en image.
> - **Ordre.** L'ordre de lecture et de tabulation suit l'ordre visuel. Une composition asymétrique ne réordonne pas le document pour l'effet.
> - **Focus.** L'état de focus se dessine comme les autres états, dans la direction de la page, avec un contraste d'au moins 3:1 contre ce qui l'entoure. Un en-tête collant ou un bandeau ne le recouvre jamais (2.4.11).
> - **Cibles.** 24 px CSS au moins, ou l'espacement équivalent (2.5.8). `[À ADAPTER]` Sur mobile, l'action principale vise plutôt 44 px.
> - **Formulaires.** Une étiquette visible accompagne chaque champ : un texte d'exemple n'est pas une étiquette. L'erreur se dit en texte à côté du champ, avec ce qui la corrige. Une information déjà donnée ne se redemande pas (3.3.7).
> - **Couleur et mouvement.** L'information ne dépend pas de la couleur seule (`SAVOIR/CRAFT/CFT-05`) ; le mouvement réduit suit « Motion et espace », plus bas.
>
> La recette (`ACTION/RECETTE-RENDU`) mesure le contraste, les noms, le clavier, les cibles, le focus et le mouvement réduit. Elle ne juge ni l'ordre de lecture, ni le zoom, ni l'espacement du texte : ceux-là se regardent sur capture, à 320 px.
>
> ### Performance : repères et leviers de conception
>
> [VEILLE 2026-11] `[À ADAPTER]` Repères de terrain, mesurés au 75e centile des visites (indicateurs de performance des navigateurs, 11-2026) : plus grand élément affiché en 2,5 s au plus, réponse à une interaction en 200 ms au plus, décalage cumulé de mise en page de 0,1 au plus. Une page ouverte en local ne mesure pas les deux premiers ; elle montre le troisième. À revoir avant 2027-04.
>
> Ce qui se décide en concevant :
> - **L'image du premier écran** est souvent l'élément le plus lourd et le plus grand. On la dimensionne à 2 fois sa taille d'affichage, en AVIF ou WebP, chargée en priorité ; les images plus bas se chargent en différé.
> - **Les polices.** `[À ADAPTER]` Deux familles et quatre fichiers au plus, en sous-ensemble, avec une police de repli de métriques voisines pour que le texte ne saute pas.
> - **La stabilité.** L'espace de chaque média se réserve (dimensions ou `aspect-ratio`) : rien ne bouge pendant le chargement.
> - **Le mouvement et la 3D** au premier écran se justifient par la thèse, et leur coût se mesure.
>
> `[À ADAPTER]` Le poids se lit avec `parcours.py verifier`. Au-delà d'environ 2 Mo pour la page, 500 Ko pour une image ou 300 Ko de polices intégrées, l'écart se décide et se dit.

**Taille.** Environ 2 900 caractères, servis par la route, au signal existant de la table du noyau (« contexte critique, responsive, performance ou mouvement »).

### 1.3 Le contrôle à ajouter

| Option | Changement |
|---|---|
| **A (recommandée)** | Deux ajouts. La **recette de rendu** mesure le décalage de mise en page pendant le chargement (navigateur local, en laboratoire), ce qui donne enfin un instrument au contrôle « Stabilité média » de Gate A : au-delà de 0,1, une réserve, jamais un verdict de terrain. Le **parcours** transforme le poids, déjà relevé, en signaux avec leur question, aux seuils `[À ADAPTER]` du texte ci-dessus. Le temps d'affichage n'est pas mesuré : en local, sans réseau, il ne voudrait rien dire. |
| B | Le parcours seulement : le poids devient un signal, sans mesure de stabilité. |
| C | Le savoir seulement, aucun outil. |

**Tests prévus pour A.** Une page piège (image sans dimensions qui pousse le texte) donne une réserve ; la même page avec ses dimensions n'en donne pas ; une page de 3 Mo déclenche le signal de poids ; une page légère, aucun.

---

## 2. B-04 — sections ordinaires (sous-lot 2, principe)

**État vérifié.**
- Le catalogue dit lui-même que ses scènes viennent « surtout du produit logiciel et du B2B ».
- Pour les sections ordinaires, il tient deux paragraphes (« Cartes », « Parties ordinaires ») et une ligne de geste dans `SAVOIR/STATE` : fonctionnalités, preuves, tarifs, questions fréquentes, contact et accès, pied de page.
- Ce sont pourtant les sections que les runs livrent ordinaires.

**Principe proposé.**
- Une route nouvelle, `BIBLIOTHEQUE/SECTIONS`, dans le catalogue, avec une entrée courte par section :
  - ce que la personne y cherche ;
  - la forme réflexe qui la rend ordinaire ;
  - deux ou trois leviers pour la rendre propre au sujet ;
  - le piège d'honnêteté, par exemple un témoignage inventé ou un logo de client absent ;
  - ce qui se vérifie sur capture.
- Sept sections : fonctionnalités, preuve (témoignages, chiffres, logos), tarifs, questions fréquentes, contact et accès (commerce local, horaires, adresse), formulaire d'inscription, pied de page.
- Environ 5 000 caractères, servis par leur route. Le tronc `DIRECTION` porte un seul renvoi, dans `BIBLIOTHEQUE/SEQUENCE`, d'environ 90 caractères.
- Le texte vous sera soumis entier avant intégration : c'est votre jugement de designer qui est en jeu.

## 3. B-03 — un savoir qui ne se voit pas (sous-lot 3, principe)

**État vérifié.** Aucune image dans les 22 fichiers de savoir. La taxonomie du style, les profils et les 41 formes du catalogue sont décrits par des phrases.

**Le risque à nommer.** Une image d'exemple se recopie. Le paquet évite déjà de fournir des thèses ou des objets d'exemple, pour qu'ils ne soient pas repris, et il lutte contre la convergence. Une planche « voici une bonne page » ferait converger les runs vers elle.

| Option | Principe |
|---|---|
| **A (recommandée)** | Des **planches de principes**, pas des exemples de style : chacune montre un mécanisme, en avant/après sur un même contenu neutre. Exemples de mécanismes : fonds voisins par la teinte ou par la valeur, vus en niveaux de gris ; rayons emboîtés ou non ; grand titre réglé ou non ; hiérarchie par la taille ou par le vide. Elles sont dessinées par du code du paquet (aucune image reprise), et chaque route qui porte le mécanisme renvoie à sa planche. **Six planches au plus**, que vous jugez à la vue avant intégration (votre règle 7). |
| B | Pas d'image dans le paquet : le « voir » passe par les références que l'agent rassemble à chaque run (`parcours.py references`, calibration avant le premier build), ce qui existe déjà. On le dit simplement dans le savoir. |
| C | Des pages d'exemple complètes, par profil de style. Je la déconseille, à cause du risque de convergence. |

---

## 4. Vérification prévue pour le sous-lot 1

1. Branche `savoir-contexte`.
2. Tests :
   - la nouvelle sous-section est servie par `SAVOIR/CONTEXT` et ne contient aucune citation d'auteur (PRO-01) ;
   - selon l'option, la mesure de stabilité et les signaux de poids, avec leurs pages pièges.
3. Le noyau et les troncs restent identiques.
4. Validation complète avec navigateur, archives régénérées, révision `R2026-11-15f`.

**Critère d'arrêt.** Si la mesure de stabilité n'est pas fiable sur une page locale, par exemple parce qu'elle varie d'une exécution à l'autre sur la même page, je ne la livre pas : je m'arrête et je vous montre les mesures.

## 5. Ce qu'il faut me dire

« D'accord, options A partout » suffit : le texte du § 1.2, l'option A du § 1.3, et le découpage avec son ordre. Les options A des § 2 et 3 n'engagent que la forme : leur texte et leurs planches vous seront soumis.

Pour corriger le texte du § 1.2, dites-moi la phrase et ce que vous voulez à la place.

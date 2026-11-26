# Lot 19 — Propositions : le niveau pro d'abord

Rédigé le 26 novembre 2026, après le run 25. Base : V1.5.0 (`R2026-11-25g`). Décision de Junior : « Pas de run sans. On se concentre sur le système et on poursuit. » Aucun run. Règle 1 : « D'accord » vaut pour les options A partout.

**Verdict de Junior sur le run 25** : « Ça fait généré et IA, et gadget, pas un vrai site pro […] et pas au niveau des références. »

## 0. Mesure

| Constat | Preuve |
|---|---|
| **À chaque run, la page joue une métaphore** au lieu d'être un site : livre (21), carton émaillé (22), affiche des départs (23), plan d'architecte (24), étiquette suspendue (25). | Runs 21 à 25. |
| **Le système pousse dans ce sens.** | Noyau : « **Pousser le geste.** Le geste qui porte l'idée se pousse jusqu'au bout » ; une esquisse « ne l'emporte que si elle bat » la modale. `CFT-01` : « Sur cette page, [un élément de l'inventaire] **devient** [le dispositif que la composition appelle] ». Pistes du tirage : « l'objet imprimé de son monde », « son rituel », « son lieu »… Lots 14 à 18 : oser, deuxième rang, armes égales, structure tirée. |
| **La modale contient l'idiome pro de la catégorie.** Au run 25, l'esquisse modale (photo de l'atelier, services, appel) était la plus proche d'un vrai site. Elle a perdu, comme à chaque run. | `Run25/livrable/planche-esquisses.png`. |
| **Le système dit déjà l'inverse, mais faiblement.** Le noyau : « Le genre se reconnaît au premier regard ; la singularité se joue d'abord dans l'objet, la donnée, la voix, la matière ou le détail. » `SAVOIR/FRAME` : « singularité sans rejet des conventions ». `SAVOIR/CONTEXT` : « [la singularité] ne requiert ni spectacle ni rupture de repère ». | `SKILL.md` l. 82 ; `design/savoir/fondements.md` ; `design/savoir/contexte.md`. |
| **Les marques de « généré » s'accumulent** : libellés décoratifs en chasse fixe, kraft, tampons, « N° 0412 », éléments inclinés, sur-titres ; un trait d'esprit à chaque section ; mentions « page de démonstration » visibles. | Runs 23 à 25 (captures). |
| **Sans photo, l'agent remplace l'image par un objet codé.** Le système prévoit pourtant l'emplacement marqué (« un asset manquant devient […] un emplacement marqué, jamais un faux asset »), mais en différé, sans dire quand le préférer. | `design/direction/diriger.md` l. 123. |
| **Tes références** : des produits finis, les conventions de leur catégorie tenues parfaitement, des images réelles, la singularité dans la marque et le détail. | `Reverse_2/References_Junior_lot1` à `lot3`. |

Noyau : 32 307 octets sur 33 000 (marge 693).

## 1. Sous-lot 19a — Un vrai produit d'abord (doctrine)

- **A (recommandée).**
  1. **Une ligne au noyau**, en tête des règles de direction (environ 330 octets) : « **Un vrai produit d'abord.** La page doit pouvoir passer pour celle qu'un bon studio livrerait à ce client : le genre se reconnaît et ses conventions sont tenues parfaitement ; l'idée vit dans la marque, le contenu et le détail. Une métaphore jouée par toute la page (objet imité, document simulé) est un gadget, sauf si le brief l'appelle. »
  2. **« Pousser le geste » précisé** : le geste est un détail, un composant, une donnée ou un cadrage poussés jusqu'au bout, pas un déguisement de la page.
  3. **La phrase d'idée de `CFT-01` élargie** : le dispositif peut être un détail (une présentation de la donnée, un composant, un cadrage d'image, une voix), pas seulement une scène entière.
  4. **La modale réhabilitée en esquisse pro** (`DIRECTION/DIVERGENCE`). Elle s'esquisse comme le ferait un bon studio : l'idiome de la catégorie, parfaitement tenu, avec ses emplacements d'image. La planche juge deux questions : laquelle passe pour un produit fini de sa catégorie, et laquelle se distingue sans cesser de l'être. Une esquisse qui se lit comme une démonstration de concept perd, sauf si le brief l'appelle.
  5. **Les pistes du tirage se traduisent en marque, en contenu ou en détail**, jamais en costume de page. On retire « l'objet imprimé de son monde » comme piste de page entière, et on la garde comme source de détail.
- **B.** Seulement les points 1 et 4.
- **C.** Ne rien changer à la doctrine ; traiter par la seule construction (lot suivant). Je ne la recommande pas : le run 25 a lu le savoir de construction, et le gadget est venu quand même.

## 2. Sous-lot 19b — Sans photo, concevoir pour la photo

- **A (recommandée).** Quand la catégorie vend par l'image (commerce, lieu, service, portfolio) et que les photos manquent, la mise en page se conçoit **pour des photos réelles**, avec des **emplacements conçus** : ratio, cadrage voulu, légende, ton dominant attendu, mention « photo à fournir » discrète. Ils remplacent l'objet codé qui tient lieu d'image. La génération reste exclue, comme tu l'as décidé. Une recette `emplacement-photo` (cadre au bon ratio, fond de ton, légende, consigne de prise de vue) et une phrase dans la règle d'asset, rendue lisible à l'étape CONSTRUCTION.
- **B.** La phrase seule, sans recette.

## 3. Sous-lot 19c — Les marques de « généré »

- **A (recommandée).**
  - Deux signaux de plus dans `verifier` (famille « Habillage de gabarit ») :
    - **chasse fixe décorative** : texte court en police à chasse fixe qui n'est ni une donnée, ni du code, ni un identifiant ;
    - **blocs inclinés** : rotation sur des blocs de contenu.
  - Une ligne dans la table de `SAVOIR/STATE` : « **Marques de démonstration** ». Elle couvre le papier ou le kraft simulés, les tampons, les numéros de pièce, l'écriture machine, les inclinaisons. Ce sont des signes de page générée quand ils ne viennent pas du vrai monde du client. Un seul se garde, sur l'idée, s'il passe le test de retrait.
- **B.** La ligne seule, sans signaux.

## 4. Sous-lot 19d — Le texte et les mentions d'exemple

- **A (recommandée).**
  - **Mentions d'exemple** : une seule, discrète, en pied de page (« contenus d'exemple : nom, adresse, prix… »). Le détail va dans la trace, pas dans des encarts « page de démonstration » ou des sous-titres « exemple » partout. La règle « marqué comme exemple » du noyau est précisée en ce sens (environ 100 octets).
  - **Texte** : simple et informatif d'abord ; un trait d'esprit au plus, à l'endroit de l'idée (`SAVOIR/CRAFT/CFT-06`).
- **B.** Les mentions seules.

## 5. Sous-lot 19e — Le test du vrai site

- **A (recommandée).** Une question en tête de la fiche de `verifier` (« D'abord ») et à l'atelier : « Passe-t-elle pour un produit fini de sa catégorie, livré par un bon studio ? Qu'est-ce qui fait démo ? » Aucun calcul : une question posée sur capture, à laquelle la trace répond.
- **B.** Rien.

## 6. Coût et budget

- **Noyau** : environ 450 octets (19a : 330 ; 19d : 100 ; un renvoi), sur 693 de marge. Si la marge manque, la ligne de 19a remplace une phrase plus faible du même bloc ; je le dirai.
- **Par run** : peu de changement ; une recette et deux signaux.

## 7. Gardes et tests (mutation rouge, échec nommé)

- **CORE-01** : « Un vrai produit d'abord » et sa phrase sur le gadget.
- **Signaux** : une page de test avec des libellés décoratifs en chasse fixe et des blocs inclinés est signalée ; une page de données en chasse fixe (prix, code) ne l'est pas.
- **Recette `emplacement-photo`** : ratio tenu à 390 et 1440 px, légende présente, aucune image fausse.
- **Pistes du tirage** : « l'objet imprimé de son monde » n'est plus tiré comme piste de page.
- Une mutation par garde.

## 8. Ce que le lot ne prouvera pas

- **Que les rendus passeront pour de vrais sites.** Seul ton regard le dira.
- **Le risque inverse, le retour au fade.** Si la modale gagne, la page peut redevenir générique. Le garde-fou est la question « se distingue-t-elle sans cesser d'être un vrai produit ? » et la singularité dans la marque et le détail.
- **Sans images réelles, un site de commerce reste incomplet.** Les emplacements conçus le diront honnêtement, sans le cacher sous un gadget.

## 9. Ordre

1. 19a à 19e ensemble : révision `R2026-11-25h`, publication V1.6.0.
2. Puis le lot de construction (fiches de composition, composants, techniques, mouvement, échelle typographique ; reprise du lot 17), qui sert ce niveau pro.
3. Un run de vérification, sur ta décision.

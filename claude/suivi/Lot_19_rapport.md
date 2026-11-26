# Lot 19 — Rapport : le niveau pro d'abord ; publication V1.6.0

- **Révision** : `R2026-11-25h`, livrée le 26 novembre 2026. Publication **V1.6.0**.
- **Branche** : `lot-19`.
- **Décision** : « À toi le choix » ; options A retenues.
- **Origine** : le verdict de Junior sur le run 25 (« généré, IA, gadget, pas un vrai site pro »).
- **Runs** : aucun.

## 1. Ce qui change

| Sous-lot | Où | Changement |
|---|---|---|
| **19a Un vrai produit d'abord** | Noyau, bloc POSTURE (`DIRECTION/STANDARD`) | Nouvelle règle : « La page doit pouvoir passer pour celle qu'un bon studio livrerait à ce client : le genre se reconnaît et ses conventions sont tenues parfaitement ; l'idée vit dans la marque, le contenu et le détail. Une métaphore jouée par toute la page (objet imité, document simulé) est un gadget, sauf si le brief l'appelle. » « Pousser le geste » précisé : le geste est « un détail, un composant, une donnée ou un cadrage ». |
| 19a | Noyau, ligne « Diverger sur image » ; `DIRECTION/DIVERGENCE` | La modale est « esquissée en vrai produit », comme la ferait un bon studio, avec ses emplacements d'image. La planche juge « laquelle passe pour un produit fini de sa catégorie, et laquelle se distingue sans cesser de l'être ». Une démonstration de concept perd, sauf si le brief l'appelle. |
| 19a | `DIRECTION/DIVERGENCE`, `SAVOIR/CRAFT/CFT-01` | « L'objet imprimé de son monde » sort des pistes du tirage. Une règle nouvelle : « Une piste se traduit en marque, en contenu ou en détail, jamais en costume de page ». La phrase d'idée dit que le dispositif est le plus souvent un détail, jamais un déguisement de toute la page. |
| **19b Concevoir pour la photo** | `CNT-01` (suite différée), recette `emplacement-photo` | Une photo manquante devient un emplacement conçu (ratio, cadrage voulu, légende, ton attendu, « photo à fournir »), jamais un objet codé. Onze recettes en tout. |
| **19c Marques de démonstration** | `parcours.py` (finition, donc `verifier`), `SAVOIR/STATE` | Deux signaux (famille « Habillage de gabarit ») : libellés décoratifs en chasse fixe (hors donnée, code, adresse) et blocs de contenu inclinés. Une ligne de table « Marques de démonstration » : kraft ou papier simulés, tampons, numéros de pièce, écriture machine, inclinaisons, mentions répétées. |
| **19d Mentions et texte** | Noyau (`CNT-01`), `CFT-06` | « Une mention discrète, en pied de page, dit ce qui est exemple ; le détail va dans la trace. » « Simple d'abord » : le texte informe, avec un trait d'esprit au plus. |
| **19e Test du vrai site** | Fiche de `verifier` (section 4), atelier (`ACTION/ATELIER-EDITION`) | Question : « Passe-t-elle pour un produit fini de sa catégorie, livré par un bon studio ? Qu'est-ce qui fait démo ? » |

- **Noyau** : 32 835 octets sur 33 000 (+528). Une première version arrivait à 32 965 ; la phrase sur la photo manquante est passée dans la suite différée du même bloc, servie avec la règle.
- **Marge restante** : 165 octets. **Le prochain lot qui touche au noyau devra en libérer**, ou relever le budget sur décision.
- **Écart à la proposition** : la ligne « Marques de démonstration » est une ligne de table à part, comme prévu. Les deux signaux sont rangés sous « Habillage de gabarit », dont la question est la plus proche.

## 2. Gardes, tests et mutations rouges

- **CORE-01** : deux phrases protégées, « **Un vrai produit d'abord.** » et la phrase sur le gadget.
- **Tests** (`parcours`, 201 cas) :
  - marques de démonstration relevées sur une page piège ;
  - rien sur une page où la chasse fixe porte des prix, une heure et du code ;
  - recette `emplacement-photo` vérifiée dans le navigateur ;
  - pistes du tirage sans « objet imprimé ».

| Mutation | Résultat |
|---|---|
| Détection de la chasse fixe décorative retirée | Rouge : P123 |
| Détection des blocs inclinés retirée | Rouge : P123 |
| Recadrage mobile retiré de la recette `emplacement-photo` | Rouge : P148 |
| Phrase sur le gadget retirée du noyau | Rouge : CORE-01 |

## 3. Préparation et livraison

- **Préparation complète** : réussie en **466 s**. Tests : `parcours` 201, `read_route` 107, `regard` 42, `check_render` 265… ; reproductibilité vérifiée.
- **Commits** : `cdec44d` sur `lot-19`, fusionné en `24d004e` sur `master` (`--no-ff`).
- **Archive GitHub** : les 164 fichiers sont identiques au commit.
- **Sortie** : `Design_Governance_V1_GITHUB_R2026-11-25h.zip` (sha256 `b3256f39…3bfa`) ; dans `claude/livraison/R2026-11-25h/` : archive Local (sha256 `2d292605…f356`) et bundle vérifié. La `25g` est retirée de DG-777.

## 4. Ce que le lot ne prouve pas

- **Que les rendus passeront pour de vrais sites** : seul le regard de Junior le dira.
- **Le risque inverse** : le retour au fade, si la modale gagne trop souvent. Le garde-fou est la question « se distingue-t-elle sans cesser d'être un vrai produit ? ».
- **Sans images réelles**, un site de commerce reste incomplet ; les emplacements conçus le disent honnêtement.
- **Le coût du lot 18** (+63 % de lecture du cache au run 25) n'est pas traité ici.

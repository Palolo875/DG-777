# Lot 14c — Rapport : quatre signaux de finition

- **Révision** : `R2026-11-25c`, livrée le 25 novembre 2026. Fin du lot 14 : publication **V1.2.0** (voir § 4).
- **Branche** : `lot-14c`.
- **Décisions** : « D'accord, on lance » (options A du lot 14) ; **H (vidéo du mouvement) retirée** sur décision de Junior (« Ok », après mon avis : les pages HTML jointes sous des noms neutres font mieux, sans code).
- **Runs** : aucun.

## 1. Ce qui change

| Signal | Où | Mesure | Question |
|---|---|---|---|
| **Texte collé au bord** | `finition` (donc `verifier`), geste « Gestion du vide » | Glyphes d'un texte à moins de 8 px du bord de la fenêtre (`BORD_MIN`, `[À ADAPTER]`), ligne par ligne ; un texte pleine largeur est ignoré | Collé par choix (fond perdu, bandeau), ou marge oubliée à cette largeur ? |
| **Contraste non textuel** | `finition`, source `ACTION/GATE-A` | Traits et remplissages d'un SVG non décoratif, et bords de champ qui ne se détachent pas par leur fond, sous 3:1 contre le fond (WCAG 2.2, 1.4.11) | Porte-t-il une information ? Si oui, 3:1 ; sinon, le dire décoratif. |
| **Commande au clavier** | `acces` (donc `verifier`) | Curseur, interrupteur, case personnalisée, onglet : la touche attendue (flèche ou espace) ne change ni sa valeur ni son état | Se manie-t-elle au clavier comme son rôle l'annonce ? |
| **Contraste pendant le mouvement** | `mouvement` (donc `verifier`) | Textes du premier écran sous leur seuil à une image intermédiaire de l'entrée, alors qu'ils le passent à la fin (mesure de `regard` sur le fond réel, image par image) | Doit-il se lire pendant l'entrée ? Sinon, paraître après son fond. |

**Un ajustement trouvé par un test existant** : la première version du signal de bord mesurait la boîte de l'élément ; un texte aligné à droite dans un bloc collé au bord était signalé à tort (test P112). La mesure porte maintenant sur les glyphes eux-mêmes.

**Évaluation (remplace H)** : pour tout rendu animé, les pages HTML sont jointes aux planches sous des noms neutres (`A.html`, `B.html`), pour que Junior juge le mouvement en vrai.

## 2. Tests et mutations rouges

4 cas avec navigateur (`parcours` : 185 cas), sur une page piège qui déclenche chaque signal et une page propre qui n'en déclenche aucun.

| Mutation | Résultat |
|---|---|
| Le signal de bord n'est plus émis | Rouge : P141 |
| Le signal de contraste non textuel n'est plus émis | Rouge : P142 |
| L'inertie au clavier n'est plus relevée | Rouge : P143 |
| Le contraste pendant l'entrée n'est plus mesuré | Rouge : P144 |

## 3. Préparation et livraison

- **Préparation complète** : réussie au second passage, en **469 s**. Le premier s'est arrêté en 12 s sur LIS-01 : j'avais allongé au-delà de 500 signes la cellule de `verifier` dans `scripts/README.md` ; resserrée. Le mode `--rapide` l'avait vu aussi, mais je l'avais enchaîné sans attendre son résultat.
- Tests : `parcours` 185, audit 196, `read_route` 106… ; quatre cartes sans défaut bloquant ; reproductibilité vérifiée.
- **Commits** : `419befb` sur `lot-14c`, fusionné en `2b52bf8` sur `master` (`--no-ff`).
- **Archive GitHub** : les 164 fichiers sont identiques au commit.
- **Sortie** : `Design_Governance_V1_GITHUB_R2026-11-25c.zip` (sha256 `689a5353…8203`) ; `claude/livraison/R2026-11-25c/` : archive Local (sha256 `2fd4df32…c533`) et bundle vérifié. La `25b` est retirée de DG-777.

## 4. Fin du lot 14 : V1.2.0

- **Version publique V1.2.0** : manifeste, titre du README (et version anglaise), fiche et notes de version, guide 3, citation (1.2.0, 25 novembre 2026), cartes régénérées ; garde VER-01 verte.
- **Journal des changements** : entrée V1.2.0 (« Voir », « Oser », quatre signaux, préparation plus rapide, budget du noyau à 33 000).
- Noyau : 31 699 octets sur 33 000.

## 5. Ce que ce sous-lot ne prouve pas

- Les signaux sont des questions, pas des verdicts : un texte au bord peut être voulu, un graphique pâle peut être décoratif.
- Le contraste non textuel est calculé contre la couleur de fond déclarée, pas contre une image ou un dégradé.

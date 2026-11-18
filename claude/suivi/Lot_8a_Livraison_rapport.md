# Lot 8a — Passe de livraison, constats restants : rapport

18 novembre 2026. Révision livrée : `R2026-11-15j` (commit `8b97ae1`, fusionné dans master en `3cc754b`). Document hors du paquet.

Les options A ont été appliquées partout. La validation complète avec navigateur passe, et l'archive GitHub est identique au commit, fichier par fichier.

## 1. Ce qui a changé

| Constat | Changement |
|---|---|
| F-09 | La note sous « Les responsabilités reliées » s'aligne à gauche, sous son titre, en mobile. Les cartes ont été régénérées ; leur fraîcheur et leur rendu sont contrôlés. Capture à 390 px jointe : `Lot_8a_carte_390_apres.png`. |
| E-09 | « Règles d'or » est retirée de `SAVOIR/INTEGRITY` : chaque règle reste chez son propriétaire. `REPASSE` s'intitule désormais « repasse ciblée, selon le mode ». |
| E-04 | Les 17 codes en capitales que citent les guides et le README, hors blocs de code, ont tous leur ligne au glossaire. Une garde le vérifie désormais (GLO-02) : tout nouveau code cité devra y être défini. |
| D-13 | Les contrats de maintenance disent pourquoi le noyau se compte en octets (ce que charge l'hôte) et le tronc en caractères (ce que lit l'agent). |
| D-18 | Les archives prennent la date du dernier commit. Elles restent reproductibles pour un même commit. Hors dépôt git, la date est fixe et déclarée (1er janvier 2026). |
| E-11 | `ACTION/PIPELINE-DIRECTION` a son propre fichier, `gouvernance/pipeline.md`. `travail.md` garde les conditions et la fiche de travail. |
| E-12 | Le gabarit `EXECUTION-SNAPSHOT` (douze champs sans usage) est retiré. Les règles de reprise restent, sous « Reprendre un run ». |
| F-10 | Deux exemples passent en trace légère : la première scène identitaire, et le profil de style. Le composant partagé gagne une preuve sur capture (`EVIDENCE`). Les exemples comptent maintenant trois traces légères et deux traces complètes, et les trois traces légères passent la commande `parcours.py trace`. |
| Typographie de lecture | Le corps, l'interligne et la mesure passent dans `SAVOIR/TYPE` (« Texte de lecture »). `SAVOIR/CONTEXT` garde ce qui relève de l'accessibilité et renvoie au savoir typographique. |
| B-20 | Écarté, avec raison, comme proposé. |

## 2. Écarts et points à relire

1. **Il n'y avait rien à ajouter au glossaire.** Le code `CORRECTION` que j'avais signalé comme absent apparaît seulement dans un bloc d'exemple du guide 3. Mon premier comptage ne retirait pas les blocs de code. Hors blocs, les 17 codes sont tous définis.
2. **Deux conditions de façade s'appuyaient sur les exemples en trace complète.**
   - **LCF-45** exigeait un champ `MODAL:` dans les exemples. Il accepte désormais aussi la ligne de trace légère « MODAL, TRAME ET PARTI: ».
   - **LCF-14** exigeait une preuve sur capture (`EVIDENCE`). Pour la tenir, elle est passée dans l'exemple du composant partagé, où elle a sa place.
3. **Deux phrases qui citaient la vue retirée ont été réécrites.** Celle du savoir sur les connexions renvoie maintenant à « Reprendre un run ». Celle qui parle de la projection YAML ne mentionne plus que la `RUN_CARD`.
4. **Les archives portent la date du dernier commit fusionné avant la préparation.** Ici, 18 novembre 2026 à 10 h 38.

## 3. Vérification

| Contrôle | Résultat |
|---|---|
| Noyau | identique (45 210 / 46 000 octets) |
| Tronc `DIRECTION` | +238 caractères pour la typographie de lecture : 31 398, marge 3 602 |
| Autres troncs | identiques |
| Régressions d'audit | 150 cas, dont 4 nouveaux (codes glosés avec mutation rouge, déroulé dans son fichier, reprise sans gabarit, exemples en trace légère) ; le test du build vérifie aussi la date des archives |
| Parcours | 152 cas, dont : les trois traces légères des exemples sont conformes |
| Recette, regard, lecteur, journal, budget, préparation | A 119, C 65, B 81 / 39 / 105 / 18 / 19 / 10 cas |
| Rendu des supports | trois cartes sans défaut bloquant à 390, 768 et 1440 px |
| Durée de préparation | 11 min 41 s |

Empreintes :
- GitHub `3214be42…5ce6a1`
- Local `394b18fd…7e8051`

## 4. Suite

**8b — la passe des sept critères de livraison.** Mesures d'abord :
- point d'entrée des trois publics ;
- redites entre guides et propriétaires (F-06) ;
- restes ;
- seuils de lisibilité ;
- langue ;
- charge de procédure pour l'agent et le mainteneur ;
- installation rejouée depuis une copie propre (F-13), commandes du README exécutées, et un exemple complet qui correspond à ce que produit le système.

Les propositions suivront, avec les chiffres.

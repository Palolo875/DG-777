# Lot 12a — Rapport : des pages d'entrée en mots, et à jour

- **Révision** : `R2026-11-15v`, livrée le 22 novembre 2026.
- **Branche** : `lot-12a`.
- **Décision** : « D'accord » à `Lot_12_Propositions.md` : options A partout. J'en déduis aussi l'accord sur mes recommandations D4 à D7 ; je les rappellerai avant 12d, seul sous-lot qu'elles touchent.
- **Runs** : aucun.

## 1. Ce qui change

| Proposition | Changement |
|---|---|
| **E3** Des mots à la place des codes | 3 codes nus retirés : `guides/2-comprendre.md` (étapes 1 et 2, devenues des liens nommés « classer avant d'agir » et « classer, puis charger ») ; `guides/3-maitriser.md` (exemple de trace : « geste de finition »). Les 11 autres occurrences mesurées étaient des commandes du lecteur, un exemple annoncé, des statuts expliqués ou le sigle « UI/UX » : elles restent. |
| | Glossaire, « Regard séparé » : « Facultatif, si l'environnement le permet : une critique faite par un second agent… » |
| **E4** + **E3** Deux gardes | **DOC-01** (garde 28) : dans le README et les guides 1 à 3, aucun code de route ou de concept, sauf dans une commande `read_route.py` ou après « par exemple ». **DOC-02** (garde 29) : toute page Markdown du paquet à **trois** clics au plus du README (voir l'écart 2). |
| **E1** README | Section « Comment l'agent lit » : noyau (règles, une ligne par obligation, index), tronc, sections au signal, outils, sans exécution de code. Ligne « Ce que coûte un run » : mesure du 20 novembre 2026, quatre runs en mode direction, de 116 à 208 tours et de 13 à 29 images, **avant** les lots 10B et 11, à refaire au lot 13. |
| **E8** Guide de niveau 1 | Section « Sans navigateur ni exécution de code » : ce qui marche, ce qui manque (déclaré non vérifié), ce que la personne peut faire (son regard remplace la capture), et la lecture sans agent. |
| **E7** Route d'instrumentation | Non déplacée (option A). |

**Écart 1.** J'avais compté 14 codes. En les relisant un par un, seuls 3 étaient de vrais codes nus. La garde DOC-01 tolère donc les commandes du lecteur et les exemples annoncés, et ne compte pas les statuts (`N/A-JUSTIFIED`…), qui sont du vocabulaire expliqué au glossaire.

**Écart 2 : DOC-02 à trois clics, pas deux.** La première préparation complète a échoué sur le contrôle de déplacement (`validate_all.py`) : il range une section dans un fichier neuf et exige que la validation de structure reste verte.
- Le fichier neuf n'était relié nulle part. J'ai ajouté à la procédure (`maintenance/README.md`, étape « Manifeste ») qu'un fichier neuf entre aussi dans le README de son dossier, et le contrôle de déplacement fait de même.
- Il restait à trois clics : le README de `design/savoir/` est lui-même à deux clics du README du paquet. Exiger deux clics obligerait à relier chaque fichier neuf depuis une page de premier niveau.
- La limite est donc **trois clics** (paquet, dossier, sous-dossier). Aujourd'hui, toutes les pages sont à deux clics au plus ; la garde attrape toujours les orphelines et les chaînes longues.

## 2. Mutations rouges

7 cas (classe `PagesPourLesPersonnes`). La phrase d'origine du guide 2 sert de cas refusé.

| Mutation | Résultat |
|---|---|
| Les commandes `read_route.py` ne sont plus tolérées | Rouge : `test_commande_et_exemple_admis`, `test_pages_reelles` |
| « par exemple » n'est plus toléré | Rouge : les deux mêmes |
| L'erreur DOC-01 n'est plus écrite | Rouge : `test_code_nu_refuse` |
| Profondeur admise à 4 clics | Rouge : `test_quatre_clics_refuses` |
| Une page inatteignable n'est plus relevée | Rouge : `test_page_orpheline_refusee` |

## 3. Préparation et livraison

- **Préparation complète** : `--require-browser --empreintes`, réussie **au second passage** (le premier a échoué sur le contrôle de déplacement : écart 2).
  - Tests : régressions d'audit 180 (173 + 7), budget 19, `parcours` 176, `read_route` 106, `regard` 41, journal 19, `check_render` A, B et C ; contrôle de déplacement PASSED.
  - Validations de structure, de carte de lecture, complète et locale : PASSED. Garde PRO-01 active.
- **Commits** : `8bdb51e` sur `lot-12a`, fusionné en `0ec8c83` sur `master` (`--no-ff`).
- **Archive GitHub** : les 151 fichiers sont identiques au commit.
- **Sortie** :
  - `Design_Governance_V1_GITHUB_R2026-11-15v.zip` (sha256 `cef9da0f…75ec`), à côté de la `k` ;
  - `claude/livraison/R2026-11-15v/` : archive Local (sha256 `bcc137f6…5aea`) et bundle vérifié.
  - La `u` est retirée de DG-777. Elle reste dans l'historique et dans le bundle.

## 4. Ce que ce sous-lot ne prouve pas

- Qu'un lecteur neuf comprend le système en deux minutes : seule une lecture extérieure le dira.
- La ligne de coût est une mesure ancienne, dite comme telle.

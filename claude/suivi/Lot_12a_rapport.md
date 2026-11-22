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
| **E4** + **E3** Deux gardes | **DOC-01** (garde 28) : dans le README et les guides 1 à 3, aucun code de route ou de concept, sauf dans une commande `read_route.py` ou après « par exemple ». **DOC-02** (garde 29) : toute page Markdown du paquet à deux clics au plus du README. |
| **E1** README | Section « Comment l'agent lit » : noyau (règles, une ligne par obligation, index), tronc, sections au signal, outils, sans exécution de code. Ligne « Ce que coûte un run » : mesure du 20 novembre 2026, quatre runs en mode direction, de 116 à 208 tours et de 13 à 29 images, **avant** les lots 10B et 11, à refaire au lot 13. |
| **E8** Guide de niveau 1 | Section « Sans navigateur ni exécution de code » : ce qui marche, ce qui manque (déclaré non vérifié), ce que la personne peut faire (son regard remplace la capture), et la lecture sans agent. |
| **E7** Route d'instrumentation | Non déplacée (option A). |

**Écart que je signale.** J'avais compté 14 codes. En les relisant un par un, seuls 3 étaient de vrais codes nus. La garde DOC-01 tolère donc les commandes du lecteur et les exemples annoncés, et ne compte pas les statuts (`N/A-JUSTIFIED`…), qui sont du vocabulaire expliqué au glossaire.

## 2. Mutations rouges

7 cas (classe `PagesPourLesPersonnes`). La phrase d'origine du guide 2 sert de cas refusé.

| Mutation | Résultat |
|---|---|
| Les commandes `read_route.py` ne sont plus tolérées | Rouge : `test_commande_et_exemple_admis`, `test_pages_reelles` |
| « par exemple » n'est plus toléré | Rouge : les deux mêmes |
| L'erreur DOC-01 n'est plus écrite | Rouge : `test_code_nu_refuse` |
| Profondeur admise à 3 clics | Rouge : `test_trois_clics_refuses` |
| Une page inatteignable n'est plus relevée | Rouge : `test_page_orpheline_refusee` |

## 3. Préparation et livraison

À compléter.

## 4. Ce que ce sous-lot ne prouve pas

- Qu'un lecteur neuf comprend le système en deux minutes : seule une lecture extérieure le dira.
- La ligne de coût est une mesure ancienne, dite comme telle.

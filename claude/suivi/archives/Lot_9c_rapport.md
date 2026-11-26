# Lot 9c — Rapport

- **Révision** : `R2026-11-15m`.
- **Branche** : `lot-9c`, fusionnée dans `master` avec `--no-ff`.
- **Décision** : « Oui » au document de propositions (`Lot_9c_Propositions.md`). Les options A s'appliquent partout.
- **Runs** : aucun.

## 1. Ce qui est intégré

| Proposition | Ce qui change | Garde |
|---|---|---|
| **P1** La modale au second degré s'observe | Dans `DIR-LEVIERS`, au noyau, la modale au second degré « ne s'estime pas : c'est ta première idée astucieuse, écrite telle qu'elle vient avant les pistes ». Les probabilités sont « un ordre de grandeur, jamais une preuve de rareté ». La piste d'attribut devient « sa forme ou son deuxième attribut qui le signe (le plus saillant est déjà modal) », dans le noyau et dans `SAVOIR/IDENTITY`. `tirage` tire désormais cette piste reformulée. | P21, P22 (`test_parcours.py`) |
| **P2** Registre des convergences | Il reste **hors paquet** : `suivi/Convergences_observees.md`, avec deux entrées (PILOT 9b). | — |
| **P3** C-1 et C-2 | Dans `journal_mobilisation.py`, une route du tronc écrite dans un fichier (`--fichier` ou redirection) n'est plus rangée dans les « Manques ». Elle va dans une rubrique « Lu hors journal (non observable) », puisque la règle de vitesse demande cette forme. Une route filtrée ou jetée reste un manque. Le libellé du tableau devient « lue hors journal, non observable ». | `test_tronc_ecrit_dans_un_fichier_n_est_pas_lu`, `test_tronc_filtre_reste_un_manque` |

Sont aussi mis à jour : `maintenance/evolution.md` (ligne `DIRECTION/DIVERGENCE`), `maintenance/README.md` (contenu de la fiche) et la fiche de version.

**Noyau** : 45 817 octets, pour un plafond de 46 000.

**Contrôle sur un vrai journal** : la fiche du run 17l, régénérée, range maintenant les huit routes du tronc écrites dans un fichier sous « Lu hors journal ». Ses « Manques » disent « servi en entier ».

## 2. Mutations rouges

| Mutation | Résultat |
|---|---|
| « Première idée astucieuse » retirée | Rouge : P21 |
| « Jamais une preuve de rareté » retiré | Rouge : P21 |
| Retour à « un attribut qui le signe » | Rouge : P22 |
| Route écrite dans un fichier remise dans les manques | Rouge : `test_tronc_ecrit_dans_un_fichier_n_est_pas_lu` |
| Rubrique « Lu hors journal » retirée | Rouge : même test |
| Route filtrée sortie des manques | Rouge : `test_tronc_filtre_reste_un_manque` |

**Erreur en cours de route.** Mon premier lancement des mutations les donnait toutes rouges, mais à cause d'un **plantage** du test : il manquait un import de `re`. J'ai repéré que ce rouge ne valait rien, corrigé le test, et relancé les mutations en distinguant un échec nommé d'un plantage.

## 3. Préparation et livraison

- **Préparation complète** : `--require-browser --empreintes`, réussie du premier coup.
  - Tests : `parcours` 161 cas avec navigateur ; journal 19 ; `read_route` 106 ; `check_render` A, B et C ; `regard` 39.
  - Validations complète et locale : PASSED.
- **Avant la préparation** : une cellule de `maintenance/README.md` dépassait 500 signes (LIS-01). Je l'ai raccourcie.
- **Commits** : `569494f` sur `lot-9c`, fusionné en `f9cf468` sur `master` (`--no-ff`).
- **Archive GitHub** : les 151 fichiers sont identiques au commit, comparés un à un.
- **Sortie** :
  - `Design_Governance_V1_GITHUB_R2026-11-15m.zip` (sha256 `c3127d81…6132`), à la racine de DG-777 ;
  - dans `claude/livraison/R2026-11-15m/` : `Design_Governance_V1_LOCAL_R2026-11-15m.zip` (sha256 `153c938c…5f16`) et le bundle `--branches`, vérifié.

## 4. Ce que ce lot ne prouve pas

- Que la convergence baissera. P1 change la façon dont l'agent nomme la modale au second degré et choisit l'attribut ; seul un run le dira, avec deux agents sur un même brief.
- Que l'attribut « le plus saillant » sera bien reconnu. C'est un jugement de l'agent.

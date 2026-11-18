# Registre des runs

Paquet installé depuis l'archive livrée, dans un dossier vide. Agent neuf sans contexte.

| Run | Date | Paquet | Brief | Agent | Modèle | Effort | Mode imposé | Journal | Coût |
|---|---|---|---|---|---|---|---|---|---|
| 9 | 2026-11-18 | R2026-11-15k | Landing « Quote-part » | non consigné | non consigné | non consigné | non consigné | `DG_JOURNAL` | non consigné |
| 10 | 2026-11-18 | R2026-11-15k | Accueil du festival « Les Lueurs » | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun | `DG_JOURNAL` demandé dans le prompt | ≈21 min, 85 appels, ≈300 k jetons |
| 11 | 2026-11-18 | R2026-11-15k | Composants data viz, tableau de bord public de vélos en libre-service | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (STANDARD choisi) | `DG_JOURNAL` demandé dans le prompt | ≈17 min, 58 appels, ≈289 k jetons |
| 12 | 2026-11-18 | R2026-11-15k | Identité et affiche A2 de « La Halle », lieu culturel | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (DIRECTION choisi) | `DG_JOURNAL` demandé dans le prompt | ≈325 k jetons ; interrompu par la limite d'usage puis repris (même agent, message de reprise) |
| 13 | 2026-11-18 | R2026-11-15k | Écran de planification d'un cabinet de kinésithérapie | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun | `DG_JOURNAL` demandé dans le prompt | interrompu par la limite d'usage (5 h), partiel dans `RunNN_partiel/` |
| 14 | 2026-11-18 | R2026-11-15k | Fiche produit du service « Grès de Loire », céramiste | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (DIRECTION choisi) | `DG_JOURNAL` demandé dans le prompt | ≈320 k jetons ; interrompu par la limite d'usage puis repris (même agent, message de reprise) |

Prompt type (runs 10 et 11) : dossier de travail, skill à lire depuis `SKILL.md`, variable `DG_JOURNAL`, dépendances installées, brief entre guillemets, « Je ne serai pas disponible », livrables (HTML autonome, captures à 1440 et 390, trace).

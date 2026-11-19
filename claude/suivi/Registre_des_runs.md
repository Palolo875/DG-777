# Registre des runs

Paquet installé depuis l'archive livrée, dans un dossier vide. Agent neuf sans contexte.

| Run | Date | Paquet | Brief | Agent | Modèle | Effort | Mode imposé | Journal | Coût |
|---|---|---|---|---|---|---|---|---|---|
| 9 | 2026-11-18 | R2026-11-15k | Landing « Quote-part » | non consigné | non consigné | non consigné | non consigné | `DG_JOURNAL` | non consigné |
| 10 | 2026-11-18 | R2026-11-15k | Accueil du festival « Les Lueurs » | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun | `DG_JOURNAL` demandé dans le prompt | ≈21 min, 85 appels, ≈300 k jetons |
| 11 | 2026-11-18 | R2026-11-15k | Composants data viz, tableau de bord public de vélos en libre-service | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (STANDARD choisi) | `DG_JOURNAL` demandé dans le prompt | ≈17 min, 58 appels, ≈289 k jetons |
| 12 | 2026-11-18 | R2026-11-15k | Identité et affiche A2 de « La Halle », lieu culturel | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (DIRECTION choisi) | `DG_JOURNAL` demandé dans le prompt | ≈325 k jetons ; interrompu par la limite d'usage puis repris (même agent, message de reprise) |
| 13 | 2026-11-18 | R2026-11-15k | Écran de planification d'un cabinet de kinésithérapie | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (STANDARD choisi) | `DG_JOURNAL` demandé dans le prompt | ≈330 k jetons ; interrompu par la limite d'usage puis repris (même agent, message de reprise) |
| 14 | 2026-11-18 | R2026-11-15k | Fiche produit du service « Grès de Loire », céramiste | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (DIRECTION choisi) | `DG_JOURNAL` demandé dans le prompt | ≈320 k jetons ; interrompu par la limite d'usage puis repris (même agent, message de reprise) |
| 15 | 2026-11-18 | R2026-11-15k | Accueil du festival « Les Lueurs » (même brief que le run 10) | **Claude, à la main**, avec le contexte des runs précédents (pas un agent neuf) | celui de la session | — | aucun (DIRECTION choisi) | `DG_JOURNAL` | 3 générations Figma ; voir `Run15/notes_de_run_Claude.md` |
| 16 | 2026-11-19 | R2026-11-15k | Billet électronique de concert (salle Le Rotonde, Angoulême ; artiste et genre au choix de l'agent) — série « capacité esthétique », code natif | sous-agent `general-purpose` | celui de la session (non vérifié) | par défaut | aucun (DIRECTION choisi) | `DG_JOURNAL` demandé dans le prompt | ≈17 min, 76 appels, ≈275 k jetons ; erreur du brief : le 14 mars 2027 est un dimanche, relevée par l'agent |

Prompt type (runs 10 et 11) : dossier de travail, skill à lire depuis `SKILL.md`, variable `DG_JOURNAL`, dépendances installées, brief entre guillemets, « Je ne serai pas disponible », livrables (HTML autonome, captures à 1440 et 390, trace).

Run 16 et suivants (série « capacité esthétique ») : même prompt type, plus une consigne de ressources : Internet gratuit et sans compte autorisé ; génération d'images, outils branchés (Figma, Canva, Adobe, connecteurs) et services payants interdits. Livrables : HTML autonome, capture ×2 à 390 px, deux ou trois agrandissements de détails.

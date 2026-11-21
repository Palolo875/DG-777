# Lot 9d — Propositions (constats reportés B-4, B-5, E-1, E-2)

Rédigé le 20 novembre 2026. Base : `R2026-11-15m` (`master` `f9cf468`). Aucun run.

Règle 1 : rien n'est intégré sans décision. « D'accord » vaut pour les options A partout.

## 0. Relecture des constats (règle 4)

| Constat | État au 20 novembre | Preuve |
|---|---|---|
| **B-4** Sources d'images pauvres | **Plus reproduit.** Au PILOT, les agents ont trouvé et intégré des images de Commons (phare de Ploumanac'h, avec licence créditée) et regardé un bol du Song à l'Art Institute of Chicago (domaine public). Ce qui reste est une limite juste : pas de photo des pièces de l'artiste du brief, que personne ne peut inventer. | Journaux 17k, 18k, 18l (`references --commons`, `--url`) |
| **B-5** Pas de calibration en `STANDARD` | **Toujours vrai dans le texte** : le bloc `ANCRE` du noyau limite « Calibrer le niveau » aux surfaces `DIRECTION`. **Non reproduit en pratique au PILOT** : les deux runs `STANDARD` (18k, 18l) ont regardé des références (maree.info, guide du port, Commons). | `design/direction/standard.md`, bloc `ANCRE` ; journaux 18k et 18l |
| **E-1** La voix du designer passe dans la page | **Observé une fois** (run 14), **non reproduit au PILOT**. Les mentions vues au PILOT (« dessiné en code », « données d'exemple ») sont des marquages demandés par le système, en langage produit. **Aucune règle** ne nomme ce défaut : `SAVOIR/CRAFT/CFT-06` (écriture) ne le cite pas. | Rapport du lot 9 ; captures du PILOT ; `CFT-06` |
| **E-2** Polices libres, sûres et à la mode | **Confirmé, et c'est le plus net.** Au PILOT, les quatre agents ont puisé dans **le même vivier** : Fraunces, Young Serif, Bricolage Grotesque, Instrument Sans, Cormorant, Barlow, Inter, IBM Plex. Ils ont retenu Young Serif, Fraunces, Plex Sans Condensed et Barlow. | Journaux (`polices`) des quatre runs |

### Pourquoi E-2 persiste (vérifié)

- `SAVOIR/TYPE-VOIX` demande déjà de chercher « par construction, pas par nom », « dans les fonderies de `SAVOIR/TOOLS/MOYENS`, pas dans une liste de polices connues ».
- `MOYENS` nomme Google Fonts, **Fontshare**, **Velvetyne** et **Collletttivo**.
- **Mais `parcours.py polices` ne sait télécharger que depuis Fontsource et Google Fonts.** L'outil ramène donc vers le vivier le plus fréquent.
- `SAVOIR/TOOLS/CONVERGENCE` nomme Inter et « serif de caractère » de façon générale, sans les familles de la vague actuelle.

### Recherche (Exa et WebSearch)

| Source | Ce qu'elle dit |
|---|---|
| C. Vaduvescu, *The Next Default*, novembre 2026 | Les consignes « anti-slop » de 2025 recommandaient elles-mêmes Fraunces, Bricolage Grotesque, Space Grotesk et Playfair, plus des appariements « serif + géométrique ». Ces polices sont devenues les nouveaux signes d'une page générée : « le remède devient le look ». Un détecteur appliqué à environ 1 600 projets Show HN classe Space Grotesk, Instrument Serif, Fraunces et Bricolage parmi les « polices d'affichage de gabarit ». Le lien de cause à effet reste une corrélation, et l'auteur le dit. |
| Muzli, *Font pairings 2026*, 2 190 sites de galeries de design | Inter apparaît sur 13 % des sites, et aucune autre police ne dépasse 5 %. Mais 94 % des appariements n'apparaissent que sur un seul site : **les polices convergent, les paires non.** |
| WIRED, *AI Has Come for Serif Fonts*, juin 2026 | Les serifs de caractère sont devenus un signe de l'esthétique IA (« tasteslop »). |
| Fontshare, FAQ et licence ITF FFL v2.0 (août 2026) | Polices gratuites, usage commercial permis, auto-hébergement permis. La licence interdit de modifier la police, de la sous-ensembler et de la convertir. Une API CSS publique existe ; **je l'ai vérifiée depuis l'environnement**, elle répond. Le catalogue compte 100 familles : 64 sous la licence FFL d'ITF, 36 sous la licence OFL. |
| Guides d'écriture d'interface (Apollo, Smashing, Built In) | Le texte d'interface sert la personne qui agit. Si une décision de design demande une explication, c'est souvent le design qu'il faut reprendre. La raison du designer va dans la documentation. Je n'ai pas trouvé de règle citable mot pour mot : c'est une synthèse de pratiques convergentes. |

## 1. Propositions

### P1 — Élargir le vivier de polices : Fontshare dans `parcours.py polices` (E-2)

- **A (recommandée).** `polices` interroge aussi Fontshare (`api.fontshare.com`) quand une famille n'est trouvée ni dans Fontsource ni dans Google Fonts, ou quand l'agent le demande avec `--source fontshare`.
  - La licence de chaque famille (FFL ou OFL) est rapportée avec sa restriction : pas de sous-ensemble, pas de conversion.
  - Une option `--catalogue` liste les familles de Fontshare par catégorie (serif, sans, affichage), pour chercher « par construction » hors du vivier habituel.
  - Les tests utilisent des réponses simulées, sans réseau, avec une mutation rouge.
  - `MOYENS` et `scripts/README.md` sont mis à jour.
- **B.** Seulement une phrase dans `TYPE-VOIX` qui pointe vers Fontshare, sans outil.

### P2 — Nommer la vague typographique actuelle (E-2)

- **A (recommandée).**
  - Une ligne datée `[VEILLE 2026-11]` dans `SAVOIR/TOOLS/CONVERGENCE`. Elle nomme les familles devenues signes de page générée : Inter ; Fraunces, Instrument Serif, Young Serif, Playfair Display ; Bricolage Grotesque, Space Grotesk ; Space Mono. Son type de source (articles et relevés de praticiens) et sa date sont indiqués, conformément à la règle 6.
  - Comme les autres marqueurs, elle sert à **nommer la modale**, jamais à interdire : `TYPE-VOIX` dit déjà que le candidat modal peut être retenu s'il est nommé comme tel.
  - `regard.py` relève ces familles dans la police réellement utilisée par le navigateur (marqueur « police de vague »), avec un test et une mutation rouge.
- **B.** La ligne de veille seule, sans marqueur.

### P3 — Un signal d'écriture : la page ne commente pas son design (E-1)

- **A (recommandée).** Une ligne dans les signaux d'enquête de `SAVOIR/CRAFT/CFT-06`, hors du noyau : « Une phrase qui commente la page, le brief ou un choix de design ("Le dessin est fixé", "le 3 avril tombe un samedi") : c'est la trace qui parle, pas le produit. Le texte dit le sujet à la personne ; la raison va dans la trace. Les marquages demandés ("exemple", "dessiné en code") restent, en langage produit. » Avec un test de présence.
- **B.** Attendre d'autres occurrences dans le carnet de goût.

### P4 — Calibrer aussi en `STANDARD` quand la décision visuelle est ouverte (B-5)

- **A (recommandée).** Dans le bloc `ANCRE` du noyau, « Sur une surface `DIRECTION` dont la décision visuelle est ouverte » devient « Sur une surface dont la décision visuelle est ouverte ». C'est le même périmètre que la déclaration de direction, qui vaut déjà pour `STANDARD` et `ITER` quand la décision visuelle est ouverte. Le noyau perd environ 12 octets ; les planchers et le tronc `STANDARD` sont à vérifier.
- **B.** Rien : au PILOT, les runs `STANDARD` l'ont fait d'eux-mêmes.

### B-4 — Clos sans proposition

Le constat n'est plus reproduit (voir la section 0).

## 2. Ordre proposé

1. Décision de Junior sur P1 à P4.
2. Intégration sur une branche, tests avec mutation rouge, préparation complète, puis révision `R2026-11-15n`.
3. Aucun run.

## Sources

- Vaduvescu, *The Next Default* : https://claudiavaduvescu.com/en/articles/the-next-default
- Muzli, *Font pairings 2026* : https://muz.li/blog/font-pairings-2026/
- WIRED, *AI Has Come for Serif Fonts* : https://www.wired.com/story/ai-has-come-for-serif-fonts/
- Codo, polices qui font « IA » : https://codo.build/blog/fonts-that-make-sites-look-ai-made
- Fontshare, FAQ : https://www.fontshare.com/faq
- Fontshare, licence ITF FFL : https://www.fontshare.com/licenses/itf-free-font-license
- Fontsource, documentation : https://fontsource.org/docs
- Apollo, guide d'écriture d'interface : https://www.apollographql.com/docs/ux-writing-style-guide
- Built In, 16 règles d'écriture d'interface : https://builtin.com/articles/effective-ux-writing
- Smashing Magazine, microcopie : https://www.smashingmagazine.com/2016/07/getting-practical-with-microcopy/

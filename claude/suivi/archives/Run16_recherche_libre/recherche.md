# Run 16 — recherche libre de Claude (hors système)

19 novembre 2026. C'est une recherche « normale », hors de la skill, faite pendant que l'agent du run 16 travaillait. Elle a servi à voir ce qu'on obtient sans la méthode de la skill : 6 recherches web, puis la capture de 7 pages ; Medium a refusé l'accès à 2 d'entre elles.

## Textuel : utile pour la fonction
- Apple, Human Interface Guidelines, Wallet : https://developer.apple.com/design/human-interface-guidelines/wallet. On y trouve les types de pass, dont le billet d'événement, les champs primaires et secondaires, le code-barres, et la mise en page par « semantic tags ». Source de référence pour les conventions.
- Refonte de la carte d'embarquement de Ryanair, sur Medium (bloqué à la capture) : https://medium.com/@Lynsey_Duncan/priority-queue-designing-ryanair-s-boarding-pass-5e32d26f514. L'ancienne carte avait trop d'informations et une hiérarchie faible. La refonte les regroupe en trois blocs : embarquement, trajet et horaires, informations du vol.
- DICE, application de billetterie : https://en.wikipedia.org/wiki/DICE_(ticketing_company) et https://www.itsnicethat.com/news/dice-rebrand-graphic-design-250220. Le billet vit dans l'application et devient un QR code animé une heure avant l'ouverture des portes. L'interface est en noir et blanc ; la couleur n'apparaît que dans l'image de l'événement.
- Le reste des résultats : des modèles (Canva, Renderforest), des concepts Dribbble « Daily UI » et des listes SEO.

## Visuel : ce qui vaut quelque chose
- **Très bon :** les billets du Pacific Coliseum (Vancouver, années 1970) sur Fonts In Use : https://fontsinuse.com/uses/7970/pacific-coliseum-concert-tickets. On y voit les vraies conventions du billet de concert : une couleur de papier par concert, une trame de sécurité, la date en script, la salle en capitales, le prix, le « Nº » et les mentions, avec une hiérarchie très nette.
- **Très bon :** le billet souvenir du Printers' Fair 2026, imprimé en typographie au plomb (Fonts In Use) : https://fontsinuse.com/uses/75847/2026-bay-area-printers-fair-and-wayzgoose-sou.
- **Moyen à faible :** « 15 inspiring examples of ticket design » sur Creative Bloq : https://www.creativebloq.com/design/ticket-design-2131860. Ce sont des projets étudiants ou de studio, souvent datés (2008-2012), d'une qualité inégale.
- **Absent :** aucun billet électronique contemporain de haut niveau n'est trouvable par une recherche simple. On tombe sur des concepts Dribbble génériques.

## Ce que ça dit pour la skill
1. Une recherche « normale » ramène surtout des listes SEO et des concepts génériques. Le bon matériau vient d'archives spécialisées comme Fonts In Use, qu'il faut savoir viser.
2. La skill ne dit pas où chercher le haut niveau (B-1, B-2). Une courte liste de sources de calibration par type d'objet aiderait : Fonts In Use, Letterform Archive, Standards Manual, les guides des plateformes (Apple Wallet)… À proposer au lot 9b, sans l'intégrer pour l'instant.
3. Pour un billet, les meilleures références sont imprimées et anciennes ; le billet électronique de qualité se juge plutôt sur les conventions des plateformes. Le run peut tirer de l'imprimé la culture graphique, et de la plateforme la convention d'usage.

## Google Images, recherche « billet de concert » (captures de Junior, 19 novembre 2026)
Fichiers : `google-images-1.jpg`, `google-images-2.jpg`.

- **Presque tout est du modèle à vendre** : Magnific (Freepik), Etsy, Canva, Shutterstock, Vecteezy. C'est la **modale observée** du genre, celle que le modèle a apprise.
- **Ses marqueurs** :
  - un billet horizontal avec un talon détaché ;
  - des encoches et des bords dentelés ;
  - un code-barres vertical sur le talon ;
  - « ADMIT ONE » ;
  - « SEAT / ROW / GATE » en étiquettes tournées ;
  - la photo de l'artiste à gauche ;
  - un titre condensé gras ;
  - un fond sombre avec un néon ou un dégradé rose-violet ;
  - une illustration de guitare ou de micro ;
  - du faux texte (« Artist's Name », « Lorem ipsum »).
- **Les seuls vrais billets** : AC/DC au Stade de France en 2015 (eBay), Carnaval 2023 (Fac Imprimeur) et « Pack Ndolo » (Cameroun). Ils ont un fond de sécurité, une grille de données dense en chasse fixe, des cases Porte / Tribune / Bloc / Rang / Place, des mentions légales et le numéro imprimé. Les modèles imitent ces signes d'authenticité sans leur fonction.
- **Hors sujet par rapport au brief** : tous ces résultats sont des billets imprimés. Le brief demande un billet sur téléphone. Le billet « en forme de billet », avec encoches, dans un écran de téléphone est lui-même une modale (Dribbble).

**Leçon pour la skill.** La recherche d'images ne sert pas à calibrer le niveau, mais elle montre très bien la modale. La skill demande de *nommer* la modale « que n'importe quelle IA produirait », de mémoire. L'observer en vrai, par une recherche d'images, la rendrait vérifiable. Il y aurait donc deux rôles distincts pour la recherche : **observer la modale** (ce qu'on évite) et **calibrer le niveau** (ce qu'on vise : archives, vrais objets, guides des plateformes). C'est une piste pour le lot 9b, pas encore une proposition.

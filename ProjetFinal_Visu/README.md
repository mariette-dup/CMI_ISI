READ ME

PROJECT NAME : Projet de Visualisation CMI-ISI – Découverte des mondes Marvel

DESCRIPTION :   Ce site a été créé dans le cadre de notre UE projet de visualisation encadrée par Bruno PINAUD et Guy MELANÇON.
Nous avons voulu au cours de ce projet mettre en avant diverses caractéristiques des mondes Marvel. Nous avons pu mener à bien ce projet grâce aux données récupérées sur le site Marvel Developper avec nos API keys.
Nous avons ainsi choisi 3 « Méchants » emblématiques de cet univers pour mettre en avant plusieurs résultats à leur sujet.
Nous avons dans un premier temps créé un graphique de type « Nœud-lien ». Sur lequel l'utilisateur peut visualiser les interactions entre le personnage principal, les comics dans lesquels il apparaît ainsi que les personnages qui apparaissent dans ces mêmes comics.
Dans un deuxième temps nous avons voulu visualiser un graphique de type « Word cloud ». Grâce aux descriptions des comics récupérées dans la base de données et l’application d’un algorithme de traitement : le tf-idf nous récupérons un ensemble de mots qui mettent en avant l’environnement de chaque « mechant ».
Pour terminer nous avons voulu mettre en évidence l’évolution du prix des comics en fonction des années de parution de ceux-ci. Nous avons également mis en avant les 5 auteurs qui écrivent le plus sur cette période de temps.
Il est temps maintenant de vous plonger dans le monde merveilleux de Marvel. Afin de découvrir l’univers d’un des trois personnages principaux cliquez sur leur image respective.
Ensuite, pour apprécier nos graphiques il ne reste plus qu’à cliquer sur la visualisation que vous souhaitez.

TABLE OF CONTENTS :
-	Un dossier Static dans lequel sont placés nos dossier statiques (images, css, fichiers textes, csv, json)
-	Un dossier Templates contenant :
	 menu.html permettant d’afficher la toute première page de notre site
	description.html pour l’affichage de l’explication du projet et la description du site
	accueil_2.html permettant de choisir le personnage
	visu.html permettant le choix de la visualisation
	mongraphe.html affiche le graphe nœud-lien
	wordcloud.html affiche le word cloud
	bubblefinal.html permet enfin l’affichage du bubble chart

-	Le fichier create_csv.py permet de créer le csv qui permettra la construction du bubble chart
-	Le fichier create_json.py permet de créer un json et un texte qui permettront la construction du Word Cloud
-	Le fichier test.py permet de créer un csv pour le Word Cloud après être passé dans l’algorithme du tf et dans les fonctions de traitement de texte (en récupérant les documents créés lors du code précédent)
-	Le fichier tf_idf.py permet de créer les matrices utiles pour l’implémentation d’un moteur de recherche basé sur la technique du tf-idf
-	Le dernier fichier est le fichier webapp.py, qui permet le lancement des routes et donc des calculs de graphes et de l’affichage de notre site de visualisation

ACCESS : Le projet sera disponible à l’adresse suivante :

USAGE : Après l’ouverture de notre site deux choix vont s’offrir à vous en cliquant sur une des deux images. « Présentation » qui vous offre la possibilité de lire une courte description du fonctionnement et du but de ce site ou « Mondes Marvel ». Après avoir cliqué sur « Mondes Marvel » vous pouvez choisir le héro sur lequel vous voulez avoir des informations (en cliquant sur l’image l’illustrant). Ensuite vous pouvez choisir le type de visualisation que vous désirez afficher.
En cliquant sur l’image en forme de graphe nœud-lien vous accéder donc à ce type de graphique pour le personnage choisi préalablement.
Le personnage choisi sera placé en rouge au milieu du graphique, les comics dans lequel il apparait sont en bleu clair, et les personnages annexes sont en vert. Il est possible de cliquer sur n’importe quel personnage afin d'obtenir son graphique égocentré.
Au fur et à mesure que l’utilisateur choisi des personnages à afficher, l’historique s’affiche en bas à gauche de la fenêtre. Si l’utilisateur clique sur un nœud représentant un comic un message d’erreur s’affichera dans cet historique.
Lorsqu'on clique sur un de ces liens, le graphe se construit autour du personnage en question, et l'arborescence se réinitialise.
Le graphe peut parfois prendre une trentaine de secondes pour se construire.
D'autre part, il peut occasionnellement être condensé en un seul point et afin de déplier le graphique, il suffit de cliquer sur le noeud (ou le tirer).
En cliquant sur l’image représentant un Word Cloud, deux options s’offrent à l’utilisateur : le choix d’un Word Cloud pour lequel le tf-idf a été calculé sur un seul document ou le choix d’un Word Cloud ou le tf-idf a été calculé sur plusieurs documents. Après le choix de ces deux options, le World Cloud s’affichera. Les mots les plus gros sont les mots avec la plus grosse fréquence.
Enfin en cliquant sur l’image représentant un bubble chart l’utilisateur verra s’afficher un bubble chart sur lequel l’axe des abscisses représente les années (en écriture américaine), l’axe des ordonnées le prix des comics dans lesquels apparaît ce personnage. La taille des bulles représente le nombre de pages du comic, la couleur permet d’expliciter l’auteur qui écrit le comic. En survolant les bulles, le titre du comic s’affiche en dessous du graphique. Nous n’avons pas réussi à implémenter complétement la fonction qui permet, lorsque l’utilisateur survole le nom d’un auteur dans la légende, de cacher les comics qui ne correspondent pas à cet auteur. En revanche nous avons su trouver d’où venait l’erreur : la fonction ne permet pas de discerner les espaces entre le nom et le prénom. C’est pour cette raison que cette fonctionnalité n’est visible que pour « others ». Si nous avions laissé seulement le prénom de chaque auteur il n’y aurait eu aucun problème. Mais pour des raisons d’aide à la compréhension de l’utilisateur nous avons laissé le nom et prénom.
À tout moment l’utilisateur peut revenir où il le souhaite sur le site.

<img width="1440" alt="Capture d’écran 2019-12-05 à 21 13 50" src="https://user-images.githubusercontent.com/50363279/70304013-3ddaba00-1801-11ea-8a46-667489bc8e5b.png">
![Capture d’écran 2019-12-05 à 21 14 19](https://user-images.githubusercontent.com/50363279/70304233-c48f9700-1801-11ea-9c78-b6543b946a96.png)


CONTRIBUTING : Nous pourrions apporter diverses améliorations à notre projet :
-	Un plus grand choix de type de visualisation
-	Un plus grand nombre de choix de héros
-	Des espaces de partages entre les utilisateurs pour échanger les avis
-	La mise en place du moteur de recherche (tf-idf)

CREDITS : Nous remercions l'auteur du graphe d3 "Les Misérables" sur lequel nous avons basé notre visualisation (https://gist.github.com/mbostock/4062045) de type nœud-lien, nous remercions également l’auteur du site « https://www.datavis.fr/index.php?page=word-cloud » grâce auquel nous avons pu nous inspirer pour réaliser le World Cloud. Enfin nous remercions l’auteur du Bubble Chart sur https://www.d3-graph-gallery.com/graph/bubble_template.html.

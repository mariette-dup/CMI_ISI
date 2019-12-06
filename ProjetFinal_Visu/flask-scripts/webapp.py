import time
from flask import *
from json import *
from tulip import tlp
import requests
import sys


app = Flask(__name__)
#app = Flask("Mon serveur")
@app.route('/')
def test_menu():
    return render_template("menu.html")

#Presenatation du site
@app.route('/description')
def description():
    return render_template("description.html")

#Choix du personnage
@app.route('/accueil_2')
def accueil_2():
    return render_template("accueil_2.html")

#Choix de la visualisation
@app.route('/accueil_2/visu')
def visu():
    global heros
    if request.args.get("heros"):
        heros=request.args.get("heros")
    return render_template("visu.html",hero=heros)


@app.route('/accueil_2/visu/affiche')
def wc():
    global visu
    if request.args.get("visu"):
        visu=request.args.get("visu")
    if visu == "0":
        if request.args.get("heros"):
            heros_deux=request.args.get("heros")
            return render_template("wordcloud.html",hero=heros_deux,visual=visu)
        else:
            return render_template("wordcloud.html",hero=heros,visual=visu)
    if visu == "2":
        if request.args.get("heros"):
            heros_deux=request.args.get("heros")
            return render_template("bubblefinal.html",hero=heros_deux,visual=visu)
        else:
            return render_template("bubblefinal.html",hero=heros)
    if visu == "1":
        if request.args.get("heros"):
            heros_deux=request.args.get("heros")
            return render_template("mongraphe.html",hero=heros_deux,visual=visu)
        else:
            return render_template("mongraphe.html",hero=heros,visual=visu)



#Visualisation Word cloud
@app.route('/accueil_2/visu/affiche/affiche_2')
def aff_2():
        type=request.args.get("type")
        print("recup :"+type)
        return render_template("cloud.html",hero=heros,type=type,visual=visu)


@app.route('/global')
def get_global():
    if request.args.get("heros"):
        heros_d=request.args.get("heros")
        return app.send_static_file("data"+heros_d+".csv")
    else:
        print("l")
        return app.send_static_file("data"+heros+".csv")

@app.route('/globaldeux')
def get_global_deux():
    if request.args.get("heros"):
        heros_d=request.args.get("heros")
        return app.send_static_file("data"+heros_d+"deux.csv")
    else:
        return app.send_static_file("data"+heros+"deux.csv")



#Fonction qui crée le json et genère le graphe
@app.route('/graph')
def generate_graph():
        #creation d'un nouveau graphe vide
         graph=tlp.newGraph()

         comic = graph.getStringProperty("comic")
         hero = graph.getStringProperty("hero")
         type_ = graph.getStringProperty("type")
         viewBorderColor = graph.getColorProperty("viewBorderColor")
         viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
         viewColor = graph.getColorProperty("viewColor")
         viewFont = graph.getStringProperty("viewFont")
         viewFontSize = graph.getIntegerProperty("viewFontSize")
         viewIcon = graph.getStringProperty("viewIcon")
         viewLabel = graph.getStringProperty("viewLabel")
         viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
         viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
         viewLabelColor = graph.getColorProperty("viewLabelColor")
         viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
         viewLayout = graph.getLayoutProperty("viewLayout")
         viewShape = graph.getIntegerProperty("viewShape")
         viewSize = graph.getSizeProperty("viewSize")
         type_node=graph.getIntegerProperty("Type")

         #Fonction qui crée les noeuds en leur affectant le nom du comic ou du personnage, le type de noeud (noeud du personnage central, d'un comic, d'un personnage autre) et le graphe auquel ça s'applique
         def create_node(nom, type, graph):
             n1=graph.addNode()
             viewLabel[n1]=nom
             type_node[n1]=type
             return n1

         name=request.args.get("name")

         char_hash= {}
         comic_hash={}
         if(name == "silversurfer"):
             name="silver surfer"
         #on récupère les données sur le personnage central depuis le site Marvel
         r= requests.get('https://gateway.marvel.com:443/v1/public/characters?name='+name+'&limit=100&apikey=4dff50d15e38e094affa81c7191ac0bd', headers={'referer': 'localhost'})

         id_hero=-1
         print("Code de retour=>",r.status_code)

         if r.status_code == 200:
                  data_reply = r.json()
                  print("Nombre de personnages trouve : ", len(data_reply["data"]["results"]));
                  for character in data_reply["data"]["results"]:
                           print("id personnage=>", character['id'], " xx nom personnage=>", character['name'])
                           id_hero=character['id']
         else:
                  print("Erreur de telechargement")

        #On récupère les données sur les comics dans lesquels apparaît notre personnage central ainsi que les autres personnages qui apparaissent dans ces comics.
         r2= requests.get('https://gateway.marvel.com:443/v1/public/characters/'+str(id_hero)+'/comics?limit=100&apikey=4dff50d15e38e094affa81c7191ac0bd', headers={'referer': 'localhost'})

         if r2.status_code == 200:
                  data_reply2 = r2.json()

        #Boucle qui crée le noeud central et rempli le dictionnaire json
         for character in data_reply["data"]["results"]:
                n1=create_node(character["name"],0,graph)
                char_hash[character["name"]]=n1


        #Boucle qui crée les noeuds des comics et rempli le dictionnaire json
         for comic in data_reply2["data"]["results"]:
             node= create_node(comic["title"],1,graph)
             comic_hash[comic["title"]]=node

        #Création des arrêtes
         for target in graph.getNodes() :
                  if type_node[target]==0:
                           source=target
         graph.addEdge(source,target)

         #Boucle qui crée les noeuds des autres personnages et rempli le dictionnaire json
         for comic in data_reply2["data"]["results"]:
                  for name in comic["characters"]["items"]:
                           if name["name"] in char_hash.keys():
                                    n=char_hash[name["name"]]
                           else:
                                    n=create_node(name["name"],2,graph)
                                    char_hash[name["name"]]=n

                           destination=comic_hash[comic["title"]]
                           graph.addEdge(n,destination)

        #Création du json
         gjson={'nodes':[],'links':[]}
         for n in graph.getNodes():
                  gjson['nodes'].append({'id':viewLabel[n],'group':type_node[n]})
         for e in graph.getEdges():
                  gjson['links'].append({'source':viewLabel[graph.source(e)],'target':viewLabel[graph.target(e)],'value':1})


         return jsonify(gjson)


def open_json():
         with open('templates/graph.json') as json_data:
             data= json.load(json_data)

         print(data)


if __name__ == '__main__':
	app.run(debug=True)

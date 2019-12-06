from lxml import etree
from flask import *
import json
import requests

def createjson(id,nb_data,nom):
    char_hash= {}
    comic_hash={}
    string =""
    for i in range (0,nb_data,100):
        description= requests.get('https://gateway.marvel.com:443/v1/public/characters/'+str(id)+'/comics?limit=100&offset='+str(i)+'&apikey=4dff50d15e38e094affa81c7191ac0bd',headers={'referer': 'localhost'})
        if description.status_code == 200:
             data_reply= description.json()

        for comic in data_reply["data"]["results"]:
            if comic["description"]:
                comic_hash[comic["title"]]=comic["description"]
                string = string +" "+comic["description"]

    gjson={'global':[]}
    for n in comic_hash.keys():
             gjson['global'].append({'titre':n,'description':comic_hash[n]})


    with open('static/'+str(nom)+'.json', 'w') as fp:
        json.dump(gjson, fp)

    fichier = open("static/data"+str(nom)+".txt","a")
    fichier.write(string)
    fichier.close()

# Attention j'ai pas regardé longeu
#Thanos
createjson(1009652,300,"thanos")
#Magneto
createjson(1009417,500,"magneto")
#Silver Surfer
createjson(1009592,600,"silversurfer")

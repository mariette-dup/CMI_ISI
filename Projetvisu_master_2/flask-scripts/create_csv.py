from flask import *
import json
import requests
import pandas as pd
import csv

def create_hash(id,nb_data,nom):
    char_hash= {}
    creator_hash={}
    comic_hash={}
    string = ""
    for i in range (0,nb_data,100):
        description= requests.get('https://gateway.marvel.com:443/v1/public/characters/'+str(id)+'/comics?limit=100&offset='+str(i)+'&apikey=4dff50d15e38e094affa81c7191ac0bd',headers={'referer': 'localhost'})
        if description.status_code == 200:
             data_reply= description.json()

        for comic in data_reply["data"]["results"]:
            if comic["dates"]:
                if comic["prices"]:
                    if comic["pageCount"]:
                        if comic["creators"]:
                            for i in range(0,len(comic["creators"]["items"])-1):
                                if comic["creators"]["items"][i]["role"]=="writer":
                                    name_save=comic["creators"]["items"][i]["name"]
                                    string=str(comic["dates"][0]['date'])
                                    date_comic=string[0:4]
                                    comic_hash[comic["title"]]=[comic["title"],date_comic,comic["prices"][0]["price"],comic["pageCount"],name_save]
                                    if name_save in creator_hash.keys():
                                        creator_hash[name_save]=creator_hash[name_save]+1
                                    else:
                                        creator_hash[name_save]=1


    creator_hash=sorted(creator_hash,key=creator_hash.get,reverse=True)
    creator_hash=creator_hash[0:6]

    for n in comic_hash.keys():
        if comic_hash[n][4] not in creator_hash:
            comic_hash[n][4]='others'

    return comic_hash


def bubble(nom,id):
    df=pd.DataFrame(create_hash(id,300,nom))
    df=df.T
    df.columns=['t','d','p','c','a']
    df.sort_values(by=['c'], inplace=True, ascending = False)
    df.to_csv("static/datadatet"+nom+".csv",sep="," , encoding = "utf-8",index=False)


def main() :
    bubble("thanos",1009652)
    bubble("magneto",1009417)
    bubble("silversurfer",1009592)

if __name__ == "__main__":
    main()

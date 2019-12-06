import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import nltk
from nltk.stem import WordNetLemmatizer
import json


def text_tfid_csv(nom,type):
    array_comic=[]
    #description par comic
    if type == 0:
        with open('static/'+nom+'.json') as json_data:
            jsont = json.load(json_data)
        for i in range (0,len(jsont['global'])):
            array_comic.append(jsont['global'][i]['description'])
        print(array_comic)
        for j in range(0,len(array_comic)-1):
            array_comic[j] = remove_string_special_characters(array_comic[j])
            array_comic[j] = traitement_texte(array_comic[j])

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(array_comic)
    #description global
    if type == 1:
        doc = open("static/data"+nom+".txt","r")
        doc_read = doc.read()
    #global
        doc_propre = remove_string_special_characters(doc_read)
        doc_propre = traitement_texte(doc_propre)
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([doc_propre])


    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    Data = {"text": feature_names, "size":denselist[0]}
    df2 = pd.DataFrame(Data)
    df2=df2.sort_values(by=["size"],ascending=False)
    df2=df2.drop(df2[df2['size'] == 0].index)
    if type==0:
        df2.to_csv("static/data"+nom+".csv",sep="," , encoding = "utf-8")
    if type==1:
        df2.to_csv("static/data"+nom+"deux.csv",sep="," , encoding = "utf-8")

def main() :
    text_tfid_csv("thanos",0)
    text_tfid_csv("magneto",0)
    text_tfid_csv("silversurfer",0)
    text_tfid_csv("thanos",1)
    text_tfid_csv("magneto",1)
    text_tfid_csv("silversurfer",1)


#enleve les caracteres speciaux

def remove_string_special_characters (s):

    stripped = re.sub('[^\w\s]',' ',s)
    stripped = re.sub('_',' ',stripped)
    stripped = re.sub('\s+',' ',stripped)
    stripped = stripped.strip()
    return stripped


def traitement_texte (data):
    wordnet_lemmatizer = WordNetLemmatizer()
    punctuations="?:!.,;"
    sentence_words = nltk.word_tokenize(data)
    stop_words = set(stopwords.words('english'))
    for word in sentence_words:
        if word in punctuations:
            sentence_words.remove(word)
    print("{0:20}{1:20}".format("Word","Lemma"))
    sentence_new=[]
    chiffres = []
    for i in range(0,50000):
        chiffres.append(str(i))
    for word in sentence_words:
        word2=wordnet_lemmatizer.lemmatize(word.lower(), pos="v")
        word2=wordnet_lemmatizer.lemmatize(word2, pos="r")
        word2=wordnet_lemmatizer.lemmatize(word2, pos="n")
        word2=wordnet_lemmatizer.lemmatize(word2, pos="a")
        if word2 not in stop_words:
            if word2 not in chiffres:
                if len(word2)>2:
                    sentence_new.append(word2)
    text=""
    for word in sentence_new:
        text=text+" "+word
    return text


if __name__ == "__main__":
    main()

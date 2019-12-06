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
import numpy as np

def text_tfid_csv(nom,type):
    array_comic=[]

    with open('static/'+nom+'.json') as json_data:
        jsont = json.load(json_data)
    for i in range (0,len(jsont['global'])):
        array_comic.append(jsont['global'][i]['description'])
    for j in range(0,len(array_comic)-1):
        array_comic[j] = remove_string_special_characters(array_comic[j])
        array_comic[j] = traitement_texte(array_comic[j])


    array_comic=np.array(array_comic)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(array_comic)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    word_idf_values = {}
    i=0
    for token in feature_names:
        i=i+1
        if(2280<i<2380):
            doc_containing_word = 0
            for document in array_comic:
                if token in nltk.word_tokenize(document):
                    doc_containing_word += 1
            word_idf_values[token] = np.log(len(array_comic)/(1 + doc_containing_word))

    df_count=pd.DataFrame.from_dict(word_idf_values,orient="index")
    df = pd.DataFrame(denselist, columns=feature_names)

    df.to_csv("static/magnetolog.csv",sep="," , encoding = "utf-8")
    df_count.to_csv("static/magnetotf.csv",sep="," , encoding = "utf-8")



def main() :
    text_tfid_csv("magneto",0)

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

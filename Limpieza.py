# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:59:53 2019

@author: HARU


"""



import pandas as pd
import os
cwd = os.getcwd()
import glob
import re
import joblib

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

from nltk.corpus import stopwords

#concateno los articulos de la carpeta
files = glob.glob('C:/Users/HARU/Desktop/a/*.csv')
union = pd.concat([pd.read_csv(fp) for fp in files], ignore_index=True,sort=True)
    
df = union.drop_duplicates(subset=["noticia"], keep='first') #tiramos las noticias repetidas
def limpieza(df):
    
# =============================================================================
#     tecnologia=df["tema"][df["tema"]=="tecnologia"].index
#     df.drop(tecnologia, inplace=True)
# =============================================================================
    opinion = df["tema"][df["tema"]=="opinion"].index
    df.drop(opinion, inplace=True) #quitamos la label de OPINION
    
    #limpiamos nombres en el dataframe
    df["tema"]=df["tema"].replace("deportes","deporte")
    df["tema"]=df["tema"].replace("culturas","cultura")
    df["tema"]=df["tema"].replace("elpais/ciencia.html","ciencia")

#   ciencia=df["tema"][df["tema"]=="ciencia"].index
    #df.drop(ciencia, inplace=True)

    
    df["tema"]=df["tema"].replace("vida","sociedad")  
    df['target'] =  df['tema']
    df.drop(['Unnamed: 0',"Unnamed: 0.1" , 'periodico', 'tema'],axis=1, inplace=True)
    df=df[["noticia","target"]]
    
    
    #empieza la limpieza
    df["noticia"]=df["noticia"].apply(lambda x: str(x))
    df['noticia']=df['noticia'].str.replace('<.*?>','')
    df['noticia']=df['noticia'].apply(lambda x: ' '.join(p.lower() for p in x.split()))    
    
    #bucles feos pero casi eficientes
    b=[]
    for i in df["noticia"]:
        a="".join(re.sub(r'\d+', " ", i))
        b.append(a)
    df["noticia"]=b
    
    b=[]
    for i in df["noticia"]:
        a=re.sub(r'[;):%«/,?"(».\s]'," ",i)
        b.append(a)
    df["noticia"]=b  
    
    b=[]
    for i in df["noticia"]:
        a="".join(re.sub('[‘’¿?'' + ¡1“ ”…]\d+', '', i))
        b.append(a)
       
    df["noticia"]=b
    
    remplazo1 = re.compile('[/()-''+' ' ‘’|!¡“”¿?\"-",;]')
    b=[]
    for i in df["noticia"]:
        a="".join(re.sub('[‘’¿?'' + ¡1“ ”…]\d+', '', i))
        a=remplazo1.sub(' ', i)
             
        b.append(a)
    df["noticia"]=b
    
    #con trampras el StopWords
    stop_words= set(stopwords.words("spanish"))
    stop_words.add("años") #ponemos palabras que aparentemente no tienen valor
    stop_words.add("dos")
    stop_words.add("año")
    stop_words.add("según")
    stop_words.add("ahora")
    stop_words.add("si")
    stop_words.add("hace")
    stop_words.add("ser")
    stop_words.add("solo")
    stop_words.add("caso")
    stop_words.add("aunque")
    stop_words.add("puede")
    stop_words.add("solo")
    stop_words.add("aunque")
    
    stop_words.add("'") #de para abajo estan las trampas
    stop_words.add("-")
    stop_words.add("' ")
    stop_words.add("- ")
    stop_words.add(" '")
    stop_words.add(" -")
    stop_words.add(" ' ")
    stop_words.add(" - ")
    #se aplica el stopwords en todo el texto
    df['noticia']=df['noticia'].apply(lambda x: ' '.join(p for p in x.split() if p not in stop_words))
    return df #devolvemos el dataframe casi limpio

df=limpieza(df)

Df_dataframe = "Dataframe_Class.pkl" #guardamos el dataframe
joblib.dump(df, Df_dataframe)





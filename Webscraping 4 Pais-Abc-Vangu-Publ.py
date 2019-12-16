# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:15:27 2019

@author: HARU
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#PUBLICO

#funciona : espana, internacional,economia, sociedad, deportes, cultura, ciencia
# no funciona :opinion (da menos resultados)

periodico="Publico"
fecha="15_12_2019"
url="https://www.publico.es/"
temas=["politica","internacional","economia", "sociedad", "culturas" ]

for tema in temas:
    print("Estoy guardando todo lo relacionado con:", tema," en la fecha:", fecha)
    response = requests.get(url+tema)
    bool(response),response.status_code
    soup = BeautifulSoup(response.text, "html.parser")
    publico= soup.find_all(class_="listing-title")    
    
    lista_links=[]
    lista_titulares=[]   
    for web in publico:
                
        link= web.find("a")["href"]
        if link.find("https:") ==-1:
            link= url +link
            lista_links.append(link)  
        else:
            lista_links.append(link)
        
        
        titular=web.find("a").text
        lista_titulares.append(titular)
        
        vanNot=[]        
        for olink in lista_links:
            response=requests.get(olink)
            bool(response)
            soup = BeautifulSoup(response.text, "html.parser")
            
            if soup.find(class_="article-text"):
                body= soup.find(class_="article-text")
                body=body.find_all("p")
                textos=""    
                for i in body:
                    textos=textos+i.text                 
                vanNot.append(textos)
    
        N_archivo= periodico[:4]+tema[:4].capitalize()+fecha
        periodicos={} #diccionario periodico. Es asi para todos. No hace falta llamarlo "periodico_tema_dia" eso ya se especifica en el valor de cada clave del diccionario
        periodicos["noticia"]=vanNot
        periodicos["tema"]=tema
        periodicos["periodico"]=periodico
        df = pd.DataFrame(periodicos)        
        df.to_csv('C:/Users/HARU/Desktop/b/'+N_archivo+'.csv')



#EL PAIS
        
#llamamos a la web         
periodico="ElPais"
fecha="13_12_2019"
url="https://www.elpais.com/"
temas=["internacional","politica","deportes","economia","cultura","tecnologia","sociedad","elpais/opinion.html","elpais/ciencia.html"]        

#llamamos a la web
for tema in temas:
    print("Periodico :", periodico, "estoy guardando todo lo relacionado con:", tema," en la fecha:", fecha)
    response = requests.get(url+tema)
    #https://elpais.com/elpais/opinion.html, https://elpais.com/elpais/ciencia.html
    bool(response),response.status_code
    soup = BeautifulSoup(response.text, "html.parser")
    
    #buscamos los titulos y los links
    infowebs = soup.find_all("h2", class_= "articulo-titulo")
    
    #obtenemos links y titulos
    lista_links = []   
    lista_titulos = []
    
    for info in infowebs:
        link=info.find('a')['href']
        if link.find("https:")==-1:
            link= "https:"+link
            lista_links.append(link)
        else:
            lista_links.append(link)
    
        titulo=info.get_text()
        lista_titulos.append(titulo)
        lista=[]
        for i in lista_links:
    
            if i.find("https://elpais.com/internacional/")==0:
                lista.append(i)
            elif i.find("https://elpais.com/politica/")==0:
                lista.append(i)
            elif i.find("https://elpais.com/deportes/")==0:
                lista.append(i)
            elif i.find("https://elpais.com/economia/")== 0:
                lista.append(i)
            elif i.find("https://cincodias.")== 0:
                lista.append(i)
            elif i.find("https://retina.elpais.com")== 0:
                lista.append(i)
            elif i.find("https://elpais.com/cultura/")== 0:
                lista.append(i) 
            elif i.find("https://elpais.com/tecnologia/")== 0:
                lista.append(i)
            elif i.find("https://elpais.com/sociedad/")== 0:
                lista.append(i)
            elif i.find("https://elpais.com/elpais/")== 0:
                lista.append(i)
           
            else: 
                print("no se pueden sacar:", i)
        
    
    lista_links=lista            
    vanNot=[]
    for olink in lista_links:
        responde= requests.get(olink)    
        bool(response)
        soup=BeautifulSoup(responde.text,"html.parser")
        
        if soup.find("div",class_="articulo-cuerpo"):
            noti= soup.find("div",class_="articulo-cuerpo")
            noti=noti.find_all("p")
            s=""
            for i in noti:
                s=s+" "+i.text        
            vanNot.append(s)
        
    N_archivo= periodico[:4]+tema[:4].capitalize()+fecha
    periodicos={} #diccionario periodico. Es asi para todos. No hace falta llamarlo "periodico_tema_dia" eso ya se especifica en el valor de cada clave del diccionario
    periodicos["noticia"]=vanNot
    if tema=="espana":    
        periodicos["tema"]="politica"
    else:
        periodicos["tema"]=tema
        
    periodicos["periodico"]=periodico
    df = pd.DataFrame(periodicos)
                  
    df.to_csv('C:/Users/HARU/Desktop/b/'+N_archivo+'.csv')
 
    
    
#LA VANGUARDIA    
periodico="Vanguardia"

    
url="https://www.lavanguardia.com/"
temas=["vida","politica","deportes","internacional","economia", "cultura"]
for tema in temas:
    print("Periodico:", periodico, ", estoy guardando todo lo relacionado con: ", tema," en la fecha: ", fecha)
    response = requests.get(url+tema)
    bool(response),response.status_code
    soup = BeautifulSoup(response.text, "html.parser")
    vang= soup.find_all(class_="story-header-title-link")
    lista_links=[]
    lista_titulos=[]
    for web1 in vang:
        if web1.get('href'):
            link=web1["href"]
        else:
            link=web1["data-href"]
        titulo=web1.text    
        lista_links.append(link)
        lista_titulos.append(titulo)

        lista=[]
        for i in lista_links:
            if i.find("https://www.lavanguardia")==0:
                lista.append(i)
            elif i.find("http://blogs.lavanguardia.com/") ==0:
                lista.append(i)
            else: 
                print("esta no entra",i)
 #Hasta aqui conseguimos links y titulos           
         
        lista_links=lista #Se iguala: el filtro nos quita algunos links que darian error
#             
# =============================================================================
        vanNot=[]
        for olink in lista_links:
            responde= requests.get(olink)    
            bool(response)
            soup=BeautifulSoup(responde.text,"html.parser")
            if soup.find(class_="story-leaf-txt-p"):
                encontrar=soup.find(class_="story-leaf-txt-p")
                encontrar=encontrar.find_all("p")
                s=""
                for i in encontrar:
                    s=s+" "+i.text        
                vanNot.append(s)
            
                
    
    N_archivo= periodico[:4]+tema[:4].capitalize()+fecha
    periodicos={} #diccionario periodico. Es asi para todos. No hace falta llamarlo "periodico_tema_dia" eso ya se especifica en el valor de cada clave del diccionario
    periodicos["noticia"]=vanNot
    periodicos["tema"]=tema
    periodicos["periodico"]=periodico
    df = pd.DataFrame(periodicos)
          
    df.to_csv('C:/Users/HARU/Desktop/b/'+N_archivo+'.csv')   





#ABC
#funciona : espana, internacional,economia, sociedad, deportes, cultura, ciencia
# no funciona :opinion (da menos resultados)
periodico="Abc"

url="https://www.abc.es/"

temas=["espana", "internacional","economia", "sociedad", "deportes", "cultura", "ciencia"]
#llamamos a la web
for tema in temas:
    print("Estoy guardando todo lo relacionado con:", tema," en la fecha:", fecha)
    response = requests.get(url+tema)
    bool(response),response.status_code
    soup = BeautifulSoup(response.text, "html.parser")

    abc= soup.find_all(class_="articulo-portada")
#titulos y links
    lista_links=[]
    lista_titulares=[]
    for a in abc:
        
        titular=a.find("a")["title"]
        lista_titulares.append(titular)
        
        link=a.find("a")["href"]
        if link.find("https:") ==-1:
            link= url +link
            lista_links.append(link)  
        else:
            lista_links.append(link)
  
    #guarda noticias
    
    vanNot=[]        
    for olink in lista_links:
        response=requests.get(olink)
        bool(response)
        soup = BeautifulSoup(response.text, "html.parser")
        body= soup.find(class_="cuerpo-texto")
        if soup.find(class_="cuerpo-texto"):
            body= soup.find(class_="cuerpo-texto")
            body=body.find_all("p")
            textos=""    
            for i in body:
                textos=textos+i.text
                
            vanNot.append(textos)
    
    N_archivo= periodico[:4]+tema[:4].capitalize()+fecha
    periodicos={} #diccionario periodico. Es asi para todos. No hace falta llamarlo "periodico_tema_dia" eso ya se especifica en el valor de cada clave del diccionario
    periodicos["noticia"]=vanNot
    if tema=="espana":    
        periodicos["tema"]="politica"
    else:
        periodicos["tema"]=tema
    
    periodicos["periodico"]=periodico
    df = pd.DataFrame(periodicos)        
    df.to_csv('C:/Users/HARU/Desktop/b/'+N_archivo+'.csv')   
     
 
    

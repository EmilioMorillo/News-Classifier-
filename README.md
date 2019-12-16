# News-Classifier-
This is a repository about the proyect I am currently working in

This is a not finished proyect. All code here can be modified in the near future.

Project

The project idea is to predict news topic from different Spanish news papers. At the end daily news from different newspapers will be classified and emailled.

First, I webscapped news from 4 different newspapepers from Spain. The idea was to chose between different ideologies. The news papers are Abc, La Vanguardia, El Pais y Público.

Second, I cleaned the data of "non powerfull" words with re and use of stopwords and created a dataframe. 

After, I tried to see which classes could I take. At the end I chose International, Politics(Spanish), Economy, Science, Society, Culture (yes, Society and Culture are pretty the same), Sport and Tecnology.

One of the points to highlight is that the dataframe is very uneven. There are not enough news about Science and Tecnology, so the accuracy lacks of those extra decimals. One thing to do is to kill both classes, or to fill with more news. Something for the future.

After that I tried to model de data to see how it classifies. Playing with tunning and GridSearch.


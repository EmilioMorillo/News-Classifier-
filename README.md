# News-Classifier-
This is a repository about the project I am currently working in

This is a not finished project. All code here can be modified in the near future.

Project

The project idea is to predict news topic from different Spanish newspapers. At the end daily news from different newspapers will be classified and emailed.

First, I web scrapped news from 4 different newspapers from Spain. The idea was to choose between different ideologies. The newspapers are Abc, La Vanguardia, El Pais y Público.

Second, I cleaned the data of "non powerful" words with re and use of stopwords and created a dataframe. 

After, I tried to see which classes could I take. At the end I chose International, Politics (Spanish), Economy, Science, Society, Culture (yes, Society and Culture are pretty the same), Sport and Technology.

One of the points to highlight is that the dataframe is very uneven. There are not enough news about Science and Technology, so the accuracy lacks of those extra decimals. One thing to do is to kill both classes, or to fill with more news. Something for the future.

After that I tried to model de data to see how it classifies. Playing with tuning and GridSearch.

The models are: LR, NB, SVM, KNN, KMEANS. To learn about them, and also analyze their results a bit. 

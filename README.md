# Book-recommender-system

### This project is a simply Book-recomenndation system
It suggests you new books based on your ( my_ratings.csv - it should contain only those ones which are in the books-modded.csv) preveious ratings.
The method makes suggestion which is trying to make clusters with Readers who are similar to your "taste". 
The result will be contain only new ones ( according to ISBN number - so there is a chance to get a book which is already read but the ISBN is different)
At the start of the code there are the defined constants, there you could change for example the MIN_NEIGHBORS and the MAX_NEIGHBORS. If you modified theese you will get 
a different result. So if you will find the balance you will get probably the famous books but stil unreaded.

## Datas
Except the "my_ratings.csv" the rest of the .csv files came from the GroupLens group they have a bunch of datasets mostly for recommendation systems. I choose from there 
it is called Book-Crossing. The only one downside of this dataset is that it was created in 2004 ( so there are a lot of new book which isn't exsisted in that time) and contains a lot of implicit datas, so there are a bunch of ratings but most of them are just zeros. However without this dataset I couldn't make this project. So in this 
way I just wanted to say thanks for those group. 
Feel free check them!

## Requirements
The project was written in Python 3.10.7 and the packages which are neccesary to get installed are included in the " requirements.txt", with their name and version as well.

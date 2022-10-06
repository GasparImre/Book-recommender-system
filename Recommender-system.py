import pandas as pd
import  csv

#_______________________KONSTANSOK_____________________________
ROWS_TO_SHOW = 10 # Sorok számát határozza meg
MINIMUM_TO_INCLUDE = 20 # A minimum értékelések számát határozza meg

books = pd.read_csv('books-modded.csv',sep=';',encoding='latin')                            # Every neccesary csv will be imported there that means 2
columns_need = ['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher']        # Minden szükséges adatot betöltünk ez 3 betöltést jelent
print(books[columns_need].head(ROWS_TO_SHOW))

ratings = pd.read_csv('ratings.csv',sep=';',encoding='latin')
columns_need = ['User-ID',"ISBN","Book-Rating"]
print(ratings[columns_need].head(ROWS_TO_SHOW))

users = pd.read_csv('users.csv',sep=';',encoding='latin')
columns_need = ['User-ID',"Location","Age"]
print(users[columns_need].head(ROWS_TO_SHOW))

books = books.iloc[:,:-6]       # there is couple of empty columns and just drop those ones there
                                # a fájl végén van néhány üres oszlop, ezeket dobjuk ki
print(f'\n____________________________Adatok Betöltve________________________________\n')

joined_datas = ratings.merge(books,how='inner')
# joined_datas = pd.merge(joined_datas,users,how='inner')



average_ratings =(joined_datas).groupby(['ISBN'], as_index=False).mean() # kell az as_index=False mert másképp indexbe helyezi az ISBN-t és utána nem lehet aszerint joinolni
sorted_average = average_ratings.sort_values(by="Book-Rating", ascending=False)
recommended_joined_datas = sorted_average.merge(books,on='ISBN', how='inner')

print("Mindenkinek ajánlott")
print(recommended_joined_datas.head(ROWS_TO_SHOW))

average_ratings['ratings-count']=joined_datas.groupby('ISBN')['ISBN'].transform('count') # hozzá kell adni egy számláló sort is mert nem tudhatjuk hogy hányan értékelik a könyvet
average_ratings = average_ratings.loc[average_ratings['ratings-count']>MINIMUM_TO_INCLUDE]
average_ratings = average_ratings.merge(books, on='ISBN', how='inner')

def recommended_for_a_fan(author,average_ratings):  # just write the name of the author and the average_ratings dataset, and you got the rated books from that author
    average_ratings = average_ratings.loc[average_ratings['Book-Author'].str.contains(author, na=False)]    # Az író nevét és a average_ratings-et kell a paraméterekhez írni és már
    sorted_average = average_ratings.sort_values(by="Book-Rating", ascending=False)                         # ki is írja az értékelt könyveket attól az írótól
    columns_need = ['Book-Rating', 'Book-Title' ]
    # filtered_ratings=sorted_average.where(filter)
    print(f"Egy {author} fannak ajánlott\n{sorted_average[columns_need].head(ROWS_TO_SHOW)}")
    print("\n")

recommended_for_a_fan("Stephen King",average_ratings)
recommended_for_a_fan("J. K. Rowling",average_ratings)

#_____________Make the personalized recommendations/Elkészítjük a személyreszabott ajánlásokat__________#

my_rating_dict = {}
with open("my_ratings.csv",'r') as data:
    for line in csv.DictReader(data):
        my_rating_dict.update({str(line['ISBN']): float(line['Rating'])})

print("Az értékelő dictionary összegyűjtve!")
print(f"Az értékelésem a 553210424 ISBN számú Metamorphosis-ra {str(my_rating_dict['553210424'])}")
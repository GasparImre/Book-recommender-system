import pandas as pd

#_______________________KONSTANSOK_____________________________
ROWS_TO_SHOW = 10 # Sorok számát határozza meg
MINIMUM_TO_INCLUDE = 20 # A minimum értékelések számát határozza meg

books = pd.read_csv('books-modded.csv',sep=';',encoding='latin')
columns_need = ['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher']        # Minden szükséges adatot betöltünk ez 3 betöltést jelent
print(books[columns_need].head(ROWS_TO_SHOW))

ratings = pd.read_csv('ratings.csv',sep=';',encoding='latin')
columns_need = ['User-ID',"ISBN","Book-Rating"]
print(ratings[columns_need].head(ROWS_TO_SHOW))

users = pd.read_csv('users.csv',sep=';',encoding='latin')
columns_need = ['User-ID',"Location","Age"]
print(users[columns_need].head(ROWS_TO_SHOW))

books = books.iloc[:,:-6]

# books =load_data(books,'books-modded.csv',5,['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher'])
# load_data(ratings,'ratings.csv',5,['User-ID',"ISBN","Book-Rating"])
# load_data(users,'users.csv',5,['User-ID',"Location","Age"])

print(f'____________________________Adatok Betöltve________________________________\n')

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

def recommended_for_a_fan(author,average_ratings):
    average_ratings = average_ratings.loc[average_ratings['Book-Author'].str.contains(author, na=False)]
    sorted_average = average_ratings.sort_values(by="Book-Rating", ascending=False)
    columns_need = ['Book-Rating', 'Book-Title' ]
    # filtered_ratings=sorted_average.where(filter)
    print(f"Egy {author} fannak ajánlott\n{sorted_average[columns_need].head(ROWS_TO_SHOW)}")
    print("\n")

recommended_for_a_fan("Stephen King",average_ratings)
recommended_for_a_fan("J. K. Rowling",average_ratings)






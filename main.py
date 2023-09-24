import numpy as np # linear algebra
import pandas as pd # data processing
import os

#import the first dataset; seperated by tabs and doesn't have any columns names so this code addresses that 
columns_names=['user_id','item_id','rating','timestamp']
df=pd.read_csv("/Users/chandra/hack2023-umass/ml-100k/u.data", sep="\t",names=columns_names)        

#import the second dataset; similar to the first
columns_names=['item_id','title','date', "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21"]
movies = pd.read_csv('/Users/chandra/hack2023-umass/ml-100k/u.item', sep='|', encoding='latin-1', names=columns_names)

#we only need the first two columns to setup before we merge the two datasets together 
movies=movies.iloc[: , 0:2]


#merge the datasets together
df = pd.merge(df, movies, on='item_id')
#drop the timestamps since we don't need it anymore
df.drop(["timestamp"], axis = 1, inplace = True)



#start setting up the reccomendation system 


'''
We will use the Item - Item recommodition method, selecting and recommending similar films (those with similar ratings).

We will make a collaborative recommodition using the ratings given by the users.

We will recommend the most liked (leader) film to everyone.
'''

moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()

selection = input("input your movie name and year ex: 'Star Wars (1977)' ")
starwars_user_ratings = moviemat[selection]
starwars_user_ratings.head()

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)


corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.sort_values('Correlation', ascending=False).head(10)


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.sort_values('rating', ascending=False).head(20)
ratings['rating_vote_number'] = pd.DataFrame(df.groupby('title')['rating'].count())
print(ratings.head())

print(ratings.sort_values('rating_vote_number',ascending=False).head())

corr_starwars = corr_starwars.join(ratings['rating_vote_number'])
print(corr_starwars.head())

final = corr_starwars[corr_starwars['rating_vote_number']>100].sort_values('Correlation',ascending=False).head()
print(final)
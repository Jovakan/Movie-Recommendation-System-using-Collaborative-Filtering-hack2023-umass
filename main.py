import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

#
#for dirname, _, filenames in os.walk('/Users/chandra/hack2023-umass/ml-100k'):
#    for filename in filenames:
#        print(os.path.join(dirname, filename))
               
#import warnings
#warnings.filterwarnings("ignore")
#warnings.warn("this will not show")
#


columns_names=['user_id','item_id','rating','timestamp']
df=pd.read_csv("/Users/chandra/hack2023-umass/ml-100k/u.data", sep="\t",names=columns_names)        
df.head(2)



columns_names=['item_id','title','date', "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21"]

movies = pd.read_csv('/Users/chandra/hack2023-umass/ml-100k/u.item', sep='|', encoding='latin-1', names=columns_names)


movies=movies.iloc[: , 0:2]
movies.head()


df = pd.merge(df, movies, on='item_id')
df.drop(["timestamp"], axis = 1, inplace = True)




moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()

starwars_user_ratings = moviemat['Star Wars (1977)']
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
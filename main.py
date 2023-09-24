import json
import pandas as pd
import os


for dirname, _, filenames in os.walk('/Users/chandra/hack2023-umass/ml-100k'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

columns_names=['user_id','item_id','rating','timestamp']
df=pd.read_csv("../input/movielens-100k-dataset/ml-100k/u.data", sep="\t",names=columns_names)        
df.head(2)




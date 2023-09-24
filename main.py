import json
import pandas as pd
from lightfm import LightFM
from lightfm.evaluation import precision_at_k

data_file = open("yelp_academic_dataset_checkin.json")
data = []
for line in data_file:
    data.append(json.loads(line))
checkin_df = pd.DataFrame(data)
data_file.close()





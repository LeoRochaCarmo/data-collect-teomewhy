#%%

import requests
import pandas as pd
from datetime import datetime
from time import sleep
import json
import os

#%%

def get_response(**kwargs):
    url = 'https://www.tabnews.com.br/api/v1/contents'
    resp = requests.get(url, params=kwargs)
    return resp

def save_data(data, option='json'):

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%s.%f')
    
    if option == 'json':
        os.makedirs('./data/contents/json', exist_ok=True)
        with open(f'./data/contents/json/{now}.json', 'w') as open_file:
            json.dump(data, open_file, indent=4)

    elif option == 'dataframe':
        os.makedirs('./data/contents/parquet', exist_ok=True)
        df = pd.DataFrame(data)
        df.to_parquet(f'./data/contents/parquet/{now}.parquet', index=False)

#%%
page = 1

while True:
    resp = get_response(page=page, per_page=100, strategy='new')
    print(page)
    if resp.status_code == 200:
        data = resp.json()
        save_data(data)
        
        if len(data) < 100:
            break

        page += 1
        sleep(2)
    
    else:
        sleep(60 * 5)
    
#%%
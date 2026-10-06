import pandas as pd
import requests


data ={
    'name':['a','b','c'],
    'age':[30,20.21],
    'add':['pune','goa','mum']
}

print("students details")
df = pd.DataFrame(data)

print(df)

print('API data')
response = requests.get('https://jsonplaceholder.typicode.com/')
print (response.json())
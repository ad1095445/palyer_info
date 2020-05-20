
import random
import requests
for i in range(1,11):
    data ={
        'id':f'客户端{i}',
        'score':random.randint(1,100000)
    }
    res = requests.post(url='http://127.0.0.1:8000/',data=data)
    print(res.status_code)
import requests
import datetime

response = requests.get("https://blockchain.info/rawaddr/42e58ccd620fab780e46095f4b3f6987aa253219")

data = response.json()
first_tr_id = data["txs"][0]["hash"]
first_tr_time = data["txs"][0]["time"]

a = [1, 2, 3, 4]

for n in range(len(a)):
    print(a[n])



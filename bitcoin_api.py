import requests
import datetime
# tr_id = data["txs"][0]["hash"]
# tr_inputs = data["txs"][0]["inputs"]
# tr_outputs = data["txs"][0]["out"]
# tr_time_stamp = data["txs"][0]["time"]


response = requests.get("https://blockchain.info/rawaddr/42e58ccd620fab780e46095f4b3f6987aa253219")

data = response.json()
first_tr_id = data["txs"][0]["hash"]
first_tr_time = data["txs"][0]["time"]
# len(data["txs"][0]["inputs"])
# print(first_tr_time)
# print(data["txs"][0]["out"])
# import datetime
# print(
#     datetime.datetime.fromtimestamp(
#         int(first_tr_time)
#     ).strftime('%Y-%m-%d %H:%M:%S')
# )
# num = 1
# for n in data["txs"]:
# 	print("transaction", num)
# 	num = num + 1

l = [1, 2, 3, 4]
for n in range(len(l)):
	print(l[n])



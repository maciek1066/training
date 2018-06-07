import requests


address = "3C47LDMVJrB6uW7yu1trLw7SrY6WxAHWny"
response = requests.get("https://blockchain.info/rawaddr/{}".format(address))
data = response.json()

#  inputs value

for tx in data["txs"]:
	tx_inp_sum = 0
	for inp in tx["inputs"]:
		tx_inp_sum += (inp["prev_out"]["value"])
		 
print(tx_inp_sum)

print("-------")
#  outputs value
for tx in data["txs"]:
	tx_out_sum = 0
	for inp in tx["out"]:
		tx_out_sum += (inp["value"])
print(tx_out_sum)
# print(data)
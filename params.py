import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1}
)

data = response.json()
print(data["results"])

# response = requests.get("https://blockchain.info/rawblock/{}".format(address)) 

print(len("3PvCAF7zhHgDGKjK1SneKc4yLxWra2J76Q"))
import requests

query = "কন্যার রূপ-গুণের বর্ণনায় বিনুদাদা বলেছিলেন?"
url = "http://localhost:8000/ask"
params = {"query": query}

response = requests.get(url, params=params)
print(response.json())

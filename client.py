import requests

url = "http://192.168.100.10:5000/predict"

data = {"x": 7}

response = requests.post(url, json=data)
print(response.json())

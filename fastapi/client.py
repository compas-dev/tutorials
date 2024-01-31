import requests

response = requests.get("http://localhost:8000")
print(response.text)

response = requests.post("http://localhost:8000/oriented_bounding_box", json={"points": [[0,0,0], [1,0,0], [0,1,0], [0,0,1]]})
print(response.json())

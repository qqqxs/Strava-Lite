import requests
import json

BASE = "http://127.0.0.1:5000"

response = requests.post(f"{BASE}/user", json={"name": "wen zirui", "age": 18})
id1 = response.json()["id"]
print(response.status_code)
print(json.dumps(response.json(), indent=2))
print("-" * 50)

response = requests.post(f"{BASE}/user", json={"name": "liu chenyu", "age": 19})
id2 = response.json()["id"]
print(response.status_code)
print(json.dumps(response.json(), indent=2))
print("-" * 50)

response = requests.post(f"{BASE}/user", json={"name": "huang zixiong", "age": 20})
id3 = response.json()["id"]
print(response.status_code)
print(json.dumps(response.json(), indent=2))
print("-" * 50)

response = requests.post(f"{BASE}/user", json={"name": "huang zixiong"})
print(response.status_code)
print(json.dumps(response.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/user/{id3}")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/user/abcd")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/users")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

response_delete = requests.delete(f"{BASE}/user/{id3}")
print(response_delete.status_code)
print(json.dumps(response_delete.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/users")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/workouts/{id1}", json={"date": "11/26/2024", "time": "5min", "distance": "1mile"})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/workouts/{id1}", json={"date": "11/27/2024", "time": "15min", "distance": "11mile"})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/workouts/{id2}", json={"date": "11/28/2024", "time": "25min", "distance": "21mile"})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/workouts/{id2}", json={"date": "11/26/2024", "time": "5min", "distance": "31mile"})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/workouts/abcd", json={"date": "11/26/2024", "time": "5min"})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/workouts/{id1}")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/follow-list/{id1}", json={"follow_id": id2})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/follow-list/{id1}", json={"follow_id": id3})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_put = requests.put(f"{BASE}/follow-list/{id1}", json={"follow_id": id1})
print(response_put.status_code)
print(json.dumps(response_put.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/follow-list/{id1}/{id2}")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/follow-list/{id1}/{id3}")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

response_get = requests.get(f"{BASE}/follow-list/{id1}/{id1}")
print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))
print("-" * 50)

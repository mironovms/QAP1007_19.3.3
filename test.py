import requests
import json

# GET
status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(f"Статус ответа от сервера на GET запрос  : {res.status_code}")

# POST
info = {
"id": 1883,
"category": {"id": 2,"name": "Cat"},
"name": "Marsik",
"photoUrls": ["string"],
"tags": [{"id": 1883,"name": "Marsik"}],
"status": "available"
}
res_post = requests.post(f"https://petstore.swagger.io/v2/pet",
                                  headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(info, ensure_ascii=False))
print(f"Статус ответа от сервера на POST запрос добавление питомца: {res_post.status_code}")

# PUT
info = {
"id": 1883,
"category": {"id": 2,"name": "Cat"},
"name": "Pussy",
"photoUrls": ["string"],
"tags": [{"id": 1883,"name": "Pussy"}],
"status": "available"
}
res_put = requests.put(f"https://petstore.swagger.io/v2/pet",
                                  headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(info, ensure_ascii=False))
print(f"Статус ответа от сервера на PUT запрос изменение питомца: {res_put.status_code}")

# DELETE
info = {
"api_key": "special-key",
"accept": "application/json",
}
res_delete = requests.delete(f"https://petstore.swagger.io/v2/pet/1883", data = info
                              )
print(f"Статус ответа от сервера на DELETE запрос удаление питомца: {res_delete.status_code}")


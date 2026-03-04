import requests
import json
URL = "https://pokemonbattle.ru"
TOKEN = "7c217ad07dace0c93d196c63559bf5c"
# read
response = requests.get(URL + '/trainers')
responsePretty = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(response.status_code,response.text, sep='\n')
if response.status_code == 200:
  print('ok')
else:
  print('not ok')
# create
response = requests.post(URL + '/pokemons',headers={"trainer_token":TOKEN}, json={
  "name": "pikachu",
  "photo": "absolute image url pokachu",
  "attack": 4
})
print(response.text)
# update
response = requests.put(URL + '/pokemons',headers={"trainer_token":TOKEN}, json={
  "pokemon_id": 1265,
  "name": "brave pikachu",
  "photo": "",
  "attack": 2
})
print(response.text)
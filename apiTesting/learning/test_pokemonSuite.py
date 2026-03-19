import requests
import pytest
URL = "https://pokemonbattle.ru"
def test_status_code():
  response = requests.get(URL)
  assert response.status_code == 200, "unexpected status code"
def test_piece_of_body():
  response = requests.get(URL + '/trainers', params={'trainer_id': "1176"})
  assert response.json()['trainer_name'] == "МашаМентор", "unexpected trainer_name"

@pytest.mark.parametrize("key, value",[("trainer_name", "MashaMentor"),("cyty ", "Moscow")])

def test_parametrs_body(key, value):
  response = requests.get(URL + '/trainers', params={'trainer_id': "1176"})
  assert response.json()[key] == value

  # trainer_name = response.json()['trainer_name'], токен можем получить из резултата запроса по ключу
  '''
  с использованием форматированных строк f"" внутри строк можно интерполировать переменные, через {variable_name}
  '''
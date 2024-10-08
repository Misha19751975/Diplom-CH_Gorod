
import requests

base_url = "https://web-gate.chitai-gorod.ru/api"

headers = { 

        'content-type': 'application/json',
        'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMDc3MDk5LCJpYXQiOjE3MjgzOTM1MzQsImV4cCI6MTcyODM5NzEzNCwidHlwZSI6MjB9.jDRnkIoiGA_VBm35lqAHVVTv26nIkrnlaNtxwXjwVlI"

}

# Найти книгу по названию

def test_russian_lang():
    resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=волшебник', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

# Найти книгу по латинице

def test_eng():
    resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase=wizard', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

# Найти книгу по ID

def test_id():
    resp = requests.get(base_url+'/v1/products/slug/master-i-margarita-3018590', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

# Получить список магазинов по городам

def test_shop():
    resp = requests.get(base_url+'/v1/shops-cities', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
# тест на пустой поиск

def test_empty():
    resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase= ', headers=headers)
    assert resp.headers["Content-Type"] == "application/json"
    assert 'Phrase должен содержать минимум 2 символа' in resp.text
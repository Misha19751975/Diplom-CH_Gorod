
import requests

base_url = "https://web-gate.chitai-gorod.ru/api"

headers = { 

        'content-type': 'application/json',
        'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjgyMDMwNTAsImlhdCI6MTcyODAzNTA1MCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjM5YjRlYWI0NTg0NmFjYWRhYTRlYmFmMTI1MzgyYWU0MDY4YTQ3NDAwYjgwMjI5YjA0Y2QyODY0YjNiNTk5MWUiLCJ0eXBlIjoxMH0.XtUnVQpSKufy_5icqiAB6bBAD2vsIwxGMXUo-5golE8"
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
    resp = requests.get(base_url+'/products/slug/master-i-margarita-3018590', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

# Получить список магазинов по городам

def test_shop():
    resp = requests.get(base_url+'/shops-cities', headers=headers)
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
# тест на пустой поиск

def test_empty():
    resp = requests.get(base_url+'/v2/search/facet-search?customer&phrase= ', headers=headers)
    assert resp.headers["Content-Type"] == "application/json"
    assert 'Phrase должен содержать минимум 2 символа' in resp.text
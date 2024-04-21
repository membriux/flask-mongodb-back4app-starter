import requests
import json

url = 'https://parseapi.back4app.com/parse/classes/Food'
headers = {
    'X-Parse-Application-Id': '{APP_ID}',
    'X-Parse-REST-API-Key': '{REST_API_KEY}',
    'Content-Type': 'application/json',
}


def create_food(food_name: str):
    data = {
        'name': food_name,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.json()



if __name__ == "__main__":
    create_food('test')

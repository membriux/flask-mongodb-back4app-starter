# Flask Mongodb (hosted on Back4App) Starter

Starter app for connecting flask app with mongo db hosted on Back4app (free DB)

Why create this template?
- Back4app provides FREE mongodb!
- There are no python resources on how to create a backend service that connects to Back4app (until this one)

**Sample Demo**

![demo1](https://github.com/membriux/flask-mongodb-back4app-starter/assets/20372706/878fcca4-b03b-486f-9b20-7a4eed6d3766)

## Before you Clone this repo

1. Create back4app.com account and create a sample database and collection
2. In back4app.com, obtain your credentials for the parse_service.py from these places:
   - API Server URL
     - ![APIKEY](api_url.png)
   - App ID and Rest API Key
     - ![App ID and api key](api_key_app_id.png)
3. Copy these values into `parse_service.py`

## Run it!

1. Install requirements `pip install -U flask requests`
1. Run it! `python app.py`

**Test it out!**

```bash
curl --location 'http://localhost:5000/food' \
--header 'Content-Type: application/json' \
--data '{
    "food": "sushi"
}'
```

### Documentation for Back4app Rest API 

Want to do more?
Here is the offical Rest API documentation for Parse: https://docs.parseplatform.org/rest/guide/



from flask import Flask, request
import parse_service

app = Flask(__name__)


@app.route('/food', methods=['POST', 'GET', 'DELETE'])
def add_food():
    if request.method == 'POST':
        user_input = request.get_json()
        food = user_input['food']
        return parse_service.create_food(food)


if __name__ == '__main__':
    app.run()

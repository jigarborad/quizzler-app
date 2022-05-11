import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
question_api = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_api.raise_for_status()
question_data = question_api.json()["results"]


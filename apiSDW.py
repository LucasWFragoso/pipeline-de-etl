import requests


sdw2023_api_url = "https://sdw-2023-prd.up.railway.app"


def get_user_api(id):
    response = requests.get(f"{sdw2023_api_url}/users/{id}")
    return response.json() if response.status_code == 200 else print("oi")


def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

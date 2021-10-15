from errors import *
import json
import requests

API_URL = "https://api.mojang.com/"

def get_player(username):
    player = requests.get(f"{API_URL}/users/profiles/minecraft/{username}")

    if player.status_code == 204:
        raise InvalidPlayer("User does not exist")

    else:
        player = player.json()

        return f"Username: {player['name']}\nUUID: {player['id']}"

def get_name(username):
    player = requests.get(f"{API_URL}/users/profiles/minecraft/{username}")

    if player.status_code == 204:
        raise InvalidPlayer("User does not exist")

    else:
        player = player.json()

        return player['name']

def get_uuid(username):
    player = requests.get(f"{API_URL}/users/profiles/minecraft/{username}")

    if player.status_code == 204:
        raise InvalidPlayer("User does not exist")

    else:
        player = player.json()

        return player['id']

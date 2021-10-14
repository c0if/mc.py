from errors import *
import requests

API_URL = "https://api.mojang.com/"

def get_player(username):
    player = requests.get(f"{API_URL}/users/profiles/minecraft/{username}").json()
    return player

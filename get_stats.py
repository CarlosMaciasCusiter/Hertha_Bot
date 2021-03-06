import os
import requests
import json

# Usefule ID's
HERTHA_BERLIN_TEAM_ID = 159
BUNDASLIGA_1 = 78

headers = {
    "x-rapidapi-key": os.environ["X_RAPIDAPI_KEY"],
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com",
}


def getPlayers():

    url = "https://api-football-v1.p.rapidapi.com/v3/players"

    querystring = {"team": str(HERTHA_BERLIN_TEAM_ID), "season": "2021"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    players = json.loads(response.text)

    x = []

    for player in players["response"]:
        x.append(player["player"]["name"])

    return x


def getInjuredPlayers():

    url = "https://api-football-v1.p.rapidapi.com/v3/injuries"

    querystring = {"team": str(HERTHA_BERLIN_TEAM_ID), "season": "2020"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    injuries = json.loads(response.text)

    injuredPlayers = []

    for injury in injuries["response"]:
        injuredPlayers.append(
            {
                "name": injury["player"]["name"],
                "player_id": injury["player"]["id"],
                "photo": injury["player"]["photo"],
                "reason": injury["player"]["reason"],
                "fixture_date": injury["fixture"]["date"],
                "fixture_timestamp": injury["fixture"]["timestamp"]
            }
        )

    return injuredPlayers


with open("injuries.json", "w") as outfile:
    json.dump(getInjuredPlayers(), outfile)

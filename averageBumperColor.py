import api_key

import requests
import json

teams = {}

event_code = input('Tba key: ')
api_url = f'event/{event_code}/matches/simple'
full_url = f'https://www.thebluealliance.com/api/v3/{api_url}'
request = requests.get(full_url, headers=api_key.request_headers)
matches = request.json()

for match in matches:
    blue = match["alliances"]["blue"]["team_keys"]
    red = match["alliances"]["red"]["team_keys"]

    for team in blue:
        teams[team] = teams.get(team, 0) + 1
    for team in red:
        teams[team] = teams.get(team, 0) - 1

print(teams)

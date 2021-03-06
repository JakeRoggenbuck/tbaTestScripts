import requests
import json
import api_key

tba_key = input('TBA event key: ')

api_url = f'event/{tba_key}/teams'
full_url = f'https://www.thebluealliance.com/api/v3/{api_url}'
request = requests.get(full_url, headers=api_key.request_headers)
teams = request.json()

for team in teams:
    print(f'Team {team["key"]} {team["nickname"]} is from {team["city"]}, {team["state_prov"]} and their rookie year was {team["rookie_year"]}')

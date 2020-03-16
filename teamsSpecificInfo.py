import requests
import json
import api_key

team_key = input('Team key: ')

api_url = f'team/{team_key}'
full_url = f'https://www.thebluealliance.com/api/v3/{api_url}'
request = requests.get(full_url, headers=api_key.request_headers)
team = request.json()

print(team)

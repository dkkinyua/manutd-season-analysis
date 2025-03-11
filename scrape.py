"""
Scraping the FBRef website was hectic. Let's use the Sofascore API to get the team's statistics

"""
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


url = 'https://sofascore.p.rapidapi.com/teams/get-squad'

query_string = {
    "teamId": "35"
}

headers = {
	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
	"x-rapidapi-host": os.getenv("RAPIDAPI_HOST")
}

response = requests.get(url, headers=headers, params=query_string)
data = response.json() # Gets the team's statistics

# let's send this data to a .json file
with open('manutd.json', 'w') as f:
    json.dump(data, f)
    

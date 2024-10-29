# API scan for FUT DB
import requests, json, os
from dotenv import load_dotenv
# ~~~~ LOAD ENV VARIABLES ~~~~
load_dotenv()

# Gets FUT info from API
# Swaps between players, clubs, leagues and nations
# Not set for easy swapping just manual changes

def get_fut_database() -> None:
    page: int = 1
    token: str | None = os.getenv(key="API_AUTH_TOKEN")
    
    with open(file="./data/fut_leagues.json",mode='r+') as file:
        file_data = json.loads(file.read())

        while page <= 4:
            try:
                url: str = f"https://api.futdatabase.com/api/leagues?page={page}"
                print(f"Calling URL: {url}")
                response: requests.Response = requests.get(url=url, headers={"X-AUTH-TOKEN": f"{token}", 'accept': 'application/json'})
                page += 1
                new_data = response.json()
                file_data["items"].extend(new_data["items"])
                file.seek(0)
                print("SUCCESS")
            except requests.exceptions.RequestException as e:
                print('Error:', e)
        
        json.dump(file_data, file, indent = 4)
        

            
get_fut_database()
import os
from dotenv import load_dotenv
from serpapi import GoogleSearch  #

# Load .env
load_dotenv()

# Ambil API key
api_key = os.getenv("SERPAPI_KEY")

# Siapkan parameter pencarian
params = {
    "engine": "google_maps",
    "q": "Gacoan Terdekat",
    "ll": "@-6.8731527,107.5423099,10z",  #"latitude,longitude"  
    "api_key": api_key
}

# Lakukan search
search = GoogleSearch(params)
results = search.get_dict()

# Print hasil
print(results)

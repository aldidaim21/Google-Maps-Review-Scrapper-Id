import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
import pandas as pd

# Load .env file
load_dotenv()

# Ambil API key
api_key = os.getenv("SERPAPI_KEY")

# Siapkan parameter pencarian
params = {
    "engine": "google_maps",
    "q": "Gacoan Terdekat",
    "ll": "@-6.8731527,107.5423099,10z",
    "api_key": api_key
}

# Lakukan pencarian
search = GoogleSearch(params)
results = search.get_dict()

# Ekstrak data dari hasil pencarian
local_results = results.get("local_results", [])

# Periksa apakah ada hasil
if not local_results:
    print("Tidak ada hasil ditemukan.")
else:
    # Ambil kolom penting termasuk place_id
    data = []
    for place in local_results:
        data.append({
            "Place ID": place.get("place_id"),
            "Nama Tempat": place.get("title"),
            "Alamat": place.get("address"),
            "Rating": place.get("rating"),
            "Jumlah Review": place.get("reviews"),
            "Kategori": place.get("type"),
            "Jarak": place.get("distance"),
            "Website": place.get("website"),
            "Telepon": place.get("phone")
        })

    # Tampilkan sebagai tabel
    df = pd.DataFrame(data)
    pd.set_option("display.max_colwidth", None)
    print(df.to_string(index=False))

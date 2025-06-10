import os
import csv
from dotenv import load_dotenv
from serpapi import GoogleSearch
import time

# Load .env
load_dotenv()

# Ambil API key
api_key = os.getenv("SERPAPI_KEY")

def get_reviews(place_id, max_reviews=200):
    all_reviews = []
    next_page_token = None
    attempts = 0
    max_attempts = 20  # Maksimal percobaan pagination
    
    while len(all_reviews) < max_reviews and attempts < max_attempts:
        params = {
            "engine": "google_maps_reviews",
            "api_key": api_key,
            "place_id": place_id,
            "sort_by": "qualityScore",
            "hl": "id",
        }
        
        # Gunakan token pagination jika ada
        if next_page_token:
            params["next_page_token"] = next_page_token
        
        try:
            search = GoogleSearch(params)
            results = search.get_dict()
            
            # Ambil reviews dari hasil
            new_reviews = results.get("reviews", [])
            all_reviews.extend(new_reviews)
            
            # Cek token untuk halaman berikutnya
            next_page_token = results.get("serpapi_pagination", {}).get("next_page_token")
            
            # Jika tidak ada halaman berikutnya, berhenti
            if not next_page_token:
                break
                
            # Tunggu sebentar antara request
            time.sleep(2)
            attempts += 1
            
        except Exception as e:
            print(f"Error mendapatkan review: {str(e)}")
            break
    
    return all_reviews[:max_reviews]

# Main program
if __name__ == "__main__":
    place_id = "ChIJK--RT9TnaC4R3vmpjNmLKMQ"
    csv_file = "GacoanReview.csv"
    
    print("Mengambil data review...")
    reviews = get_reviews(place_id, max_reviews=100)
    
    if not reviews:
        print("Tidak ada review ditemukan.")
    else:
        print(f"Berhasil mendapatkan {len(reviews)} review.")
        
        # Siapkan data untuk CSV
        csv_data = []
        for review in reviews:
            csv_data.append({
                "User": review.get("user", {}).get("name", "Anonymous"),
                "Rating": review.get("rating", ""),
                "Date": review.get("date", ""),
                "ISO_Date": review.get("iso_date", ""),
                "Review": review.get("snippet", ""),
                "Review_Length": len(review.get("snippet", "")),
                "Response": review.get("response", {}).get("snippet", "") if review.get("response") else ""
            })
        
        # Simpan ke CSV
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            if csv_data:
                writer = csv.DictWriter(file, fieldnames=csv_data[0].keys())
                writer.writeheader()
                writer.writerows(csv_data)
                print(f"Data review berhasil disimpan ke {csv_file}")
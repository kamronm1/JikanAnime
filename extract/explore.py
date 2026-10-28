import requests
import time

BASE_URL = "https://api.tenrai.org/v1"
YEAR = 2026

for season in ["winter", "spring", "summer", "fall"]:
    url = f"{BASE_URL}/seasons/{YEAR}/{season}"
    response = requests.get(url, timeout=10)
    data = response.json()

    print(season, response.status_code)
    print("  anime on this page:", len(data["data"]))
    print("  first title:", data["data"][0]["title"])
    print("  pagination:", data["pagination"])

    time.sleep(1)
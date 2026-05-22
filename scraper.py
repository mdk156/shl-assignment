import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"

response = requests.get(BASE_URL)

soup = BeautifulSoup(response.text, "html.parser")

data = []

links = soup.find_all("a")

for link in links:

    text = link.get_text(strip=True)

    href = link.get("href")

    if href and "product-catalog/view" in href:

        full_url = "https://www.shl.com" + href

        data.append({
            "name": text,
            "url": full_url
        })

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

df.to_csv("shl_catalog.csv", index=False)

print("Catalog scraped successfully")
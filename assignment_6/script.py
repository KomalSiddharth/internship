import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_amazon_product_links(category_url, max_items=100):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1",  # Do Not Track Request Header
    }
    
    product_links = []
    page = 1
    
    while len(product_links) < max_items:
        url = f"{category_url}&page={page}"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page} for URL: {url} (Status Code: {response.status_code})")
            break
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if '/dp/' in href and href not in product_links:
                product_links.append("https://www.amazon.com" + href)
                if len(product_links) >= max_items:
                    break
        
        page += 1
        time.sleep(2)
    
    return product_links

def scrape_amazon_categories(categories):
    all_data = []

    for category_name, category_url in categories.items():
        print(f"Scraping category: {category_name}")
        product_links = get_amazon_product_links(category_url)
        if product_links:  # Only append if links are found
            category_data = {
                "Category": category_name,
                "Product_Link": product_links
            }
            df_category = pd.DataFrame(category_data)
            all_data.append(df_category)
        else:
            print(f"No links retrieved for category: {category_name}")

    df_all_categories = pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()
    return df_all_categories

categories = {
    "Industrial & Scientific": "https://www.amazon.com/s?k=industrial+scientific",
    "Printers": "https://www.amazon.com/s?k=printers",
    "Gaming Laptops": "https://www.amazon.com/s?k=gaming+laptop",
    "Baby Furniture": "https://www.amazon.com/s?k=baby+furniture",
    "Innerwear": "https://www.amazon.com/s?k=innerwear",
    "Baby Food": "https://www.amazon.com/s?k=food",
    "Handmade Products": "https://www.amazon.com/s?k=handmade+products",
    "Fashion": "https://www.amazon.com/s?k=fashion"
}

df_all_categories = scrape_amazon_categories(categories)

if not df_all_categories.empty:
    df_all_categories.to_csv("products.csv", index=False)
    print("Scraping complete. Data saved to products.csv")
else:
    print("No data scraped, CSV file not created.")

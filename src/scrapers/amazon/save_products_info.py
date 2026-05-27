from dotenv import load_dotenv
import os, csv
from src.scrapers.amazon.scraper import scrape_product

load_dotenv()

def save_amazon_to_csv():
    print("========AMAZON========")
    
    raw_asins = os.getenv("ASINS")
    if not raw_asins:
        return print("ASINS no definidos")
    
    asins = raw_asins.split(",")
    
    os.makedirs("./data", exist_ok=True)
    
    with open("./data/amazon-products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        writer.writerow(["ASIN", "Título", "Precio", "Disponibilidad"])
        
        for asin in asins:
            product = scrape_product(asin)
            writer.writerow([asin, product["title"], product["price"], product["availability"]])
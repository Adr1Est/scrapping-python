from dotenv import load_dotenv
import os, csv
from src.amazon.amazon_product_scrapper import amazon_product_scrapper

load_dotenv()

asins = os.getenv("ASINS").split(",")

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    writer.writerow(["ASIN", "Título", "Precio", "Disponibilidad"])
    
    for asin in asins:
        product = amazon_product_scrapper(asin)
        writer.writerow([asin, product["title"], product["price"], product["availability"]])

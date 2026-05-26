from dotenv import load_dotenv
import os 
from src.amazon_product_scrapper import amazon_product_scrapper

load_dotenv()

asins = os.getenv("ASINS").split(",")
for asin in asins:
    amazon_product_scrapper(asin)


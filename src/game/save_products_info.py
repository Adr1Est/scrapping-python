from dotenv import load_dotenv
from src.game.scraper import scrape_product
import os, csv

load_dotenv()

game_codes = os.getenv("GAME_PRODUCTS").split(",")

def save_game_to_csv():
    os.makedirs("./data", exist_ok=True)
    
    with open("./data/game-products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        writer.writerow(["Codígo", "Título", "Precio", "Plataformas", "Edición", "Lanzamiento"])
        
        for code in game_codes:
            game = scrape_product(code)
            writer.writerow([code, game["title"], game["price"], game["platform"], game["edition"], game["release_data"]])
        
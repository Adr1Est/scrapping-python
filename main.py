from src.amazon.save_products_info import save_to_csv
from src.game.scraper import scrape_product

def main():
    # save_to_csv()
    scrape_product("246786")
    
if __name__ == "__main__":
    main()
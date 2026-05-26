from src.amazon.save_products_info import save_to_csv
from src.game.save_products_info import save_game_to_csv

def main():
    save_to_csv()
    save_game_to_csv()
    
if __name__ == "__main__":
    main()
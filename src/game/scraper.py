import requests
from bs4 import BeautifulSoup
from src.utils.headers import headers

def scrape_product(code):
    url = f"https://www.game.es/{code}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        product_title = soup.select_one("h2.product-title span.cm-txt").get_text(strip=True)
        
        product_info_html = soup.find("div", class_="product-info")
        dl = product_info_html.find("dl")
        
        product_info = {}
        
        for dt in dl.find_all("dt"):
            key = dt.get_text(strip=True)
            
            dd = dt.find_next_sibling("dd")
            if not dd:
                continue
            
            values = [span.get_text(strip=True) for span in dd.find_all("span", class_="cm-txt")]
            
            product_info[key] = values[0] if len(values) == 1 else values
            
        product_price = soup.find("input", id = "ProductPrice")
            
        print(product_title)
        print(product_info)
        print(product_price["value"])
        
        return {
            "title": product_title,
            "platform": product_info["Plataforma:"],
            "edition": product_info["Edición:"],
            "release_data": product_info["Lanzamiento:"] if product_info["Lanzamiento:"] else "Desconocida",
            "price": product_price["value"]
        }
    else:
        print("Petición fallida -> ", response.status_code)(url, headers=headers)
from bs4 import BeautifulSoup
from src.lib.http_client import get

def scrape_product(asin):
    url = f"https://www.amazon.es/dp/{asin}"
    
    response = get(url)
      
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        productTitle = soup.find("span", id="productTitle")
        productPrice = soup.find("span", id="apex-pricetopay-accessibility-label")
        productAvailable = soup.find("span", class_ = "primary-availability-message")
        title = productTitle.get_text(strip=True) if productTitle else "No encontrado"
        price = productPrice.get_text(strip=True) if productPrice else "No encontrado"
        availability  = productAvailable.get_text(strip=True) if productAvailable else "No encontrado"
        print(title)
        print(f"{price} -  {availability}")
        return  {
            "title": title,
            "price": price,
            "availability": availability
        }
    else:
        print("Petición fallida -> ", response.status_code)
    
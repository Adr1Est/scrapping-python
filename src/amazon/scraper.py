import requests
from bs4 import BeautifulSoup

def scrape_product(asin):
    url = f"https://www.amazon.es/dp/{asin}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9",
    }
    
    response = requests.get(url, headers=headers)
      
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
        print("Petición fallida -> ", response.status_code)(url, headers=headers)
    
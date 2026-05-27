import requests
from src.utils.headers import headers as default_headers

def get(url, headers=None, timeout=10):
    response = requests.get(
        url,
        headers=headers or default_headers,
        timeout=timeout,
    )
    
    return response
import requests
from bs4 import BeautifulSoup

url = 'https://mercadinhossaoluiz.com.br/loja/355/categoria/13726'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://mercadinhossaoluiz.com.br/'
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Use the full class list from your HTML sample
        product_items = soup.find_all('div', {
            'class': lambda x: x and 'store-card-product' in x.split()
        })
        
        products = []
        for item in product_items:
            product_description = item.find('div', class_='product-description')
            if product_description:
                price_element = product_description.find('p', class_='current-price-product')
                price = ' '.join(price_element.stripped_strings) if price_element else 'N/A'
                
                # Get the NEXT <p> tag after price element
                name_element = price_element.find_next('p') if price_element else None
                name = name_element.get_text(strip=True) if name_element else 'N/A'
                
                products.append((name, price))
        
        print(f'Found {len(products)} products')
        for idx, (name, price) in enumerate(products, 1):
            print(f'{idx}. Product: {name}, Price: {price}')
    else:
        print(f'Error: HTTP {response.status_code}')

except Exception as e:
    print(f'Error: {str(e)}')
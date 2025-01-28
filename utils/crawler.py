from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

url = 'https://mercadinhossaoluiz.com.br/loja/355/categoria/13796'

# Configure Firefox options
options = FirefoxOptions()
#options.add_argument('--headless')  # Remove this to see the browser
options.set_preference('general.useragent.override', 
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0')

# Initialize Firefox driver with Service object
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

try:
    driver.get(url)
    
    # Wait for content to load
    driver.implicitly_wait(50)
    
    # Find product containers
    product_items = driver.find_elements(
        By.CSS_SELECTOR,
        'div.MuiGrid-root.store-card-product'
    )
    
    products = []
    for item in product_items:
        try:
            price_element = item.find_element(By.CSS_SELECTOR, 'p.current-price-product')
            price = price_element.text
            name_element = price_element.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div/div[3]/div[1]/div/div/div/div/div[1]/div/div[1]/p[2]')
            name = name_element.text
            products.append((name, price))
        except Exception as e:
            print(f"Error extracting product: {str(e)}")
            products.append(('N/A', 'N/A'))
    
    print(f"\nFound {len(products)} products:")
    for idx, (name, price) in enumerate(products, 1):
        print(f'{idx}. {name} - {price}')

finally:
    next
    #driver.quit()
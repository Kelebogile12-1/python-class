from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

def electronic(url):
    driver.get(url)
    time.sleep(5)  # wait for the page to fully load

    # Parse the page
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find all product containers
    product_items = soup.find_all("div", class_="search-product grid")

    # Create a list to store data
    products = []

    for item in product_items:
        name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
        price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
        
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            products.append({"Name": name, "Price": price})

    # Convert to pandas DataFrame
    df = pd.DataFrame(products)

    # Save to CSV
    df.to_csv("myLaptops.csv", index=False, encoding="utf-8")

    print("Data saved to myLaptops.csv")
    print(df.head())  # Display first few rows for verification

    driver.quit()

# Run the scraper
electronic("https://www.takealot.com/all?_sb=1&_r=1&_si=c6d9135a49bdef377840c6e9b647981b&qsearch=laptops")


from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()

#print(soup.prettify()
# Find all product containers
def electronic(url):
    driver.get(url)
    time.sleep(5)  # wait for products to load
    soup = BeautifulSoup(driver.page_source, "html.parser")
   
    product_items = soup.find_all("div", class_="search-product grid")

    for item in product_items:
        name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
        price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            print(f"{name} - {price}")
            myfile=open('myLaptops.csv', 'w')       
            myfile.write(f"{name}-{price}\n") 
        
    driver.quit()

electronic("https://www.takealot.com/all?_sb=1&_r=1&qsearch=laptop&via=suggestions&_si=c6d9135a49bdef377840c6e9b647981b")


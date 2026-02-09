
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

import matplotlib.pyplot as plt

def scrapping_Products(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(7)  # wait for products to load
    soup = BeautifulSoup(driver.page_source, "html.parser")
    product_items = soup.find_all("div", class_="search-product grid")
    # Store data in a list of dictionaries
    products = []
    for item in product_items:
        name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
        price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            products.append({"Product Name and specs": name, "Price": price, })
   


    driver.quit()
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(products)
    df.to_csv("Fridge.csv", index=False)
    print(df)
def clean_data():
    print("\ncleaning data")
    df= pd.read_csv("Fridge.csv")
    #remove R, commas, spaces - convert to number
    df['clean_price'] = (
        df['Price']
        .str.replace("R", "",regex=False)
        .str.replace(",", "",regex=False)
        .astype(int)
    )
    #extract barnd name from the first word
    df['brand']=(
        df['Product Name and specs']
        .str.split().str[0]
         .apply(lambda x: x if not x.isdigit() else "Unknown")
    )
    df['category'] = df['clean_price'].apply(
        lambda x : "budget friendly" if x < 4000 else "Mid-Range" if x <= 8000 else "premium"
    )
    df.to_csv("takealot_clean.csv", index=False)
    print("Cleaned data saved takealot_clean")
    return df

# Run the scraper


def analyze_data(df):
    print("\n Starting analysis...")
    # 1. PRICE DISTRIBUTION
    plt.figure()
    plt.hist(df["clean_price"])
    plt.title("Price Distribution of Phones")
    plt.xlabel("Price (Rand)")
    plt.ylabel("Frequency")
    plt.savefig("price_distribution.png")
    plt.close()
    # 2. BRAND COUNT
    plt.figure()
    df["brand"].value_counts().plot(kind="bar")
    plt.title("Number of Phones Per Brand")
    plt.xlabel("Brand")
    plt.ylabel("Count")
    plt.savefig("brand_count.png")
    plt.close()
    print("Analysis complete! Plots saved as 'price_distribution.png' and 'brand_count.png'.")
    print("\n Starting analysis...")
    # 1. PRICE DISTRIBUTION
    plt.hist(df["clean_price"])
    plt.title("Price Distribution of Phones")
    plt.xlabel("Price (Rand)")
    plt.ylabel("Frequency")
    plt.show()
    # 2. BRAND COUNT
    plt.figure()
    df["brand"].value_counts().plot(kind="bar")
    plt.title("Number of Phones Per Brand")
    plt.xlabel("Brand")
    plt.ylabel("Count")
    plt.show()
    print(" Visualisations complete.")

scrapping_Products("https://www.takealot.com/all?_sb=1&_r=1&qsearch=television&via=suggestions&_si=c60259fbac8b1729703b1a7ccd2bc536")
clean_info = clean_data()
analyze_data(clean_info)











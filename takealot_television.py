from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import matplotlib.pyplot as plt
# List of known TV brands
tv = ["Samsung", "LG", "Telefunken", "Sony", "Hisense", "JVC", "Digimark", "Supersonic"]
# Scrape product data from Takealot
def scrapping_Products(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(22)  # wait for products to load
    soup = BeautifulSoup(driver.page_source, "html.parser")
    product_items = soup.find_all("div", class_="search-product grid")
    products = []
    for item in product_items:
        name_tag = item.find("h4", class_="product-card-module_product-title_16xh8")
        price_tag = item.find("span", class_="currency plus currency-module_currency_29IIm")
        if name_tag and price_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            products.append({"Product Name and specs": name, "Price": price})
    driver.quit()
    df = pd.DataFrame(products)
    df.to_csv("television.csv", index=False)
    print(df)
# Identify brand from product name
def tv_brand_displayer(name):
    for brand in tv:
        if brand.lower() in name.lower():
            return brand
    return "Unknown"
# Clean and transform scraped data
def clean_data():
    print("\nCleaning data...")
    df = pd.read_csv("mytelevision.csv")
    # Clean price column
    df['clean_price'] = (
        df['Price']
        .str.replace("R", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(int)
    )
    # Extract brand using helper function
    df['brand'] = df['Product Name and specs'].apply(tv_brand_displayer)
    # Categorize price ranges
    df['category'] = df['clean_price'].apply(
        lambda x: "budget friendly" if x < 4000 else "Mid-Range" if x <= 8000 else "premium"
    )
    df.to_csv("takealot_tv.csv", index=False)
    print("Cleaned data saved to 'takealot_tv.csv'")
    return df
# Analyze and visualize data
def analyze_data(df):
    print("\nStarting analysis...")
    # Price distribution
    plt.figure()
    plt.hist(df["clean_price"], bins=10, color='skyblue', edgecolor='black')
    plt.title("Price Distribution of Televisions")
    plt.xlabel("Price (Rand)")
    plt.ylabel("Frequency")
    plt.savefig("TV_price_distribution.png")
    plt.show()
    # Brand count
    plt.figure()
    df["brand"].value_counts().plot(kind="bar", color='orange')
    plt.title("Number of Televisions Per Brand")
    plt.xlabel("Brand")
    plt.ylabel("Count")
    plt.savefig("TV_brand_count.png")
    plt.show()
    print("Analysis complete! Plots saved.")
# Run the full pipeline
scrapping_Products("https://www.takealot.com/all?_sb=1&_r=1&_si=c60259fbac8b1729703b1a7ccd2bc536&qsearch=television")
clean_info = clean_data()
analyze_data(clean_info)












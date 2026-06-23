import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

df = pd.DataFrame(quotes, columns=["Quote"])

df.to_csv("Dataset/quotes.csv", index=False)
import matplotlib.pyplot as plt

plt.bar(["Quotes"], [len(df)])
plt.title("Total Quotes Scraped")

plt.savefig("Screenshots/quotes_chart.png")

plt.show()
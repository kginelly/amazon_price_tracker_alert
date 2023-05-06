import requests
import lxml
from bs4 import BeautifulSoup

url = "Input the product you want to keep track on."
header = {
    "User-Agent": "Input your details",
    "Accept-Language": "Input your details"
}

response = requests.get(url, headers=header)
food = BeautifulSoup(response.content, "lxml")
print(food.prettify())

price = food.find(class_="a-offscreen").get_text()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# Email alert: When the price decreases to your targeted number, you will receive an email notification
import smtplib

title = food.find(id="productTitle").get_text().strip()

print(title)

BUY_PRICE = 8

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("Input your SMTP address", port=587) as connection:
        connection.starttls()
        result = connection.login("Input your email", "Input your password")
        connection.sendmail(
            from_addr="Input your email",
            to_addrs="Input your email",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
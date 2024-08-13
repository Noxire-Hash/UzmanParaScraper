from bs4 import BeautifulSoup
import requests


class UzmanParaScraper:
    "This is a scraper for UzmanPara you need to provide a stock name to get the data example: user_stock='AEFES'"

    def __init__(self, user_stock: str):
        soup = BeautifulSoup(requests.get(
            'https://uzmanpara.milliyet.com.tr/canli-borsa/').content, 'html.parser')
        self.user_stock = soup.find(class_="zebra", id=f"h_tr_id_{user_stock}")
        self.classes = set()
        self.ids = set()
        self.state = "null"
        self.price_id = f"h_td_id_{user_stock}"
        self.user_stock_name = user_stock

    def find_all_classes(self):
        """Returns all classes of the stock"""
        if self.user_stock:
            if self.user_stock.get("class"):
                self.classes.update(self.user_stock.get("class"))

            for child in self.user_stock.find_all(True):  # True means all tags
                if child.get("class"):
                    self.classes.update(child.get("class"))
        return self.classes

    def find_all_ids(self):
        """Returns all the ids of the stock"""
        if self.user_stock:
            if self.user_stock.get("id"):
                self.ids.update(self.user_stock.get("id"))

            for child in self.user_stock.find_all(True):  # True means all tags
                if child.get("id"):
                    self.ids.update(child.get("id"))
        return self.ids

    def find_stock_state(self):
        """Returns the state of the stock (up, down, flat)"""
        if self.user_stock:
            self.classes = self.find_all_classes()
            if not self.classes:
                print(
                    "ERROR: 100 - Classes not found (BorsaIST maybe closed or couldn't retrieve data from YeniPara)")
                return "null"

            for i in self.classes:
                if i == 'currency-down':
                    self.state = 'down'
                    break
                elif i == 'currency-up':
                    self.state = 'up'
                    break
                elif i == 'currency-flat':
                    self.state = 'flat'
                    break

            if self.state == "null":
                print("Stock state not found")
            return self.state

    def get_price(self):
        """Returns the price of the stock"""
        price_element = self.user_stock.find(
            id=f"h_td_fiyat_id_{self.user_stock_name}")
        if price_element:
            return price_element.text.strip()
        else:
            return "Price not found"

    def create_dump(self, func):
        """Creates a dump file with the data"""
        data = func()
        open("dump.txt", "w").write(data)
        return data

    def get_precentage(self):
        """Returns the precentage of the stock"""
        precentage_element = self.user_stock.find(
            id=f"h_td_yuzde_id_{self.user_stock_name}")
        if precentage_element:
            return precentage_element.text.strip()
        else:
            return "Precentage not found"

    def stock_info(self):
        """Returns a dictionary with stock_name, price, precentage and state"""
        return {
            "stock_name": self.user_stock_name,
            "price": self.get_price(),
            "precentage": self.get_precentage(),
            "state": self.find_stock_state()
        }

    def make_it_pretty(self):
        """Returns a pretty string with stock_name, price, precentage and state"""
        stock_info = self.stock_info()
        return f"Stock Name: {stock_info['stock_name']}\nPrice: {stock_info['price']} TL\nPrecentage: {stock_info['precentage']}%\nState: {stock_info['state']}"


ups = UzmanParaScraper(user_stock="ALARK")

print(type(ups.stock_info()))

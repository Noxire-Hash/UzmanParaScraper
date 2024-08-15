from bs4 import BeautifulSoup
import requests


class UPSCORE:
    "This is a scraper for UzmanPara you need to provide a stock name to get the data example: user_stock='AEFES'"

    def __init__(self, user_stock: str):
        self.endpoint = 'https://uzmanpara.milliyet.com.tr'

        soup_bist100 = BeautifulSoup(requests.get(
            f"{self.endpoint}/canli-borsa/bist-100-hisseleri/").content, 'html.parser')

        self.user_stock = soup_bist100.find(
            class_="zebra", id=f"h_tr_id_{user_stock}")
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

    def get_href(self):
        """Returns the href of the stock"""
        if self.user_stock:
            a_tag = self.user_stock.find('a', href=True)
            if a_tag:
                return a_tag['href']
        return "Href not found"

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

    def create_dump(self, func):
        """Creates a dump file with the data"""
        data = func()
        with open("dump.txt", "w", encoding="utf-8") as file:
            file.write(data)
        return data

    def goto_stock(self):
        """Opens the stock page"""
        href = self.get_href()
        if href:
            soup_stock_page = BeautifulSoup(requests.get(
                f"{self.endpoint}{href}").content, 'html.parser')
            self.user_stock_page = soup_stock_page
            return self.user_stock_page
        else:
            return "Href not found"

    def get_general_info(self):
        soup = self.goto_stock()
        soup.find_all("div", class_="currency")
        tr = soup.find_all("tr")
        print(tr)
        currency_td = tr.find_all("td", class_="currency")
        value_td = tr.find_all("td", class_="value")
        print(currency_td, value_td)

    def get_technic_analysis(self):
        pass

    def get_basic_analysis(self):
        pass

    def get_page_data(self):
        soup = self.goto_stock()
        data = {}
        for tr in soup.find_all('tr'):
            currency_td = tr.find('td', class_='currency')
            value_tds = tr.find_all('td', class_='right')

            if currency_td and value_tds:
                currency_name = currency_td.get_text(strip=True)
                currency_values = [td.get_text(strip=True) for td in value_tds]
                if len(currency_values) == 1:
                    data[currency_name] = currency_values[0]
                else:
                    data[currency_name] = currency_values

        return data
    pass

# UzmanParaScraper

UzmanParaScraper is a Python-based web scraper designed to extract stock data from the UzmanPara website. This tool allows users to retrieve stock information by providing a stock name.

## Features

- **Scrape Stock Data**: Retrieve stock data by providing a stock name.
- **Find All Classes**: Extract all CSS classes associated with the stock.
- **Find All IDs**: Extract all HTML IDs associated with the stock.
- **Determine Stock State**: Identify whether the stock is up, down, or flat based on its CSS classes.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/UzmanParaScraper.git
    ```
2. Navigate to the project directory:
    ```sh
    cd UzmanParaScraper
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Import the [`UzmanParaScraper`](command:_github.copilot.openSymbolFromReferences?%5B%22UzmanParaScraper%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22e%3A%5C%5CUzmanParaScraper%5C%5CUzmanParaScraper.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fe%253A%2FUzmanParaScraper%2FUzmanParaScraper.py%22%2C%22path%22%3A%22%2FE%3A%2FUzmanParaScraper%2FUzmanParaScraper.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A6%7D%7D%5D%5D "Go to definition") class:
    ```python
    from UzmanParaScraper import UzmanParaScraper
    ```
2. Create an instance of the scraper with the desired stock name:
    ```python
    scraper = UzmanParaScraper('AEFES')
    ```
3. Use the available methods to retrieve data:
    ```python
    classes = ups.find_all_classes()
    ids = ups.find_all_ids()
    state = ups.find_stock_state()
    ```

## Lack of BIST100 API

Currently, there is no official API available for developers to access BIST100 stock data. This project aims to solve that problem on a small scale by scraping data from the UzmanPara website. Note that this tool currently works only with BIST100 companies.

## TODO

- **Get News**: Implement functionality to retrieve the latest news related to the stock.
- **Push Notifications via Email**: Add a feature to send email notifications for stock updates.
- **Find Stock Name from Company Name or Vice Versa**: Implement a method to find the stock name given a company name or find the company name given a stock name.
- **Support More Companies**: Extend the scraper to support companies beyond the BIST100.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

Feel free to customize this README further based on your specific needs and project details.

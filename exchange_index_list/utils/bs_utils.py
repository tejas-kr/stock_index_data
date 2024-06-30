import requests
from bs4 import BeautifulSoup
from utils.logger import logger


class BSService:
    exchange_urls = {
        "nifty": "https://www.moneyworks4me.com/best-index/nse-stocks/top-nifty50-companies-list",
        "sensex": "https://www.moneyworks4me.com/best-index/bse-stocks/top-bse30-companies-list/"
    }

    def __init__(self, exchange: str):
        """
        BSService Constructor

        :param exchange: (str) Name of the Exchnage.
        """
        self._exchange = exchange
        self._req_obj = requests.get(
            self.exchange_urls[self._exchange.lower()],
            headers={
                "User-Agent": "insomnia / 9.2.0"
            }
        )
        logger.info(f"Request Object Create for {self._exchange}")

    def get_soup(self) -> BeautifulSoup:
        """get_soup

        Get the soup object

        :return: BeautifulSoup Object containing the HTML Page data
        """
        soup = BeautifulSoup(self._req_obj.text, "lxml")
        logger.info("Soup Object created")
        return soup

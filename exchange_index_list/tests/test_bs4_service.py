from bs4 import BeautifulSoup
from utils.bs_utils import BSService


def test_bs_service() -> None:
    """test_bs_service

     :return: None
     """

    bs_obj = BSService(exchange="Nifty")
    test_soup = bs_obj.get_soup()

    assert isinstance(test_soup, BeautifulSoup)

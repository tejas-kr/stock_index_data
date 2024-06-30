from logging import Logger
from typing import Dict, List, Optional
from exchange_index_list.utils.bs_utils import BSService
from exchange_index_list.exchanges.abstractions import Exchange


class NiftyExchange(Exchange):
    """NiftyExchange
    """

    def __init__(self, logger: Logger) -> None:
        self._logger = logger
        self._bs_obj = BSService(exchange="nifty")
        self._logger.info("Nifty Object created")

    def get_all_data(self) -> Optional[List[Dict]]:
        """get_all_data
        Get all data of the stocks listed in the index.

        :return: List of Dict of all stock's data listed in the index
        """
        all_data: List[Dict] = []
        try:
            _soup = self._bs_obj.get_soup()
            table_main_all_data = _soup.find(id="stock-list-table")
            table_rows = table_main_all_data.find_all("tr")[1:]

            for row in table_rows:
                row_tds = row.find_all("td")
                row_data_dict = {
                    "companyName": row_tds[1].find("a").text,
                    "LTP": row_tds[2].text,
                    "marketCap": row_tds[4].text,
                }
                all_data.append(row_data_dict)

            return all_data
        except Exception as exp:
            self._logger.exception(exp)


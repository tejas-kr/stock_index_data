from enum import Enum
from utils.logger import logger
from exchange_index_list.exchanges.nifty import NiftyExchange
from exchange_index_list.exchanges.sensex import SensexExchange
from exchange_index_list.exchanges.abstractions import Exchange
from typing import Literal, Dict, List, Optional


class IndexService(Enum):
    NSENifty = NiftyExchange
    BSESensex = SensexExchange


class IndexData:
    """IndexData
    """

    def __init__(self, index_name: Literal["NSENifty", "BSESensex"]) -> None:
        """
        IndexData Constructor

        :param index_name: Index Name. Allowed options are ("NSENifty" and "BSESensex")
        """
        self._index_name = index_name

    def get_index_data(self) -> Optional[List[Dict]]:
        """get_index_data

        :return: Optional[List[Dict]] List of index data. Returns None in case of exception
        """
        try:
            exchange_index_obj: Exchange = IndexService[self._index_name].value(logger=logger)
            data: List[Dict] = exchange_index_obj.get_all_data()
            return data
        except Exception as exp:
            logger.exception(exp)
            return None

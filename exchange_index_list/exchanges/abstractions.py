from typing import Dict, List, Optional
from abc import ABC, abstractmethod


class Exchange(ABC):
    """Exchange Abstract Base class
    """

    @abstractmethod
    def get_all_data(self) -> Optional[List[Dict]]:
        """get_all_data
        Get all data of the stocks listed in the index.

        :return: List of Dict of all stock's data listed in the index
        """
        ...

import abc
import csv
import random
from typing import List, Tuple


class Item(abc.ABC):

    CONDITIONS: List[Tuple[str,float]] = []
    ITEMS: List[Tuple[str,str,int,int,int]] = []

    @classmethod
    def load_conditions(cls) -> None:
        with open('./item_attributes', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                Item.CONDITIONS.append((row[0], float(row[1])))

    # TODO - finish this class






# TODO - implement the Armor class






# TODO - implement the Weapon class

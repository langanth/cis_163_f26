import datetime
import abc 
from typing import Optional

from item import *
from printer import Printer

class CharacterDeathException(Exception):
    def __init__(self, st, character) -> None:
        super().__init__(st)
        self.character = character

class MonsterDeathException(Exception):
    def __init__(self, st, monster) -> None:
        super().__init__(st)
        self.monster = monster

class Character(abc.ABC):
    # TODO: implement this class



# TODO: look over Priest class and be sure you understand it
class Priest(Character):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.last_healing = datetime.datetime.now() - datetime.timedelta(minutes=2)


    def take_damage(self, enemy) -> int:
        Printer.info(enemy.name + " senses the holiness of " + self.name + " and chooses not to attack!")
        return 0

    def heal(self, target) -> Optional[int]:
        if datetime.datetime.now() - self.last_healing < datetime.timedelta(minutes = 2):
            Printer.alert(self.name + " hasn't recovered from the last healing!")
            return None
        self.last_healing = datetime.datetime.now()
        amt = random.randint(0, 25)
        target.health += amt
        return amt


# TODO: implement Tank class






# TODO: implement DPT class






# TODO: implement Bard class





# TODO: implement Monster class


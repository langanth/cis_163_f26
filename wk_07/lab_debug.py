class InvalidInventoryError(Exception):
    pass


class InvalidMoneyError(Exception):
    pass


class VendingMachine:
    VALID_ROWS = {"A", "B", "C", "D", "E", "F"}
    VALID_COLS = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    VALID_DENOMINATIONS = {0.05, 0.10, 0.25, 0.50, 1.00, 2.00, 5.00}

    def __init__(self, inventory, money):
        self._inventory = inventory
        self._money = money
        self._credit = 0.0

    def insert_money(self, value):
        if value not in self.VALID_DENOMINATIONS:
            raise InvalidMoneyError("Invalid denomination")

        self._credit += value
        self._money[value] = self._money.get(value, 0) + 1

    def get_credit(self):
        return self._credit

    def dispense_change(self):
        change_needed = self._credit
        change_given = {}

        for denom in sorted(self.VALID_DENOMINATIONS):
            if self._money.get(denom, 0) == 0:
                break

            while change_needed >= denom and self._money.get(denom, 0) > 0:
                change_needed = round(change_needed - denom, 2)
                self._money[denom] -= 1
                change_given[denom] = change_given.get(denom, 0) + 1

        if change_needed != 0:
            raise InvalidMoneyError("Cannot provide exact change")

        self._credit = 0.0
        return change_given

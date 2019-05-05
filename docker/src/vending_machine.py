from enum import IntEnum
from dataclasses import dataclass


class InsufficientAmountError(Exception):
    pass

class BeverageNotFoundError(Exception):
    pass

class Coin(IntEnum):
    _10 = 10
    _100 = 100

@dataclass
class Beverage:
    name: str

@dataclass
class VendingMachine:    
    # フィールド
    amount: int = 0

    def insert(self, coin: Coin) -> None:
        if coin != Coin._100:
            raise ValueError

        self.amount += coin._100

    def push_button(self, beverage_name: str) -> Beverage:
        if self.amount < 100:
            raise InsufficientAmountError
        beverage = Beverage(name = beverage_name)
        return beverage

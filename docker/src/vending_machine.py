from enum import IntEnum
from dataclasses import dataclass
from dataclasses import field
from typing import List
from errors import InsufficientAmountError, BeverageNotFoundError

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
        if self.is_not_existing(beverage_name): 
            raise BeverageNotFoundError
        return Beverage(name = beverage_name)

    def is_not_existing(self, beverage_name: str) -> bool:
        if beverage_name == 'コーラ':
            return False
        if beverage_name == '烏龍茶':
            return False
        return True

from enum import IntEnum
from dataclasses import dataclass

class InsufficientAmountError(Exception):
    pass

class Coin(IntEnum):
    _10 = 10
    _100 = 100

@dataclass
class VendingMachine:    
    # フィールド
    amount: int = 0

    def insert(self, coin: Coin) -> None:
        if coin != Coin._100:
            raise ValueError

        self.amount += coin._100

    def push_button(self, beverage: str) -> str:
        if self.amount < 100:
            raise InsufficientAmountError

        return beverage

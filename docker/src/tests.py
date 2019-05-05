import pytest

from vending_machine import VendingMachine, Coin, Beverage
from errors import InsufficientAmountError, BeverageNotFoundError

class Test:

    vm: VendingMachine

    @pytest.fixture(scope='function', autouse=True)
    def scope_function(self):
        self.vm = VendingMachine()
        yield

    def test_dispense_cola_beverage(self):
        
        self.vm.insert(Coin._100)
        beverage = self.vm.push_button('コーラ')

        assert beverage.name == 'コーラ'

    def test_dispense_beverage(self):
        self.vm.insert(Coin._100)
        beverage = self.vm.push_button('烏龍茶')

        assert isinstance(beverage, Beverage)

    def test_dispense_oolong_tea_beverage(self):
        self.vm.insert(Coin._100)
        beverage = self.vm.push_button('烏龍茶')

        assert beverage.name == '烏龍茶'

    def test_dispense_beverage_not_found_zavas(self):
        self.vm.insert(Coin._100)
        with pytest.raises(BeverageNotFoundError):
            beverage = self.vm.push_button('zavas')

    def test_dispense_cola_without_insert_coin(self):
        with pytest.raises(InsufficientAmountError):
            assert 'コーラ' == self.vm.push_button('コーラ')

    def test_insert_100_yen(self):
        self.vm.insert(Coin._100)

    def test_insert_10_yen(self):
        with pytest.raises(ValueError):
            self.vm.insert(Coin._10)
    
    def test_is_existing_cola(self):
        assert not self.vm.is_not_existing('コーラ')
    
    def test_is_existing_oolong_tea(self):
        assert not self.vm.is_not_existing('烏龍茶')
    
    def test_is_not_existing_zavas(self):
        assert self.vm.is_not_existing('zavas')

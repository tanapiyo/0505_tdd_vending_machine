import pytest

from vending_machine import VendingMachine, Coin, Beverage, InsufficientAmountError

def test_dispense_cola_beverage():
    vm = VendingMachine()
    vm.insert(Coin._100)
    beverage = vm.push_button('コーラ')

    assert beverage.name == 'コーラ'

def test_dispense_beverage():
    vm = VendingMachine()
    vm.insert(Coin._100)
    beverage = vm.push_button('烏龍茶')

    assert isinstance(beverage, Beverage)

def test_dispense_oolong_tea_beverage():
    vm = VendingMachine()
    vm.insert(Coin._100)
    beverage = vm.push_button('烏龍茶')

    assert beverage.name == '烏龍茶'

def test_dispense_cola_without_insert_coin():
    vm = VendingMachine()
    with pytest.raises(InsufficientAmountError):
        assert 'コーラ' == vm.push_button('コーラ')

def test_insert_100_yen():
    vm = VendingMachine()
    vm.insert(Coin._100)

def test_insert_10_yen():
    vm = VendingMachine()
    with pytest.raises(ValueError):
        vm.insert(Coin._10)
 
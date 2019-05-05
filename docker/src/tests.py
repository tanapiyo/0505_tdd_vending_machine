import pytest

from vending_machine import VendingMachine, Coin, InsufficientAmountError

def test_dispense_cola():
    vm = VendingMachine()
    vm.insert(Coin._100)
    assert 'コーラ' == vm.push_button('コーラ')

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
 

#!/usr/bin/env python3
import pytest
from lib.cash_register import CashRegister
from decimal import Decimal

import io
import sys

def test_add_item():
    register = CashRegister()
    register.add_item("apple", Decimal('1.00'), 3)
    assert register.total == Decimal('3.00')
    assert register.items == ["apple", "apple", "apple"]

def test_apply_discount():
    register = CashRegister(20)
    register.add_item("banana", Decimal('1.00'), 5)
    assert register.apply_discount() == "After the discount, the total comes to $4.00."

    register_no_discount = CashRegister()
    register_no_discount.add_item("orange", Decimal('1.00'), 3)
    assert register_no_discount.apply_discount() == "There is no discount to apply."

def test_void_last_transaction():
    register = CashRegister()
    register.add_item("grape", Decimal('2.00'), 2)
    register.add_item("pear", Decimal('3.00'), 1)
    register.void_last_transaction()
    assert register.total == Decimal('4.00')
    assert register.items == ["grape", "grape"]

def test_multiple_transactions():
    register = CashRegister()
    register.add_item("kiwi", Decimal('1.50'), 2)
    register.add_item("mango", Decimal('2.00'), 3)
    assert register.total == Decimal('8.50')
    assert register.items == ["kiwi", "kiwi", "mango", "mango", "mango"]

    register.void_last_transaction()
    assert register.total == Decimal('3.00')
    assert register.items == ["kiwi", "kiwi"]

#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 2  # Set precision to 2 decimal places for financial calculations

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = Decimal('0.00')
        self.items = []
        self.last_transaction = {"title": None, "amount": Decimal('0.00'), "quantity": 0}

    def add_item(self, title, price, quantity=1):
        amount = Decimal(str(price)) * quantity
        self.last_transaction = {"title": title, "amount": amount, "quantity": quantity}
        self.total += amount
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (Decimal(self.discount) / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.last_transaction["title"]:
            self.total -= self.last_transaction["amount"]
            for _ in range(self.last_transaction["quantity"]):
                self.items.remove(self.last_transaction["title"])
            self.last_transaction = {"title": None, "amount": Decimal('0.00'), "quantity": 0}

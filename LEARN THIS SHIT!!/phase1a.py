#!/usr/bin/env python3

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity

    def restock(self, amount):
        self.quantity += amount


laptop = Product("MacBook", 100000, 5)

print("Initial total stock value:", laptop.get_total_value())

laptop.restock(3)

print("Total stock value after restock:", laptop.get_total_value())

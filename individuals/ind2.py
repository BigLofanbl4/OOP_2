#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 13
# Создать класс Goods (товар). В классе должны быть представлены поля: наи менование
# товара, дата оформления, цена товара, количество единиц товара, номер накладной, по
# которой товар поступил на склад. Реализовать методы изменения цены товара, изменения
# количества товара (увеличения и умень шения), вычисления стоимости товара.


from datetime import datetime


class Goods:
    def __init__(self, name, date, price, amount, invoice_number):
        self.name = str(name)
        self.date = self._validate_date(date)
        self.price = self._validate_price(price)
        self.amount = self._validate_amount(amount)
        self.invoice_number = str(invoice_number)

    def _validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Incorrect date")

    def _validate_price(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Price must be positive")
        return value

    def _validate_amount(self, value):
        value = int(value)
        if value < 0:
            raise ValueError("Amount must be positive")
        return value

    def read(self):
        self.name = input("Enter good's name: ")
        self.date = self._validate_date(input("Enter date (YYYY-MM-DD): "))
        self.price = self._validate_price(input("Enter price: "))
        self.amount = self._validate_amount(input("Enter amount: "))
        self.invoice_number = input("Enter invoice number: ")

    def display(self):
        print(f"Good's name: {self.name}")
        print(f"Date: {self.date}")
        print(f"Price: {self.price}")
        print(f"Amount: {self.amount}")
        print(f"Invoice number: {self.invoice_number}")

    def change_price(self, new_price):
        self.price = self._validate_price(new_price)

    def increase_amount(self, amount):
        self.amount += self._validate_amount(amount)

    def decrease_amount(self, amount):
        amount = self._validate_amount(amount)
        if self.amount >= amount:
            self.amount -= amount
        else:
            self.amount = 0

    def calc_total_cost(self):
        return self.amount * self.price


if __name__ == "__main__":
    item = Goods("Desktop", "2024-04-26", 50000.99, 10, "INV123")
    item.display()
    item.change_price(55000.0)
    item.display()

    total_cost = item.calc_total_cost()
    print(total_cost)

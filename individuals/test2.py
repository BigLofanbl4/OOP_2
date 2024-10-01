#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

from ind2 import Goods


class GoodsTest(unittest.TestCase):
    def test_valid_initialization(self):
        item = Goods("Desktop", "2024-10-01", 50000.99, 10, "INV123")
        self.assertEqual(item.name, "Desktop")
        self.assertEqual(item.date, datetime.strptime("2024-10-01", "%Y-%m-%d"))
        self.assertEqual(item.price, 50000.99)
        self.assertEqual(item.amount, 10)
        self.assertEqual(item.invoice_number, "INV123")

    def test_invalid_initialization(self):
        self.assertRaises(
            ValueError, Goods, "Name", "2024.10.1", 100, 10, "INV123"
        )
        self.assertRaises(
            ValueError, Goods, "Name", "2024-10-1", "bruh", 10, "INV123"
        )
        self.assertRaises(
            ValueError, Goods, "Name", "2024-10-1", -100, 10, "INV123"
        )
        self.assertRaises(
            ValueError, Goods, "Name", "2024-10-1", 100, "bruh", "INV123"
        )
        self.assertRaises(
            ValueError, Goods, "Name", "2024-10-1", -00, -10, "INV123"
        )

    def test_change_price(self):
        item = Goods("Desktop", "2024-10-01", 50000.99, 10, "INV123")
        item.change_price(10000.5)
        self.assertEqual(item.price, 10000.5)
        self.assertRaises(ValueError, item.change_price, -10)
        self.assertRaises(ValueError, item.change_price, "bruh")

    def test_increase_amount(self):
        item = Goods("Desktop", "2024-10-01", 50000.99, 10, "INV123")
        item.increase_amount(10)
        self.assertEqual(item.amount, 20)
        self.assertRaises(ValueError, item.increase_amount, -10)
        self.assertRaises(ValueError, item.increase_amount, "bruh")

    def test_decrease_amount(self):
        item = Goods("Desktop", "2024-10-01", 50000.99, 10, "INV123")
        item.decrease_amount(5)
        self.assertEqual(item.amount, 5)
        item.decrease_amount(10)
        self.assertEqual(item.amount, 0)
        self.assertRaises(ValueError, item.decrease_amount, -10)
        self.assertRaises(ValueError, item.decrease_amount, "bruh")

    def test_calc_total_cost(self):
        item = Goods("Desktop", "2024-10-01", 50000, 10, "INV123")
        self.assertEqual(item.calc_total_cost(), 50000 * 10)


if __name__ == "__main__":
    unittest.main()

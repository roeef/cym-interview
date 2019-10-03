from statistics import StatisticsError
from unittest import TestCase

from Inventory import Inventory


class TestInventory(TestCase):
    inv = Inventory('./testData/inventory.txt')

    def test_get_categories_for_stroe(self):
        # test multi Value search
        self.assertEqual(self.inv.get_categories_for_stroe(1), {10, 1, 2})
        # test non existing value
        self.assertEqual(self.inv.get_categories_for_stroe(9), set())
        # test single value result
        self.assertEqual(self.inv.get_categories_for_stroe(30), {2})

    def test_get_item_inventory(self):
        # single item
        self.assertEqual(self.inv.get_item_inventory('shirt'), [{'store': 1, 'category': 10, 'item_name': 'shirt', 'items': 10, 'price': 100}])
        # no items
        self.assertEqual(self.inv.get_item_inventory('blah'), [])
        # multiple items with same name
        self.assertEqual(self.inv.get_item_inventory('socks'), [{'store': 2, 'category': 10, 'item_name': 'socks', 'items': 100, 'price': 45}, {'store': 2, 'category': 10, 'item_name': 'socks', 'items': 100, 'price': 60}])


    def test_get_median_for_category(self):
        # even number of items median
        self.assertEqual(self.inv.get_median_for_category(10), 52.5)

        # uneven number of items median
        self.assertEqual(self.inv.get_median_for_category(2), 7)
        # single item median
        self.assertEqual(self.inv.get_median_for_category(120), 200)
        try:
            self.inv.get_median_for_category(33)
        except StatisticsError:
            print ("pass")
        else:
            self.fail("No Median For Empty Data");



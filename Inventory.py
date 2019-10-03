import json
from statistics import median


class Inventory(object):
    def __init__(self, file_source='inventory.txt'):
        with open(file_source, 'r') as f:
            self.inventory_dict = json.load(f)


    """
    Inventory Management system 
    """
    def get_categories_for_stroe(self, store):
        """
        Given a store id you should return all the categories ids in the inventory.
        :param store: store id
        :return: all the categories ids in the inventory
        """
        result_categories=set()
        for item in self.inventory_dict:
            if item['store'] == store:
                result_categories.add(item['category'])
        return result_categories

    def get_item_inventory(self, req_item):
        """
        Given items name return all the items across all stores.
        :param req_item: item name
        :return: all the items across all stores
        """
        result_items = []
        for current_item in self.inventory_dict:
            if current_item['item_name'] == req_item:
                result_items.append(current_item)
        return result_items

    def get_median_for_category(self, category):
        """
        Given category id return the median of the prices for all items in the category.
        :param category: category name
        :return: the median of the prices for all items in the category
        """
        prices = []
        for item in self.inventory_dict:
            if item['category'] == category:
                prices.append(item['price'])
        return median(prices)

from flask import Flask, jsonify

from Inventory import Inventory

app = Flask(__name__)
inv = Inventory()

@app.route('/')
def index():
  return 'Inventory Api Up and running'

@app.route('/get_categories_for_store/<int:store_id>')
def get_categories_for_store(store_id):
    print (store_id)
    return jsonify(list(inv.get_categories_for_stroe(store_id)))

#adding variables
@app.route('/get_item_inventory/<string:item>')
def get_item_inventory(item):
    return jsonify(inv.get_item_inventory(item))

@app.route('/get_median_for_category/<int:category>')
def show_post(category):
    return jsonify(inv.get_median_for_category(category))


if __name__ == '__main__':
    app.run()

from flask import Flask, request, jsonify
from sqlconnection import get_sql_connection
import json

import Product_Dao
import Orders_Dao
import Uom_Dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = Uom_Dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = Product_Dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    Product_id = Product_Dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'Product_id': Product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = Orders_Dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    Order_id = Orders_Dao.insert_order(connection, request_payload)
    response = jsonify({
        'Order_id': Order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = Product_Dao.delete_product(connection, request.form['Product_id'])
    response = jsonify({
        'Product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)    
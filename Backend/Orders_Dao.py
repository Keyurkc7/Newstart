from datetime import datetime
from sqlconnection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders "
             "(Customer_name, Total, datetime)"
             "VALUES (%s, %s, %s)")
    order_data = (order['Customer_name'], order['Total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO order_detail "
                           "(Order_id, Product_id, Quantity, Total_price)"
                           "VALUES (%s, %s, %s, %s)")

    order_details_data = []
    for order_detail_record in order['order_detail']:
        order_details_data.append([
            order_id,
            int(order_detail_record['Product_id']),
            float(order_detail_record['Quantity']),
            float(order_detail_record['Total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

def get_order_details(connection, Order_id):
    cursor = connection.cursor()

    query = "SELECT * from order_detail where order_id = %s"

    query = "SELECT order_detail.Order_id, order_detail.Quantity, order_detail.Total_price, products.Product_name, products.Price_per_unit FROM order_detail LEFT JOIN products on order_detail.Product_id = products.Product_id where order_detail.Order_id =1;"

    data = (Order_id, )

    cursor.execute(query, data)

    records = []
    for (Order_id, Quantity, Total_price, Product_name, Price_per_unit) in cursor:
        records.append({
            'Order_id': Order_id,
            'Quantity': Quantity,
            'Total_price': Total_price,
            'Product_name': Product_name,
            'Price_per_unit': Price_per_unit
        })

    cursor.close()

    return records

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (Order_id, Customer_name, Total, datetime) in cursor:
        response.append({
            'Order_id': Order_id,
            'Customer_name': Customer_name,
            'Total': Total,
            'datetime': datetime,
        })

    cursor.close()

    # append order details in each order
    for record in response:
        record['order_detail'] = get_order_details(connection, record['Order_id'])

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
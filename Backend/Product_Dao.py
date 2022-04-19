from multiprocessing import connection

from sqlconnection import get_sql_connection
def get_all_products(connection):

    

    cursor = connection.cursor()
    query = ("SELECT products.Product_id, products.Product_name, products.UOM_id, products.Price_per_unit, uom.Uom_name FROM products inner join uom on products.UOM_id=uom.Uom_id;")
    cursor.execute(query)

    response=[]

    for (Product_id, Product_name, UOM_id, Price_per_unit, uom_name) in cursor:
         response.append(
             {
                 'Product_id': Product_id,
                 'Product_name': Product_name,
                 'UOM_id': UOM_id,
                 'Price_per_unit': Price_per_unit,
                 'uom_name': uom_name



             }
         )


    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products (Product_name, UOM_id, Price_per_unit) values ('%s','%s','%s');")
    data = (product['Product_name'], product['UOM_id'], product['Price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, Product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where Product_id=" + str(Product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    

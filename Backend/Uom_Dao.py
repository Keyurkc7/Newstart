def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    response = []
    for (Uom_id, Uom_name) in cursor:
        response.append({
            'Uom_id': Uom_id,
            'Uom_name': Uom_name
        })
    return response


if __name__ == '__main__':
    from sqlconnection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))
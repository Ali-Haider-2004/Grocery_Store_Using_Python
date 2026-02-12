from datetime import datetime
from sql_connection import get_sql_connection
         
def insert_order(connection, order):
    cursor = connection.cursor()

        # Insert Orders function:
    order_query = ("INSERT INTO orders "
                   "(name, total, date_time)"
                   "VALUES (%s, %s, %s)")
                   
    order_data = (order['name'], order['total'], datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

# def insert_details(connection, order_details):
#     cursor = connection.cursor()

    order_details_query = ("INSERT INTO order_details "
                   "(order_id, product_id, quantity, total_price)"
                   "VALUES (%s, %s, %s, %s)")
    
    # order_details_data = (order_details['order_id'], order_details['product_id'], order_details['quantity'], order_details['total_price'])
    # cursor.execute(order_details_query, order_details_data)
    # order_id = cursor.lastrowid

        # Insert Orders details function:
    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()
    return order_id

        # Get all Orders function
def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []
    for (order_id, name, total, date_time) in cursor:
        response.append({
            'order_id': order_id,
            'name': name,
            'total': total,
            'date_time': date_time
        })
    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    print(insert_order(connection, {
        'name': 'null order',
        'total': '60',
        'order_details': [
            {
                'product_id': 5,
                'quantity': 3,
                'total_price': 270
            }
        ]
    }))

    # print(insert_details(connection, {
    #     'order_id': 2,
    #     'product_id': 1,
    #     'quantity': 1,
    #     'total_price': 120
    # }))

import pymysql

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()

def main():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="airbnb",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        # 1. 새로운 제품 추가: Python 스크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요. 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
        def insert_product():
            sql = 'INSERT INTO Products VALUES(NULL, %s, %s, %s, %s)'
            args = ('New Product1', 77.00, 48, '2024-02-05 15:00:18')
            result = execute_query(connection, sql, args)
            print("INSERT 성공")
        # insert_product()

        # 2. 고객 목록 조회: 'Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
        def select_customers():
            sql = 'SELECT * FROM Customers'
            result = execute_query(connection, sql)
            for row in result:
                print(row)
        # select_customers()

        # 3. 제품 재고 업데이트: 제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
        def update_product_quantity(productID, quantity_sold):
            sql = 'UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s'
            execute_query(connection, sql, (quantity_sold, productID))
            print('UPDATE 성공')
        # update_product_quantity(1, 11)
        
        # 4. 고객별 총 주문 금액 계산: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
        def sum_order_amouts():
            sql = 'SELECT customerID, SUM(totalAmount) AS total FROM Orders GROUP BY customerID'
            result = execute_query(connection, sql)
            for row in result:
                print(row['customerID'], row['total'])
            print('SELECT 성공')
        # sum_order_amouts()
        
        # 5. 고객 이메일 업데이트: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
        def update_customer_email(update_email, customer_id):
            sql = 'UPDATE Customers SET email = %s WHERE customerID = %s'
            execute_query(connection, sql, (update_email, customer_id))
            print('UPDATE 성공')
        # update_customer_email('update@email.com', 3)
        
        # 6. 주문 취소: 주문을 취소하는 Python 스크립트를 작성하세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
        def cancel_order(order_id):
            sql = 'DELETE FROM Orders WHERE orderID = %s'
            execute_query(connection, sql, (order_id))
            print('DELETE 성공')
        # cancel_order(3)

        # 7. 특정 제품 검색: 제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.
        def select_specific_product(product_name):
            sql = 'SELECT * FROM Products WHERE productName = %s'
            result = execute_query(connection, sql, (product_name))
            print(result)
        # select_specific_product('Ok Change')

        # 8. 특정 고객의 모든 주문 조회: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
        def select_customer_orders(customer_id):
            sql = 'SELECT * FROM Orders WHERE customerID = %s'
            result = execute_query(connection, sql, (customer_id))
            for row in result:
                print(row)
        # select_customer_orders(2)

        # 9. 가장 많이 주문한 고객 찾기: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
        def select_orderKing():
            sql = 'SELECT customerID, COUNT(*) as count FROM Orders GROUP BY customerID ORDER BY count DESC LIMIT 1'
            result = execute_query(connection, sql)
            print(result)
        select_orderKing()
    finally:
        connection.close()
main()
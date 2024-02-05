import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="classicmodels",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

try:
    # cursor 생성
    with connection.cursor() as cursor:
        # SQL 쿼리 실행
        sql = "SELECT * FROM customers"
        cursor.execute(sql)

        # 결과 가져오기
        result = cursor.fetchall()
        for row in result:
            print(row)
finally:
    connection.close()

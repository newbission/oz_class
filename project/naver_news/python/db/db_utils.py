import pymysql


def get_connection():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="naver",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            print("execute success")


def commit_querys(connection):
    try:
        connection.commit()
    except:
        print("commit fail")

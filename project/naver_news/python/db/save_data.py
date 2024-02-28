# 스크랩 데이터 가져오기
import db.db_utils as db_utils

def save_data(scrap_data):
    try:
        connection = db_utils.get_connection()
        sql = "INSERT INTO naver_opinions (title, press, journalist, upload_time, update_time, naver_url, original_url, summary, header, thumbnail_url, thumbnail_file_name, category) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for opinions_by_category in scrap_data:
            for opinion in opinions_by_category:
                args = (
                    opinion["title"],
                    opinion["press"],
                    opinion["journalist"],
                    opinion["upload_time"],
                    opinion["update_time"],
                    opinion["naver_url"],
                    opinion["original_url"],
                    opinion["summary"],
                    opinion["header"],
                    opinion["thumbnail_url"],
                    opinion["thumbnail_file_name"],
                    opinion["category"]
                )
                db_utils.execute_query(connection, sql, args)
            db_utils.commit_querys(connection)
    finally:
        db_utils.close_connection(connection)

import mysql.connector


class MySqlDbContext:

    def __init__(self) -> None:
        self.connection = self.init_db_connection()

    def init_db_connection(self):
        return mysql.connector.connect(
            host="",
            user="",
            password="",
            port="",
            database=""
        )

    def select(self, query: str):
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        return mycursor.fetchall()

    def fire_query(self, query: str):
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        mycursor.commit()
        return {
            "rows effected": mycursor.rowcount
        }

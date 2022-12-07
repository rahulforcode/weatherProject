import mysql.connector

class DBCon:
    __db = ''
    def __init__(self) -> None:
        self.__connect("<host>","<user>","<password>","<dbname>")

    def __connect(self, host, user, password, database):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def __getCursor(self):
        return self.__db.cursor()
        
    def insert(self, sql, values=None):
        cursor = self.__getCursor()
        if values == None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, values)
        self.__db.commit()
        cursor.close()
        return True   

    def execute(self, sql, values=None):
        cursor = self.__getCursor()
        if values == None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, values)
        data = cursor.fetchall()
        cursor.close()
        return data  
          
    def close(self):
        self.__db.close()

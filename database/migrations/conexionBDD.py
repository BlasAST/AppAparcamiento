import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        connection = mysql.connector.connect(
            host='mysql_aparcamiento',
            user='root',
            password='blas1234',
            database='db_aparcamiento'

        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado a MySQL Server versión ", db_Info)
            my = connection.cursor()
            return my,connection
    except Error as e:
        print("Error al conectar a MySQL", e)
        return e

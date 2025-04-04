import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='blas',
            password='blas',
            database='db_aparcamiento'

        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado a MySQL Server versión ", db_Info)
            return connection
    except Error as e:
        print("Error al conectar a MySQL", e)
        return None, None

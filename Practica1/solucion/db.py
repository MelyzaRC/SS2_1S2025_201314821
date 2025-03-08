# --------------------------------------------------------------------
# MELYZA ALEJANDRA RODRIGUEZ CONTRERAS 
# 201314821
# LABORATORIO DE SEMINARIO DE SISTEMAS 2
# PRACTICA 1
# --------------------------------------------------------------------


# IMPORTS
from constantes import COLORES, FIN_LINEA ,SERVER, DATABASE
import pyodbc

# CONECTAR_DB: CONECTA A LA BASE DE DATOS
def conectar_db():
    try:
        conn_str = f"DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
        conn = pyodbc.connect(conn_str,autocommit=True)
        return conn
    except pyodbc.Error as e:
        print(COLORES["rojo"] + "Error al conectar a la base de datos: " + str(e) + FIN_LINEA)
        return None
    
# CERRAR CONEXION DB: CIERRA LA CONEXION A LA BASE DE DATOS
def cerrar_conexion_db(conn):
    try:
        conn.close()
    except pyodbc.Error as e:
        print(COLORES["rojo"] + "Error al cerrar la conexión a la base de datos: " + str(e) + FIN_LINEA)
    
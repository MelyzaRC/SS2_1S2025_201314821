# --------------------------------------------------------------------
# MELYZA ALEJANDRA RODRIGUEZ CONTRERAS 
# 201314821
# LABORATORIO DE SEMINARIO DE SISTEMAS 2
# PRACTICA 1
# --------------------------------------------------------------------


COLORES = {
    "rojo": "\033[31m",
    "verde": "\033[32m",
    "azul": "\033[34m",
    "amarillo": "\033[33m"
}
FIN_LINEA = "\033[0m"
SERVER = ".\SQLEXPRESS"
DATABASE = "FlightDataWarehouse"
CONN_STR = f"DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"
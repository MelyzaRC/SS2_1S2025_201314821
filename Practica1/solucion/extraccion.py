import pandas as pd
from constantes import COLORES, FIN_LINEA

def extraer():
    path = input("INGRESE EL PATH DEL ARCHIVO CSV o presione ENTER [data.csv]: ")
    if(path == ""):
        path = "data.csv"
    try:
        df = pd.read_csv(path)
        print("\n" + COLORES["verde"] + str(len(df)) +  " DATOS EXTRAÍDOS CON ÉXITO\n\n" + FIN_LINEA)
        print(df)
        print("\n") 
        return df
    except Exception as e:
        print(f"ERROR AL EXTRAER INFORMACIÓN DEL ARCHIVO: {e}")
        return None
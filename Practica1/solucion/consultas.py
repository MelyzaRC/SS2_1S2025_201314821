# --------------------------------------------------------------------
# MELYZA ALEJANDRA RODRIGUEZ CONTRERAS 
# 201314821
# LABORATORIO DE SEMINARIO DE SISTEMAS 2
# PRACTICA 1
# --------------------------------------------------------------------


# IMPORTS
from constantes import COLORES, FIN_LINEA, DATABASE
import os
import pyodbc
from db import conectar_db, cerrar_conexion_db

def borrarModeloDB():
    print("Modelo de base de datos borrado exitosamente \n")
   
def crearModeloDB():
    print("Modelo de base de datos creado exitosamente \n")

def consulta_cantidad_datos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM (
        SELECT 'DimPilot' AS TABLA ,COUNT(*) AS CANTIDAD_DATOS FROM dbo.DimPilot
        UNION 
        SELECT 'DimFlightArrival' AS TABLA ,COUNT(*) AS CANTIDAD_DATOS FROM dbo.DimFlightArrival
        UNION 
        SELECT 'DimDepartureTime' AS TABLA ,COUNT(*) AS CANTIDAD_DATOS FROM dbo.DimDepartureTime
        UNION 
        SELECT 'DimFlightDeparture' AS TABLA ,COUNT(*) AS CANTIDAD_DATOS FROM dbo.DimFlightDeparture
        UNION 
        SELECT 'DimPassenger' AS TABLA ,COUNT(*) AS CANTIDAD_DATOS FROM dbo.DimPassenger
        UNION 
        SELECT 'FactFlight' AS TABLA ,COUNT(*) AS CANTIDAD_DATOS FROM dbo.FactFlight
    ) x
    ORDER BY x.TABLA ASC 
    ;
    """)
    rows = cursor.fetchall()
    print("\n-----------------------------------")
    for row in rows:
        print(COLORES["azul"] ,"TABLA:    " , FIN_LINEA, row.TABLA)
        print(COLORES["azul"] , "REGISTROS:" , FIN_LINEA, row.CANTIDAD_DATOS)
        print("-----------------------------------")
    print("\n")
    cerrar_conexion_db(conn)

def consulta1(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
        gender AS GENERO, 
        COUNT(*) AS TOTAL, 
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM dbo.DimPassenger) AS PORCENTAJE
        FROM dbo.DimPassenger 
        GROUP BY gender;
    """)
    rows = cursor.fetchall()
    print("\n-----------------------------------")
    for row in rows: 
        print(COLORES["azul"] ,"GÉNERO:            " , FIN_LINEA, row.GENERO)
        print(COLORES["azul"] ,"TOTAL DE PASAJEROS:" , FIN_LINEA, row.TOTAL)
        print(COLORES["azul"] ,"PORCENTAJE:        " , FIN_LINEA, round(row.PORCENTAJE,2), "%")
        print("-----------------------------------")
    print("\n")
    cerrar_conexion_db(conn)

def consulta2(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT x.year, x.month, x.nationality  FROM (SELECT b.nationality, c.month, c.year, ROW_NUMBER() OVER (PARTITION BY b.nationality ORDER BY c.year DESC, c.month DESC) AS rn
        FROM dbo.FactFlight a, dbo.DimPassenger b, dbo.DimDepartureTime c
        WHERE a.passenger = b.id_dim_passenger
        AND a.departure_time = c.id_dim_departure_time) x 
        where x.rn = 1
        ;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nAÑO      MES     NACIONALIDAD" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.year, "\t", row.month, "\t", row.nationality)
    print("\n")
    cerrar_conexion_db(conn)

def consulta3(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.country_name AS PAIS, b.airport_country_code AS CODIGO_PAIS,  count(*) AS TOTAL 
        FROM dbo.FactFlight a, dbo.DimFlightDeparture b 
        WHERE a.flight_departure = b.id_dim_flight_departure 
        GROUP BY b.country_name, b.airport_country_code
        ORDER BY b.country_name ASC 
        ;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nCOD.PAIS         VUELOS          PAIS" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.CODIGO_PAIS, "\t\t", row.TOTAL, "\t\t", row.PAIS)
    print("\n")
    cerrar_conexion_db(conn)

def consulta4(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT TOP 5
            a.airport_name AS AEROPUERTO, a.country_name AS PAIS, a.airport_country_code AS CODIGO_PAIS, count(*) AS TOTAL_VUELOS
        FROM 
            dbo.FactFlight b, 
            dbo.DimFlightDeparture a 
        WHERE a.id_dim_flight_departure = b.flight_departure 
        group by a.airport_name, a.country_name,  a.airport_country_code 
        ORDER BY TOTAL_VUELOS DESC 
        ;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nVUELOS\t PAIS\t CODIGO\t\t\t\tVUELOS" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.TOTAL_VUELOS, "\t", row.CODIGO_PAIS, "\t", row.AEROPUERTO, "\t\t", row.PAIS, "\t\t")
    print("\n")
    cerrar_conexion_db(conn)

def consulta5(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.status AS STATUS, count(*) AS VUELOS FROM dbo.FactFlight a
        GROUP BY a.status
        ORDER BY VUELOS ASC;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nSTATUS\t\tTOTAL_VUELOS" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.STATUS, "\t", row.VUELOS)
    print("\n")
    cerrar_conexion_db(conn)

def consulta6(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT TOP 5
        b.airport_name AS DESTINO, count(*) AS VISITAS
        FROM dbo.FactFlight a , dbo.DimFlightArrival b 
        WHERE a.flight_arrival = b.id_dim_flight_arrival 
        group by b.airport_name
        ORDER BY VISITAS DESC;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nVISITAS\t DESTINO" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.VISITAS, "\t", row.DESTINO)
    print("\n")
    cerrar_conexion_db(conn)

def consulta7(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT TOP 5 b.continents AS CONTINENTE, count(*) AS VISITAS
        FROM dbo.FactFlight a, dbo.DimFlightDeparture b 
        where a.flight_departure = b.id_dim_flight_departure
        GROUP by b.continents
        ORDER BY VISITAS DESC 
        ;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nVISITAS\t CONTINENTE" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.VISITAS, "\t", row.CONTINENTE)
    print("\n")
    cerrar_conexion_db(conn)

def consulta8(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        WITH Ranking AS (
            SELECT 
                b.gender AS GENERO, 
                b.age AS EDAD, 
                COUNT(*) AS VIAJES,
                ROW_NUMBER() OVER (PARTITION BY b.gender ORDER BY COUNT(*) DESC) AS rn
            FROM dbo.FactFlight a
            JOIN dbo.DimPassenger b ON a.passenger = b.id_dim_passenger
            GROUP BY b.gender, b.age
        )
        SELECT GENERO, EDAD, VIAJES
        FROM Ranking
        WHERE rn <= 5
        ORDER BY GENERO ASC, VIAJES DESC;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nGENERO\t EDAD\t VIAJES" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.GENERO, "\t", row.EDAD, "\t", row.VIAJES)
    print("\n")
    cerrar_conexion_db(conn)

def consulta9(): 
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            b.month as MES, 
            b.year AS ANIO, 
            COUNT(*) AS TOTAL_VUELOS
        FROM dbo.FactFlight a, dbo.DimDepartureTime b
        WHERE a.departure_time = b.id_dim_departure_time
        GROUP BY b.year, b.month
        ORDER BY b.year DESC, b.month ASC;
    """)
    rows = cursor.fetchall()
    print(COLORES["verde"] ,"\nMES\t ANIO\t VUELOS" , FIN_LINEA)
    print(COLORES["verde"] + "------------------------------------------------------------------"        + FIN_LINEA)
    for row in rows: 
        print(row.MES, "\t", row.ANIO, "\t", row.TOTAL_VUELOS)
    print("\n")
    cerrar_conexion_db(conn)

def borrar_modelo(): 
    conn = conectar_db()
    cursor = conn.cursor()
    with open("script_borrar.sql", "r", encoding="utf-8") as file:
        sql_script = file.read()

    for statement in sql_script.split(";"):
        if statement.strip(): 
            cursor.execute(statement)
            conn.commit() 
    
    cursor.close()
    cerrar_conexion_db(conn)

def crear_modelo(): 
    conn = conectar_db()
    cursor = conn.cursor()
    with open("script_db.sql", "r", encoding="utf-8") as file:
        sql_script = file.read()

    for statement in sql_script.split(";"):
        if statement.strip(): 
            cursor.execute(statement)
            conn.commit() 
    
    cursor.close()
    cerrar_conexion_db(conn)

def verificar_modelo():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'FactFlight'")
    rows = cursor.fetchall()
    if len(rows) > 0:
        cerrar_conexion_db(conn)
        return True
    else:
        cerrar_conexion_db(conn)
        return False
    



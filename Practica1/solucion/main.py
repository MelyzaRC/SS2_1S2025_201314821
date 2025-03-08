

# --------------------------------------------------------------------
# MELYZA ALEJANDRA RODRIGUEZ CONTRERAS 
# 201314821
# LABORATORIO DE SEMINARIO DE SISTEMAS 2
# PRACTICA 1
# --------------------------------------------------------------------


# IMPORTS
from constantes import COLORES, FIN_LINEA   # type: ignore
import os                                   # type: ignore
import consultas                            # type: ignore
import extraccion                           # type: ignore
import transformacion                       # type: ignore  
import carga                                # type: ignore

def extraer_informacion():
    global data
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA) 
    print(COLORES["amarillo"] + "EXTRAER INFORMACIÓN DE LOS ARCHIVOS FUENTES"                               + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    data = extraccion.extraer()
    presione_enter()
    
def transformar_informacion():
    global data 
    global data_transformada
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA) 
    print(COLORES["amarillo"] + "TRANSFORMAR INFORMACIÓN"                                                   + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    data_transformada= transformacion.transformar(data)
    presione_enter()

def cargar_informacion():
    global data_transformada
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA) 
    print(COLORES["amarillo"] + "CARGAR INFORMACIÓN"                                                        + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    carga.cargar(data_transformada)
    presione_enter()

# LIMPIAR_PANTALLA: BORRA TODO LO QUE ESTE EN PANTALLA
def limpiar_pantalla():
    os.system("cls")

def presione_enter():
    input(COLORES["azul"] + "Presione enter para continuar..." + FIN_LINEA)
    menu()

def presione_enter_consultas():
    input(COLORES["azul"] + "Presione enter para continuar..." + FIN_LINEA)
    sub_menu_consultas()

# SALIR: SALIR DE LA APLICACION
def salir():
    limpiar_pantalla()
    print(COLORES["verde"] + "\nSaliendo...\n\n" + FIN_LINEA) 
    exit()

# BORRAR MODELO: VACIA LA INFORMACION CONTENIDA EN LAS TABLAS DE LA BASE DE DATOS
def borrar_modelo():
    limpiar_pantalla()
    print(COLORES["verde"] + "Borrar modelo" + FIN_LINEA)
    consultas.borrarModeloDB()
    input("")
    menu()

# CREAR MODELO: CARGA LOS DATOS OBTENIDOS DESDE EL CSV 
def crerar_modelo():
    limpiar_pantalla()
    print(COLORES["verde"] + "Crear modelo" + FIN_LINEA)
    consultas.crearModeloDB()
    input("")
    menu()

# INFORMACION DE LAS TABLAS CARGADAS: MUESTRA UN COUNT DE CADA UNA DE LAS TABLAS CARGADAS
def informacion_tablas_cargadas():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA) 
    print(COLORES["amarillo"] + "INFORMACIÓN DE TABLAS CARGADAS"                                            + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta_cantidad_datos()
    presione_enter()
    menu()

# PORCENTAJE DE PASAJEROS POR GÉNERO: MUESTRA EL PORCENTAJE DE PASAJEROS POR GÉNERO
def consulta1():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 1 - PORCENTAJE DE PASAJEROS POR GÉNERO"                           + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta1()
    presione_enter_consultas()

# NACIONALIDADES CON SU AÑO DE MAYOR FECHA DE SALIDA: NACIONALIDADES TOMANDO EN CUENTA EL AÑO DE MAYOR FECHA DE SALIDA
def consulta2():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 2 - NACIONALIDADES CON SU AÑO DE MAYOR FECHA DE SALIDA"           + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    
    presione_enter_consultas()

# VUELOS POR PAIS: MUESTRA LOS VUELOS POR PAIS
def consulta3():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 3 - VUELOS POR PAIS"                                              + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta3()
    presione_enter_consultas()

# TOP 5 AEROPUERTOS CON MAYOR NÚMERO DE PASAJEROS: MUESTRA LOS TOP 5 AEROPUERTOS CON MAYOR NÚMERO DE PASAJEROS
def consulta4():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 4 - TOP 5 AEROPUERTOS CON MAYOR NÚMERO DE PASAJEROS"              + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta4()
    presione_enter_consultas()

# ESTADO DE VUELO: MUESTRA EL ESTADO DE VUELO
def consulta5():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 5 - ESTADO DE VUELOS"                                             + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta5()
    presione_enter_consultas()

# PAISES MAS VISITADOS: MUESTRA LOS PAISES MAS VISITADOS
def consulta6():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 6 - TOP 5 PAISES MÁS VISITADOS"                                   + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta6()
    presione_enter_consultas()

# CONTINENTES MAS VISITADOS: MUESTRA LOS CONTINENTES MAS VISITADOS
def consulta7():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 7 - TOP 5 CONTINENTES MÁS VISITADOS"                              + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta7()
    presione_enter_consultas()

# EDADES POR GÉNERO QUE MÁS VIAJAN: MUESTRA LAS EDADES POR GÉNERO QUE MÁS VIAJAN
def consulta8():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 8 - TOP 5 EDADES POR GÉNERO QUE MÁS VIAJAN"                       + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta8()
    presione_enter_consultas()

# VUELOS POR FECHA: MUESTRA LOS VUELOS POR FECHA
def consulta9():
    limpiar_pantalla()
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    print(COLORES["amarillo"] + "CONSULTA 9 - VUELOS POR FECHA"                                             + FIN_LINEA)
    print(COLORES["amarillo"] + "------------------------------------------------------------------"        + FIN_LINEA)
    consultas.consulta9()
    presione_enter_consultas()

# SUB MENU CONSULTAS: CONSULTAS REQUERIDAS EN EL ENUNCIADO
def sub_menu_consultas():
    limpiar_pantalla()
    opcion = 0
    print(COLORES["azul"] + "------------------------------------------------------------------"      + FIN_LINEA)
    print(COLORES["azul"] + "CONSULTAS:"                                                              + FIN_LINEA)
    print(COLORES["azul"] + " 1.  PORCENTAJE DE PASAJEROS POR GÉNERO"                                 + FIN_LINEA)
    print(COLORES["azul"] + " 2.  NACIONALIDADES CON SU AÑO DE MAYOR FECHA DE SALIDA"                 + FIN_LINEA) 
    print(COLORES["azul"] + " 3.  VUELOS POR PAÍS"                                                    + FIN_LINEA)
    print(COLORES["azul"] + " 4.  TOP 5 AEROPUERTOS CON MAYOR NÚMERO DE PASAJEROS"                    + FIN_LINEA)
    print(COLORES["azul"] + " 5.  ESTADO DE VUELO"                                                    + FIN_LINEA)
    print(COLORES["azul"] + " 6.  TOP 5 PAÍSES MÁS VISITADOS"                                         + FIN_LINEA)
    print(COLORES["azul"] + " 7.  TOP 5 CONTINENTES MÁS VISITADOS"                                    + FIN_LINEA)
    print(COLORES["azul"] + " 8.  TOP 5 EDADES POR GÉNERO QUE MÁS VIAJAN"                             + FIN_LINEA)
    print(COLORES["azul"] + " 9.  VUELOS POR FECHA"                                                   + FIN_LINEA)   
    print(COLORES["azul"] + " 0.  REGRESAR"                                                           + FIN_LINEA)
    print(COLORES["azul"] + "------------------------------------------------------------------"      + FIN_LINEA) 
    try:
        opcion = int(input(COLORES["azul"] + "\nSeleccione una opcion: "                              + FIN_LINEA))
        if opcion < 0 or opcion > 9:
            print(COLORES["rojo"] + "Opción inválida [PRESIONE ENTER PARA CONTINUAR]"                 + FIN_LINEA)
            input("")
            sub_menu_consultas()
        else:
            switch = {
                1: consulta1                    ,       
                2: consulta2                    ,
                3: consulta3                    ,
                4: consulta4                    ,
                5: consulta5                    ,
                6: consulta6                    ,
                7: consulta7                    ,
                8: consulta8                    ,
                9: consulta9                    ,   
                0: menu        
            }
            switch.get(opcion, lambda: "")()
    except ValueError:
        print(COLORES["rojo"] + "Debe ingresar un número válido[PRESIONE ENTER PARA CONTINUAR]"             + FIN_LINEA)
        input("")
        sub_menu_consultas()
    return ""

# MENU: LISTADO DE OPCIONES DISPONIBLES
def menu():
    limpiar_pantalla()
    opcion = 0
    print(COLORES["azul"] + "------------------------------------------------------------------"      + FIN_LINEA) 
    print(COLORES["azul"] + "OPCIONES:"                                                               + FIN_LINEA) 
    print(COLORES["azul"] + " 1.  BORRAR MODELO"                                                      + FIN_LINEA)
    print(COLORES["azul"] + " 2.  CREAR MODELO"                                                       + FIN_LINEA)
    print(COLORES["azul"] + " 3.  EXTRAER INFORMACIÓN DE LOS ARCHIVOS FUENTES"                        + FIN_LINEA)
    print(COLORES["azul"] + " 4.  TRANSFORMAR INFORMACIÓN"                                            + FIN_LINEA)
    print(COLORES["azul"] + " 5.  CARGAR INFORMACION"                                                 + FIN_LINEA)
    print(COLORES["azul"] + " 6.  CANTIDAD DE DATOS POR TABLA"                                        + FIN_LINEA)
    print(COLORES["azul"] + " 7.  CONSULTAS"                                                          + FIN_LINEA)
    print(COLORES["azul"] + " 0.  SALIR"                                                              + FIN_LINEA)
    print(COLORES["azul"] + "------------------------------------------------------------------"      + FIN_LINEA) 
    try:
        opcion = int(input(COLORES["azul"] + "\nSeleccione una opcion: "                              + FIN_LINEA))
        if opcion < 0 or opcion > 7:
            print(COLORES["rojo"] + "Opción inválida [PRESIONE ENTER PARA CONTINUAR]"                 + FIN_LINEA)
            input("")
            menu()
        else:
            switch = {
                1: borrar_modelo                    ,
                2: crerar_modelo                    ,   
                3: extraer_informacion              ,
                4: transformar_informacion          ,
                5: cargar_informacion               ,
                6: informacion_tablas_cargadas      , 
                7: sub_menu_consultas               , 
                0: salir        
            }
            switch.get(opcion, lambda: "")()
    except ValueError:
        print(COLORES["rojo"] + "Debe ingresar un número válido[PRESIONE ENTER PARA CONTINUAR]"             + FIN_LINEA)
        input("")
        menu()
    return ""
    

if __name__ == "__main__":
    print(menu())
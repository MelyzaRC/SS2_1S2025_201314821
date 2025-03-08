from tqdm import tqdm
from constantes import COLORES, FIN_LINEA   # type: ignore
import db as database                       # type: ignore


def cargar(data):
    dim_pilot               = data[0]
    dim_departure_time      = data[1]
    dim_flight_arrival      = data[2]
    dim_flight_departure    = data[3]
    dim_passenger           = data[4]
    fact_flight             = data[5]
    errores = 0

    try: 
        conn = database.conectar_db()
        cursor = conn.cursor()
        # ----------------------------------------------------------------------
        # PILOTO  
        # ----------------------------------------------------------------------
        errores = 0
        for _, row in tqdm(dim_pilot.iterrows(), total=len(dim_pilot), desc=COLORES["verde"] + "CARGANDO DIM_PILOTOS:         " + FIN_LINEA):
            try:
                cursor.execute("""
                IF NOT EXISTS (SELECT 1 FROM DimPilot WHERE id_dim_pilot = ?)
                BEGIN
                    INSERT INTO DimPilot (id_dim_pilot, pilot_name)
                    VALUES (?, ?)
                END
            """, row['id_dim_pilot'], row['id_dim_pilot'], row['Pilot Name'])
            except Exception as e:
                errores += 1
                continue 
        print("PILOTOS           [" + COLORES["azul"] + "OK" + FIN_LINEA + "]")
        print("ERRORES         " , COLORES["rojo"] , errores , FIN_LINEA , "\n")
        


        # ----------------------------------------------------------------------
        # DEPARTURE TIME
        # ----------------------------------------------------------------------
        errores = 0
        for _, row in tqdm(dim_departure_time.iterrows(), total=len(dim_departure_time), desc=COLORES["verde"] + "CARGANDO DIM_DEPARTURE_TIME:  " + FIN_LINEA):
            try:
                cursor.execute("""
                    IF NOT EXISTS (SELECT 1 FROM DimDepartureTime WHERE id_dim_departure_time = ?)
                    BEGIN
                        INSERT INTO DimDepartureTime (id_dim_departure_time, [date], [year], [month], [day])
                        VALUES (?, ?, ?, ?, ?)
                    END
                """, row['id_dim_departure_time'], row['id_dim_departure_time'], row['Departure Date'], row['year'], row['month'], row['day'])
            except Exception as e:
                errores += 1
                continue 
        print("DEPARTURE TIME    [" + COLORES["azul"] + "OK" + FIN_LINEA + "]")
        print("ERRORES         " , COLORES["rojo"] , errores , FIN_LINEA , "\n")

        # ----------------------------------------------------------------------
        # FLIGHT ARRIVAL
        # ----------------------------------------------------------------------
        errores = 0
        for _, row in tqdm(dim_flight_arrival.iterrows(), total=len(dim_flight_arrival), desc=COLORES["verde"] + "CARGANDO DIM_FLIGHT_ARRIVAL:  " + FIN_LINEA):
            try:
                cursor.execute("""
                    IF NOT EXISTS (SELECT 1 FROM DimFlightArrival WHERE id_dim_flight_arrival = ?)
                    BEGIN
                        INSERT INTO DimFlightArrival (id_dim_flight_arrival, [airport_name])
                        VALUES (?, ?)
                    END
                """, row['id_dim_flight_arrival'], row['id_dim_flight_arrival'], row['Arrival Airport'])
            except Exception as e:
                errores += 1
                continue 
        print("FLIGHT ARRIVAL    [" + COLORES["azul"] + "OK" + FIN_LINEA + "]")
        print("ERRORES         " , COLORES["rojo"] , errores , FIN_LINEA , "\n")
        
        # ----------------------------------------------------------------------
        # FLIGHT DEPARTURE
        # ----------------------------------------------------------------------
        errores = 0
        for _, row in tqdm(dim_flight_departure.iterrows(), total=len(dim_flight_departure), desc=COLORES["verde"] + "CARGANDO DIM_FLIGHT_DEPARTURE:" + FIN_LINEA):
            try:
                cursor.execute("""
                    IF NOT EXISTS (SELECT 1 FROM DimFlightDeparture WHERE id_dim_flight_departure = ?)
                    BEGIN
                        INSERT INTO DimFlightDeparture (id_dim_flight_departure, [airport_name], [airport_country_code], [country_name], [airport_continent], [continents])
                        VALUES (?, ?, ?, ?, ?, ?)
                    END
                """, row['id_dim_flight_departure'], row['id_dim_flight_departure'], row['Airport Name'], row['Airport Country Code'], row['Country Name'], row['Airport Continent'], row['Continents'])
            except Exception as e:
                errores += 1
                continue 
        print("FLIGHT DEPARTURE  [" + COLORES["azul"] + "OK" + FIN_LINEA + "]")
        print("ERRORES         " , COLORES["rojo"] , errores , FIN_LINEA , "\n")
       
        # ----------------------------------------------------------------------
        # PASSENGER
        # ---------------------------------------------------------------------- 
        errores = 0                      
        for _, row in tqdm(dim_passenger.iterrows(), total=len(dim_passenger), desc=COLORES["verde"] + "CARGANDO DIM_PASSENGER:       " + FIN_LINEA):
            try:
                cursor.execute("""
                    IF NOT EXISTS (SELECT 1 FROM DimPassenger WHERE id_dim_passenger = ?)
                    BEGIN
                        INSERT INTO DimPassenger (id_dim_passenger, [passenger_id], [first_name], [last_name], [gender], [age], [nationality])
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    END
                """, row['id_dim_passenger'], row['id_dim_passenger'], row['Passenger ID'], row['First Name'], row['Last Name'], row['Gender'], row['Age'], row['Nationality'])
            
            except Exception as e:
                errores += 1
                continue  
        print("PASSENGER         [" + COLORES["azul"] + "OK" + FIN_LINEA + "]")
        print("ERRORES         " , COLORES["rojo"] , errores , FIN_LINEA , "\n")

        # ----------------------------------------------------------------------
        # FLIGHTS
        # ----------------------------------------------------------------------
        errores = 0
        for _, row in tqdm(fact_flight.iterrows(), total=len(fact_flight), desc=COLORES["verde"] + "CARGANDO FACT FLIGHTS:        " + FIN_LINEA):
            try:
                cursor.execute("""
                    INSERT INTO FactFlight ([passenger], [departure_time], [flight_departure], [flight_arrival], [pilot], [status])
                        VALUES (?, ?, ?, ?, ?,?)
                """, row['passenger'], row['departure_time'], row['flight_departure'], row['flight_arrival'], row['pilot'], row['status'])
            
            except Exception as e:
                errores  += 1
                print("Error al insertar datos en la fila:")
                print(row)
                print(f"Error: {e}")
                input("Presione ENTER para continuar")
                continue  
        print("FLIGHTS         [" + COLORES["azul"] + "OK" + FIN_LINEA + "]")
        print("ERRORES         " , COLORES["rojo"] , errores , FIN_LINEA , "\n")

    except Exception as e:
        print("Error al insertar datos en la fila:")
        print(row)
        print(f"Error: {e}")
    
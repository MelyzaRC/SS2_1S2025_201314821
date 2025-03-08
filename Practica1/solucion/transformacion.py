import pandas as pd 
from constantes import COLORES, FIN_LINEA

def parse_dates(date_str):
        for fmt in ('%m/%d/%Y', '%m-%d-%Y'):
            try:
                return pd.to_datetime(date_str, format=fmt)
            except ValueError:
                continue
        return pd.NaT 

def transformar(df): 
    df['Arrival Airport'] = df['Arrival Airport'].replace(["0", "-"], "No especificado")
    # ----------------------------------------------------------------------
    # PILOTO  
    # ----------------------------------------------------------------------
    dim_pilot = df[['Pilot Name']].drop_duplicates().copy()
    dim_pilot['id_dim_pilot'] = range(1, len(dim_pilot) + 1)
    print(COLORES["verde"] +"")
    print("dim_pilot: ", len(dim_pilot) , " registros",FIN_LINEA)
    print(dim_pilot.head())
    
    # ----------------------------------------------------------------------
    # ARRIVAL AIRPORT
    # ----------------------------------------------------------------------
    dim_flight_arrival = df[['Arrival Airport']].drop_duplicates().copy()
    dim_flight_arrival['id_dim_flight_arrival'] = range(1, len(dim_flight_arrival) + 1)
    print(COLORES["verde"] +"")
    print("dim_flight_arrival: ", len(dim_flight_arrival) , " registros",FIN_LINEA)
    print(dim_flight_arrival.head())

    # ----------------------------------------------------------------------
    # DEPARTURE TIME
    # ----------------------------------------------------------------------
    df['Departure Date'] = df['Departure Date'].apply(parse_dates)
    dim_departure_time = df[['Departure Date']].drop_duplicates().copy()
    dim_departure_time['id_dim_departure_time'] = range(1, len(dim_departure_time) + 1)
    dim_departure_time['year']  = dim_departure_time['Departure Date'].dt.year
    dim_departure_time['month'] = dim_departure_time['Departure Date'].dt.month
    dim_departure_time['day']   = dim_departure_time['Departure Date'].dt.day
    print(COLORES["verde"] +"")
    print("dim_departure_time: ", len(dim_departure_time) , " registros",FIN_LINEA)
    print(dim_departure_time.head())

    # ----------------------------------------------------------------------
    # FLIGHT DEPARTURE
    # ----------------------------------------------------------------------
    dim_flight_departure = df[['Airport Name', 'Airport Country Code', 'Country Name', 'Airport Continent', 'Continents']].drop_duplicates().copy()
    dim_flight_departure['id_dim_flight_departure'] = range(1, len(dim_flight_departure) + 1)
    dim_flight_departure = dim_flight_departure.drop_duplicates(subset=['Airport Name'])
    print(COLORES["verde"] +"")
    print("dim_flight_departure: ", len(dim_flight_departure) , " registros", FIN_LINEA)
    print(dim_flight_departure.head())

    # ----------------------------------------------------------------------
    # PASSENGER
    # ----------------------------------------------------------------------
    
    dim_passenger = df[['Passenger ID', 'First Name', 'Last Name', 'Gender', 'Age', 'Nationality']].drop_duplicates().copy()
    dim_passenger['id_dim_passenger'] = range(1, len(dim_passenger) + 1)
    print(COLORES["verde"] +"")
    print("dim_passenger: ", len(dim_passenger) , " registros", FIN_LINEA)
    print(dim_passenger.head())
    print("\n")

    # ----------------------------------------------------------------------
    # FLIGHTS
    # ----------------------------------------------------------------------
    df['pilot']           = df['Pilot Name'].map(dim_pilot.set_index('Pilot Name')['id_dim_pilot'])
    df['departure_time']   = df['Departure Date'].map(dim_departure_time.set_index('Departure Date')['id_dim_departure_time'])
    df['passenger']   = df['Passenger ID'].map(dim_passenger.set_index('Passenger ID')['id_dim_passenger'])
    df['flight_departure']   = df['Airport Name'].map(dim_flight_departure.set_index('Airport Name')['id_dim_flight_departure'])
    df['flight_arrival']   = df['Arrival Airport'].map(dim_flight_arrival.set_index('Arrival Airport')['id_dim_flight_arrival'])
    df['status'] = df['Flight Status']
    fact_flight = df[['passenger', 'pilot','departure_time','flight_departure', 'flight_arrival','status']].copy()
    fact_flight['id_fact_flight'] = range(1, len(fact_flight) + 1)
    print(COLORES["verde"] +"")
    print("dim_passenger: ", len(fact_flight) , " registros", FIN_LINEA)
    print(fact_flight.head())
    print("\n")

    return [dim_pilot, dim_departure_time,dim_flight_arrival, dim_flight_departure, dim_passenger, fact_flight]
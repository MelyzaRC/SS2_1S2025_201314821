
CREATE DATABASE FlightDataWarehouse;
DROP TABLE FactFlight;
DROP TABLE DimPassenger;
DROP TABLE DimPilot;
DROP TABLE DimFlightDeparture;

DROP TABLE DimFlightArrival;
DROP TABLE DimDepartureTime;

USE FlightDataWarehouse;
GO

CREATE TABLE DimPassenger (
	id_dim_passenger  INT PRIMARY KEY,
    passenger_id NVARCHAR(50) ,
    first_name NVARCHAR(50),
    last_name NVARCHAR(50),
    gender NVARCHAR(10),
    age INT,
    nationality NVARCHAR(50)
);
GO


CREATE TABLE DimFlightDeparture (
    id_dim_flight_departure INT PRIMARY KEY,
    airport_name NVARCHAR(100),
    airport_country_code NVARCHAR(10),
    country_name NVARCHAR(50),
    airport_continent NVARCHAR(50),
    continents NVARCHAR(50)
);
GO

CREATE TABLE DimFlightArrival (
    id_dim_flight_arrival INT PRIMARY KEY,
    airport_name NVARCHAR(100)
);
GO

CREATE TABLE DimDepartureTime (
    id_dim_departure_time INT PRIMARY KEY,
    [date] DATE,
    [year] INT,
    [month] INT,
    [day] INT
);
GO



CREATE TABLE DimPilot (
    id_dim_pilot	INT PRIMARY KEY	,
    pilot_name		NVARCHAR(100)
);
GO



CREATE TABLE FactFlight (
    id_fact_flight INT IDENTITY(1,1) PRIMARY KEY,
    passenger INT,
    departure_time INT,
    flight_departure INT,
    flight_arrival INT,
    pilot INT,
    status NVARCHAR(25),
    CONSTRAINT FK_FactFlight_Passenger FOREIGN KEY (passenger) 
        REFERENCES DimPassenger(id_dim_passenger),
    CONSTRAINT FK_FactFlight_DepartureDate FOREIGN KEY (departure_time) 
        REFERENCES DimDepartureTime(id_dim_departure_time),
    CONSTRAINT FK_FactFlight_DepartureAirport FOREIGN KEY (flight_departure) 
        REFERENCES DimFlightDeparture(id_dim_flight_departure),
    CONSTRAINT FK_FactFlight_ArrivalAirport FOREIGN KEY (flight_arrival) 
        REFERENCES DimFlightArrival(id_dim_flight_arrival),
    CONSTRAINT FK_FactFlight_Pilot FOREIGN KEY (pilot) 
        REFERENCES DimPilot(id_dim_pilot)
);
GO
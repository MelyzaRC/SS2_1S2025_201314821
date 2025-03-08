USE FlightDataWarehouse;

-- CONSULTA 1 
SELECT 
gender AS GENERO, 
COUNT(*) AS TOTAL, 
COUNT(*) * 100.0 / (SELECT COUNT(*) FROM dbo.DimPassenger) AS PORCENTAJE
FROM dbo.DimPassenger 
GROUP BY gender;

-- CONSULTA 2
SELECT x.year, x.month, x.nationality FROM (SELECT b.nationality, c.month, c.year, ROW_NUMBER() OVER (PARTITION BY b.nationality ORDER BY c.year DESC, c.month DESC) AS rn
FROM dbo.FactFlight a, dbo.DimPassenger b, dbo.DimDepartureTime c
WHERE a.passenger = b.id_dim_passenger
AND a.departure_time = c.id_dim_departure_time) x 
where x.rn = 1
;

-- CONSULTA 3
SELECT b.country_name AS PAIS, b.airport_country_code AS CODIGO_PAIS,  count(*) AS TOTAL 
FROM dbo.FactFlight a, dbo.DimFlightDeparture b 
WHERE a.flight_departure = b.id_dim_flight_departure 
GROUP BY b.country_name, b.airport_country_code
ORDER BY b.country_name ASC 
;

-- CONSULTA 4
SELECT TOP 5
a.airport_name AS AEROPUERTO, a.country_name AS PAIS, a.airport_country_code AS CODIGO_PAIS, count(*) AS TOTAL_VUELOS
FROM 
dbo.FactFlight b, 
dbo.DimFlightDeparture a 
WHERE a.id_dim_flight_departure = b.flight_departure 
group by a.airport_name, a.country_name,  a.airport_country_code 
ORDER BY TOTAL_VUELOS DESC 
;

-- CONSULTA 5
SELECT a.status AS STATUS, count(*) AS VUELOS FROM dbo.FactFlight a
GROUP BY a.status
ORDER BY VUELOS ASC;

-- CONSULTA 6
SELECT TOP 5
b.airport_name AS DESTINO, count(*) AS VISITAS
FROM dbo.FactFlight a , dbo.DimFlightArrival b 
WHERE a.flight_arrival = b.id_dim_flight_arrival 
group by b.airport_name
ORDER BY VISITAS DESC;

-- CONSULTA 7
SELECT TOP 5 b.continents AS CONTINENTE, count(*) AS VISITAS
FROM dbo.FactFlight a, dbo.DimFlightDeparture b 
where a.flight_departure = b.id_dim_flight_departure
GROUP by b.continents
ORDER BY VISITAS DESC 
;

-- CONSULTA 8
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

-- CONSULTA 9
SELECT 
    b.month as MES, 
    b.year AS ANIO, 
    COUNT(*) AS TOTAL_VUELOS
FROM dbo.FactFlight a, dbo.DimDepartureTime b
WHERE a.departure_time = b.id_dim_departure_time
GROUP BY b.year, b.month
ORDER BY b.year DESC, b.month ASC;
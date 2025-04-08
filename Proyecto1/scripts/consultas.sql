use sgfood;

select 'DimCliente'		as TABLA , count(*) as REGISTROS from DimCliente	union 
select 'DimFecha'		as TABLA , count(*) as REGISTROS from DimFecha		union
select 'DimProducto'	as TABLA , count(*) as REGISTROS from DimProducto	union
select 'DimProveedor'	as TABLA , count(*) as REGISTROS from DimProveedor	union
select 'DimSucursal'	as TABLA , count(*) as REGISTROS from DimSucursal	union
select 'DimUbicacion'	as TABLA , count(*) as REGISTROS from DimUbicacion	union
select 'DimVendedor'	as TABLA , count(*) as REGISTROS from DimVendedor	union
select 'FactCompras'	as TABLA , count(*) as REGISTROS from FactCompras	union
select 'FactVentas'		as TABLA , count(*) as REGISTROS from FactVentas;

DELETE FROM DimCliente;
DELETE FROM DimFecha;
DELETE FROM DimProducto; 
DELETE FROM DimProveedor;
DELETE FROM DimSucursal;
DELETE FROM DimUbicacion;
DELETE FROM DimVendedor;
DELETE FROM FactCompras;
DELETE FROM FacVentas;
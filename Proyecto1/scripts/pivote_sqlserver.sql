CREATE DATABASE pivote;
USE pivote; 

CREATE TABLE compras_pivote (
	Fecha				VARCHAR(200)	NULL	,  
	CodProveedor		VARCHAR(200)	NULL	,  
	NombreProveedor		VARCHAR(200)	NULL	,  
	DireccionProveedor	VARCHAR(200)	NULL	,  
	NumeroProveedor		VARCHAR(200)	NULL	,  
	WebProveedor		VARCHAR(200)	NULL	,  
	CodProducto			VARCHAR(200)	NULL	,  
	NombreProducto		VARCHAR(200)	NULL	,  
	MarcaProducto		VARCHAR(200)	NULL	,  
	Categoria			VARCHAR(200)	NULL	,  
	SodSuSursal			VARCHAR(200)	NULL	,  
	NombreSucursal		VARCHAR(200)	NULL	,  
	DireccionSucursal	VARCHAR(200)	NULL	,  
	Region				VARCHAR(200)	NULL	,  
	Departamento		VARCHAR(200)	NULL	,  
	Unidades			VARCHAR(200)	NULL	,  
	CostoU				VARCHAR(200)	NULL 
);

CREATE TABLE ventas_pivote (
	Fecha				VARCHAR(200)	NULL	,  
	CodigoCliente		VARCHAR(200)	NULL	,  
	NombreCliente		VARCHAR(200)	NULL	,  
	TipoCliente			VARCHAR(200)	NULL	,  
	DireccionCliente	VARCHAR(200)	NULL	,  
	NumeroCliente		VARCHAR(200)	NULL	,  
	CodVendedor			VARCHAR(200)	NULL	,  
	NombreVendedor		VARCHAR(200)	NULL	,  
	Vacacionista		VARCHAR(200)	NULL	,  
	CodProducto			VARCHAR(200)	NULL	,  
	NombreProducto		VARCHAR(200)	NULL	,  
	MarcaProducto		VARCHAR(200)	NULL	,  
	Categoria			VARCHAR(200)	NULL	,  
	SodSuSursal			VARCHAR(200)	NULL	,  
	NombreSucursal		VARCHAR(200)	NULL	,  
	DireccionSucursal	VARCHAR(200)	NULL	,  
	Region				VARCHAR(200)	NULL	,  
	Departamento		VARCHAR(200)	NULL	,  
	Unidades			VARCHAR(200)	NULL	,  
	PrecioUnitario		VARCHAR(200)	NULL  
);
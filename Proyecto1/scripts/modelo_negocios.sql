
CREATE DATABASE sgfood;
USE sgfood;
CREATE TABLE DimSucursal(
	IdDimSucursal		INT				NOT NULL	IDENTITY	,
	SodSucursal			VARCHAR(10)		NOT NULL				,		 
	NombreSucursal		VARCHAR(25)		NOT NULL				,
	DireccionSucursal	VARCHAR(250)	NOT NULL				, 
	PRIMARY KEY (IdDimSucursal)
);

CREATE TABLE DimProducto(
	IdDimProducto		INT				NOT NULL	IDENTITY	,
	CodProducto			VARCHAR(10)		NOT NULL				,		 
	NombreProducto		VARCHAR(250)	NOT NULL				,
	MarcaProducto		VARCHAR(100)	NOT NULL				, 
	Categoria			VARCHAR(100)	NOT NULL				,
	PRIMARY KEY (IdDimProducto)
);

CREATE TABLE DimFecha(
	IdDimFecha			INT				NOT NULL	IDENTITY	,
	Dia					INT				NOT NULL				,		 
	Mes					INT				NOT NULL				,
	Anio				INT				NOT NULL				, 
	PRIMARY KEY (IdDimFecha)
);

CREATE TABLE DimUbicacion(
	IdDimUbicacion		INT				NOT NULL	IDENTITY	,
	Region				VARCHAR(50)		NOT NULL				,		 
	Departamento		VARCHAR(50)		NOT NULL				,
	PRIMARY KEY (IdDimUbicacion)
);

CREATE TABLE DimProveedor(
	IdDimProveedor		INT				NOT NULL	IDENTITY	,
	CodProveedor		VARCHAR(10)		NOT NULL				,		 
	NombreProveedor		VARCHAR(250)	NOT NULL				,
	DireccionProveedor	VARCHAR(250)	NOT NULL				,
	NumeroProveedor		INT				NOT NULL				,
	WebProveedor		VARCHAR(5)		NOT NULL				,
	PRIMARY KEY (IdDimProveedor)
);

CREATE TABLE FactCompras(
	IdFactCompras		INT				NOT NULL	IDENTITY	, 
	DimSucursal			INT				NOT NULL				, 
	DimProducto			INT				NOT NULL				,
	DimFecha			INT				NOT NULL				,
	DimUbicacion		INT				NOT NULL				,
	DimProveedor		INT				NOT NULL				,
	Unidades			INT				NOT NULL				, 
	CostoU				DECIMAL(18,2)	NOT NULL				,
	PRIMARY KEY(IdFactCompras)											,
	FOREIGN KEY(DimSucursal)	REFERENCES DimSucursal(IdDimSucursal)	,
	FOREIGN KEY(DimProducto)	REFERENCES DimProducto(IdDimProducto)	,
	FOREIGN KEY(DimFecha)		REFERENCES DimFecha(IdDimFecha)			,
	FOREIGN KEY(DimUbicacion)	REFERENCES DimUbicacion(IdDimUbicacion)	,
	FOREIGN KEY(DimProveedor)	REFERENCES DimProveedor(IdDimProveedor)	
);

CREATE TABLE DimCliente(
	IdDimCliente		INT				NOT NULL	IDENTITY	,
	CodigoCliente		VARCHAR(10)		NOT NULL				,		 
	NombreCliente		VARCHAR(250)	NOT NULL				,
	TipoCliente			VARCHAR(25)		NOT NULL				,
	DireccionCliente	VARCHAR(250)	NOT NULL				,
	NumeroCliente		VARCHAR(15)		NOT NULL				,
	PRIMARY KEY (IdDimCliente)
);

CREATE TABLE DimVendedor(
	IdDimVendedor		INT				NOT NULL	IDENTITY	,
	CodVendedor			VARCHAR(10)		NOT NULL				,		 
	NombreVendedor		VARCHAR(250)	NOT NULL				,
	Vacacionista		VARCHAR(5)		NOT NULL				,
	PRIMARY KEY (IdDimVendedor)
);

CREATE TABLE FactVentas(
	IdFactVentas		INT				NOT NULL	IDENTITY	, 
	DimSucursal			INT				NOT NULL				, 
	DimProducto			INT				NOT NULL				,
	DimFecha			INT				NOT NULL				,
	DimUbicacion		INT				NOT NULL				,
	DimCliente			INT				NOT NULL				,
	DimVendedor			INT				NOT NULL				,
	Unidades			INT				NOT NULL				, 
	PrecioUnitario		DECIMAL(18,2)	NOT NULL				,
	PRIMARY KEY(IdFactVentas)											,
	FOREIGN KEY(DimSucursal)	REFERENCES DimSucursal(IdDimSucursal)	,
	FOREIGN KEY(DimProducto)	REFERENCES DimProducto(IdDimProducto)	,
	FOREIGN KEY(DimFecha)		REFERENCES DimFecha(IdDimFecha)			,
	FOREIGN KEY(DimUbicacion)	REFERENCES DimUbicacion(IdDimUbicacion)	,
	FOREIGN KEY(DimCliente)		REFERENCES DimCliente(IdDimCliente)		,
	FOREIGN KEY(DimVendedor)	REFERENCES DimVendedor(IdDimVendedor)	
);

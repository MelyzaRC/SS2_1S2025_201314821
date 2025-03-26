><img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/Usac_logo.png" alt="drawing" width="75">
>
>Universidad San Carlos de Guatemala
>
>Facultad de Ingeniería 
>
>Escuela de Ciencias y Sistemas 
>
>Primer Semestre, 2025
>
>Laboratorio de Seminario de Sistemas 2


| Nombre                               | Carnet    |
| ------------------------------------ | --------- |
|  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvke8Pr8T6xz52yM8v0ieg0oQy9L9SwfkO4hy4IKoRpxyQBKSGUWto7sWmzj9YYgm1VzU&usqp=CAU" alt="drawing" width="20"> &nbsp; Melyza Alejandra Rodríguez Contreras | 201314821 |


# Proyecto 1

## Descripción general 

> <img src="https://png.pngtree.com/png-vector/20240719/ourmid/pngtree-food-app-icon-vector-png-image_7228673.png" alt="drawing" width="250"> 
>
>***SG-Food***, una megaempresa dedicada a la compra, distribución y comercialización de productos de diversas marcas y categorías que requiere una solución de *Business Intelligence* para optimizar sus procesos de análisis de ventas e inventarios. Debido al crecimiento significativo en sus operaciones, el sistema actual presenta tiempos de respuesta lentos y problemas en la base de datos principal. Este proyecto propone implementar una solución de BI que optimice los tiempos de respuesta y reduzca la carga sobre la base de datos central, permitiendo un análisis eficiente de datos de compras y ventas.

## Arquitectura de la solución 

A continuación, se presenta la arquitectura de la solución propuesta durante el desarrollo de este proyecto. 

<img src="images/diagrama.png" alt="drawing" > 

## Resumen de tecnologías utilizadas 

| Tecnología | Versión | Descripción | 
| -- | -- | -- |
| <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/microsoft-windows-22-logo.png" alt="drawing" width="100">  <br> **Sistema operativo Windows**| 11| Windows es un sistema operativo gráfico desarrollado por Microsoft, conocido por su interfaz amigable y su amplia compatibilidad con software y hardware. Es utilizado en computadoras personales, servidores y dispositivos móviles. Su versión más popular es Windows 10, aunque Windows 11 también está disponible con mejoras de rendimiento y seguridad.|
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Visual_Studio_Icon_2022.svg/2048px-Visual_Studio_Icon_2022.svg.png" alt="drawing" width="100">  <br> **IDE Microsoft Visual Studio**|2022 |Microsoft Visual Studio es un entorno de desarrollo integrado (IDE) utilizado para crear aplicaciones, sitios web y servicios. Soporta múltiples lenguajes de programación como C#, C++, JavaScript y Python. Ofrece herramientas de depuración, diseño, control de versiones y compilación, facilitando el desarrollo de software eficiente y robusto. |
| <img src="https://bladebridge.com/wp-content/uploads/2022/01/SSIS-1x3-1.png" alt="drawing" width="200">  <br> **Extensión SQL Server Integration Services Projects 2022**|1.5 | La extensión SQL Server Integration Services Projects 2022 para Visual Studio permite diseñar, implementar y administrar paquetes de Integration Services (SSIS). Facilita la creación de flujos de trabajo ETL, como transformaciones y carga de datos, proporcionando herramientas para la depuración, prueba y despliegue en entornos de SQL Server.|
|  <img src="https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1582234330/sql1_txc0vs.png" alt="drawing" width="100">  <br> **SQL Server 2022 (RTM)**|16.0.1000 | SQL Server 2022 (RTM) es la versión más reciente del sistema de gestión de bases de datos de Microsoft. Ofrece mejoras en rendimiento, seguridad y escalabilidad, con nuevas características como la integración con Azure, capacidades avanzadas de inteligencia artificial, y optimización de consultas y almacenamiento en la nube.|
| <img src="https://cdn.prod.website-files.com/655b60964be1a1b36c746790/655b60964be1a1b36c746d41_646dfce3b9c4849f6e401bff_supabase-logo-icon_1.png" alt="drawing" width="100">  <br> **Postgres SQL con Supabase**| 15.8|Supabase es una plataforma que proporciona backend como servicio, basada en PostgreSQL. Ofrece bases de datos gestionadas, autenticación, almacenamiento y funciones en tiempo real. Al usar SQL en Supabase, puedes interactuar directamente con la base de datos PostgreSQL mediante consultas, vistas, funciones y triggers, todo desde su interfaz. |


## Proceso ETL 

### Orígen de datos 

<img src="https://cdn-icons-png.flaticon.com/512/7600/7600437.png"  alt="drawing" width="30"> **.comp** 

>Los archivos con la extensión ***.comp*** contienen las información relacionada con las diferentes adquisiciones o compras realizadas a proveedores por parte de ***SG-Food***.


|Campos del archivo| Ejemplo del campo|
|--|--|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> Fecha|11/01/2020|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> CodProveedor|P0001|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> NombreProveedor|CESAR ADRIAN GERONIS ROMERO|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> DireccionProveedor|10 avenida 4-54 zona 12|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> NumeroProveedor|42022451|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> WebProveedor|S|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> CodProducto|AC00005|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> NombreProducto|Gaseosa Postobón|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> MarcaProducto|BRETANA
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> Categoria|Bebidas|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> SodSucursal|S0001|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> NombreSucursal|Sucursal1|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> DireccionSucursal|kilometro 20 carretera al pacifico, parque industrial unisur, local no. 1, delta barcenas,|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> Region|Suroccidente1|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> Departamento|Quetzaltenango|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> Unidades|583|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png"  alt="drawing" width="15"> CostoU|508.35|

<img src="https://cdn-icons-png.flaticon.com/512/7600/7600437.png"  alt="drawing" width="30"> **.vent** 

>Los archivos con extensión ***.vent*** contienen la información relacionada con las ventas realizadas por la megacorporación ***SG-Food*** a los diferentes clientes con los que cuentan en sus carteras. 

|Campos del archivo| Ejemplo del campo|
|--|--|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> Fecha|14/01/2020|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> CodigoCliente|C0001|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> NombreCliente|Jose Arturo Bayardi Lozano|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> TipoCliente|Minorista|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> DireccionCliente|calzada atanasio tzul 22-00 zona 12, el cortijo ii, oficina 100|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> NumeroCliente|69555645|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> CodVendedor|V0001|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> NombreVendedor|Nelson Mario Caffera Morandi|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> Vacacionista|1|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> CodProducto|AC00003|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> NombreProducto|Queso Camembert kaserei champiñón |
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> MarcaProducto|MONTICELLO|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> Categoria|Charcutería|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> SodSucursal|S0001|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> NombreSucursal|Sucursal1|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> DireccionSucursal|kilometro 20 carretera al pacifico, parque industrial unisur, local no. 1, delta barcenas,|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> Region|Suroccidente1|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> Departamento|Quetzaltenango|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> Unidades|34|
|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Sign-check-icon.png/800px-Sign-check-icon.png" alt="drawing" width="15"> PrecioUnitario|398.27|


### Estrategia de tablas pivote 

Para hacer más sencillo el proceso ETL, se utilizó la estrategia de creación de tablas *pivote*, estas tablas se definen como herramientas auxiliares que nos ayudarán a realizar de mejor manera el proceso de transformación, ya que cargamos todos los datos en el estado original en que fueron definidos en el archivo fuente, esto, nos permitirá detectar errores en los registros y áreas de transformación. 

A continuación, se detalla los motores de base de datos utilizados y la definición de las diferentes tablas utilizadas para la implementación de la estrategia de tablas pivote en los dos fabricantes de base de datos utilizados. 

- **SQL Server**

<img src="https://logonoid.com/images/sql-server-logo.png" alt="drawing" width="150"> 


|Tabla|Descripción|
|--|--|
|<img src="https://cdn-icons-png.flaticon.com/512/11784/11784642.png" alt="drawing" width="100"> <br> **compras_pivote**|Tabla auxiliar para registrar los datos de las compras en la forma en que fueron representados en los archivos de orígen de datos. Esta tabla está asociada al contenido de los archivos ***.comp***. Esta tabla está implementada en **SQL Server**.|
|<img src="https://cdn-icons-png.flaticon.com/512/11784/11784642.png" alt="drawing" width="100"> <br> **ventas_pivote**|Tabla auxiliar para registrar los datos de las ventas realizadas a los clientes, en la forma en que fueron representados en los archivos de orígen de datos. Esta tabla está asociada al contenido de los archivos ***.vent***. Esta tabla está implementada en **SQL Server**.|


**DDL de las tablas:**
```
CREATE TABLE compras_pivote (
	Fecha				NVARCHAR(200)	NULL	,  
	CodProveedor		NVARCHAR(200)	NULL	,  
	NombreProveedor		NVARCHAR(200)	NULL	,  
	DireccionProveedor	NVARCHAR(200)	NULL	,  
	NumeroProveedor		NVARCHAR(200)	NULL	,  
	WebProveedor		NVARCHAR(200)	NULL	,  
	CodProducto			NVARCHAR(200)	NULL	,  
	NombreProducto		NVARCHAR(200)	NULL	,  
	MarcaProducto		NVARCHAR(200)	NULL	,  
	Categoria			NVARCHAR(200)	NULL	,  
	SodSuSursal			NVARCHAR(200)	NULL	,  
	NombreSucursal		NVARCHAR(200)	NULL	,  
	DireccionSucursal	NVARCHAR(200)	NULL	,  
	Region				NVARCHAR(200)	NULL	,  
	Departamento		NVARCHAR(200)	NULL	,  
	Unidades			NVARCHAR(200)	NULL	,  
	CostoU				NVARCHAR(200)	NULL 
);

CREATE TABLE ventas_pivote (
	Fecha				NVARCHAR(200)	NULL	,  
	CodigoCliente		NVARCHAR(200)	NULL	,  
	NombreCliente		NVARCHAR(200)	NULL	,  
	TipoCliente			NVARCHAR(200)	NULL	,  
	DireccionCliente	NVARCHAR(200)	NULL	,  
	NumeroCliente		NVARCHAR(200)	NULL	,  
	CodVendedor			NVARCHAR(200)	NULL	,  
	NombreVendedor		NVARCHAR(200)	NULL	,  
	Vacacionista		NVARCHAR(200)	NULL	,  
	CodProducto			NVARCHAR(200)	NULL	,  
	NombreProducto		NVARCHAR(200)	NULL	,  
	MarcaProducto		NVARCHAR(200)	NULL	,  
	Categoria			NVARCHAR(200)	NULL	,  
	SodSuSursal			NVARCHAR(200)	NULL	,  
	NombreSucursal		NVARCHAR(200)	NULL	,  
	DireccionSucursal	NVARCHAR(200)	NULL	,  
	Region				NVARCHAR(200)	NULL	,  
	Departamento		NVARCHAR(200)	NULL	,  
	Unidades			NVARCHAR(200)	NULL	,  
	PrecioUnitario		NVARCHAR(200)	NULL  
);
```

- **Postgres**

<img src="https://miro.medium.com/v2/resize:fit:512/0*ioDeujW3euLCfXew.png" alt="drawing" width="200"> 

|Tabla|Descripción|
|--|--|
|<img src="https://cdn-icons-png.flaticon.com/512/11784/11784642.png" alt="drawing" width="100"> <br> **compras_pivote**|Tabla auxiliar para registrar los datos de las compras en la forma en que fueron representados en los archivos de orígen de datos. Esta tabla está asociada al contenido de los archivos ***.comp***. Esta tabla está implementada en **Postgres** con **Supabase**.|
|<img src="https://cdn-icons-png.flaticon.com/512/11784/11784642.png" alt="drawing" width="100"> <br> **ventas_pivote**|Tabla auxiliar para registrar los datos de las ventas realizadas a los clientes, en la forma en que fueron representados en los archivos de orígen de datos. Esta tabla está asociada al contenido de los archivos ***.vent***. Esta tabla está implementada en **Postgres** con **Supabase**.|

**DDL de las tablas:**

```
CREATE TABLE compras_pivote (
    fecha                VARCHAR(200),  
    cod_proveedor        VARCHAR(200),  
    nombre_proveedor     VARCHAR(200),  
    direccion_proveedor  VARCHAR(200),  
    numero_proveedor     VARCHAR(200),  
    web_proveedor        VARCHAR(200),  
    cod_producto         VARCHAR(200),  
    nombre_producto      VARCHAR(200),  
    marca_producto       VARCHAR(200),  
    categoria           VARCHAR(200),  
    sod_sucursal        VARCHAR(200), 
    nombre_sucursal     VARCHAR(200),  
    direccion_sucursal  VARCHAR(200),  
    region              VARCHAR(200),  
    departamento        VARCHAR(200),  
    unidades            VARCHAR(200), 
    costo_unitario      VARCHAR(200) 
);

CREATE TABLE ventas_pivote (
    fecha                VARCHAR(200),  
    codigo_cliente       VARCHAR(200),  
    nombre_cliente       VARCHAR(200),  
    tipo_cliente         VARCHAR(200),  
    direccion_cliente    VARCHAR(200),  
    numero_cliente       VARCHAR(200),  
    cod_vendedor        VARCHAR(200),  
    nombre_vendedor     VARCHAR(200),  
    vacacionista        VARCHAR(200),  
    cod_producto        VARCHAR(200),  
    nombre_producto     VARCHAR(200),  
    marca_producto      VARCHAR(200),  
    categoria           VARCHAR(200),  
    sod_sucursal        VARCHAR(200),
    nombre_sucursal     VARCHAR(200),  
    direccion_sucursal  VARCHAR(200),  
    region              VARCHAR(200),  
    departamento        VARCHAR(200),  
    unidades            VARCHAR(200),
    precio_unitario     VARCHAR(200)
);
```



><img src="https://cdn-icons-png.flaticon.com/512/561/561739.png" alt="drawing" width="25">  **NOTA:** 
>
>***DDL (Data Definition Language)*** es un conjunto de instrucciones en bases de datos que definen la estructura y organización de los datos. Incluye comandos como **CREATE, ALTER** y **DROP**, que se utilizan para crear, modificar o eliminar tablas, índices y otros objetos en la base de datos.

### Extracción de datos

- **Herramientas utilizadas**

**Execute SQL Task**

<img src="images/h1.png" alt="drawing" width="200"> 



### Transformación de datos
### Carga de datos 

## Modelo de DataWarehouse

## Manual de implementación 

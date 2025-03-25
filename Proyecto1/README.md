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

A continuación se presenta la arquitectura de la solución propuesta durante el desarrollo de este proyecto. 

<img src="images/diagrama.png" alt="drawing" > 

## Tecnologías utilizadas 

| Tecnología | Versión | Descripción | 
| -- | -- | -- |
| <img src="https://cdn.freebiesupply.com/logos/thumbs/2x/microsoft-windows-22-logo.png" alt="drawing" width="100">  <br> **Sistema operativo Windows**| 11| Windows es un sistema operativo gráfico desarrollado por Microsoft, conocido por su interfaz amigable y su amplia compatibilidad con software y hardware. Es utilizado en computadoras personales, servidores y dispositivos móviles. Su versión más popular es Windows 10, aunque Windows 11 también está disponible con mejoras de rendimiento y seguridad.|
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Visual_Studio_Icon_2022.svg/2048px-Visual_Studio_Icon_2022.svg.png" alt="drawing" width="100">  <br> **IDE Microsoft Visual Studio**|2022 |Microsoft Visual Studio es un entorno de desarrollo integrado (IDE) utilizado para crear aplicaciones, sitios web y servicios. Soporta múltiples lenguajes de programación como C#, C++, JavaScript y Python. Ofrece herramientas de depuración, diseño, control de versiones y compilación, facilitando el desarrollo de software eficiente y robusto. |
| <img src="https://bladebridge.com/wp-content/uploads/2022/01/SSIS-1x3-1.png" alt="drawing" width="200">  <br> **Extensión SQL Server Integration Services Projects 2022**|1.5 | La extensión SQL Server Integration Services Projects 2022 para Visual Studio permite diseñar, implementar y administrar paquetes de Integration Services (SSIS). Facilita la creación de flujos de trabajo ETL, como transformaciones y carga de datos, proporcionando herramientas para la depuración, prueba y despliegue en entornos de SQL Server.|
|  <img src="https://images.datacamp.com/image/upload/f_auto,q_auto:best/v1582234330/sql1_txc0vs.png" alt="drawing" width="100">  <br> **SQL Server 2022 (RTM)**|16.0.1000 | SQL Server 2022 (RTM) es la versión más reciente del sistema de gestión de bases de datos de Microsoft. Ofrece mejoras en rendimiento, seguridad y escalabilidad, con nuevas características como la integración con Azure, capacidades avanzadas de inteligencia artificial, y optimización de consultas y almacenamiento en la nube.|
| <img src="https://cdn.prod.website-files.com/655b60964be1a1b36c746790/655b60964be1a1b36c746d41_646dfce3b9c4849f6e401bff_supabase-logo-icon_1.png" alt="drawing" width="100">  <br> **Postgres SQL con Supabase**| 15.8|Supabase es una plataforma que proporciona backend como servicio, basada en PostgreSQL. Ofrece bases de datos gestionadas, autenticación, almacenamiento y funciones en tiempo real. Al usar SQL en Supabase, puedes interactuar directamente con la base de datos PostgreSQL mediante consultas, vistas, funciones y triggers, todo desde su interfaz. |


## Proceso ETL 

### Orígen de datos 
### Estrategia de tablas pivote 

Para hacer más sencillo el proceso ETL, se utilizó la estrategia de creación de tablas *pivote*, estas tablas se definen como herramientas auxiliares que nos ayudarán a realizar de mejor manera el proceso de transformación. 

### Extracción de datos

- **Herramientas utilizadas**

**Execute SQL Task**

<img src="images/h1.png" alt="drawing" width="200"> 



### Transformación de datos
### Carga de datos 

## Modelo de DataWarehouse

## Manual de implementación 

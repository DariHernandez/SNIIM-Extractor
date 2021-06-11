# SNIIM EXTRACTOR
**python version: 3.9**

**Extraer información** de la página **[www.economia-sniim.gob.mx](http://www.economia-sniim.gob.mx/nuevo/Home.aspx?opcion=Consultas/MercadosNacionales/PreciosDeMercado/Agricolas/ConsultaFrutasYHortalizas.aspx?SubOpcion=4|0)**, generar un **reporte** en un archivo de **excel** y **enviar** el reporte **por correo**. 

**Proyecto con GUI** (interfaz gráfica de usuario).

# Install
## Tird party modules

Instala los módulos de terceros, desde pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

Es necesario tener instalados los siguientes programas: 

* [Google Chrome](https://www.google.com/intl/es/chrome) última versión

# Run the program

## GUI

Para **ejecutar** el programa con **interfaz gráfica**, **ejecute** con su interprete de **python 3.9**, el archivo **__ main__.py**.

La interfaz gráfica, además de permitirte ejecutar el programa, le facilitará configurarlo (mas detalles en la sección de configuración).

![Home](https://i.imgur.com/MxUmYe7.png)

## Terminal

Para **iniciar** el programa **en terminal** / sin interfaz gráfica, **ejecute** el archivo **sniim_run.py** con su interprete de **python 3.9**.

Ejecutando el programa de esta forma **no se podrán actualizar las configuraciones** y se ejecutará con la **última configuración establecida** (mas detalles en la sección de configuración). 

# Config

## Config GUI

La pantalla de configuración es la siguiente: 

![Config screen](https://i.imgur.com/X4SN2SB.png)

### CORREO

En esta sección se **establecen** el **correo** desde el que se **enviarán** los **emails**, y el **correo** que los **recibirá**. 

NOTA: el programa soporta los correos de: gmail.com, outlook.com, hotmail.com, live.com, yahoo.com y aol.com, pero, **algunos** de estos **servicios de correo** requieren una **configuración especial**. 

**En caso de querer cambiar el correo desde el que se envían los emails, [contáctarme](mailto:hernandezdarifrancisco@gmail.com)**. 

### MERCADO DE DESTINO

**Lista de mercados de destino** para obtener los datos. 

NOTA: **Cada mercado** debe ser escrito **exactamente** como se muestra en la página: **mayusculas, minusculas, comillas, signos**, etc. 

### PRODUCTOS

**Lista de productos** a extraer, con su respectiva calidad (opcional). 

NOTA: Deben ser los **mismos nombres** que se muestran en la página, pero **no importan mayusculas y minusculas**. 

## config.json

Todas las **configuraciones** se guardan en el **archivo config.json**, por lo que, **puede editarlo manualmente**.
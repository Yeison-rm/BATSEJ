# BATSEJ

# Introducción

Este sistema calcula las comisiones a cobrar a los comercios basándose en el número de peticiones exitosas y no exitosas durante un período específico. La información se extrae de una base de datos SQLite y se utiliza para calcular las comisiones según las condiciones establecidas en el contrato.
Finalmente, los resultados se envían a través de correo electrónico.

# Informacion base de datos SQLITE

# Tabla apicall:

    date_api_call = 'Fecha de la llamada a la API.'
    commerce_id = 'Identificador del comercio (clave que referencia a commerce).'
    ask_status = 'Estado de la petición (éxito o no éxito).'
    is_related = 'Información adicional que podría ser relevante para el procesamiento.'

# Tabla commerce:

    commerce_id = 'Identificador del comercio (clave primaria).'
    commerce_nit = 'Número de identificación tributaria del comercio.'
    commerce_name = 'Nombre del comercio.'
    commerce_status = 'Estado del comercio (activo o inactivo).'
    commerce_email = 'Correo electrónico del comercio.'

# Diagrama de Base de Datos

# +----------------+    +-------------------+
# |    Commerce    |    |      ApiCall      |
# +----------------+    +-------------------+
# | commerce_id    |<---| commerce_id       |
# | commerce_nit   |    | date_api_call     |
# | commerce_name  |    | ask_status        |
# | commerce_status|    | is_related        |
# | commerce_email |    +-------------------+
# +----------------+                 

# Componentes del Sistema:    
El sistema está compuesto por cuatro módulos principales:

    - constants.py: Define los parámetros constantes utilizados en el cálculo.
    - query.py: Extrae los datos relevantes de la base de datos. 
    - use_cases.py: Calcula las comisiones y genera un reporte.
    - services.py: Envía los resultados por correo electrónico.
    - main.py: Ejecuta el flujo de trabajo completo del sistema.

# Paso 1: constants.py
Este archivo define los parámetros constantes que se utilizan en el sistema.

# Descripción:

    - api_call_data: Contiene las fechas de inicio y fin para el periodo de análisis.
    - commerce: Mapea los identificadores de los comercios a sus nombres correspondientes.
    - email_credentials: Contiene las credenciales necesarias para el envío de correos electrónicos (correo electrónico del remitente y contraseña).
    - smtp_settings: Configura el servidor SMTP para el envío de correos electrónicos.

# Paso 2: query.py
Este módulo se encarga de extraer los datos necesarios desde la base de datos SQLite.

# Descripción:

    - Se conecta a la base de datos SQLite.
    - Ejecuta una consulta SQL que agrupa los datos de las peticiones API exitosas y no exitosas por comercio.
    - Devuelve un DataFrame con la información necesaria para el cálculo de comisiones.

# Paso 3: use_cases.py
Este módulo utiliza los datos obtenidos para calcular las comisiones, generar un reporte en formato Excel, y guardar el archivo en un directorio específico con un nombre basado en la fecha y hora actual.

# Descripción:

    - Cálculo de Comisiones: Calcula las comisiones basándose en las peticiones exitosas y no exitosas, aplicando descuentos y calculando el IVA.
    - Creación de Directorio y Archivo: Verifica si el directorio resultado existe y lo crea si es necesario. Luego, guarda el archivo Excel en este directorio con un nombre basado en la fecha y hora actual para evitar sobrescribir archivos anteriores.
    - Generación del Archivo Excel: Guarda el DataFrame en un archivo Excel con un nombre único que incluye la fecha y hora del cálculo.

# Paso 4: services.py
Este módulo se encarga de enviar los resultados por correo electrónico.

# Descripción:

    - Envío de Correo: Envía un correo electrónico con el archivo Excel adjunto que contiene el resumen de las comisiones. Utiliza la configuración del servidor SMTP y las credenciales del remitente definidas en constants.py.

# Paso 5: main.py
Este módulo ejecuta el flujo de trabajo completo del sistema y envía los resultados por correo electrónico.

# Descripción:

    - Carga de Datos: Utiliza la función load_commerce_api_call_data para cargar los datos de las llamadas a la API desde la base de datos entre las fechas especificadas en api_call_data.
    - Cálculo de Comisiones: Utiliza la función calculate_commissions para calcular las comisiones basadas en los datos cargados.
    - Envío de Resultados: Utiliza la función send_email para enviar un correo electrónico con el archivo Excel que contiene el resumen de las comisiones.

# Notas

    - Asegúrate de que los directorios y archivos mencionados existen y son accesibles antes de ejecutar el script.
    - Verifica que las credenciales y configuraciones de correo electrónico en constants.py son correctas para asegurar que el envío del correo funcione correctamente.
import sqlite3
import pandas as pd

# Conexión a la base de datos
conn = sqlite3.connect('database/database.sqlite')

def load_commerce_api_call_data(start_date, end_date):
    """
    Carga los datos desde las tablas 'apicall' y 'commerce' de la base de datos SQLite.

    Returns:
        tuple: Una tuple que contiene un dataFrame:
            - result_df (pd.DataFrame): DataFrame con los datos necesarios para realizar el calculo de comisiones
    """

    query = """
    WITH cte_group AS
    (SELECT c.commerce_nit, c.commerce_name, c.commerce_email,
    apc.ask_status, COUNT(*) AS transation_count
    FROM apicall apc 
    INNER JOIN commerce c ON apc.commerce_id = c.commerce_id 
    WHERE date_api_call BETWEEN '{}' AND '{}'
    AND c.commerce_status = 'Active'
    GROUP BY c.commerce_nit, c.commerce_name, c.commerce_email, apc.ask_status)
    SELECT cgp.commerce_nit, cgp.commerce_name, cgp.commerce_email, 
    (SELECT transation_count FROM cte_group ct_success 
    WHERE ct_success.commerce_nit = cgp.commerce_nit AND ct_success.ask_status = 'Successful') success,
    (SELECT transation_count FROM cte_group ct_success 
    WHERE ct_success.commerce_nit = cgp.commerce_nit AND ct_success.ask_status = 'Unsuccessful') unsuccess
    FROM cte_group cgp
    GROUP BY cgp.commerce_nit, cgp.commerce_name, cgp.commerce_email
    """.format(start_date, end_date)
    
    result_df = pd.read_sql_query(query, conn)
    
    conn.close()
    
    return result_df
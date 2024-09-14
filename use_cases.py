from constants import commerce
import pandas as pd

def calculate_commissions(commerce_df):
    """
    Calcula las comisiones a cobrar a cada comercio basándose en el número de peticiones exitosas y no exitosas.
    
    Args:
        apicall_df (pd.DataFrame): DataFrame con los datos de las llamadas a la API.
        commerce_df (pd.DataFrame): DataFrame con los datos de los comercios.
        
    Returns:
        pd.DataFrame: DataFrame con los resultados de las comisiones, incluyendo el valor de la comisión, IVA y total.
    """
    iva = 0.19
    results = []

    for _, row in commerce_df.iterrows():
        commerce_name = row['commerce_name']
        commerce_nit = row['commerce_nit']
        peticiones_exitosas = row['success']
        peticiones_no_exitosas = row['unsuccess']

        # Calcular comisiones en base a las condiciones del contrato
        valor_comision = 0
        descuento = 0
        if commerce_name == commerce['innovexa']:
            valor_comision = peticiones_exitosas * 300
        elif commerce_name == commerce['nexatech']:
            if peticiones_exitosas <= 10000:
                valor_comision = peticiones_exitosas * 250
            elif peticiones_exitosas <= 20000:
                valor_comision = peticiones_exitosas * 200
            else:
                valor_comision = peticiones_exitosas * 170
        elif commerce_name == commerce['quantumleap']:
            valor_comision = peticiones_exitosas * 600
        elif commerce_name == commerce['zenith']:
            if peticiones_exitosas <= 22000:
                valor_comision = peticiones_exitosas * 250
            else:
                valor_comision = peticiones_exitosas * 130
            if peticiones_no_exitosas > 6000:
                descuento = valor_comision * 0.05  # Aplicar descuento del 5%
        elif commerce_name == commerce['fusionwave']:
            valor_comision = peticiones_exitosas * 300
            if 2500 <= peticiones_no_exitosas <= 4500:
                descuento = valor_comision * 0.05  # Aplicar descuento del 5%
            elif peticiones_no_exitosas > 4500:
                descuento = valor_comision * 0.08  # Aplicar descuento del 8%

        valor_iva = valor_comision * iva
        valor_total = valor_comision + valor_iva - descuento
        
        results.append({
            'Fecha-Mes': 'Desde 2024-07-01 hasta 2024-08-31',
            'Nombre': commerce_name,
            'Nit': commerce_nit,
            'Valor_comision': valor_comision,
            'Valor_iva': valor_iva,
            'Descuento': descuento,
            'Valor_Total': valor_total,
            'Correo': row['commerce_email']
        })
    
    return pd.DataFrame(results)
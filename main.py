from constants import api_call_data
from database.query import load_commerce_api_call_data
from use_cases import calculate_commissions
from services import send_email

## Inicializa todo
data = load_commerce_api_call_data(api_call_data['start_date'], api_call_data['end_date'])
print(data.head())

comisitions = calculate_commissions(data)
print(comisitions)

# Envía los resultados por correo electrónico
send_email('resultado', 'ramirezyeison115@gmail.com')



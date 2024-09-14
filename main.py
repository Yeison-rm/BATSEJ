from constants import api_call_data
from database.query import load_commerce_api_call_data
from use_cases import calculate_commissions

## Inicializa todo
data = load_commerce_api_call_data(api_call_data['start_date'], api_call_data['end_date'])

print(data.head())

comisitions = calculate_commissions(data)

print(comisitions)
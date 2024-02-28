import requests
import json

# URL de la API de Square para crear un objeto en el catálogo
url = "https://connect.squareup.com/v2/catalog/object"

# Credenciales de autorización
headers = {
    'Authorization': 'sandbox-sq0csb-p6j01x0fhk_QhLYpD5yxZVTcl00v9evfU2Zr0dtl9z4',
    'Content-Type': 'application/json',
}

# Datos del nuevo producto
data = {
    "idempotency_key": "UNIQUE_ID",
    "object": {
        "type": "ITEM",
        "item_data": {
            "name": "Nombre del Producto",
            "description": "Descripción del Producto",
            "variations": [
                {
                    "type": "ITEM_VARIATION",
                    "item_variation_data": {
                        "name": "Variación del Producto",
                        "pricing_type": "FIXED_PRICING",
                        "price_money": {
                            "amount": 1000,  # Precio en centavos
                            "currency": "USD"
                        }
                    }
                }
            ]
        }
    }
}

# Envía la solicitud para crear el producto
response = requests.post(url, headers=headers, data=json.dumps(data))

# Imprime la respuesta del servidor
print(response.json())

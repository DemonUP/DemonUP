import os
import requests

HTB_TOKEN = os.getenv("HTB_TOKEN")
if not HTB_TOKEN:
    raise ValueError("No se encontró la variable de entorno 'HTB_TOKEN'.")

api_url = "https://app.hackthebox.com/api/v4/user/info"
headers = {
    "Authorization": f"Bearer {HTB_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(api_url, headers=headers)

# Imprimir código de estado y cuerpo de la respuesta para ver qué pasa
print("Status code:", response.status_code)
print("Response text:", response.text)

# Si no es 200, forzar excepción
if response.status_code != 200:
    raise Exception(f"Error al obtener datos de HTB: {response.status_code} - {response.text}")

data = response.json()  # Aquí ya hacemos el .json() solo si el status_code fue 200

# Continúa con tu lógica...
rank = data.get("rank", "N/A")
points = data.get("points", "N/A")
user_name = data.get("name", "N/A")

print("Rank:", rank)
print("Points:", points)
print("User:", user_name)

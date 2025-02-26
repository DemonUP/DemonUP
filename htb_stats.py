import os
import requests

# 1. Obtenemos el token desde la variable de entorno que inyectaremos en GitHub Actions
HTB_TOKEN = os.getenv("HTB_TOKEN")
if not HTB_TOKEN:
    raise ValueError("No se encontró la variable de entorno 'HTB_TOKEN'.")

# 2. Endpoint de la API v4 de Hack The Box para obtener información de TU usuario
#    (Si deseas usar tu Account Identifier, puedes usar: /api/v4/user/profile/<ACCOUNT_IDENTIFIER>)
api_url = "https://app.hackthebox.com/api/v4/user/info"

# 3. Encabezados para la autenticación
headers = {
    "Authorization": f"Bearer {HTB_TOKEN}",
    "Content-Type": "application/json"
}

# 4. Hacemos la solicitud GET a la API
response = requests.get(api_url, headers=headers)
if response.status_code != 200:
    raise Exception(f"Error al obtener datos de HTB: {response.status_code} - {response.text}")

# 5. Procesamos la respuesta JSON
data = response.json()

# Ejemplo de campos que podrías extraer (ajusta según la estructura que devuelva la API):
rank = data.get("rank", "N/A")
points = data.get("points", "N/A")
user_name = data.get("name", "N/A")

# 6. Generamos un archivo SVG sencillo con las estadísticas
svg_template = f"""
<svg width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="120" fill="#2d2d2d"/>
  <text x="10" y="30" fill="#00FF41" font-size="18">Hack The Box Stats</text>
  <text x="10" y="60" fill="#FFFFFF" font-size="16">User: {user_name}</text>
  <text x="10" y="80" fill="#FFFFFF" font-size="16">Rank: {rank}</text>
  <text x="10" y="100" fill="#FFFFFF" font-size="16">Points: {points}</text>
</svg>
"""

# 7. Guardamos el SVG en el repositorio
with open("htb_stats.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Archivo htb_stats.svg actualizado correctamente.")

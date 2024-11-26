import requests
import pandas as pd
import os
from dotenv import load_dotenv
import json

# Cargar el archivo .env
load_dotenv()

# Obtener la clave API desde el entorno
API_KEY = os.getenv("API_KEY")

# Variables para la consulta
league_id = 39
season = 2022

# URL de la API para obtener los máximos goleadores de la liga
url = "https://v3.football.api-sports.io/players/topscorers"

# Parámetros de la solicitud
params = {
    "league": league_id,
    "season": season
}

# Encabezados de la solicitud (API puede requerir una clave de autorización)
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

# Realizar la llamada a la API
try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error
    
    # Convertir la respuesta a JSON
    data = response.json()
    
    # Guardar el JSON en un archivo
    filename = f'topscorers_data_{season}.json'
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Datos de los goleadores guardados exitosamente en '{filename}'")
except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud: {e}")

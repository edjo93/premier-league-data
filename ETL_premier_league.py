import json
import pandas as pd

filename = "standings_data_2022.json"

# Cargar los datos guardados desde el archivo JSON
with open(filename, 'r') as json_file:
    data = json.load(json_file)

# Extraer los standings
standings = data['response'][0]['league']['standings'][0]

# Crear una lista de diccionarios para almacenar los datos relevantes
standings_data = []
for team in standings:
    standings_data.append({
        'Position': team['rank'],
        'Team': team['team']['name'],
        'MP': team['all']['played'],
        'W': team['all']['win'],
        'D': team['all']['draw'],
        'L': team['all']['lose'],
        'GF': team['all']['goals']['for'],
        'GA': team['all']['goals']['against'],
        'GD': team['goalsDiff'],
        'Pts': team['points'],
        'Last 5': team.get('form', "")
    })

# Crear un DataFrame con pandas
df = pd.DataFrame(standings_data)

# Mostrar el DataFrame
print(df)

import json
import pandas as pd
import streamlit as st

# Nombre del archivo JSON que contiene los datos de los standings
filename_standings = "standings_data_2022.json"
filename_topscorers = "topscorers_data_2022.json"

# Cargar los datos guardados desde el archivo JSON
with open(filename_standings, 'r') as json_file:
    data = json.load(json_file)

# Extraer los standings
standings = data['response'][0]['league']['standings'][0]

# Crear una lista de diccionarios para almacenar los datos relevantes
standings_data = []
for team in standings:
    standings_data.append({
        'Position': team['rank'],
        'Logo': team['team']['logo'],  # Agregar el logo del equipo
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

# Crear un DataFrame con pandas para los standings
df_standings = pd.DataFrame(standings_data)

# Cargar los datos de los máximos goleadores desde el archivo JSON
with open(filename_topscorers, 'r') as json_file:
    data_scorers = json.load(json_file)

# Extraer los datos de los máximos goleadores
scorers = data_scorers['response']

# Crear una lista de diccionarios para almacenar los datos relevantes de los goleadores
scorers_data = []
for player_data in scorers:
    player = player_data['player']
    statistics = player_data['statistics'][0]

    scorers_data.append({
        'Player': player['name'],
        'Team': statistics['team']['name'],
        'Goals': statistics['goals']['total'],
        'Assists': statistics['goals'].get('assists', 0),
        'Appearances': statistics['games'].get('appearences', 0),
        'Photo': player['photo']
    })

# Crear un DataFrame con pandas para los goleadores
df_scorers = pd.DataFrame(scorers_data)

# Crear la interfaz de Streamlit
st.title('Tabla de Posiciones - Premier League Temporada 2022')

# Mostrar la tabla de posiciones
if not df_standings.empty:
    # Añadir la columna de logos al DataFrame de forma visual en Streamlit
    df_standings['Logo'] = df_standings['Logo'].apply(lambda x: f'<img src="{x}" width="50">')
    st.write(df_standings.to_html(escape=False, index=False), unsafe_allow_html=True)
else:
    st.write("No se pudieron obtener los datos de la tabla de posiciones.")

# Mostrar la lista de los máximos goleadores
st.title('Máximos Goleadores - Temporada 2022')

if not df_scorers.empty:
    # Mostrar detalles individuales de cada goleador con una foto
    st.markdown("### Detalles de los Máximos Goleadores")
    for index, row in df_scorers.iterrows():
        st.markdown(f"#### {index + 1}. {row['Player']} - {row['Team']}")
        st.image(row['Photo'], width=100)
        st.markdown(f"- **Goles**: {row['Goals']}")
        st.markdown(f"- **Asistencias**: {row['Assists']}")
        st.markdown(f"- **Apariciones**: {row['Appearances']}")
        st.markdown("---")
else:
    st.write("No se pudieron obtener los datos de los goleadores.")

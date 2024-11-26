import json
import pandas as pd
import streamlit as st

# Nombre del archivo JSON que contiene los datos de los goleadores
filename = "topscorers_data_2022.json"

# Cargar los datos guardados desde el archivo JSON
with open(filename, 'r') as json_file:
    data = json.load(json_file)

# Extraer los datos de los máximos goleadores
scorers = data['response']

# Crear una lista de diccionarios para almacenar los datos relevantes de los goleadores
scorers_data = []
for player_data in scorers:
    player = player_data['player']
    statistics = player_data['statistics'][0]

    scorers_data.append({
        'Player': player['name'],
        'Team': statistics['team']['name'],
        'Goals': statistics['goals']['total'],
        'Assists': statistics['goals']['assists'],
        'Appearances': statistics['games']['appearences'],
        'Photo': player['photo']
    })

# Crear un DataFrame con pandas para los goleadores
df_scorers = pd.DataFrame(scorers_data)

# Crear la interfaz de Streamlit
st.title('Máximos Goleadores - Temporada 2022')

# Mostrar la lista de los máximos goleadores
if not df_scorers.empty:
    # Mostrar la información en una tabla
    st.dataframe(df_scorers)

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

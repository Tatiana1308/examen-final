import pandas as pd
import folium
from folium.plugins import HeatMap

# Cargar datos de población de Cundinamarca
cundinamarca_data = pd.read_csv('cundinamarca_poblacion.csv')

# Crear mapa coroplético de Cundinamarca
cundinamarca_map = folium.Map(location=[4.6, -74.1], zoom_start=8)

# Agregar capa de población a la mapa
folium.Choropleth(
    geo_data=open('cundinamarca_municipios.geojson').read(),
    data=cundinamarca_data,
    columns=['Municipio', 'Población'],
    key_on='feature.properties.NOMBRE_MUNICIPIO',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Población'
).add_to(cundinamarca_map)

# Mostrar mapa
cundinamarca_map

# Cargar datos de centroides de Tolima
tolima_data = pd.read_csv('tolima_centroides.csv')

# Crear mapa de centroides de Tolima
tolima_map = folium.Map(location=[3.7, -75.2], zoom_start=8)

# Agregar capa de centroides a la mapa
for index, row in tolima_data.iterrows():
    folium.CircleMarker(
        location=[row['Latitud'], row['Longitud']],
        radius=5,
        color='red',
        fill=True,
        fill_opacity=0.5
    ).add_to(tolima_map)

# Mostrar mapa
tolima_map
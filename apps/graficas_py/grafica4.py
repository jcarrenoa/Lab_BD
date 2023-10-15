import streamlit as sl
import pandas as pd
import plotly as plt
import plotly.express as px
import pyodbc

def app(connection):

    sl.title("Grafica del numero de accidentes con respecto a su severidad")
    with sl.form("my_form", clear_on_submit=True):
        # TODO:
        x = sl.selectbox('Selecciona un estado', ["Sin Severity", 1, 2, 3], key='estado_key')
        sub = sl.form_submit_button(label='Aceptar')

    #Se pone como predeterminado sin severity y que tmbn sea una opcion
    if sub:
        if x == "Sin Severity":
            query = '''
                SELECT State, count(State) As Num_accidentes 
                FROM Accidents 
                GROUP BY State
            '''
        else:
            query = f'''
                SELECT State, count(State) As Num_accidentes
                FROM Accidents
                WHERE Severity = {x}
                GROUP BY State
            '''

        df = pd.read_sql_query(query, connection)

        fig = px.choropleth(
            df,
            locations='State',  # Columna con nombres de estados
            locationmode="USA-states",  # Define el modo de ubicación como Estados de EE. UU.
            color='Num_accidentes',  # Valores para colorear el mapa de calor
            scope="usa",  # Establece el alcance en Estados Unidos
            color_continuous_scale="YlOrRd",  # Puedes elegir otra escala de colores
            title=f'Número de accidentes por estado(Severidad: {x})',  # Título del gráfico
        )

        # Personaliza el diseño del gráfico
        fig.update_geos(
            showcoastlines=True,
            coastlinecolor="Black",
        )

        sl.plotly_chart(fig, use_container_width=True)

        sl.header("Dataframe generado:")
        
        sl.write(df)
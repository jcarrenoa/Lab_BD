import streamlit as sl
import pandas as pd
import plotly as plt
import plotly.express as px
import pyodbc

def app(connection, columnas):

    sl.title("Mapa de calor de correlación segun parametros escogidos")
    columnas = sl.multiselect('Selecciona las columnas', columnas)
    sl.header("Seleccionados: ")
    sl.write("{}".format(", ".join(columnas)))
    if len(columnas) != 0:
        query = f'''
            SELECT {"{}".format(", ".join(columnas))}
            FROM Accidents
            '''
        df = pd.read_sql_query(query, connection)
        correlation_matrix = df.corr()
        fig = px.imshow(correlation_matrix, x=correlation_matrix.columns, y=correlation_matrix.columns)
        fig.update_layout(title='Mapa de calor de correlación')
        sl.plotly_chart(fig, use_container_width=True)
        sl.header("Dataframe generado:")
        sl.write(df)
import streamlit as sl
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def app(connection, state_codes, state_names):
    sl.title("Grafica de accidentes segun el estado")
    x = ""
    with sl.form("my_form", clear_on_submit=True):
        # TODO:
        sl.selectbox('Selecciona un estado', list(state_codes.values()), key='estado_key')
        sub = sl.form_submit_button(label='Aceptar')

    if sub:
        x = str(sl.session_state["estado_key"])
    
        sl.write(x)

        if x in state_names:
            codigo_estado = state_names[x]

        if x == "":
            query = '''
                WITH Años(Start_Time, Years) AS
                (
                SELECT Start_Time, YEAR(Start_Time) AS Years FROM Accidents
                )

                SELECT distinct MONTH(Start_Time) AS mes,Years AS AÑO, count(*) OVER (PARTITION BY Years ORDER BY MONTH(Start_Time)) AS Contador
                    FROM Años
                    ORDER BY Years ASC, mes ASC
            '''

        else:
            x = "'"+codigo_estado+"'"
            query = f'''
                WITH Años(Start_Time, Years) AS
                    (
                    SELECT Start_Time, YEAR(Start_Time) AS Years 
                        FROM Accidents
                        WHERE State = {x}
                    )

                SELECT distinct MONTH(Start_Time) AS mes,Years AS AÑO, count(*) OVER (PARTITION BY Years ORDER BY MONTH(Start_Time)) AS Contador
                    FROM Años
                    ORDER BY Years ASC, mes ASC
            '''

        df = pd.read_sql_query(query, connection)

        # Crear una columna "Mes_Año" que combine Mes y Año
        df['Mes_Año'] = df['mes'].astype(str) + '/' + df['AÑO'].astype(str)

        df = df.drop(['mes','AÑO'], axis=1)

        fig = px.line(df, x='Mes_Año', y='Contador', title='Número de accidentes por mes y año')

        sl.plotly_chart(fig, use_container_width=True)

        sl.header("Dataframe generado:")
        
        sl.write(df)

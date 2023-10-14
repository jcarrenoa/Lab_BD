import streamlit as sl
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def app(connection):
    query_1 = '''with paises(id_pais) as 
    (
        select distinct a.State
        from Accidents a
    )

    select *
    from paises p
    order by p.id_pais asc
    '''
    state_code = pd.read_sql_query(query_1, connection).to_numpy().tolist()
    state_codes = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
               'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'DC': 'District of Columbia',
               'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois',
               'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana',
               'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
               'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
               'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
               'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
               'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
               'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
               'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin',
               'WY': 'Wyoming'}
    #Crear un diccionario con el nombre de los estados y su respectivo codigo
    state_codes = {code[0]: state_codes[code[0]] for code in state_code}
    state_names = {v: k for k, v in state_codes.items()}
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
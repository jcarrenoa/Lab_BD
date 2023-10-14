import streamlit as sl
import pandas as pd
import plotly as plt
import plotly.express as px
import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=ARCCESS;DATABASE=US_Accidents;UID=sa;PWD=123456')
x = input('Ingreso del Estado:') #Valor que este en la barra de opciones

#Crear un diccionario con los codigos de los estados y su respectivo nombre
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
state_names = {v: k for k, v in state_codes.items()}

codigo_estado = ""  

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
fig.show()
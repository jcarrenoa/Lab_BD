import streamlit as sl
from streamlit_option_menu import option_menu
from apps.graficas_py import grafica1, grafica2, grafica3, grafica4
import pyodbc
import pandas as pd

def app(server, database, username, password):

    class MultiApp():

        def __init__(self, server, database, username, password):
            self.apps = []
            #Esta linea corresponde a la conexion a la base de datos de Azure con Python
            #self.connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=aaron02.database.windows.net;DATABASE=US_Accidents;UID=administrador;PWD=a123456@')

            #Esta linea corresponde a la conexion a la base de datos local con Python
            #self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER=ARCCESS;DATABASE=US_Accidents ;UID=sa;PWD=123456')
            
            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}'+f';SERVER={server};DATABASE={database};UID={username};PWD={password}')
            query_1 = '''with paises(id_pais) as 
            (
                select distinct a.State
                from Accidents a
            )

            select *
            from paises p
            order by p.id_pais asc
            '''
            state_code = pd.read_sql_query(query_1, self.connection).to_numpy().tolist()
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
            self.state_codes = {code[0]: state_codes[code[0]] for code in state_code}
            self.state_names = {v: k for k, v in self.state_codes.items()}
            query_columnas = '''select a.Humidity, a.Precipitation_in, a.Pressure_in, a.Severity, a.Temperature_F, a.Visibility_mi,
                                a.Wind_Chill_F, a.Wind_Speed_mph
                                from Accidents a'''
            self.columnas = pd.read_sql_query(query_columnas, self.connection).columns.tolist()

        def add_app(self, title, funtion):
            self.apps.append({"title": title, "funtion": funtion})

        def run(self, conection):

            with sl.sidebar:
                app = option_menu(
                    menu_title= None,
                    options= ['Grafica #1', 'Grafica #2', 'Grafica #3', 'Grafica #4'],
                    icons=['bar-chart-line-fill', 'bar-chart-line-fill', 'bar-chart-line-fill', 'bar-chart-line-fill'],
                    menu_icon = 'cast',
                    orientation = "vertical",
                    default_index=  0,
                )
            
            if app == "Grafica #1":
                grafica1.app(conection, self.state_codes, self.state_names)
            if app == "Grafica #2":
                grafica2.app(conection, self.state_codes, self.state_names)
            if app == "Grafica #3":
                grafica3.app(conection)
            if app == "Grafica #4":
                grafica4.app(conection, self.columnas)
              
    appr = MultiApp(server, database, username, password)
    appr.run(appr.connection)
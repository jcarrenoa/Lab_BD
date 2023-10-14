import streamlit as sl
import pyodbc
import pandas as pd
import numpy as np

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=US_Accidents ;UID=sa;PWD=123456')
query = '''with paises(id_pais) as 
(
	select distinct a.State
	from Accidents a
)

select *
from paises p
order by p.id_pais asc
'''
state_code = pd.read_sql_query(query, connection).to_numpy().tolist()
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
state_codes = {code[0]: state_codes[code[0]] for code in state_code}
state_names = {v: k for k, v in state_codes.items()}

def app():
    sl.title("Grafica del numero de accidenstes por estado")
    sl.text("Aqui va la grafica 1")
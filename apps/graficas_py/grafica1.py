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
    state_codes = {code[0]: state_codes[code[0]] for code in state_code}
    state_names = {v: k for k, v in state_codes.items()}
    sl.title("Grafica del numero de accidentes por estado")
    states = sl.multiselect('Selecciona los estados', list(state_codes.values()), default=list(state_codes.values()))
    sl.header("Seleccionados: ")
    if len(states) == 0:
        states_string = "p.id_estado is null      "
    else:
        states_string = ""
    for state in states:
        states_string = states_string + f"p.id_estado = \'{state_names[state]}\' or "
    states_string = states_string[:-4]
    sl.write("{}".format(", ".join(states)))
    query_count = f'''
            with countAccidents(id_estado, contado) as 
        (
        	select distinct a.State, count(a.State)
        	from Accidents a
        	group by a.State
        )

        select *
        from countAccidents p
        where {states_string}
        order by p.contado desc
    '''
    count = pd.read_sql_query(query_count, connection)
    fig = go.Figure()
    fig = fig.add_trace(go.Bar(x=count["id_estado"], y=count["contado"], orientation='v', name='Grafica Num. Accidentes'))

    sl.plotly_chart(fig, use_container_width=True)

    sl.header("Dataframe generado:")
    
    sl.write(count)
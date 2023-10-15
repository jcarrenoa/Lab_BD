import streamlit as sl
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def app(connection, state_codes, state_names):  
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
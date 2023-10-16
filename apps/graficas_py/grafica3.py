import streamlit as sl
import pandas as pd
import plotly as plt
import plotly.express as px


def grafica3(connection, sub, x):
    if sub:
        if x == "Sin Severidad":
            query = '''
                WITH Horas(Hora) AS
                (SELECT DATEPART(HH, Start_Time) AS OnlyHour
                    FROM Accidents
                )

                SELECT Hora, count(Hora) AS Num_accidentes FROM Horas
                    GROUP BY Hora
                    ORDER BY Hora ASC
            '''
        else:
            query = f'''
                WITH Horas(Hora) AS
                (SELECT DATEPART(HH, Start_Time) AS OnlyHour
                    FROM Accidents
                    WHERE Severity = {x}
                )

                SELECT Hora, count(Hora) AS Num_accidentes FROM Horas
                    GROUP BY Hora
                    ORDER BY Hora ASC
            '''

        df = pd.read_sql_query(query, connection)

        # Crea un gráfico de barras
        fig = px.bar(df, x='Hora', y='Num_accidentes', title=f'Numero de accidentes por hora (Severidad: {x})')

        # Personaliza el gráfico si es necesario
        fig.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')))  # Personaliza el color de las barras
        fig.update_xaxes(title_text='Horas del día')  # Personaliza el título del eje X
        fig.update_yaxes(title_text='Número de accidentes')  # Personaliza el título del eje Y

        fig.update_xaxes(type='category')

        return fig, df


def grafica4(connection, sub, x, twi, message_j):
    #Se pone como predeterminado sin severity y que tmbn sea una opcion
    if sub:
        if x == "Sin Severidad":
            query_sev = f'''
                with dn (State, civil_twilight) as
                (
                	select a.State, a.Civil_Twilight
                	from Accidents a
                	where {twi}
                )

                SELECT a.State, count(a.State) As Num_accidentes
                FROM dn a
                GROUP BY a.State
                ORDER BY Num_accidentes desc
            '''
        else:
            query_sev = f'''
                with dn (State, civil_twilight) as
                (
                	select a.State, a.Civil_Twilight
                	from Accidents a
                	where {twi} and a.Severity = {x}
                )

                SELECT a.State, count(a.State) As Num_accidentes
                FROM dn a
                GROUP BY a.State
                ORDER BY Num_accidentes desc
            '''

        df = pd.read_sql_query(query_sev, connection)

        fig = px.choropleth(
            df,
            locations='State',  # Columna con nombres de estados
            locationmode="USA-states",  # Define el modo de ubicación como Estados de EE. UU.
            color='Num_accidentes',  # Valores para colorear el mapa de calor
            scope="usa",  # Establece el alcance en Estados Unidos
            color_continuous_scale="YlOrRd",  # Puedes elegir otra escala de colores
            title=f'Número de accidentes por estado (Severidad: {x}, Jornada: {message_j})',  # Título del gráfico
        )

        # Personaliza el diseño del gráfico
        fig.update_geos(
            showcoastlines=True,
            coastlinecolor="Black",
        )

        return fig, df

def app(connection):

    sl.title("Graficas segun la severidad del accidente")
    
    with sl.form("my_form", clear_on_submit=True):
        # TODO:
        x, twi = sl.columns(2)
        twi = sl.selectbox('Selecciona la jornada', ["Todos", "Noche", "Dia"], key='severidad_key')
        message_j = twi
        if twi == "Noche":
            twi = 'a.Civil_Twilight = \'Night\''
        elif twi == "Dia":
            twi = 'a.Civil_Twilight = \'Day\''
        else:
            twi = "a.Civil_Twilight = \'Day\' or a.Civil_Twilight = \'Night\' or a.Civil_Twilight = Null"
        x = sl.selectbox('Selecciona un estado de severidad', ["Sin Severidad", 1, 2, 3], key='estado_key')
        sub = sl.form_submit_button(label='Aceptar')

    if sub:
        
        fig3, df3 = grafica3(connection, sub, x)
        fig4, df4 = grafica4(connection, sub, x, twi, message_j)

        with sl.container():

            sl.plotly_chart(fig3, use_container_width=True)
            sl.plotly_chart(fig4, use_container_width=True)

        sl.header("Dataframe generado:")
            
        with sl.container():
            col1, col2 = sl.columns(2)
            col1.write("Dataframe de la grafica de numero de accidentes por hora:")
            col1.write(df3)
            col2.write("Dataframe de la grafica de numero de accidentes por estado:")
            col2.write(df4)
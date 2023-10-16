import streamlit as sl
from streamlit_option_menu import option_menu
from apps import inicio, graficas

#Titulo de la pagina
sl.set_page_config(
    page_title = "BD Lab #1",
)

#Variables de conexion a la base de datos
server = 'ARCCESS'
bd = 'US_Accidents '
password = '123456'
user = 'sa'

#Inicio de la aplicacion
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, funtion):
        self.apps.append({"title": title, "funtion": funtion})

    def run():

        #Menu principal (Inicio, Graficas)
        
        with sl.sidebar:
            app = option_menu(
                menu_title="Menu",
                options= ['Inicio', 'Graficas'],
                icons=['house-fill', 'bar-chart-line-fill'],
                menu_icon = 'chat-text-fill',
                default_index= 1,
                orientation = "horizontal",
            )

        if app == "Inicio":
            inicio.app()
        if app == "Graficas":
            graficas.app(server, bd, user, password)
                         
    run()
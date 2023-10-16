import streamlit as sl
from streamlit_option_menu import option_menu
from PIL import Image
from apps import inicio, graficas

sl.set_page_config(
    page_title = "BD Lab #1",
)

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
    #            styles={
    #                "container": {"padding": "5!important","background-color":'black'},
    #    "icon": {"color": "white", "font-size": "23px"}, 
    #    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
    #    "nav-link-selected": {"background-color": "#02ab21"},}
            )
        
        if app == "Inicio":
            inicio.app()
        if app == "Graficas":
            graficas.app()
                         
    run()
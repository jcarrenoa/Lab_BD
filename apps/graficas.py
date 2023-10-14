import streamlit as sl
from streamlit_option_menu import option_menu
from apps.graficas_py import grafica1, grafica2, grafica3, grafica4
import pyodbc

def app():

    class MultiApp:

        def __init__(self):
            self.apps = []
            self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER=ARCCESS;DATABASE=US_Accidents ;UID=sa;PWD=123456')

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
                grafica1.app(conection)
            if app == "Grafica #2":
                grafica2.app(conection)
            if app == "Grafica #3":
                grafica3.app()
            if app == "Grafica #4":
                grafica4.app()
                            
    appr = MultiApp()
    appr.run(appr.connection)
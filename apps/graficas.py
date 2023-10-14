import streamlit as sl
from streamlit_option_menu import option_menu

def app():
    sl.write("Graficas")
    sl.text("Aqui van las graficas")

    class MultiApp:

        def __init__(self):
            self.apps = []

        def add_app(self, title, funtion):
            self.apps.append({"title": title, "funtion": funtion})

        def run():

            with sl.sidebar:
                app = option_menu(
                    menu_title= None,
                    options= ['Grafica #1', 'Grafica #2', 'Grafica #3', 'Grafica #4'],
                    icons=['bar-chart-line-fill', 'bar-chart-line-fill', 'bar-chart-line-fill', 'bar-chart-line-fill'],
                    menu_icon = 'cast',
                    orientation = "vertical",
                    default_index=  0,
        #            styles={
        #                "container": {"padding": "5!important","background-color":'black'},
        #    "icon": {"color": "white", "font-size": "23px"}, 
        #    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        #    "nav-link-selected": {"background-color": "#02ab21"},}
                )
            
            if app == "Grafica #1":
                sl.text("1")
            if app == "Grafica #2":
                sl.text("2")
            if app == "Grafica #3":
                sl.text("3")
            if app == "Grafica #4":
                sl.text("4")
                            
        run()     
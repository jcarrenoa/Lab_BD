import streamlit as sl

def app():
    sl.title("Inicio")
    with sl.container():
        sl.header("Sobre el Laboratiorio realizado")
        sl.write(
            """
            El laboratorio realizado en Python utiliza las librerías Pandas, Streamlit, pyodbc y Plotly para crear una página web 
            interactiva que muestra gráficas basadas en datos de accidentes en los Estados Unidos. Los usuarios pueden explorar y 
            analizar estos datos de manera dinámica, aplicar filtros interactivos y obtener información detallada sobre la frecuencia y 
            naturaleza de los accidentes.    
            """
        )
    
    with sl.container():
        sl.write("---")
        text_column, image_column = sl.columns(2)
        with text_column:
            sl.header("Integrantes:")
            sl.write(
                """
                ➤ Arteta Sebastian\n
                ➤ Julio Luna\n
                ➤ Rodriguez Aaron\n
                """
            )

        with image_column:
            sl.empty()
    
    with sl.container():
        sl.write("---")
        sl.header("Profesor:")
        sl.write(
            """
            ➤ Paba Jimeno\n
            """
        )

    with sl.container():
        sl.write("---")
        sl.header("Librerias Utilizadas:")
        sl.write(
            """
            ➤ Pandas\n
            ➤ Plotly\n
            ➤ Streamlit\n
            ➤ Pyobdc\n
            """
        )
        sl.write("***NOTA: La version de python utilizada para este proyecto es la 3.10.10 por limitaciones de algunas dependencias de la libreria Streamlit***")

    with sl.container():
        sl.write("---")
        sl.header("Recursos web:")
        sl.write(
            """
            ➤ Data set: Sobhan Moosavi. (2023). *US Accidents (2016 - 2023)* [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DS/199387\n
            ➤ Repositorio: https://github.com/jcarrenoa/Lab_BD.git
            """)

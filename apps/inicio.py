import streamlit as sl

def app():
    sl.title("Inicio")
    with sl.container():
        sl.header("Sobre el Laboratiorio realizado")
        sl.write(
            """
            En este laboratiorio hecho para la materia "Base de datos"
            se pueden apreciar el uso de muchos recursos para su respectiva realizacion     
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

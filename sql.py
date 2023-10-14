import pyodbc
import pandas as pd

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=US_Accidents ;UID=sa;PWD=123456')
query = '''WITH Horas(Hora) AS
	(SELECT DATEPART(HH, Start_Time) AS OnlyHour 
		FROM Accidents
	)

SELECT Hora, count(Hora) AS Contador FROM Horas
	GROUP BY Hora
	ORDER BY Hora ASC
'''
df = pd.read_sql_query(query, connection)
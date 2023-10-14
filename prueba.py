import pyodbc
import pandas as pd

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=US_Accidents ;UID=sa;PWD=123456')
query = '''with paises(id_pais) as 
(
	select distinct a.State
	from Accidents a
)

select *
from paises p
order by p.id_pais asc
'''
df = pd.read_sql_query(query, connection)
print(df.head())
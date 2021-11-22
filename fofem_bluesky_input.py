# -*- coding: utf-8 -*-
"""fofem_bluesky_input.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qe3Zv3bln1fAiNagVTRfw5e_e3o3Qck4
"""

!pip install pyodbc
!pip install pandas
import pyodbc
import pandas

# Commented out IPython magic to ensure Python compatibility.
# %%sh
# curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
# sudo apt-get update
# sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=content/postprocess_2020_CC_for_MW.mdb;')
cursor = conn.cursor()
rows = cursor.execute('select * from FOF_FCCS_67')
df = pandas.DataFrame([tuple(t) for t in rows])
print(df)
# can also access the pyodbc data as follows:
# cursor.execute('select * from FOF_FCCS_67')
# for row in cursor.fetchall():
#     print (row)
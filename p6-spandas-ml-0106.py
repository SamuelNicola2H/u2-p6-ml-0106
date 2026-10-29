import pandas as pd
import numpy as np

serie_amigos=["Pedro","Morgan","Farfan","El Adrian","Jesse","Nava","Mario"]
print("--- Serie listado de amigos NC 0106 ---")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("--- Serie listado valor de billetes MX NC 0106 ---")
dinero=pd.Series(serie_billetes)
print(dinero)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["Veinte","Cincuenta","Cien","Doscientos","Quinientos","Mil"]
print("--- Serie listado nombre y valor de billetes MX NC 0106 ---")
tablabilletes=pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)

# Diccionario DataFrame
# Diccionario de valor monedas y nombre
print("--- Datos de diccionario a DataFrame en pandas ---")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["Veinte","Cincuenta","Cien","Doscientos","Quinientos","Mil"]
}

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)
print("Casa de cambio de Samuel Nicola NC 0106")
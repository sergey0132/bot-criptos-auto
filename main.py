import time 
from datetime import datetime
from funcion_coger_datos import obtener_precios_cripto
from SaveFunction import save_as_sql
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

if __name__ == "__main__":
    
    print("🤖 Iniciando robot de criptomonedas...")
    
    # BUCLE INFINITO

    # 1. Ejecutamos tu función
    df = obtener_precios_cripto()
    """
    Funcion que nos recoge los datos con API, y ahi es donde añadimos o quitamos monedas que nos interesan
    """
   
    if df is not None:
        print(f"✅ Datos guardados a las {datetime.now()}")
        save_as_sql(df, name='Cripto_information', place="sqlite:///criptos.db")
        """ 
        Una funcion que guarda y añade nueva informacion en formato SQL
        """
    else:
        print('❗ ERROR')

        

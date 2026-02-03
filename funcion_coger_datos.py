import requests
import pandas as pd
from datetime import datetime

def obtener_precios_cripto():
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # ⚠️ Voy a poner una URL falsa abajo para PROVOCAR un error y que veas el resultado
    # url = "https://api.coingecko.com/esta_pagina_no_existe" 
    
    mis_parametros = {
        'ids': 'bitcoin,ethereum,solana,ripple,Dogecoin',
        'vs_currencies': 'eur',
        'include_last_updated_at': 'true'
    }

    print("📡 Conectando a la API...")

    try:
        respuesta = requests.get(url, params=mis_parametros)
        respuesta.raise_for_status()
        
        datos = respuesta.json()
        
        lista_filas = []
        for moneda, info in datos.items():
            fila = {
                'cripto': moneda,
                'precio_eur': info['eur'],
                'fecha_extraccion': datetime.now()
            }
            lista_filas.append(fila)

        return pd.DataFrame(lista_filas)

    # AQUÍ ESTÁ EL CAMBIO 👇
    # Capturamos 'Exception' que es la madre de todos los errores para ver cualquiera
    except Exception as error:
        
        # 1. Sacamos el TIPO de error (La "Clase")
        tipo_de_error = type(error).__name__
        
        # 2. Imprimimos el reporte técnico
        print("\n🚨 --- DIAGNÓSTICO DE ERROR ---")
        print(f"📛 Tipo (Class): {tipo_de_error}")
        print(f"📝 Mensaje: {error}")
        
        # Esto es súper útil para un Data Engineer:
        if tipo_de_error == 'ConnectionError':
            print("💡 Consejo: Revisa tu conexión a internet.")
        elif tipo_de_error == 'HTTPError':
            print("💡 Consejo: La URL existe, pero el servidor nos rechazó (404, 500, etc).")
            
        return None

if __name__ == "__main__":
    df = obtener_precios_cripto()
    if df is not None:
        print(df)
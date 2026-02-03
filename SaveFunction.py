from sqlalchemy import create_engine
import pandas as pd

def save_as_sql(df,name,place):
        # 1. Tu conexión (La tubería)
        engine = create_engine(place)

        # 2. Supongamos que ya tienes tus tablas limpias del paso anterior
        # df_clientes (con su primary key generada)
        # df_ventas (con su foreign key correcta)

        # 3. GUARDADO DIRECTO (Sin tocar el disco duro)
        df.to_sql(
            name=name,       # Nombre de la tabla en SQL
            con=engine,             # La conexión
            if_exists='append',     # 'fail', 'replace' o 'append' (Añadir al final)
            index=False             # Importante: No guardes el índice de Pandas (0,1,2...) si no lo necesitas
        )

        print("¡Datos inyectados directamente en la vena de SQL!")
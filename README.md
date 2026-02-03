# bot-criptos-auto
# 🪙 Crypto ETL Pipeline: Automated Data Ingestion

## 📋 Descripción del Proyecto
Este proyecto implementa un pipeline **ETL (Extract, Transform, Load)** automatizado que monitoriza y extrae precios de criptomonedas en tiempo real.

El sistema se conecta a la API pública de **CoinGecko**, procesa y limpia los datos utilizando **Pandas**, y los historiza automáticamente en una base de datos relacional **SQLite**. Este repositorio está diseñado para ser la base de un sistema de análisis financiero, permitiendo la integración posterior con herramientas de BI (como Power BI o Tableau) o modelos de predicción.

## 🚀 Características Principales
* **Extracción Automatizada:** Conexión robusta a API externa con manejo de errores (timeouts, códigos HTTP).
* **Transformación de Datos:** Limpieza y estandarización de formatos JSON a estructuras tabulares mediante Pandas.
* **Persistencia:** Almacenamiento histórico incremental en SQLite (`.db`).
* **Configurable:** Permite ajustar fácilmente las monedas a rastrear y la frecuencia de actualización.

## 🛠️ Tecnologías Utilizadas (Tech Stack)
* **Lenguaje:** Python 3.10+
* **Manipulación de Datos:** Pandas
* **Conexión API:** Requests
* **Base de Datos / ORM:** SQLite / SQLAlchemy
* **Fuente de Datos:** CoinGecko API
* **Tiempo: ** Datetime


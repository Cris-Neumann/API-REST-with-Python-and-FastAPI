<h1 align="center"> API REST construída con framework FastAPI y web server Uvicorn </h1>

## Índice

- [Resumen del proyecto](#Resumen-del-proyecto)
- [Arquitectura empleada](#Arquitectura-empleada)
- [Instalaciones adicionales](#Instalaciones-adicionales)

## Resumen del proyecto
Este proyecto de API (Application Programming Interface) fue construido con el framework FastAPI, y extrae información desde un servidor seleccionado, cuyos datos están almacenada en una base de datos SQL Server, conectando a dicho origen de datos y creando modelos de tablas a través de la librería de Python SQLAlchemy, definiendo esquemas para validación con la librería de Python Pydantic, estableciendo algunas operaciones de ruta como ejemplo, para posteriormente conectar con un servidor web Uvicorn, a través del cual el cliente puede ejecutar peticiones de datos, las cuales son testeadas con la extensión de VSCode Thunder Client. Para autenticarse y autorizar usuarios de la API de manera segura, se utiliza el protocolo de autorización OAuth 2.0 y el estándar JSON Web Token (JWT) a modo de ejemplo.

## Arquitectura empleada
El esquema general del modo en que se relacionan las partes del sistema es el siguiente:
<br/><br/>

![python_and_fastapi](https://github.com/Cris-Neumann/API-REST-with-Python-and-FastAPI/assets/99703152/d16d178f-6cdc-4a40-b23f-c2e3653423bd)

## Instalaciones adicionales
Adicional a las librerías detallas en archivo requirements.txt, es necesario instalar el conector ODBC (Open Database Connectivity) para SQL Server: ODBC Driver 18: https://acortar.link/lsyUnp.

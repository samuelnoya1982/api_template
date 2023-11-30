# Libreías a importar
from flask import Flask # es un microframework para el desarrollo web en Python.
from flask_restful import Api # extensión para Flask que añade soporte para crear APIs RESTful.
from flask_sqlalchemy import SQLAlchemy # extensión que añade soporte para SQLAlchemy a Flask. 
from dotenv import load_dotenv, find_dotenv # dotenv es una librería que permite cargar variables de entorno desde un archivo .env.
from flask_jwt_extended import JWTManager
import os # es una librería incorporada en Python para interactuar con el sistema operativo
# SI SE VA A OCUPAR EN GCP AGREGAR ESTAS DOS TAMBIEN

from google.cloud import logging
from flask_cors import CORS


# INICIACION DE LAS VARIABLES DE ENTORNO QUE CONTIENE EL ARCHIVO .env 
load_dotenv()

# CREACION DE LA APLICACIÓN FLASK 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("CONEXION")

# CREACION DE INSTANCIAS
db = SQLAlchemy(app) 
api = Api(app)


"""Aquí vienen todos los endpoints de la api. Tendremos un endpoint por cada recurso y a su vez una clase por cada 
recurso."""

from api.recursos.recursos import *
api.add_resource(Recurso_1, "/enpoint_1")  
api.add_resource(Recurso_2, "/enpoint_2")  


# ------------------------------------------ SI FUESE UN ENTORNO EN GCP REEMPLAZAR POR -----------------------------------
"""
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'api/credenciales/credenciales.json'
load_dotenv()

# SETEO EL LOGGING DE GCP PARA SER USADO POR LA APLICACION
client = logging.Client()
logger = client.logger(os.environ["LOG"])

# FLASK
app = Flask(__name__)
CORS(app)

# CONEXION DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("CONEXIONDB")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_KEY") # SOLO SI SE USAN TOKENS
app.config['CORS_HEADERS'] = 'Content-Type'
jwt = JWTManager(app) # SOLO SI SE USAN TOKENS
db = SQLAlchemy(app)
api = Api(app)

from api.recursos.recursos import *
api.add_resource(Recurso_1, "/enpoint_1")
api.add_resource(Recurso_2, "/enpoint_2")    

"""
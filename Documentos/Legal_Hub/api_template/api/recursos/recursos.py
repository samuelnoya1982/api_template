from api.modelos.orm_1 import Tabla
from flask_restful import Resource
from sqlalchemy import text
from api import db
import pandas as pd
import json

class Recurso_1(Resource):

    def get (self):
        sql="CALL ProcedureUno()"
        df = pd.read_sql_query(sql,con=db.engine)
        if len(df)>0: 
            buff=df.to_json(orient='records') 
            procedureUno=json.loads(buff)
            return procedureUno
        else:
            return {"Warning:":"No hay datos disponibles"}      


class Recurso_2(Resource):

    def get (self):
        sql="CALL ProcedureDos()"
        df = pd.read_sql_query(sql,con=db.engine)
        if len(df)>0: 
            buff=df.to_json(orient='records') 
            procedureDos=json.loads(buff)
            return procedureDos
        else:
            return {"Warning:":"No hay datos disponibles"}      


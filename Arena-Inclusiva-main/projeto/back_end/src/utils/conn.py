import os
import secrets

from dotenv import load_dotenv
from fastapi import Depends, HTTPException 
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.utils.logger import setup_logger

import mysql.connector as mysql

load_dotenv()
Security = HTTPBearer()
logger = setup_logger(__name__)




class Connection:
    
    @staticmethod
    def get_connect():

        try:
            connection = mysql.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database=os.getenv("DB_NAME")
            )

            return connection
        
        except Exception as e:

            logger.error(f"Erro ao conectar ao MySQL: {e}")

            raise Exception("Erro ao conectar ao banco de dados")
            
    # def token(authorization: HTTPAuthorizationCredentials = Depends(Security)):

    #     expected = os.getenv("TOKEN", "")

    #     if authorization is None or not secrets.compare_digest(authorization.credentials, expected):

    #         logger.error("Token inválido")

    #         raise HTTPException(status_code=401, detail="Token inválido")
        
    #     return True
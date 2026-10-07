from fastapi import HTTPException
from mysql.connector import errorcode

from src.utils.logger import setup_logger
import mysql.connector as mysql

logger = setup_logger(__name__)

class Queries:

    @staticmethod
    def insert(connection: mysql.connection.MySQLConnection, sql: str, params):
        try:

            cur = connection.cursor(dictionary=True)

            if params is not None:
                cur.execute(sql, params)
            else:
                cur.execute(sql)  

            connection.commit()

            return True

        except mysql.Error as e:
        
            logger.error(f"Erro ao inserir dados: {e}")

            if e.errno == errorcode.ER_DUP_ENTRY:
                raise HTTPException(status_code=409, detail="Este registro já existe.")
            
            raise HTTPException(status_code=500, detail=f"Erro ao inserir dados no banco de dados{e.msg}")
        
        except Exception as e:
    
            logger.error(f"Erro genérico: {e}")
            raise HTTPException(status_code=500, detail=f"Erro interno no servidor: {e.msg}")
        
        finally:

            if 'cur' in locals(): 
                cur.close()
    
            connection.close()
from conexion import Conexion

class CursorPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def __enter__(self):
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor
    
    def __exit__(self, exception_type , exception_value, exception_traceback):
        if exception_value:
            self.__conn.rollback()
        else:
            self.__conn.commit()
            self.__cursor.close()
        self.__conn.close()
import mysql.connector.pooling as pool


class Conexion:
    __HOST = '127.0.0.1'
    __USER = 'root'
    __PASSWORD = 'Pa$$w0rd'
    __DATABASE = 'python_mysql'
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.MySQLConnectionPool(
                        pool_size=cls.__MAX_CON, 
                        pool_name='my_pool',  
                        host=cls.__HOST,
                        user=cls.__USER,
                        passwd=cls.__PASSWORD,
                        database=cls.__DATABASE
                    )
                return cls.__pool
            except Exception as e:
                print(e)
        else:
            return cls.__pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_connection()
        return conexion

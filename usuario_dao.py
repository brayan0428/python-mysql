from cursor_pool import CursorPool
from usuario import Usuario

class UsuarioDAO:
    __SELECCIONAR = 'select * from usuarios order by id'
    __INSERTAR = 'insert into usuarios (username,password) values(%s, md5(%s))'
    __ACTUALIZAR = 'update usuarios set username = %s, password = md5(%s) where id = %s'
    __ELIMINAR = 'delete from usuarios where id = %s'

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for r in registros:
                usuario = Usuario(r[0], r[1], r[2])
                usuarios.append(usuario)
            return usuarios
    @classmethod    
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            cursor.execute(cls.__INSERTAR, (usuario.get_username(), usuario.get_password()))
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            cursor.execute(cls.__ACTUALIZAR, (usuario.get_username(), usuario.get_password(), usuario.get_id_usuario()))
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, id):
        with CursorPool() as cursor:
            cursor.execute(cls.__ELIMINAR, (id,))
            return cursor.rowcount
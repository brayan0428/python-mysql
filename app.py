from usuario_dao import UsuarioDAO
from usuario import Usuario

def validarOpcion(opcion):
    if opcion == 1:
       listarUsuarios()
    if opcion == 2:
        insertarUsuario()
    if opcion == 3:
        actualizarUsuario()
    if opcion == 4:
        eliminarUsuario()
    print('\n')


def listarUsuarios():
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        print(usuario)

def insertarUsuario():
    username = input("Ingrese el username: ")
    password = input("Ingrese el password: ")
    usuario = Usuario(username=username,password=password)
    usuarios_insertados = UsuarioDAO.insertar(usuario)
    print(f'Usuarios insertados: {usuarios_insertados}')

def actualizarUsuario():
    id = input("Ingrese el id del usuario: ")
    username = input("Ingrese el username: ")
    password = input("Ingrese el password: ")
    usuario = Usuario(id,username,password)
    usuarios_actualizados = UsuarioDAO.actualizar(usuario)
    print(f'Usuarios actualizados: {usuarios_actualizados}')

def eliminarUsuario():
    id = input("Ingrese el id del usuario: ")
    usuarios_eliminados = UsuarioDAO.eliminar(id)
    print(f'Usuarios eliminados: {usuarios_eliminados}')

if __name__ == "__main__":
    opcion = 0
    while opcion != 5:
        print (
            f'Seleccione una opción: \n'
            f'  1 - Listar Usuario \n'
            f'  2 - Insertar Usuario \n'
            f'  3 - Actualizar Usuario \n'
            f'  4 - Eliminar Usuario \n'
            f'  5 - Salir \n'
        )
        opcion = int(input("Ingrese la opción (1-5): "))
        validarOpcion(opcion)
# -*- coding: utf-8 -*-

def protected(func):
    def wrapper(password):

        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper


@protected
def protected_fund():
    print('Tu contraseña es corecta.')




if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))

    protected_fund(password)

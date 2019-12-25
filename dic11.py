# -*- coding: utf-8 -*-
import random


def run():
    number_found = False
    i = int(raw_input("Ingresa un número: "))
    j = int(raw_input("Ingresa un número mayor: "))
    random_number = random.randint(i, j)

    while not number_found:
        number = int(raw_input("Intenta adivinar un número: "))

        if number == random_number:
            print("Felicidades, adivinaste el numero")
            number_found = True
        elif number > random_number:
            print("El número es mas pequeño")
        else:
            print("El número es más grande")




if __name__ == '__main__':
        run()

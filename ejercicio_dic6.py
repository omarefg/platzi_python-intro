# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print("C A L C U L A D O R A   D E  D I V I S A S")
    print("Convierte pesos mexicanos a pesos Colombianos.")
    print("")

    ammount = float(raw_input("Ingresa la cantidad de pesos Mexicanos que quieres convertir"))

    result = foreign_exchange_calculator(ammount)
    print("${} pesos Mexicanos son ${} pesos Colombianos".format(ammount, result))
    print("")

if __name__ == "__main__":
    run()

# -*- coding: utf-8 -*-



#               otra manera de lograr el ejercicio
#def palindrome2(word):
#    reversed_word = wod[::-1]
#
#   if reversed_word == word
#       return True
#
#   return False
#
#
#
#


def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)


    reversed_word = "".join(reversed_letters)

    if reversed_word == word:
        return True

    return False




if __name__ == '__main__':
    word = str(raw_input("Escribe una palabra: "))

    result = palindrome(word)

    if result is True:
        print("{} sí es un palíndromo.".format(word))
    else:
        print("{} no es un palíndromo.".format(word))

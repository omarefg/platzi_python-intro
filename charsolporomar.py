# -- coding: utf-8 --

'''
'abacabad' c
'abacabaabacaba' _
'abcdefghijklmnopqrstuvwxyziflskecznslkjfabe' d
'bcccccccccccccyb' y
'''

def first_not_repeating_char(char_sequence):
    pass

def first_not_repeating_char_without_tuples(char_sequence):
    chars = list(char_sequence)
    repeated_chars = []
    non_repeated_char = '_'

    for index, char in enumerate(chars):
        if chars.index(char) != index:
            repeated_chars.append(char)

    for char in chars:
        try:
            repeated_chars.index(char)
        except ValueError:
            non_repeated_char = char
            break

    return non_repeated_char



if __name__ == '_main_':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char_without_tuples(char_sequence)
    print(result)
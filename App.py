import re, os, sys; 

symbol_regex = re.compile(r'[!@#$%^&*(),.?:{}|<>]')
number_regex = re.compile(r'[0-9]')

def printMenu():
    os.system('cls')
    checked = True

    while checked:
        print("Ingresa una opción para correr el programa que desees...")
        print("1 - Validación de un palindromo")
        print("2 - Identificar parentisis balanceados")
        print("3 - Invertir el orden de las palabras")
        print("4 - Salir del programa\n")
        selection = input()
        if selection == "" or not(1 <= int(selection) <= 4):
            checked = True
            input("Debes ingresar una opcion correcta. Toca una tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            checked = False
            if selection == "1":
                print("Hola, ingresa una palabra para saber si es, o no un palindromo...\n")                   
                word = input()
                result = palindromeValidation(word)
                print(result)
                input("Presiona una tecla para continuar...")
                printMenu()
            elif selection == "2":
                print("Hola, ingresa un texto con parentesis, para saber si estos estan balanceados o no...\n")
                text = input()
                result = pairParenthesisControl(text)
                print(result)
                input("Presiona una tecla para continuar...")
                printMenu()
            elif selection == 3:
                print("Hola, ingresa un texto a ver si lo podemos invertir!\n")
                input_text = input()
                print("\n\nTexto Invertido: \n")
                reverseText(input_text)
                input("Presiona una tecla para continuar...")
                printMenu()
            else: 
                print("Gracias por darme la oportunidad")
                sys.exit()


def palindromeValidation(word):
    if(word == ""):
        print("Deberías ingresar una palabra");
        return False
    elif (len(word) <= 1):
        print("Debes ingresar una palabra... No una letra.")
        return False
    elif(word.count(" ") > 0):
        print("Parece que estas escribiendo más de una palabra...")
        return False
    elif(number_regex.search(word)):
        print("No podes ingresar caracteres raros")
        return False
    elif(symbol_regex.search(word)):
        print("No podes poner numeros...")
        return False
    else:
        word_list = [character for character in word]
        word_list_reverse = word_list[::-1]
        if (word_list == word_list_reverse):
            return True
        else: 
            return False


def pairParenthesisControl(text):
    parenthesis_list = [c for c in text if c == "(" or c == ")"]
    list_check = [parenthesis_list[i] for i in range(0, len(parenthesis_list), 2)]
    if all(e == list_check[0] for e in list_check):
        return True
    else:
        return False

def reverseText(text):
    if not text:
       print("Debes ingresar un texto válido")
    elif number_regex.search(text):
        print("No podes ingresar numeros...")
    else: print(text.split(" ")[::-1])


printMenu()

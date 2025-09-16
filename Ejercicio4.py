def mayus(cadena):

    contador =  0

    #Recorre la cadena y verifica si es mayuscula, si lo es suma 1 al contador
    for i in cadena:
        if i.isupper(): contador += 1

    return contador


def main():
    cadena = input("Ingrese una cadena de caracteres: ")

    print("La cadena tiene ", mayus(cadena), " caracteres mayusculas")



if __name__ == "__main__":
    main()

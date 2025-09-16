def filtrar_palabras(lista, n):

    for i in range(len(lista)):
        #compruebo si la longitud de la palabra es mayor que n
        if len(lista[i]) > n:
            print(lista[i])



def main():
    lista = ["hola", "adios", "coche", "moto", "avion", "helicoptero"]
    #Numero de letras por el cual se filtra
    n = 6
    filtrar_palabras(lista, n)


if __name__ == '__main__':
    main()
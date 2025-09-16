def mas_larga(list):

    num_letras = 0

    #Guarda la palbra mas larga
    palabra_larga = ""

    #Recorre toda la lista de palabras
    for i in range(0, len(list)):
        palabra = list[i]

        #Cuenta el numero de letras de la palabra
        letras = len(palabra)

        if letras > num_letras:
            num_letras = letras
            palabra_larga = list[i]

    return palabra_larga




def main():


    list_words = ["hola", "adios", "coche", "moto", "avion", "helicoptero"]


    palabra_larga = mas_larga(list_words)

    print("La palabra mas larga es: " , palabra_larga)




if __name__ == "__main__":
    main()
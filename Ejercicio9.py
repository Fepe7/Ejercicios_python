from itertools import count


def contar_vocales(palabra):
    contador_a = palabra.count("a")
    contador_e = palabra.count("e")
    contador_i = palabra.count("i")
    contador_o = palabra.count("o")
    contador_u = palabra.count("u")

    print("Tiene " , contador_a , " vocales a")
    print("Tiene " , contador_e , " vocales e")
    print("Tiene " , contador_i , " vocales i")
    print("Tiene " , contador_o , " vocales o")
    print("Tiene " , contador_u , " vocales u")




def main():
    palabra = input("Ingrese una palabra: ")

    contar_vocales(palabra)



if __name__ == "__main__":
    main()
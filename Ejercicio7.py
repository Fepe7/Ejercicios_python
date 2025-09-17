# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con
# la letra a.
# También se puede hacer elegir al usuario la letra a buscar. (Un poco mas
# emocionante)




def main():


    nombres = ["Ana", "Luis", "Alberto", "Maria", "Antonio", "Beatriz", "Alicia"]

    #Transforma la letra en mayuscula para que no haya problemas al comparar
    letra = input("Ingrese la letra a buscar: ").upper()


    contador = 0
    for nombre in nombres:
        #Mira si tiene la letra al principio, al tener find, y haberla pasado a mayuscula, no habra problemas
        if letra == nombre[0]:
            contador += 1


    print("Esta es la lista de nombres: ")
    print(nombres)
    print("La cantidad de nombres que hay con esa letra es: " , contador)


if __name__ == "__main__":
    main()


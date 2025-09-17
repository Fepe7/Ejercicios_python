def main():


    edades  = []
    mayores_20 = []

    for i in range(10):
        #Pregunta la edad y la introduce en la lista
        edades.append(int(input("Ingrese la edad de la persona " +str(i+1) + ": ")))


    #Recorre la lista y elimina las edades menores a 20
    for i in range(len(edades)):
        if edades[i] > 20:
            mayores_20.append(edades[i])

    #Imprime la lista final
    print("La cantidad de personas mayores de 20 es de: " , len(mayores_20))




if __name__ == "__main__":
    main()

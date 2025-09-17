def main():


    n_binario = input("Ingrese un numero binario: ")


    resultado = 0

    for i in range(len(n_binario)):
        if n_binario[i] == "1":
            #Segun la posicion del 1 se sube a la potencia de su posicion
            #Cuando se resta 1 a uno lo que hacemos es convertir el orden del indice de derecha a izquierda, tal y como se hace en binario
            resultado += 2**(len(n_binario)-1-i)

    print(resultado)

if __name__ == "__main__":
    main()

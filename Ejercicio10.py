def es_bisiesto(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        return True
    else:
        return False


def main():
    year = int(input("Ingrese un año: "))

    if es_bisiesto(year):
        print("El año ",  year, " es bisiesto")
    else:
        print("El año ",  year, " no es bisiesto")




if __name__ == "__main__":
    main()
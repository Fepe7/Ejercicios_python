

def max_in_list(list):

    n = 0

    for i in range(len(list)):
        if list[i] > n:
            n = list[i]


    return n




def main():


    list = [1134,22,363,423,521,65,723,81,941,12,323,423,123,123]


    print("Esta es la lista: ")
    print(list)

    print()

    print("El numero mas grande es: " , max_in_list(list))


if __name__ == '__main__':
    main()



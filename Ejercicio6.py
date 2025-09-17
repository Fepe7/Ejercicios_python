def main():
    year = int(input("Ingrese el año del curso: "))

    alumnos = []

    for i in range(3):
        name = input("Ingrese el nombre del estudiante: ")
        year_nac = int(input("Ingrese el año de nacimiento: "))
        #Crea persona
        persona = Persona(name, year_nac)
        #Lo mete en alumnos
        alumnos.append(persona)

    for i in range(len(alumnos)):
        edad = year - alumnos[i].year_nac
        print(f"El alumno" ,  alumnos[i].name ,  "tiene " , edad,  "años")


class Persona:
    def __init__(self, name, year_nac):
        self.name = name
        self.year_nac = year_nac



if __name__ == "__main__":
    main()
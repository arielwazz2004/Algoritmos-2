#CRUD - diccionario

notas = {}

def agregarNota(notas, titulo, contenido):
    notas[titulo]=contenido
    
def verNotas(notas):
    if not notas:
        print("No se han agregado notas")
    else:
        for titulo, contenido in notas.items():
            print(f"{titulo} : {contenido}")      

def editarNota(notas,titulo, nuevoContenido):
    if titulo in notas:
        notas[titulo]=nuevoContenido
        print("La nota e actualizo exitosamente")
    else:
        print("La asignatura no exite")
    
def eliminarNota(notas, titulo):
    if titulo in notas:
        del notas[titulo]
        print("la nota fue eliminada exitosamente...")


def menuNotas():
    while True:
        print("----- Menú Notas -----")
        print("1. Agregar nota")
        print("2. Ver nota")
        print("3. Editar nota")
        print("4. Eliminar nota")
        print("5. Salir")
        
        opcion=int(input("Ingrese una opcion:"))
        
        match opcion:
            case 1:
                print("----------- Agregar Nota ---------")
                titulo= input("Ingrese el titulo de la nota: ")
                contenido=float(input("Ingrese el contenido de la nota: "))
                agregarNota(notas, titulo, contenido)
                print("Nota agregada correctamente")
            case 2:
                print("----------- Ver Nota ---------")
                verNotas(notas)
                
            case 3:
                print("----------- Editar Nota ---------")
                titulo = input("Ingrese el titulo de la nota que desea editar: ")
                nuevoContenido = float(input("Ingrese la nueva nota: "))
                editarNota(notas, titulo, nuevoContenido)
                
            case 4:
                print("----------- Eliminar Nota ---------")
                titulo= input("Ingrese el titulo de la nota: ")
                eliminarNota(notas,titulo)

            case 5:
                print("Saliendo..")

                break
        
            case _:
                print("Opcion incorrecta")
                
            
menuNotas()

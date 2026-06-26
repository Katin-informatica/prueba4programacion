#Sistema gestion de peliculas
peliculas=[]
def mostrar_menu():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     MENU PRINCIPAL")
    print("1.  Agregar pelicula")
    print("2.   Buscar pelicula")
    print("3.  Eliminar pelicula")
    print("4. Actualizar pelicula")
    print("5.  Mostrar pelicula")
    print("6.       Salir")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=")
def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese opcion: "))
            if 1<=opcion<=6:
                return opcion
            else:
                print("Ingrese opcion valida")
        except ValueError:
            print("DEBE INGRESAR UN CARACTER VALIDO")
            
def validar_titulo(titulo):
    if titulo.strip()=="":
        return False
    return True
def validar_duracion(duracion):
    try:
        duracion=int(duracion)
        if duracion>0:
            return True
        return False
    except ValueError:
        return False
def validar_calificacion(calificacion):
    try:
        calificacion=float(calificacion)
        if 0.0<=calificacion<=10.0:
            return True
        return False
    except ValueError:
        return False
    
def agregar_pelicula(lista):
    titulo=input("Ingrese nombre de la pelicula: ")
    duracion=int(input("Ingrese duracion de la pelicula: "))
    calificacion=float(input("Ingrese calificacion de la pelicula (0.0-10.0)"))
    
    if not validar_titulo(titulo):
        print(" El titulo no puede estar vacio.")
        return
    
    if not validar_duracion(duracion):
        print("La duracion debe ser mayor que 0")
        return
    
    if not validar_calificacion(calificacion):
        print("La calificacion debe se entre 0.0 a 10.0")
        return
    pelicula={
        "Titulo":titulo.strip(),
        "duracion":int(duracion),
        "calificacion":float(calificacion),
        "disponible":False
    
    }
    
    
    lista.append(pelicula)
    print(f"Pelicula{titulo} registrada correctamente ")
    
def buscar_pelicula(lista,titulo):
    for i in range(len(lista)):
        if lista[i]["titulo"]==titulo:
            return i
    return -1

def eliminar_pelicula(lista):
    titulo=input("Ingrese nombre de la pelicula que desea eliminar: ")
    posicion=buscar_pelicula(lista,titulo)
    if posicion !=-1:
        lista.pop(posicion)
        print(f"Pelicula {titulo} eliminada correctamente") 
    else:
        print(F"pelicula {titulo} no se encuentra registrada")
        
def actualizar_disponibilidad(lista):
    for i in range (len(lista)):
        if lista[i]["calificacion"]>=7.0:
            lista[i]["disponible"]=True
        else:
            lista[i]["disponible"]=False
            
def mostrar_peliculas(lista):
    actualizar_disponibilidad(lista)
    for i in range(len(lista)):
        if lista[i]["disponible"]==True:
            estado="DISPONIBLE"
        else:
            estado="NO DISPONIBLE"
        
        print(f"Titulo:{lista[i]["titulo"]}")
        print(f"Duracion:{lista[i]["duracion"]}")
        print(f"Calificacion:{lista[i]["calificacion"]}")
        print(f"Estado:{estado}")
while True:
    mostrar_menu()
    opcion=leer_opcion()
    if opcion == 1:
        agregar_pelicula(peliculas)
    elif opcion==2:
        titulo=input("Ingrese nombre de pelicula que desea buscar: ")
        posicion= buscar_pelicula(peliculas,titulo)
        if posicion != -1:
            if peliculas [posicion]["disponible"]==True:
                estado="DISPONIBLE"
            else:
                estado="NO DISPONIBLE"
            print(f"Pelicula encontrada en la posicion: {posicion}")
            print(f"Titulo: {peliculas[posicion]["titulo"]}")
            print(f"Duracion: {peliculas[posicion]["duracion"]}")
            print(f"Calificacion: {peliculas[posicion]["calificacion"]}")
            print(f"Estado: {estado}")
        else:
            print (f"Pelicula {titulo} no se encuentra registrada")
    elif opcion==3:
        eliminar_pelicula(peliculas)
    
    elif opcion==4:
        actualizar_disponibilidad(peliculas)
        print("Estados actualizados correctmente")
        
    elif opcion == 5:
        mostrar_peliculas(peliculas)
        
    elif opcion == 6:
        print("Finalizando sistema...")
        break
    
    
    #₍^. .^₎⟆
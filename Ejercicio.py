from os import system;
from collections import Counter

conta = 1
while conta == 1:
    try:
        system("clear")
        universidades = {}
        
        NumeroUniversidad = int(input("\nCuantas Universidad Votaran: \t"))
        
        contador2 = 1
        while NumeroUniversidad != 0:
            system("clear")
            NombreUniversidad = input(f"Cual es el nombre de la universidad #{contador2}: \t")
            
            if NombreUniversidad in universidades.keys():
                system("clear")
                input("Ese Nombre de universidad ya existe enter para continuar")
            else:
                contador2 += 1
                universidades[NombreUniversidad] = []
                cerrar = 1
                contador = 1
                while cerrar == 1:
                    system("clear")
                    print("\n\n------- aceptar (A) - rechazar (R) - nulo (N) - blanco (B) - Terminar Votacion (X)")
                    voto = input(f"\n Cual es tu voto persona #{contador}: \t")
                    
                    if voto in "ARNBarnb":
                        universidades[NombreUniversidad].append(voto.upper())
                        contador += 1
                        system("clear")
                    elif voto.lower() == "x":
                        universidades[NombreUniversidad].append("X")
                        cerrar = 2
                    else:
                        system("clear")
                        input(f"\n\n ----Ingresa un Valor Valido Enter para continuar-----")
            NumeroUniversidad -= 1
        conta = 0
        system("clear")
        print(f"Numero de Universidades: {len(universidades)}")
        
        uniA = 0
        uniR = 0
        uniE = 0

        for clave in universidades:
            print(f"\nUniversidad: {clave}")
            conteo=Counter(universidades.get(clave))
            for i in universidades.get(clave):
                print(f"Voto: {i}")
                
            if conteo['A'] > conteo['R']:
                uniA += 1
            if conteo['A'] < conteo['R']:
                uniR += 1
            if conteo['A'] == conteo['R']:
                uniE +=1
                
            print(f"{clave}: {conteo['A']} Aceptan - {conteo['R']} Rechazan - {conteo['B']} Blancos - {conteo['N']} Nulos ")    
        print(f"\nUniversidades que aceptan: {uniA}")
        print(f"Universidades que Rechazan: {uniR}")
        print(f"Universidades con Empate: {uniE}")
        
    except:
        system("clear")
        input("\nIngresa un Valor Valido Enter para continuar") 
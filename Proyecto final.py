import csv
from msvcrt import kbhit

while True:
    print("Bienvenidos al programa para elegir su proximo auto")
    print("a continuacion haremos algunas preguntas para ofrecerle las mejores ofertas")

    csvfile = open('automoviles.csv')
    data = list(csv.DictReader(csvfile,delimiter = ";"))

    print('ingrese que marca de vehiculo que desea comprar: ')
    marca = str(input('marca: '))

    print("ingrese el tipo de combustible que prefiere para su vehiculo")
    combustible = str(input('tipo de combustible: '))

    print('ingrese la cantidad de puertas deseada(tres/cinco): ')
    puertas = str(input('numero de puertas: '))

    lista_marca = []


    for k in data:
        if (k.get('marca') == marca) and (k.get('tipo_combustible') == combustible) and (k.get('num_puertas') == puertas):  
            lista_marca.append(k)
        else:
            pass
    
    
    if len(lista_marca) != 0:
        print('las mejores ofertas son:', lista_marca)
    else:
        print('No se encontraron coincidencias')




    print('desea seguir consultando?: si/no')
    seguir = str(input())
    if seguir == 'si':
        pass
    elif seguir == 'no':
        print('gracias por su consulta!!!!!!')
        break
    else:
        ('ingrese valor valido')
        
    

        
    csvfile.close ()
import csv
from msvcrt import kbhit

print("Bienvenidos al programa para elegir su proximo auto")
print("a continuacion haremos algunas preguntas para ofrecerle las mejores ofertas")

csvfile = open('automoviles.csv')
data = list(csv.DictReader(csvfile,delimiter = ";"))
control = True

if __name__ == '__main__':
    while control:
            csvfile = open('automoviles.csv')
            data = list(csv.DictReader(csvfile,delimiter = ";"))
            print('ingrese que marca de vehiculo desea comprar: ')
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
            while True:
                seguir = str(input())
                if seguir == 'si':
                    break                    
                elif seguir == 'no':
                    print('gracias por su consulta!!!!!!')
                    control = False
                    break
                else:
                    print('ingrese valor valido')
            
        

            
csvfile.close ()
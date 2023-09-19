entrada = input('Introduce el color:\n')#pedimos el color a buscar
tupla = ("rojo","azul","verde","negro")#declaramos la tupla
if entrada in tupla:#si el color buscado esta dentro, corre la tupla
    print('El color que buscas está en la lista.')
else:#de ser lo contrario, se corre el else
    print('El color que buscas no está en la lista.')
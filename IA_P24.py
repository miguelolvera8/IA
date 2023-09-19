x = 0#declaramos las variables
while x <= 30:#se inicia el while, y se rompe cuando x sea mayor que 30
    x = x+1
    if x == 4 or x == 6 or x == 10:#ejecutamos la primer condicion, si es igual a 4, 6, o 10, imprime y se salta al siguiente ciclo
        print("Se salto el valor: ", x)
        continue
    
    print("El valor del bucle es: ", x)#cuando sea igual a 15, se va a romper el bucle
    if x == 15:
        break

if x == 15:#cuando se rompa el bucle, se imprime ya fuera del ciclo while lo siguiente
        print('se rompió la ejecución del bucle cuando x valía ', x)
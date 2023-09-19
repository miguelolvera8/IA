edad = int(input('¿Cuál es tu edad?\n'))#pide la edad
if edad <= 0:#si la edad es menor o igual que 0 se ejecuta lo siguiente
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:#si esta entre 1 y 18 años, ejecuta el elif e imprime que es menor de edad
	print('Eres menor de edad.')
elif edad < 100:#si es menor que 100 años, pero mayor de 18, ejecuta lo siguiente
	print('Eres mayor de edad.')
elif edad >=18 and edad <=45:#si tiene entre 18 y 45, imprime que tiene entre 18 y 45 xD
    print("tienes entre 18 y 45")
elif edad >100 and edad <=120:#y si tiene entre 100 y 120, imprime que pocos viven hasta esa edad
    print("pocos viven hasta esta edad")
else:
	print('Edad no válida.')#de ser ninguno el caso, ya sea un numero negativo o mayor a 120, ejecuta lo siguiente
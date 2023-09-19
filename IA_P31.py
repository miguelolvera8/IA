#def colores(*args):
#	pass

#colores('rojo', 'azul', 'verde', 'amarillo')#aqui tiene 4 argumentos
#colores('lila', 'negro', 'rojo')#aqui tiene 3 argumentos
#colores('rosa')#aqui tiene un argumento
#colores('marrón', 'naranja')#aqui tiene dos argumentos
def colores(*args):#definimos la funcion con args para que pueda variar de acuerdo a lo que vayamos pidiendo
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')#imprimimos los valores que se mandaron

colores('rojo', 'azul')#mandamos los diferentes valores
colores('lila', 'negro', 'rojo')
colores('rosa','negro')
colores('marrón', 'naranja')
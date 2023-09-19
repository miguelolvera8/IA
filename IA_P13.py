#para eliminar una posicion especifica, y luego guardar se usa guardarLista(para guardatr la posicion que se desea eliminar) asi:
#guardarLista = colores.pop(0)
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
g1 = colores.pop(-2)#deseamos elminiar rojo y guardarlo en g1
g2 = colores.pop(-1)#deseamos elminiar blanco y guardarlo en g2, asi
print(colores,"\n")
print(g1,g2)#imprimimos la lista completa y vemos que ya no aparecen los elementos que eliminamos
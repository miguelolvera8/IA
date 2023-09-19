teclado1 = {#declaramos el diccionario
    "Categoria": "Teclados",
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99"
}
teclado2 = {#inicializamos el diccionario, con "categoria","modelo" y "precio", con su respectivo valor
    "Categoria": "Teclados",
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
}

del teclado1#eliminamos todo el diccionario 1
del teclado2["Categoria"]#eliminamos unicamente Categoria
del teclado2["Precio"]#eliminamos unicamente Precio
print(teclado2["Modelo"])#mostramos la seccion modelo de teclado2
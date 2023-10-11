"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.
"""
frase = input("dime una frase: ")
letra = input("dime una letra: ")
cont = 0
for i in frase:
    if i == letra:
        cont += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, cont, frase))

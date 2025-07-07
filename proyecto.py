#INPUTS PARA SELECCION DEL TEXTO Y LETRAS

texto = input('Ingresa el texto a analizar: ')
letra1 = input('Selecciona la letra que quieras buscar: ')
letra2 = input('Selecciona la letra que quieras buscar: ')
letra3 = input('Selecciona la letra que quieras buscar: ') 

#se convierte el texto en una lista para contar las letras seleccionadas por el usuario 
lista = list(texto.lower()) 

#se convierte el texto en una lista de palabras
palabras = texto.split(' ') 

#1) Cantidad de letras repetidas
print(f'La letra "{letra1}" "{letra2}" "{letra3}" se repite : {lista.count(letra1)} veces, {lista.count(letra2)} veces y {lista.count(letra3)} veces')

#2) Cantidad de palabras
print(f'La cantidad de palabras que se usan en este texto son : {len(palabras)} palabras')

#3) Primera y ultima letra
print(f'La primer letra del texto es "{lista[0]}" y "{lista[-1]}" es la ultima')

#4) Palabras invertidas
print(f'{palabras[::-1]}')
print(f'{" ".join(lista[::-1])}')


#5) Existe la palabra Python
print(f'Existe la palabra "Python": {'Python'.lower() in palabras}')

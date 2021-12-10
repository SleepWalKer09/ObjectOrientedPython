"""
Similares a listas pero en lugar de indices usan llaves
No tienen orden interno
SON MUTABLES
Pueden iterarse
"""
diccionario = {'Chris': 23, 'Ericka': 60, 'Jaime': 7}
#cambiar valor
diccionario['Jaime'] = 20
#agregar al diccionario
diccionario['Pedro'] = 89
diccionario

#iterar dentro del diccionario
for llave in diccionario.keys():
    print(llave)
for valor in diccionario.items():
    print(llave,valor)

#buscar en el diccionaro
'Chris' in diccionario #regresa True o False
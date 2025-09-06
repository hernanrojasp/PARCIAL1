
def suma_lista(lista):
    resultado = 0

    for i in lista:
        resultado = resultado + i
    if resultado > 100:
        
        return 'mayor'
    else:                   ##error es de sintaxis, faltaban los : en esta linea##
        return 'menor'
    
print(suma_lista([10, 20, 30]))  # Salida: menor
print(suma_lista([60, 50, 10]))  # Salida: mayor



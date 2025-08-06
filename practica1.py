edad = int(input("Ingresa tu edad:"))
boleto = "Edad no válida"
if edad >= 0 and edad < 4:
    boleto = "Entrada gratis"
elif edad >= 4 and edad <= 12:
    boleto = "Boleto infantil $40"
elif edad >= 13 and edad <= 59:
    boleto = "Boleto general $70"
elif edad >= 60:
    boleto = "Adulto mayor con descuento de $35"

print("Tipo de boleto:", boleto)
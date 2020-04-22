from calculadora import *

def esO(o) :
	if o != "+" and o != "-" and o != "*" and o != "/" :
		valido = False
	else:
		valido = True
	return valido

print("Bienvenido a la calculadora")
operacion = input("Indique la operacion (+, -, *, /): ")
while esO(operacion) == False:
	print("No es una operacion valida")
	operacion = input("Indique la operacion (+, -, *, /): ")
else:
	oper1 = input("Indique el primer numero:")
	oper2 = input("Indique el segundo numero:")
 
	if oper1.isnumeric() == True and oper2.isnumeric() == True:
		oper1 = int(oper1)
		oper2 = int(oper2)
		if operacion == "+" :
			print(suma(oper1, oper2))
		elif operacion == "-" :
			print(resta(oper1, oper2))
		elif operacion == "*" :
			print(multiplicacion(oper1, oper2))
		elif operacion == "/" :
			print(division(oper1, oper2))
		else :
			print("No es una operacion valida")
	else :
		print("Error! Ambos digitos deben tener formato numerico")


num1=20
num2=4

print("la suma es :",(num1+num2))
print("la resta es :",(num1-num2))
print("la multiplicacion es :",(num1*num2))
print("la division es :",(num1/num2))
print("la division extacta es :",(num1//num2))
print("la potencia es :",(num1**num2))

#Concatenacion en Python

texto1="Hola"
texto2="Mundo"
textoFinal=texto1+texto2
print(textoFinal)
print("El saludo es: %s %s" %(texto1,texto2))

saludoFinal="Saludo {}{}".format(texto1,texto2)
print(saludoFinal)

saludoFinal2="Saludo {y}{x}".format(x=texto1,y=texto2)
print(saludoFinal2)
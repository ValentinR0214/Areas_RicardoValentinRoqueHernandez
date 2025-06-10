
opcion = 0
print("1- Cuadrado")
print("2- Rectangulo")
print("3- Circulo")
print("4- Triangulo")
opcion = int(input("Elige qué figura calcular su área: "))
if opcion == 1: 
    num1 = 0
    num1 = int(input("Ingresa el lado: "))
    area = num1 * num1
    print("El area del cuadrado es: ",area)
elif opcion == 2: 
    num1 = 0
    num1 = int(input("Ingresa el lado menor: "))
    num2 = 0
    num2 = int(input("Ingresa el lado mayor: "))
    area = num1 * num2
    print("El area del rectangulo es: ",area)
elif opcion == 3: 
    num1 = 0
    num1 = int(input("Ingresa el radio: "))
    pi = 3.1416
    area = pi * (num1 * num1)
    print("El area del circulo es: ",area)
elif opcion == 4: 
    num1 = 0
    num1 = int(input("Ingresa la base: "))
    num2 = 0
    num2 = int(input("Ingresa la altura: "))
    area = (num1 * num2) / 2
    print("El area del triangulo es: ",area)
else:
    print("No se eligio nada Chau")
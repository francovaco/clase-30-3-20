  num=int(input("Ingrese un numero entero positivo:  "))
for i in range(1, num+1, 2):
    for j in range(i, 0, -2):
        print(j, end="")
    print("")
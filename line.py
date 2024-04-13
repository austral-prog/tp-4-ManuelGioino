def line():
    Coeficiente_A= float(input("Ingrese el coeficiente A:"))
    Coeficiente_B= float(input("Ingrese el coeficiente B:"))
    X1=float(input("Ingrese el coeficiente X1:"))
    X2=float(input("Ingrese el coeficiente X2:"))

    print(f"El coeficiente A de su ecuación de la recta es: {Coeficiente_A}")
    print(f"El coeficiente B de su ecuación de la recta es: {Coeficiente_B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {Coeficiente_A}X + {Coeficiente_B}")
    print("")
    print("Dados los siguientes puntos:")

    print(f"\tP1 ({X1}, {Coeficiente_A*X1+Coeficiente_B})")
    print(f"\tP2 ({X2}, {Coeficiente_A*X2+Coeficiente_B})")
    Y1=Coeficiente_A*X1+Coeficiente_B
    Y2=Coeficiente_A*X2+Coeficiente_B
    distanciaX = (X2-X1)
    DistanciaY = (Y2-Y1)
    print("")
    print(f"La distancia entre ellos es: {(distanciaX**2+DistanciaY**(2))**(1/2)}")

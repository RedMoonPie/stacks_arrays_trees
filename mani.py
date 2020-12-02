from PIla import pila

ab=pila()
if __name__== "__main__":
    while (True):
        print("*****--Menu--*****\n" +
              "1.push\n" +
              "2.sacar\n" +
              "3.cimax\n" +
              "4.tama\n"+
              "5. vaciar \n")
        n = input("Ingrese la opcion: \n")
        if n == "1":
            nodo = input("Digite el valor a agregar: \n")
            if nodo.isdigit():
                nodo = int(nodo)
                ab.push(nodo)
            else:
                print("\nIngresa solo digitos...")
        elif n == "2":
            print("Preorden.....\n")
            ab.sacar()

        elif n == "3":
            print("posorden.....\n")
            ab.cimax()


        elif n == "4":
            print("inorden.....\n")
            ab.tama()
        elif n == "5":
            print("Vaciar\n")
            ab.vaciar()

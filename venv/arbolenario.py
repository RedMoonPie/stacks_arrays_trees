class Nodo:
    def __init__(self,dato):
        self.izq=None
        self.der=None
        self.dato=dato
    def verDato(self):
        return self.dato

class Lista:
    def __init__(self):
        self.cab=None
        self.col=None
    def agregar(self,dato):
        node = Nodo(dato)
        if self.cab is None:
            self.cab=node
            self.col=node
        else :
            node.der=self.cab
            self.cab=node

    def mostrar(self):
        temp=self.cab
        while temp != None:
            print(temp.verDato(), end=' ')
            temp = temp.der
ab=Lista()
if __name__=="__main__":
    while (True):
        print("*****--Menu--*****\n" +
              "1.push\n" +
              "2.sacar\n" +
              "3.cimax\n" +
              "4.tama\n" +
              "5. vaciar \n")
        n = input("Ingrese la opcion: \n")
        if n == "1":
            nodo = input("Digite el valor a agregar: \n")
            ab.agregar(nodo)
        elif n == "2":
            print("Preorden.....\n")
            ab.mostrar()

        elif n == "3":
            print("posorden.....\n")
            ab.cimax()


        elif n == "4":
            print("inorden.....\n")
            ab.tama()
        elif n == "5":
            print("Vaciar\n")
            ab.vaciar()

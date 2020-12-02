from random import randint

class Nodo():

    def __init__(self,valor):

        self.valor = valor
        self.izq = None
        self.der = None


class Busquedabinaria:

    def __init__(self):
        self.raiz = None


    def agregar(self, a,elemento):
        if a == None:
            a = Nodo(elemento)

        else:
            d = a.valor
            if elemento < d:
                a.izq = self.agregar(a.izq,elemento)
            else:
                a.der=self.agregar(a.der,elemento)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.izq)
            print(a.valor)
            self.inorder(a.der)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.valor)
            self.preorder(a.izq)
            self.preorder(a.der)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.izq)
            self.postorder(a.der)
            print(a.valor)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.valor:
                return a.valor
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.izq)
                else:
                    return self.buscar(dato, a.der)




ab=Busquedabinaria()
ab.raiz = ab.agregar(ab.raiz,8400)
j = 0
while (j != 200):
    ab.raiz = ab.agregar(ab.raiz, randint(7801, 9000))
    j = j + 1

if __name__=="__main__":



    while(True):
        print("*****--Menu--*****\n"+
              "1.agregar\n"+
              "2.preorden\n"+
              "3.posorden\n"+
              "4.inorden")
        n = input("Ingrese la opcion: \n")
        if n == "1":
            nodo=input("Digite el valor a agregar: \n")
            if nodo.isdigit():
                nodo = int(nodo)
                ab.raiz = ab.agregar(ab.raiz, nodo)
            else:
                print("\nIngresa solo digitos...")
        elif n == "2":
            print("Preorden.....\n")
            if ab.raiz == None:
                print("Vacio")
            else:
                ab.preorder(ab.raiz)

        elif n == "3":
            print("posorden.....\n")
            if ab.raiz == None:
                print("Vacio")
            else:
                ab.postorder(ab.raiz)


        elif n == "4":
            print("inorden.....\n")
            if ab.raiz == None:
                print("Vacio")
            else:
                ab.inorder(ab.raiz)


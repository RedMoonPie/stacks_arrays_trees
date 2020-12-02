class Nodo2:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
    def verNodo(self):
        return self.dato


class pila:
    cima=Nodo2
    tam=0
    def __init__(self):
        self.cima=None
        tam=0

    def vacia(self):
       return self.cima is None


    def push(self,elemento):
        aux=Nodo2(elemento)
        aux.sig=self.cima
        self.cima=aux
        self.tam=self.tam+1

    def sacar(self):
        aux=self.cima.dato
        self.cima=self.cima.sig
        self.tam=self.tam-1
        return print(aux)

    def cimax(self):
        return print(self.cima.dato)

    def tama(self):
        return print(self.tam)
    def vaciar(self):
        while self.vacia() is not True:
            self.sacar()

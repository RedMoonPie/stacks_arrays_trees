import self as self


class Lista_Doble:

    def __init__(self):
        self.ini = None
        self.cola = None


    def vacio(self):

        if self.ini is None:
            return True
        else:
            return False

    def InserPrimer(self, dato):
        temporal = Nodo(dato)
        if self.vacio() == True:
            self.ini = temporal
            self.cola = temporal
        else:
            temporal.sig = self.ini
            self.ini.Ant = temporal
            self.ini = temporal

    def listar(self):

        print("*****************")
        temporal = self.ini
        while temporal != None:
            print(temporal.verNodo(), end=' ')
            temporal = temporal.sig

    def listarcola(self):
        print("*****************")
        temporal = self.cola
        while temporal != None:
            print(temporal.verNodo(), end=' ')
            temporal = temporal.Ant

    def borrarprimero(self):
        if self.vacio() == False:
            self.ini = self.ini.sig
            self.ini.Ant = None

    def borrarult(self):
        if self.cola.Ant == None:
            self.ini = None
            self.cola = None
        else:
            self.cola=self.cola.Ant
            self.cola.sig = None

    def borrarposi(self, pos):
        Ant = self.ini
        actual = self.ini
        k = 0
        if pos > 0:
            while k != pos and actual.sig != None:
                Ant = actual
                actual = actual.sig
                k = k + 1
            if k == pos:
                temporal=actual.sig
                Ant.sig=actual.sig
                temporal.Ant=Ant
    def listarli(self,pos):
            x=[]
            temporal = self.cola
            while temporal != None:
                x.append(temporal.verNodo())
                temporal = temporal.Ant
            if pos > len(x)-1:
                return "^"
            else:
                return x[pos]


class Nodo:

    def __init__(self, dato):
        # punteros para unir luego
        self.sig = None
        self.Ant = None
        self.ele = dato

    def verNodo(self):
        return self.ele


class Pila(object):

    def __init__(self):

        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):

        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacia")

    def vacia(self):
        return self.items == []

    def impr(self):
        if not self.items:
            return print ("vacia")

        return print(self.items)
    def ele(self,x):
        if not self.items:
            return print ("vacia")
        if len(self.items)-1 < x:
            return "^"
        else:
            return self.items[x]


class Cola(object):

    def __init__(self):

        self.items = ['A', 'B', 'C', 'X', 'Y', 'Z']

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):

        try:
            return self.items.pop(0)

        except:
            raise ValueError("La cola esta vacia")

    def vacia(self):
        return self.items == []

    def impr(self,x):
        if not self.items:
            return print ("vacia")
        if len(self.items)-1 < x:
            return "^"
        else:
            return self.items[x]
    def tamño(self):
        return len(self.items)

    def impr2(self):
        if not self.items:
            return print ("vacia")

        return print(self.items)
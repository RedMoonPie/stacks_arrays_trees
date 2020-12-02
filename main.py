from Listas import Pila as pil
from Listas import Cola as col
from Listas import Lista_Doble as dob
from PIla import pila
pl=pila()
pil3 = pil()
pil2 = pil()
pil1 = pil()
col1 = col()
dob1 = dob()
# numeros declarados
pil.apilar('1');pil.apilar('2');pil.apilar('3');pil.apilar('4')
# variables declaradas
col = col1
# variables no declaradas
dob = dob1
# incorrectas
incorrecta = pil2
# correctas
correcta = pil3

iter = -1;
sentencia = ""
while iter < 10:
    b1 = False
    b2 = False
    b3 = False
    k = -1;
    v = -1;
    l = -1;
    iter = iter + 1
    sentencia = input("Digite la sentencia \n")

    if len(sentencia) - 1 == 4:
        while k < col.tamño():
            k = k + 1

            if sentencia[0] == col.impr(k) or sentencia[0] == dob.listarli(k):
                print("aun no")

                b1 = True

                # borrar adicionar
                if sentencia[0] == dob.listarli(k):
                    col.encolar(dob.listarli(k))
                    dob.borrarult()


                # igual
                if sentencia[1] == '=':
                    print("aun no 2 ")
                    if sentencia[2].isalnum():
                        while v < col.tamño():
                            v = v + 1
                            if sentencia[2] == col.impr(v) and sentencia[2].isupper() or sentencia[2].isdigit() or sentencia[2]==dob.listarli(v):

                                b2 = True
                                try:
                                    # borrar adicionar

                                    if sentencia[2] == dob.listarli(v):
                                        col.encolar(dob.listarli(v))
                                        dob.borrarult()
                                except IndexError:
                                    print()
                                # adicion digito
                                z = -1
                                z1 = len(pil.items) - 1
                                if sentencia[4].isdigit():
                                    while z < z1:
                                        z = z + 1
                                        if pil.ele(z) == sentencia[4]:
                                            n1 = True
                                            break
                                        else:
                                            n1 = False

                                    if not n1:
                                        print("El digito se ha agregado")
                                        pil.apilar(sentencia[4])

                                if sentencia[3] == '+' or sentencia[3] == '-' or sentencia[3] == '/' or sentencia[3] == '*':
                                    print("coco")

                                    while l < col.tamño():
                                        l = l + 1
                                        if sentencia[4].isalnum():

                                            if sentencia[4] == col.impr(l) and sentencia[4].isupper() or sentencia[4].isdigit() or sentencia[4]==dob.listarli(l):
                                                print("aun no 3")

                                                b3 = True

                                                # borrar adicionar

                                                if sentencia[4] == dob.listarli(l):
                                                    col.encolar(dob.listarli(l))
                                                    dob.borrarult()

                                                # adicion digito
                                                z = -1
                                                z1 = len(pil.items)-1
                                                if sentencia[4].isdigit():
                                                    while z < z1:
                                                        z=z+1
                                                        if pil.ele(z) == sentencia[4]:
                                                            n1=True
                                                            break
                                                        else:
                                                            n1=False

                                                    if not n1:
                                                        print("El digito se ha agregado")
                                                        pil.apilar(sentencia[4])

                                                print ("correctamente armado")
                                                l=col.tamño()
                                                v=col.tamño()
                                                k=col.tamño()
                                                correcta.apilar(sentencia)




                                            else:


                                                if l > col.tamño() - 1 and b3 == False:
                                                    l=col.tamño()
                                                    v=col.tamño()
                                                    k=col.tamño()
                                                    dob.InserPrimer(sentencia[4])

                                                    print("la variable " + sentencia[
                                                    4] + "no se encuentra definida\n - se ha agregado a "
                                                             "variables no definidas")

                                                    break

                                else:
                                    print("Operador invalido 0=0[X]0")
                                    incorrecta.apilar(sentencia)
                                    break








                            else:

                                if v > col.tamño() - 1 and b2 == False:
                                    l=col.tamño()
                                    v=col.tamño()
                                    k=col.tamño()

                                    dob.InserPrimer(sentencia[2])
                                    print("la variable " + sentencia[
                                        2] + "no se encuentra definida\n - se ha agregado a variables no definidas")
                                    incorrecta.apilar(sentencia)
                    else:

                        print("caracter invalido")
                        incorrecta.apilar(sentencia)


                else:
                    print(" El operador debe ser =")
                    incorrecta.apilar(sentencia)




            else:

                    if k >= col.tamño() - 1 and b1 == False:
                        dob.InserPrimer(sentencia[0])
                        l=col.tamño()
                        v=col.tamño()
                        k=col.tamño()

                        print("la variable '" + sentencia[
                            0] + "' no se encuentra definida.\n - se ha agregado a variables no definidas")
                        incorrecta.apilar(sentencia)



    else:
        print("Sentencia incompleta o nada digitado")
        incorrecta.apilar(sentencia)
print("*****************No definidas*********************")
dob.listar()
print("\n*****************variables definidas*********************")
col.impr2()
print("\n*****************correctos*********************")
correcta.impr()
print("\n*****************incorrectos*********************")
incorrecta.impr()
print("*****************Digitos*********************")
pil.impr()
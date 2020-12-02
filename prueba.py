from Listas import Pila as pil
from Listas import Cola as col
from Listas import Lista_Doble as dob
from Listas import Nodo as nd
pil1 = pil()
col1 = col()
dob1 = dob()
nd = nd(5)
# numeros declarados
pil = pil1
# variables declaradas
col = col1
# variables no declaradas
dob = dob1
# incorrectas
incorrecta = pil1
# correctas
correcta = pil1

dob.InserPrimer(2)
dob.InserPrimer(3)
dob.InserPrimer(4)
dob.InserPrimer(5)
dob.InserPrimer(6)
print(dob.listarli(6))

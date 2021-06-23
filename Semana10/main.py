from graphviz import Graph
from graphviz import Source
n = int(input("Ingrese cuántos países va a ingresar: "))
paises = []
for _ in range(n):
  paises.append(input("Ingrese el nuevo país: "))
dicc = {}
############### DICCIONARIO ###############
for pais in paises:
  v = int(input(f"Ingrese la cantidad de paises vecinos de {pais}: "))
  vecinos = []
  for _ in range(v):
    vecino = input()
    if vecino in dicc:
      if pais not in dicc[vecino]:
        vecinos.append(vecino)
    else:
      vecinos.append(vecino)
  dicc[pais] = vecinos
################# ORDENAR ASCENDENTEMENTE ###############
inicio = input("Ingrese el país de partida: ")
i_ini = paises.index(inicio)
final = input("Ingrese el país de destino: ")
i_fin = paises.index(final)
if i_fin < i_ini:
  pais_i = final
  pais_f = inicio
else:
  pais_i = inicio
  pais_f = final
################# CONTAR ###############
dicc2 = dicc.copy()
x = False
list = []
while dicc2[pais_i] == []:
  list.append(pais_i)
  pais_i = paises[paises.index(pais_i)-1]
for i in range(paises.index(pais_i), n):
  recorrido = list + [paises[x] for x in range(paises.index(pais_i),i+1) if len(dicc2[paises[x]]) != 0]
  for vecino in dicc2[paises[i]]:
    if (len(dicc2[vecino]) != 0) or vecino == pais_f or (vecino == pais_i and len(dicc2[vecino]) == 0):
      recorrido.append(vecino)
    if recorrido[-1] == pais_f:
      x = True
      break
  if x == True:
    break
print(f"La cantidad de paises por los que pasamos para ir desde {inicio} hacia {final} es {len(recorrido)}")
############### GRAPHOS ###############
g = Graph()
for pais in paises:
  for vecino in dicc[pais]:
    if (vecino in recorrido) and (pais in recorrido):
      if abs(recorrido.index(vecino) - recorrido.index(pais)) == 1:
        g.edge(pais, vecino, color = 'red')
    else:
      g.edge(pais, vecino)
print(g)
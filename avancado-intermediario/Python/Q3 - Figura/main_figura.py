#Caso a "main_figura.ipnynb" nao funcione direito em outros compiladores fiz esse .py tambem


from figura import Figura
from circulo import Circulo
from retangulo import Retangulo


print("Inicilizando Objetos...\n")
fig = Figura(2.0,3.0)
print("_______\n")
circ = Circulo(4.1,4.1,1.4)
print("_______\n")
retang = Retangulo(1.1,1.1,4.2,4.2)
print("_______\n")

print("Atribuindo Variáveis...\n")

fig_var: Figura = fig
fig_var.desenhar()
print(" ")

fig_var = circ
fig_var.desenhar()
print(" ")

fig_var = retang
fig_var.desenhar()
print(" ")



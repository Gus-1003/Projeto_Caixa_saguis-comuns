print("Inicio do projeto Caixa de Saguis.")
print("O som1 ira significar para o animal o botão da esquerda. O som2 o botão da direita.")

aperto = 0
hab = input("Esse animal já está habituado?")
print(f"Você declara que esse animal, {hab}, está habituado")

#=======================================================================================
exp = 1
print(f"Inicio do expeiremento {exp}:")

aproxima = 30
print(f"O animal foi posicionado inicialmente a {aproxima}cm das barras.")

posicao_animal = int(input("Qual a distancia do animal para as barras:"))
if(posicao_animal < aproxima):
    print("Liberar 0,5ml de recompensa")

bottom = int(input("O som1 foi tocado qual barra o animal apertou? (1 - esquerda e 2 -direita)"))

if bottom == 1:
    print("liberar 0,5ml de rec")
    aperto += 1
else:
    print("não liberar nada")

print(f"Até agora o animal apertou na barra {aperto} vezes.")
if aperto>=20:
    print("Ir para a proxima etapa.")

#=======================================================================================
exp += 1
print("Reiniciando o experimento.")
print(f"Inicio do expeiremento {exp}:")

aproxima = 30
print(f"O animal foi posicionado inicialmente a {aproxima}cm das barras.")

posicao_animal = int(input("Qual a distancia do animal para as barras:"))
if(posicao_animal < aproxima):
    print("Liberar 0,5ml de recompensa")

bottom = int(input("O som1 foi tocado qual barra o animal apertou? (1 - esquerda e 2 -direita)"))

if bottom == 1:
    print("liberar 0,5ml de rec")
    aperto += 1
else:
    print("não liberar nada")

print(f"Até agora o animal apertou na barra {aperto} vezes.")
if aperto>=20:
    print("Ir para a proxima etapa.")
else:
    print("Reiniciando o experimento.")


#=======================================================================================
exp += 1
print("Reiniciando o experimento.")
print(f"Inicio do expeiremento {exp}:")

aproxima = 30
print(f"O animal foi posicionado inicialmente a {aproxima}cm das barras.")

posicao_animal = int(input("Qual a distancia do animal para as barras:"))
if posicao_animal < aproxima:
    print("Liberar 0,5ml de recompensa")

bottom = int(input("O som2 foi tocado qual barra o animal apertou? (1 - esquerda e 2 -direita)"))

if bottom == 2:
    print("liberar 0,5ml de rec")
    aperto += 1
else:
    print("não liberar nada")

print(f"Até agora o animal apertou na barra {aperto} vezes.")
if aperto>=20:
    print("Ir para a proxima etapa.")
else:
    print("Reiniciando o experimento.")


if exp >= 50:
    print("Experimento seguirá para a próxima fase.")

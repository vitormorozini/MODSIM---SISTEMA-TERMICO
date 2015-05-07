# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:36:59 2015

@author: vitor_000
"""

#Considereando um intervalo de Tempo de 30 dias - Medições realizadas no ultimo dia
from Funções import *
import matplotlib.pyplot as plt

Massa = [100000, 140000, 180000] #Massa de água em gramas
QTDEGARRAFAS = [100/2, 140/2, 180/2] #Quantidade de garrafas (valor em kg de água - calculado com base na densidade)
T = [0, 0, 0]

Rad = radiacao(0.95,30) #Revestimento preto - Absorvidade = 0.95
Conv = conveccao(1.74) #Valor de h usado para "Madeira Foleada" - Fonte: sp.senai.br

Liq = Rad + Conv

for i in range(3):
         T[i] = Ti(Liq, Massa[i], 1)
         
print(Rad)
print(Conv)
print(Liq)
print(T)


plt.plot(T,QTDEGARRAFAS)
plt.ylabel('Quantidade de garrafas') #Garrafa pet de 2L
plt.xlabel('Temperatura interna FINAL do refrigerador')
plt.title(r'Refrigerador Passivo')
plt.show()

ALFA = [0.95, 0.05] #Coeficiente de absortividade preto e espelhado, reespectivamente.
T = [0,0]
Rad = [0,0]
Liq = [0,0]
Conv = conveccao(1.74)

for i in range(2):
    Rad[i] = radiacao(ALFA[i],30) #Tempo
    Liq[i] = Rad[i] + Conv
    T[i] = Ti(Liq[i], 180000, 1) 

print(Rad)
print(Conv)
print(Liq)
print(T)

plt.plot(T,ALFA)
plt.ylabel('Coeficiente de absortividade') #Depende do material que reveste o refrigerador
plt.xlabel('Temperatura interna FINAL do refrigerador')
plt.title(r'Refrigerador Passivo')
plt.show()

caloresp = [0.6, 1, 3.24] #calor específico do alcool, água e hidrogênio reespectivamente
Tint = [0,0,0]

Rad = radiacao(0.95,30) #Coef de absortividade do preto; Tempo
Conv = conveccao(1.74) #h da "Madeira Foleada"
Liq = Rad + Conv

for i in range(3):
    Tint[i] = Ti(Liq, 180000, caloresp[i])

print(Rad)
print(Conv)
print(Liq)
print(Tint)

plt.plot(Tint,caloresp)
plt.ylabel('Calor específico da substância') #Depende da substância que está dentro da garrafa
plt.xlabel('Temperatura interna FINAL do refrigerador')
plt.title(r'Refrigerador Passivo')
plt.show()
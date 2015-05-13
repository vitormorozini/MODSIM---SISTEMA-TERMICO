# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:13:55 2015

@author: vitor_000
"""

#Considereando um intervalo de Tempo de 30 dias - Medições realizadas no ultimo dia
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

#Gráfico_1: O parâmetro a ser variado será a massa de líquido, o qual é equivalente a variar a quantidade de garrafas no interior do refrigerador.
#Parâmetros a ser variado considerado: Substância - Água (c = 1) ; Superfície que reveste o refrigerador - Branca (a = 0.2)

T0 = [-5] #Temperaturas iniciais
tempodias = range(30) #Dados obtidos em um intervalo de tempo de 30 dias.

def func(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.2 #Parâmetro a ser variado
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 200000 #100 Garrafas Pet de 2L de água
    c = 1 #Parâmetro a ser variado
    
    Deriv = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv


def func1(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.2 #Parâmetro a ser variado
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 100000 #50 Garrafas Pet de 2L de água
    c = 1 #Parâmetro a ser variado
    
    Deriv1 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv1

def func2(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.2 #Parâmetro a ser variado
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 150000 #75 Garrafas Pet de 2L de água
    c = 1 #Parâmetro a ser variado
    
    Deriv2 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv2

deriv = odeint(func,T0[0],tempodias)
deriv1 = odeint(func1,T0[0],tempodias)
deriv2 = odeint(func2,T0[0],tempodias)

#print(deriv)
#print(deriv1)
#print(deriv2)

plt.plot(deriv, 'bo', label = '100 garrafas') #100 garrafas
plt.legend(loc = 'upper left')
plt.plot(deriv2, 'r', label = '75 garrafas') #75 garrafas
plt.legend(loc = 'upper left')
plt.plot(deriv1, 'g', label = '50 garrafas') #50 garrafas
plt.legend(loc = 'upper left')
plt.ylabel('Temperatura [graus Celsius]') 
plt.xlabel('Tempo [dias]')
plt.title(r'Variando a quantidade de garrafas')
plt.show()

#Gráfico_2: O parâmetro a ser variado será o "a", o qual é equivalente a variar o material da superfície que reveste o refrigerador.
#Parâmetros a ser variado considerado: Substância - Água (c = 1) ; Quantidade de garrafas pet de 2L - 75 (equivalente a 150000g de água)

def func3(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.05 #Superfície espelhada
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 150000 #Parâmetro a ser variado
    c = 1 #Parâmetro a ser variado
    
    Deriv3 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv3
    
def func4(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.2 #Superfície branca
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 150000 #Parâmetro a ser variado
    c = 1 #Parâmetro a ser variado
    
    Deriv4 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv4

def func5(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.95 #Superfície preta
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 150000 #Parâmetro a ser variado
    c = 1 #Parâmetro a ser variado
    
    Deriv5 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv5

deriv3 = odeint(func3, T0[0], tempodias)
deriv4 = odeint(func4, T0[0], tempodias)
deriv5 = odeint(func5, T0[0], tempodias)

#print(deriv3)
#print(deriv4)
#print(deriv5)

plt.plot(deriv3, 'bo', label = 'Superfície espelhada') #Superfície espelhada
plt.legend(loc = 'upper left')
plt.plot(deriv4, 'g', label = 'Superfície branca') #Superfície branca
plt.legend(loc = 'upper left')
plt.plot(deriv5, 'r', label = 'Superfície preta') #Superfície preta
plt.legend(loc = 'upper left')
plt.ylabel('Temperatura [graus Celsius]') 
plt.xlabel('Tempo [dias]')
plt.title(r'Variando o revestimento do refrigerador')
plt.show()

#Gráfico_3: O parâmetro a ser variado será o "c", o qual é equivalente a variar a substância no interior das garrafas.
#Parâmetros a ser variado considerado: Superfície que reveste o refrigerador - Branca (a = 0.2)  ; Quantidade de garrafas pet de 2L - 75 (equivalente a 150000g de água)

def func6(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.2 #Parâmetro a ser variado
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 150000 #Parâmetro a ser variado
    c = 0.6 #Calor específico do álcool
    
    Deriv6 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv6

def func7(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.2 #Parâmetro a ser variado
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 150000 #Parâmetro a ser variado
    c = 1 #Calor específico da água
    
    Deriv7 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv7
    
def func8(p,l):
    for i in range(30):
        t = i*1
    A = 2
    a = 0.2 #Parâmetro a ser variado
    G = 1300
    cos = 0.705
    h = 1.74
    T = 17
    k = 1 #Parâmetro pode ser variado
    m = 150000 #Parâmetro a ser variado
    c = 1.25 #Calor específico do ar atmosférico
    
    Deriv8 = k*t*A*(a*G*cos + h*T)/m*c
    return Deriv8
        
deriv6 = odeint(func6,T0[0],tempodias)
deriv7 = odeint(func7,T0[0],tempodias)
deriv8 = odeint(func8,T0[0],tempodias)

#print(deriv6)
#print(deriv7)
#print(deriv8)

plt.plot(deriv6, 'bo', label = 'Álcool') #Álcool
plt.legend(loc = 'upper left')
plt.plot(deriv7, 'g', label = 'Água') #Água
plt.legend(loc = 'upper left')
plt.plot(deriv8, 'r' , label = 'Ar atmosférico') #Ar atmosférico
plt.legend(loc = 'upper left')
plt.ylabel('Temperatura [graus Celsius]') 
plt.xlabel('Tempo [dias]')
plt.title(r'Variando a substância no interior da garrafa')
plt.show()
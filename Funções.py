# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:47:23 2015

@author: vitor_000
"""

def radiacao(a,DELTAT0):
    r = a*1300*0.705*DELTAT0*2
    r1 = r*4.18 #Transformando Jaule para caloria
    return r1
    
def conveccao(h):
    c = h*6*17*30
    c1 = c*3.6
    return c1
#3.6 representa a adaptação de h para o Sistema Internacional
    
 #def fourier():
#    f = (0.17*5*8)/0.03
#   return f

def liquido(m,c,T):
    l =  m*c*(T-(-5))
    return l
#Tinicial do líquido é -5 graus Celsius    

def latente(m,L):
    l1 = m*L
    return l1
    
def Ti(L,m,c):
    T = L/m*c - 5
    return T 

def alfa(G,g,T,DELTAT):
    a = G/g*0.705*T*DELTAT*2
    return a

#O TEMPO É REPRESENTADO EM DIAS
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:21:05 2021

@author: leore
"""
#conditions de l'équilibre général (cas particulier avec symétrie des dotations initiales)
a=1/2 #a=alpha
Px=a/(1-a)
Py=1
W1x=2
W1y=1
W2x=1
W2y=2
R1=Px*W1x+Py*W1y
R2=Px*W2x+Py*W2y
x1=a*(R1/Px)
y1=(1-a)*(R1/Py)
x2=a*(R2/Px)
y2=(1-a)*(R2)
print(x1,y1,x2,y2,Px,Py)

"""
def Ui(xi,yi):
    return ((xi)**a)*((yi)**(1-a))
R1=Px*W1x+Py*W1y
W1y=W1x*Px+W1y-Px*x1
R2=Px*W2x+Py*W2y"""

"""
#CPO:
print (a*(1/x1)+(1-a)*((-Px)/(W1y))==0)
print (x1)"""
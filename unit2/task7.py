a=input("Ввести длину")
b=input("Ввести ширину")
h=input("Ввести высоту")
M=input("Ввести площадь окон и дверей в процентах десятичной дробью")
N=input("Ввести объем краски на 1м2")
R=input("Ввести стоимость 1 литра краски")
a1=float(a)
b1=float(b)
h1=float(h)
M1=float(M)
N1=float(N)
R1=float(R)
s=2*h1*(a1+b1)*(1-M1)
V=s*N1
F=V*R1
print(V)
print(F)
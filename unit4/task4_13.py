n1= int(input('n1='))
n2= int(input('n2='))
n3= int(input('n3='))
n4= int(input('n4='))


mx = (n1 if (n1 > n2 and n1 > n2 and n1 > n4)
         else (n2 if (n2 > n3 and n3 > n4) 
         else (n3 if n3 > n4 else n4)))

print(mx)
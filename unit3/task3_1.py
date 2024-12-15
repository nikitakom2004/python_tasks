s= int(input('s='))
v= int(input('v='))
t=s*1000/v
print(t)
h=t//3600
r=t%3600
m=r//60
r=r%60
print(h,m,r)

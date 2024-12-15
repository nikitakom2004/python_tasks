s= int(input('s='))
t=24*3600-s
h=t//3600
r=t%3600
m=r//60
r=r%60
print(h,m,r)
n = int(input('n='))

x = n

l1=x%10
x=x//10
l2=x%10
x=x//10
l3=x%10
x=x//10
l4=x%10
x=x//10
l5=x
p=l1*10000+l2*1000+l3*100+l4*10+l5
if p==n:
    print('палиндром')
else:
    print('не палиндром')

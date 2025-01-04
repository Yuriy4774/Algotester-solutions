n,res = int(input()),0
#500 непотрібно бо n >= 1
sp = [200,100,50,20,10,5,2,1]
n = 500-n
i = 0
while n >0:
    res+=(n//sp[i])
    n-=(n//sp[i])*sp[i]
    #print(n,res,sp[i])
    i+=1
print(res)
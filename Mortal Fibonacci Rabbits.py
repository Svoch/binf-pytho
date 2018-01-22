import numpy as np

n=86
m=20

fibo = np.zeros(shape=(n),dtype=int)
fibo[0] = 1
fibo[1] = 1
fibo[2] = 1
for i in range(2,n):
    if(i<m):
        fibo[i] = fibo[i-1] + fibo[i-2]
    else:
        if(i-m-1>=0):
            fibo[i] = fibo[i-1] + fibo[i-2] - fibo[i-m-1]
        else:
            fibo[i] = fibo[i-1] + fibo[i-2] - 1


def mortalFibonacci(n,m):
    if(n<0):
        return 0
    if(n==0):
        return 1
    if(n==1):
        return 1
    if(n==2):
        return 1
    if(n<=m):
        return mortalFibonacci(n-1,m) + mortalFibonacci(n-2,m)
    #print "computing mortalFibonacci( " + n.__str__() + " , " + m.__str__() +" )..."
    return mortalFibonacci(n-1,m) + mortalFibonacci(n-2,m) - mortalFibonacci(n-m-1,m) #+ mortalFibonacci(n-m-1,m)



print fibo

#for i in range(1,20):
#    print mortalFibonacci(i,3)

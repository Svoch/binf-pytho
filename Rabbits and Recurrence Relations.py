def kFibonacci(n,k):
    if(n==1):
        return 1
    if(n==2):
        return 1
    return kFibonacci(n-1,k) + k*kFibonacci(n-2,k)

print kFibonacci(3,1)

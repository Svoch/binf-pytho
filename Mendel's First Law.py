# (k,2) + (m,1)(k,1) + (m,2)*3/4 + (m,1)*(n,1)*1/2

k = 25
m = 26
n = 15

def factorial(n):
    if(n==0):
        return 1
    return factorial(n-1)*n

def C(m,n):
    return factorial(m)/(factorial(n)*factorial(m-n))

atLeastOneDominant = C(k,2) + C(m,1)*C(k,1) + C(m,2)*3/4.0 + C(m,1)*C(n,1)/2.0 + C(k,1)*C(n,1)
allPossibleSelections = C(m+n+k,2)

anotherAllPossibleSelections = C(k,2) + C(m,1)*C(k,1) + C(m,2) + C(m,1)*C(n,1) + C(n,2) + C(k,1)*C(n,1)


allrecessive = C(m,2)*1/4.0 + C(n,2) + C(m,1)*C(n,1)*2/4.0

print 1 - allrecessive/(allPossibleSelections*1.0)
print atLeastOneDominant/(allPossibleSelections*1.0)

#print maybeAllPossibleSelections
#print allPossibleSelections

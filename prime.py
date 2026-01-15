def prime(n):
    if n<1:
        return "not prime"
    else:
        for i in range(2,n):
            if n%i==0:
                return "not prime"
    return "prime" 


print(prime(5))
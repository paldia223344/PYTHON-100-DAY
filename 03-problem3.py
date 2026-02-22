#Fibonacci using recursion 
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
N = int(input("Enter a Number"))
print(f"Fibonacci series for {N} :  ")
for i in range (N):
    print(fibonacci(i))

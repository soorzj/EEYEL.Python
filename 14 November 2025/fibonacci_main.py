import fibonacci_module
n=int(input("Enter the number of fibonacci numbers required:"))
fib=fibonacci_module.fibonacci(n)
print("The required fibonacci numbers are:",fib)
n=int(input("For nth fibonacci number, enter n:"))
nfib=fibonacci_module.nth_fibonacci(n)
print(n,"th fibonacci number is:",nfib)
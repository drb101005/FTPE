#prime number checker
def is_prime(n):
    return n > 1 and not any(n % i == 0 for i in range(2, int(n**0.5)+1))

n = int(input("Enter a number: "))
msg = "a prime" if is_prime(n) else "not a prime"
print(f"{n} is {msg} number.")

#Arithmatic operator
n1=float(input("enter first number ")) 
n2=float(input("enter second number ")) 
op=input("enter opera on +,-,*,/,% ") 
if op=="+": 
    result=n1+n2 
    print("Result of Additon=",n1 + n2) 
elif op=="-": 
    result=n1-n2 
    print("Result of Subtrac on=",n1 - n2) 
elif op=="*": 
    result=n1*n2 
    print("Result of Mul plica on=",n1 * n2) 
elif op=="/": 
    result=n1/n2 
    print("Result of Division=",n1 / n2) 
elif op=="%": 
    result=n1%n2 
    print("Result of Modulus=",n1 % n2) 
else: 
    print("Invalid Statement") 
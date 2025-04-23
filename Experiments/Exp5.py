#Even or Odd numbers
number=int(input("Enter a Number ")) 
if number%2==0: 
    print(f"{number} is even") 
else: 
    print(f"{number} is odd")
#part 2 (Not rally needed)
num = input("Enter a number up to which the odd and even numbers should be listed: ")
num = int(num)
i = 0
while i < num:
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")
    i += 1
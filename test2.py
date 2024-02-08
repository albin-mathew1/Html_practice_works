a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))
n=50
for i in range(1, n):
    if a%i==0 and b%i==0:
        result=i
print(result)

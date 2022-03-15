def find_gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

arr=list(map(int,input("Enter the 10 numbers").split()))
num1 = arr[0]
num2 = arr[1]
gcd = find_gcd(num1, num2)
for i in range(2, len(arr)):
    gcd = find_gcd(gcd, arr[i])
print("GCD is: ",gcd)
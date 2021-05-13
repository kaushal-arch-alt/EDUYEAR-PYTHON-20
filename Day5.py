#PROGRAM1
'''n=int(input("Enter first number:"))
m=int(input("Enter second numver:"))
for ele in range(n,m):
    if ele % 5 == 0 and ele % 7 == 0:
        print(ele,end="," if ele < m else "")


#PROGRAM 2:

def terms(no_of_terms,digit):
    sum=0
    for ele in range(1,no_of_terms+1):
        num =digit*ele
        sum = sum + int(num)
    print(sum)

no_of_terms=int(input())
digit=input()
terms(no_of_terms,digit)

#PROGRAM 3:

#Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)
sum=0
while True:
    user_input=input("Enter a number:")
    if user_input == 'q':
        break
    user_input=int(user_input)
    sum=sum+user_input
    print("Press q to quit.")
print(sum)

#PROGRAM 4:
#Write a loop to find the factorial of any number The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.

def fact(n):
    result=1
    i=0
    while n>i:
        result = result * (n-i)
        i+=1
    print(result)

fact(7)


#PROGRAM 5:

#input: python language is best programming language output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e

str="python language is best programming language"

for i in range(len(str)):
    end_value="-"
    if str[i]==" " or i==len(str)-1 or str[i+1]==" ":
        end_value=" "
    if i%2==0:
        print(str[i].upper(),end=end_value)
    else:
        print(str[i],end=end_value)
'''
list=[9,3,2,5,7]
#list.sort()
#print(sorted(list))
#print(list)
print(list[::-1])
print(list)
print(list.reverse())
print(list)

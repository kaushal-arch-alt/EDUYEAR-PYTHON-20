#PROGRAM 1:
list=[]
n=int(input("Enter how many numbers want to add in a list:"))
c=0
'''maxx=0
even=0
odd=0
while c<n:
    x=int(input())
    list.append(x)
    c+=1

for ele in list:
    if ele % 2 ==0:
        even+=1
    else:
        odd+=1
print("Total Even numbers:{} and Total Odd numbers:{}".format(even,odd))

#PROGRAM 2:
while c<n:
    x=int(input())
    list.append(x)
    c+=1
minn=list[0]
for ele in range(len(list)):
    if list[ele] > maxx:
        maxx=list[ele]
    if list[ele] < minn:
        minn=list[ele]
print("Maximum number is:{}".format(maxx))
print("Minimum number is:{}".format(minn))


#PROGRAM 3

while c<n:
    x=int(input())
    list.append(x)
    c+=1

if list == list[::-1]:
    print("Palindrome")
else:
    print("No")

str="mom"
print(reversed(str))
print(str[::-1])
print(str==str[::-1])
#print("".join(reversed(str)))
#print("".join(reversed(str))==str)

'''
#PROGRAM 4
while c<n:
    x=int(input())
    list.append(x)
    c+=1
print("Palindrome numbers are:")
# check through the list to check
# number is palindrome or not
for ele in list:
    num = str(ele)
    if num == num[::-1]:
        print(ele,end=" ")

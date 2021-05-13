#PROGRAM1:
'''def count_y(word):
    countt=0
    for letter in word:
        if letter=='y':
            countt+=1
    return countt


word=input("Enter a word:")
count_of_y=word.count('y')
print("Occurance of y:",count_of_y)
'''
#program 2
word=input("Enter a word:")
even_char=word[::2]
print("Even characters of word are:",even_char)
print("Count of y in word:",word.count('y'))
print("Changing cases:",word.swapcase())

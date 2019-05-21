# This line prints "hello world!"
# print('hello world!')
# print('hello world 2!')

# myverylongstring
# MyVeryLongString #Upper camel case
# myVeryLongString #camel case
# my_very_long_string #snake case

# myString = 'summer'
# print(myString)

# print(myString+"hello world")
# x = 2
# print(x)

# two = str('2')
# print(1 + 2)
# print('1' + two)

# print(int('1') + int('2'))

# list or array

# summer=10
# if summer%2==0:
#     print("this is even")
# else:
#     print("this is odd")
# print(summer)

# l = [1,2,3,4,5]

# for number in l:
#     if number%2==0:
#         print(number)

# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
# print('hello')

# i=0
# while i<100:
#     if i%2==0:
#         print (i)
#     i=i+1

# a=[]
# i=1
# while i<=100:
#     a.append(i)
#     i += 1          # i = i + 1
# # print(a)
# for number in a:
#     if number%2==0:
#         print(number)
    

# result = add(1, 5)

# resultTwo = add(result, 10)
# print(resultTwo)

# def isEvenNumber(i):
#     if i%2==0:
#         return True
#     else: 
#         return False

# n=0
# while n<100:
#     if isEvenNumber(n):
#         print (n)
#     n += 1
    
# def isOddNumber(i):
#     if i%2==0:
#         return False
#     else:
#         return True

# n=0
# while n<=100:
#     if isOddNumber(n):
#         print (n)
#     n=n+1

# def isPrimeNumber(i): 
#     n=2
#     while n < i:
#         if i%n==0:
#             return False 
#         n=n+1
#     return True 

# n=0
# while n<=100000:
#     if isPrimeNumber(n):
#         print(n)
#     n=n+1



# with open('alice.txt', 'r') as file:
#     novel = file.read().replace('\n', '')
#     words = novel.split(' ')
#     # print(words)
#     count=0
#     for name in words:
#         if name=="Alice":
#             count=count+1
#     print(count)

star =[]
n=0

while n<=5:
    star.append("*")
    print(' '.join(star))
    n=n+1


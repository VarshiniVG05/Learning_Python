#  WHILE LOOP:

#1.  Print numbers from 1 to 10 

# i=1
# while i <=10:
#     print(i)
#     i=i+1

# 2. Print the square of each number from 1 to 10

# i=1
# while i<=10:
#     print(i+i)
#     i=i+1

# 3. Print each character in a string

# text="varshini"
# i=0
# while  i<len(text):
#     print(text[i]) 
#     i+=1   

# 4. Sum of numbers from 1 to 10 

# number=0
# i=1
# while i<=10:
#     number +=i
#     i+=1
# print (number,"is the sum of numbers from 1 to 10")

# 5. Print each element in a list

# element=["volleyball","handball","cricket"]
# i=0
# while i<len(element):
#     print(element[i])
#     i=i+1

# 6. Print numbers from 10 to 1(reverse order)

# number=10
# while number>=1:
#     print(number)
#     number-=1

# 7. Print only even numbers from 10 to 20

# i=10
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1

# 8. Print the multiples of 5 between 20 to 50

# number=20
# while number <=50:
#     if number %5==0:
#         print(number)
#     number+=1

# 9. Print the factorial of a number

# number=int(input("enter a number"))
# factorial=1
# while number>=1:
#     factorial*=number
#     number-=1
# print(factorial,"is the factorial")

# 10. Print numbers from a list that are greater than 10

# numbers=[3,5,34,56,2565,8,0,546,-54]
# index=0
# while index<len(numbers):
#     if numbers [index]>10:
#         print(numbers[index])
#     index+=1

# 11. Print all prime numbers between 10 and 20

# number=10
# while number <=20:
    

# 12. Find the largest number in a list DOUBT

# numbers=[395,30,4546,423,243,346,-5345]
# largest=numbers
# 
# 
# 
# print(largest,"is the largest number")

# 13. Count the number of vowels in a string DOUBT

# str="I am a graduate"
# count=0
# i=0
# vowels="aeiou"
# whil

# # 14. Print product of 1 to 5

# number=1
# product=1
# while number<=5:
#     product*=number
#     print({number},{product})
#     number+=1

# 15. Reverse a number 

# number=int(input("enter a number"))
# reversed=0
# while number!=0:
#     order=number%10
#     reversed=reversed*10+order
#     number//=10
# print(str(reversed))


# CONTROL STATEMENTS

# 1. Print numbers from 1 to 10,but stop when the number is 5

# for number in range (1,11):
#     print(number)
#     if number==5:
#         break

# 2. Find the 1st negative number in a list

# numbers=[35,67,-89,64,-745,-9,-78563,5435,754]
# minimum=0
# for i in numbers:
#     if i <0:
#         minimum=i
#         break
# print(minimum)

# 3. Iterate over a list and stop if you encounter a zero

# list=[1,4,7,0,9,3]
# for item in list:
#     if item==0:
#         break
#     print(item)

# 4. Print numbers from 1 to 10,skipping 5 

# for i in range (1,11):
#     if i !=5:
#         print(i)

# 5. Print only even numbers from 1 to 10

# for number in range (1,11):
#     if number %2==0:
#         print (number)

# 6. Iterate over a list and skip the negative numbers

# numbers=[2,6,-8,3,4]
# for element in numbers:
#     if element<0:
#         continue
#     print(element)

# 7. Print characters of a string, skipping vowels DOUBT

# str=int(input("enter a text"))
# def print_consonents(a):
#     vowels="aeiouAEIOU"
#     for consonents in a:
#         if consonents not in vowels:
#             print(consonents)


# 8. Iterate over numbers from 1 to 20,but skip multiples of 3

# for number in range (1,21):
#     if number % 3==0:
#         continue
#     print(number)

# 9. Iterate over a list and use pass for future implementation 

# numbers=[1,2,3,4,5,6,7]
# for item in numbers:
#     if item%2==0:
#         pass
#     else:
#         print(item)

# 10. Iterate over numbers from 1 to 10,skip 5 and stop at 8

# for i in range(1,11):
#     if i ==5:
#         continue
#     if i==9:
#         break
#     print(i)

# 11. Print only odd numbers from 1 to 10,but use pass for even numbers

# for i in range(1,11):
#     if i%2==0:
#         pass
#     else:
#         print(i)

# 12. Iterate over a list,skip negatives,print positives,stop at zero

# numbers=[1,-2,3,-4,5,-6,0,45,3234]
# for number in numbers:
#     if number<0:
#         continue
#     if number==0:
#         break
#     print(number)

# 13. Skip the first half of a list,process the second half,use pass for future

# numbers=[1,2,3,4,5,6,7,8,9]
# half=len(numbers)//2
# for i in range(len(numbers)):
#     if i<half:
#         pass
#     else:
#         print(numbers[i])

# 14. Get input from user like numbers until user enters zero,after that have to print the product of numbers 

# product=1
# while True:
#     number=int(input("enter a number"))
#     if number==0:
#         break
#     product*=number
# print(product)


# 15. Get input from user like number until user enters negative number, after that have to print the sum of numbers.

# total=0
# while True:
#     number=float(input("enter a number"))
#     if number<0:
#         break
#     total+=number
# print({total})


# conditional statements
# even or odd


# number=int(input("enter a number:"))


# if number%2==0:
#     print("its a even number",number)
# else:
#     print("its a odd number",number)

# compare two number find largest number

# a=int(input("enter a number"))
# b=int(input("enter another number"))
# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("a is lesser than b")

# else:
#     print("a is equal to b")

# find a largest number among 3 numbers

#number1=int(input("enter a number1:"))
#number2=int(input("Enter a number2:"))
#number3=int(input("Enter a number3:"))


#if number1>number2 and number1>number3:
#    print("number1 is the largest number")

#elif number2>number1 and number2>number3:
#    print("number2 is the largest number")

#elif (number1<number2 or number1>number2) and (number2<number3 or number1>number3):
#    print("number3 is the largest number")
#else:
#    print("all are equal")

#ASSESSMENT

# 1. Check even or odd:
#number=int(input("enter a number"))
#if number % 2==0:
#   print("even")
#else:
#    print("odd")

# 2. Check if a number is divisible by 5:

#number=int(input("enter a number"))
#if number % 5==0:
#    print("the number is divisible by 5")
#else:
#  print("the number is not divisible by 5")

# 3. Compare 2 numbers and print the largest one:


# number1=int(input("enter a number"))
# number2=int(input("enter a number"))
# if number1>number2:
#     print(number1, "is the largest number")
# else:
#     print(number2,"is the largest number")

#if x>y:
#    print("1")
#else:
#    print("4")

# 4. Check if a string contains a specific sub string 

# text="I am a graduate from the Women's Christian College,Chennai"
# substring="College"
# if substring in text:
#     print("the text contains a substring")
# else:
#     print("the text doesn't contain a substring")
# 5. Check if a number is between 1 and 10 

#number=int(input("enter a number"))
#if number>0 and number<11:
#    print("the number lies between 1  and 10")
#else:
#    print("the number doesn't lie between 1 and 10")

# 6. Check if a character is a vowel:

#vowels= ('a'),('e'),('i'),('o'),('u')
#character=input("enter a character")
#if character in vowels:
#    print('the character is a vowel')
#else: 
#    print('the character is a consonent')

# 7. Check if a person is eligible to vote
 
# age=int(input('enter an age'))
# if age>=18:
#     print("the person's age is",age ,"the person is eligible to vote")
# else:
#     print("the person's age is", age ,"the person is not eligible to vote")


# 8. Check leap year:

# year=int(input("enter a year"))
# if (year % 4 ==0 and year %100  !=0) or (year% 400 == 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")


# 9. check if a given number is  multiple of 3 and 7:

# number=int(input("enter a number"))
# if number% 3==0  and number%7==0:
#     print(number, "is divisible by 3 and 7")
# else:
#     print(number,"is not divisible by 3 and 7")

# 10. Check if a person is a teenager(age 13 to 19):

# number=int(input("enter a number"))
# if number>=13 and number<=18:
#     print("the person's age is",number,",the person is a teenager")
# else:
#     print("the person's age is",number,",the person is not a teenager")

# 11. Find the largest of three numbers

# number1=int(input("enter a number1"))
# number2=int(input("Enter a number2"))
# number3=int(input("Enter a number3"))
# if number1>number2 and number1>number3:
#     print("number1 is the largest number")
# elif number2>number1 and number2>number3:
#     print("number2 is the largest number")
# elif (number1<number2 or number1>number2) and (number2<number3 or number1>number3):
#     print("number3 is the largest number")
# else:
#     print("all are equal")

# 12. Check if a number is divisible by both 5 and 11:
# number=int(input("enter a number"))
# if number % 5==0 and number % 11==0:
#     print(number,"is divisible by both 5 and 11")
# elif number % 5==0:
#     print(number,"is divisible by 5  only")
# elif number % 11==0:
#     print(number,"is divisible by 11 alone")
# else:
#     print(number,"is not divisible by both 5 and 11")

#13. Determine the grade based on marks:

# mark=int(input("enter a mark"))
# if mark >=91 and mark <=100:
#     print(mark,"commes under A grade")
# if mark >=81 and  mark<=90:
#     print(mark,"comes under B grade")
# if mark >=71 and mark<=80:
#     print(mark,"comes under C grade")
# if mark >=61 and mark<=70:
#     print(mark,"comes under D grade")
# if mark >=0 and mark<=60:
#     print(mark,"comes under E grade")

#14. Check if a number is positive and even

# number=int(input("enter a number"))
# if number >0 and number%2==0:
#     print(number, "is positive and even")
# elif number <0 and number%2==0:
#     print(number,"is even but negative")
# elif number<0 and number %2!=0:
#     print(number,"is not positive and not even")

# 15. Check if a number lies  between 10 and 20:

# number=int(input("enter a number"))
# if number >10  and number <20:
#     print(number,"lies between 10 and 20")
# else:
#     print(number,"doesn't lie between 10 and 20")

# 16. Determine if a string is empty:

# string=str(input("enter a string"))
# str=" "
# if string!=str:
#     print("the string is not empty")
# else:
#     print("the string is empty")

# 17. Check if a number is positive or negetive
 
# number=int(input("enter a number")) 
# if number >0:
#     print("the number is  positive")
# elif number<0:
#     print("the number is negative")
# else:
#     print("the number is  NIL")

# 18. Check if a number is prime or a not prime number:

#number=int(input("enter a number"))

# ASSESSMENT 2 (NESTEDIF)

# 1. Find the largest of three numbers:

# number1=int(input("enter a number1"))
# number2=int(input("enter a number2"))
# number3=int(input("enter a number3"))

# if number1>number2:
#     if number1>number3:
#         print("number1 is the largest number")
#     else:
#         print("number3 is the largest number")

# elif number1<number2:
#     if number2>number3:
#         print("number2 is the largest number")
#     else:
#         print("number3 is the largest number")

# elif (number1>number2 or number2>number1):
#     if (number1<number3 or number3>number2):
#         print("number3 is the largest number")

# elif number1==number2:
#     if number2==number3:
#         print("all are equal")
#     else:
#         if number2>number3:
#             print("number1 and number2 are equal")
#         else:
#             print("number3 is the largest number")

# 2. Check if a number is divisible by 2,3 or both 

# number=int(input("enter a number"))
# if number%2==0:
    # if number%3==0:
        # print(number,"is divisible by both 2 and  3")
    # else:
        # print(number,"is divisible by 2 alone")
# else:
    # if number%3==0:
        # print(number,"is divisible by 3 alone")
    # else:
        # print(number,"is not divisible by 2 or 3")

# 3. check if a number lies between the 10 - 50:

# number=int(input("enter a number"))
# if number >= 10:
#     if number<=50:
#         print(number,"lies between the range 10 - 50")
#     else:
#         print(number,"is greater than 50")
# else:
#     print(number,"is less than 10")

# 4. Check if a year is a leap year:

# year=int(input("enter a year"))
# if year % 4==0:
#     if year % 100==0:
#         if year%400==0:
#             print(year,"is a leap year")
#         else:
#             print(year,"is not a leap year")
#     else:
#         print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

# 5. Check if a number if is positive, negative, or zero, and whether it is even or odd:

# number=int(input("Enter a number"))

# if number >=0:
#     if number==0:
#         print("NIL")
#     else:
#         if number % 2==0:
#             print(number,"is a positive and even")
#         else:
#             print(number,"is positive and odd")
# else:
#     if number % 2==0:
#         print(number,"is negative and even")
#     else:
#         print(number,"is negative and odd")

# 6. Check if a number is positive, negative or zero:

# number=int(input("enter a number"))
# if number>=0:
#     if number ==0:
#         print("NIL")
#     else:
#         print(number,"is positive")
# else:
#     print(number,"is negative")

#7. Check if a number is even or odd and within a 1 - 10 range

# number = int(input("Enter a number between 1 and 10"))

# if number>=1 and number <=10:
#     if number %2==0:
#         print(number,"is even")
#     else:
#         print(number,"is odd")
# else:
#     print(number,"is not within the range of 1 to 10")

# 8. check if a person is eligible to vote by citizen:

# age=int(input("enter an age"))
# if age >=18:
#     print("the person is",age,",the person is eligible to vote")
# else:
#     print("the person is not eligible to vote")

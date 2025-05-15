# import random 
# import collection
# print(random.random())

# print(random.uniform(1,100))

# print(random.randint(1,10))

# subjects=["accounts","commerce","economics","maths","english"]
# print(random.choice(subjects))
# print(random.choices(subjects,k=2))

# namedtuple
# myTuple=collections.namedtuple("Student",["name","age","qualification"])

           
# newType=myTuple("varshini",20,"bcom")

# print(newType)

# CHOCOLATE GAME

# chocolates = ["dairy milk","kitkat","perk","munch","5star","milkybar"]

# my_chocolate = random.choice(chocolates)

# attempts = 1
# max_attempts = 10
# print("Available options:", ', '.join(chocolates))

# while attempts <= max_attempts:
#     user_guess = input(f"Attempt {attempts}: Enter a chocolate name: ")

#     if user_guess == my_chocolate:
#         print("You guessed it correctly!")
#         break
#         second_round=input("Do you want to play again ?  yes or no :")
#         if second_round=="yes":
#             continue
#         elif second_round=="no":
#             break
#     else:
#         print("You guessed it wrong.")
#         attempts += 1

# if attempts == max_attempts:
#     print("Try again later! The correct chocolate was:", my_chocolate)



# # MAP,REDUCE,FILTER

# 1. Square the numbers in a list
# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)

# # 2. convert to upper case

# words=["Vithya","Janaranjani","Harini","Sheela","Shreeranjini","Sumaiya","Shereen"]
# upper_case=list(map(str.upper,words))
# print(upper_case)

# 3. add 10 to each number in a list

# numbers = [1,2,3,4,5]
# added_numbers = list(map(lambda x: x + 10, numbers))
# print("After adding 10:", added_numbers)

# 4. Double each number in a list
# 
# numbers=[1,2,3,4,5,6,7,8,9]
# doubled=list(map(lambda x : x*2,numbers))
# print(doubled)

# 5. Capitalize the first letter of each string in a list

# words=["pondicherry","chennai","kerala","maharashttra","delhi"]
# capitalised_words=list(map())

# 6. Filter out even numbers from a list

# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print (even_numbers)

# 7. filter out words shorter than 4 characters

# words = ["moon", "sun","is","star", "the", "am", "it","a"]
# filtered_words = list(filter(lambda word: len(word) >=3, words))
# print(filtered_words)

# 8. filter out numbers greater than 10

# numbers=[1,78,45,24,11,10,4,2,9]
# greater_numbers=list(filter(lambda x:x>10,numbers))
# print (greater_numbers)

# 9. filter out the strings containing the letter "a"

# strings=['varshini','shree','harini','shereen']
# filtered_string=list(filter(lambda x:'a' in x,strings))
# print (filtered_string) 

# 10. filter out the numbers that are not divisible by 3

# numbers=[1,2,3,4,5,6,7,8,9,12,15,17,18]
# filtered_string=list(filter(lambda x: x%3!=0,numbers))
# print (filtered_string)

# 11. filter out negative numbers from the list

# numbers=[0,1,2,3,-3,-2,-1,4,5,-5,-4]
# filtered_string=list(filter(lambda x:x<0,numbers))
# print (filtered_string)

# 12. find out the numbers that are not divisible by 3

# numbers=[1,2,3,4,5,6,7,8,9,12,15,17,18]
# filtered_string=list(filter(lambda x: x%3!=0,numbers))
# print (filtered_string ,"are the numbers that are not divisible by 3")

# 13. find the product of all the numbers in a list 

# from functools import reduce
# numbers = [2,3,4,5]
# product = reduce(lambda x,y:x*y,numbers)
# print(product) 

# 14. Concatenate a list of strings

# from functools import reduce
# strings=["my ","name ","is ","Varshini"]
# result=reduce(lambda x,y:x+y,strings)
# print(result)  

# 15. find the maximum number in a list

# from functools import reduce

# numbers=[3,7,2,9,5]
# maximum=reduce(lambda x,y:x if x>y else y,numbers)
# print(maximum) 

# 16. Compute the sum of squares of numbers in a list

# numbers=[1,2,3,4]
# squares=map(lambda x:x**2,numbers)
# result=sum(squares)
# print(result)


# 17. Compute the factorial of a number using reduce

# from functools import reduce
# number=5
# factorial=reduce(lambda x,y:x*y,range(1,number+1),1)
# print(factorial) 
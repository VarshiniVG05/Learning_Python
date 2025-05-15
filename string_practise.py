# 1. Reverse a string without using slicing
# def reverse_string(Varshini):
#     result=""
#     for char in Varshini:
#         result=char+result
#     return result

# 2. String compression(run-length encoding) DOUBT

# def run_length_encoding(Varshini):
#     if not Varshini:
#         return ""
    
#     encoded_string = ""
#     count = 1
#     for i in range(1, len(Varshini)):

# 3. Finnd all palindromes in a string



# 4. Extract all words starting with a specific letter

# x=["pink","yellow","boat","blue","violet","brown","green"]
# y="b"
# res=[]
# for word in x:
#     if word.startswith(y):
#         res.append(word)
# print({y},res)

# 5. Find the first non repeated character in a string 

# 6. Remove vowels from a string DOUBT

# vowels=("AEIOUaeiou")
# str="I am Varshini"
# str2=str.translate(vowels)
# print(str2)

# 7. Swap  case of each letter

# string="i LOVE pondicherry"
# swapped_string=string.swapcase()
# print(swapped_string)

# 8. Count frequency of characters

# string=input("enter a string")
# dic={}
# for ch in string:
#     if ch in dic:
#         dic[ch]+=1
#     else:
#         dic[ch]=1
# for key in dic:
#     print(key,dic[key])

# 9. Detect valid anagrams. check if two strings are anagrams 

# def check_anagram(string1, string2):
#     if len(string1) != len(string2):
#         return False
#     sorted_str1 = sorted(string1)
#     sorted_str2 = sorted(string2)
#     return sorted_str1 == sorted_str2

# STRING

# 1. in a para, replace "is" with "was" and count the number of "a"

# paragraph = "Varshini is a volleyball player. She is also a student"
# # paragraph = paragraph.replace("is", "was")
# a_count = paragraph.count('a')
# print(paragraph)
# print("Number of 'a':", a_count)

# 2. get input from user, check if it is an email id 

# 3. get input from user, check its valid password

# password = input("Input your password: ")

# is_valid = True

# if len(password) < 6 or len(password) > 12:
#     print("Not valid.Total characters should be between 6 and 12")
#     is_valid = False

# if not any(char.isupper() for char in password):
#     print("Not valid.It should contain at least one uppercase letter")
#     is_valid = False

# if not any(char.islower() for char in password):
#     print("Not valid.It should contain at least one lowercase letter")
#     is_valid = False

# if not any(char.isdigit() for char in password):
#     print("Not valid.It should contain at least one digit")
#     is_valid = False

# if any(char.isspace() for char in password):
#     print("Not valid.It should not contain any space")
#     is_valid = False

# if is_valid:
#     print("Valid Password")

# 4. login task-get input from user

# attempts = 0
# user_pass = {"user123": "password123"}

# while attempts < 3:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
    
#     if username in user_pass and user_pass[username] == password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid input. Please try again.")
#         attempts += 1
# else:
#     print("Too many attempts. Access denied.")
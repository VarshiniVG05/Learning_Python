# LIST 

#  1. Sum of all elements in a list. IP:[1,2,3,4)] OP:[10]

# myList=[1,2,3,4]
# res=0
# for val in myList:
#     res+=val
# print(res)

# #  2. Find the maximum and minimum elements in a list IP[3,5,1,7] OP: Max:7,Min:1

# myList=[3,5,1,7]
# max=0
# min=0
# for item in myList:
#     if item>min:
#         max=item
# for item in myList:
#     if item<max:
#         min=item
# print (max)
# print(min)
    


#  3. Remove duplicates from from a list(without using set) IP:[1,2,2,3,1] OP:[1,2,3]

# myList=[1,2,2,3,1]
# newList=[]
# for val in myList:
#     if val not in newList:
#         newList.append(val)
# print(newList)

# 4. Count frequency of each element in a list IP:[1,2,2,3,1] OP:[1:2,2:2,3:1]

# myList=[1,2,2,3,1]
# count_frequency={}
# for item in myList:
#     if item in count_frequency:
#         count_frequency[item] +=1
#     else:
#         count_frequency[item]=1
# print(count_frequency)

# 5. Reverse a list without using reverse function IP:[1,2,3] OP[3,2,1]

# myList=[1,2,3]
# reversedList=myList[::-1]
# print(reversedList)

# 6. Check if list is a palindrome IP[1,2,3,2,1] OP: yes

# myList=[1,2,3,2,1]
# def palindrome_check(myList):
#     return myList==myList[::-1]
# if myList:=palindrome_check:
#     print("yes")
# else:
#     print("no")


# 7. Find second largest element in a list IP[4,2,7,1] OP[4]

# numbers = [4,2,7,1]
# numbers.sort()
# print(numbers[-2])
        

# 8. Split list into two equal halves IP:[1,2,3,4] OP:[1,2],[3,4]

# myList=[1,2,3,4]
# mid=len(myList)//2
# half1=myList[:mid]
# half2=myList[mid:]
# print(half1)
# print(half2)

# 9. Merge two lists without duplicates IP[1,2],[2,3] OP[1,2,3]

# list1 = [1,2]
# list2 = [2,3]
# merged_list = list(set(list1 + list2))
# print(merged_list)


# 10. Count even and odd numbers in a list IP[1,2,3,4] OP: even:2,odd:2

# numbers = [1,2,3,4]
# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("even numbers", even_count)
# print("odd numbers", odd_count)

# 11. Find the product of all elements in a list IP:[2,3,4] OP[24]

# myList=[2,3,4]
# res=1
# for val in myList:
#     res*=val
# print(res)


# 13. Find Duplicates in a List (Return List of Duplicates) IP[1,2,3,2,1,4] OP[2,1]

# def find_duplicates(items):
#     seen = set()
#     duplicates = []
#     for item in items:
#         if item in seen:
#             duplicates.append(item)
#         else:
#             seen.add(item)
#     return duplicates

# myList=[1,2,3,2,1,4]
# print(find_duplicates(myList))

# 14. In a list of array store even and odd numbers in a new list and print

# myList = [1,2,3,4,5,6,7,8]
# even=[]
# odd=[]
# for num in myList:
#     if num%2==0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("even numbers are",even)
# print("odd numbers are",odd)


# TUPLE
# 1. add a new elements in tuple without using list constructor. IP(1,2,3,4,5) OP(1,2,3,4,5,6,7,8,9,10)

# myTuple=(1,2,3,4,5)
# new_element=(6,7,8,9,10)
# new_tuple=myTuple+new_element
# print(new_tuple)

# 2. add a new elements in tuple without using list constructor. IP(“python”,”C”,”C++”) OP(“python”,”C”,”C++”,”java”,”java script”,”node js”)

# myTuple=("python,C,C++")
# new_element=("java,java script,node js")
# new_tuple=myTuple+new_element
# print(new_tuple)

# number=int(input("enter a number:"))


# mytuple=(1,2,3,4,5)


# myList=[]


# for i in mytuple:
#     myList.append(i)


# print(myList)

# myList.append(6)


# mytuple=tuple(myList)

# print(mytuple)






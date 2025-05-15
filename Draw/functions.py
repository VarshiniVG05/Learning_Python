#  LAMBDA TASK

# 1. add 2 numbers

# add_two_numbers=lambda x,y:x+y
# x=1
# y=2
# result=add_two_numbers(x,y)
# print(result)

# 2. find the maximum of 2 numbers 

# max_number=lambda x,y: x if x>y else y
# x=7
# y=4
# result=max_number(x,y)
# print(result)

# 3. square a number

# square_of_number=lambda x: x**2
# x=5
# result=square_of_number(x)
# print(result)

# 4. reverse a string

# reverse_string = lambda x: ''.join(reversed(x))
# x="varshini"
# result=reverse_string(x)
# print(result)

# 5. check if a number is even 

# is_even=lambda x: "even" if x%2==0 else "odd"
# print(is_even(5))


# ARGUMENTS AND KEYWORD ARGUMENTS TASK 

# 1. sum of all arguments 

# def sum_args(*args):
#     result=0
#     for x in args:
#         result +=x
#     return result 
# print(sum_args(1,2,3,4))

# 2. multiply all arguments

# def product_args(*args):
#     result=1
#     for x in args:
#         result *=x
#     return result
# print(product_args(2,3))

# 3. concatenate all arguments

# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args:
#         result += str(arg)
#     for key, value in kwargs.items():
#         result += str(value)
#     return result
# print(concatenate("happy"," may day"))

# 4. Print arguments and keywords 

# def print_argument(*args):
#     print(print_argument("arg"))

# def print_kwargs(**kwargs):
#     print(print_kwargs("kwarg"))

# 5. display dictionery contents

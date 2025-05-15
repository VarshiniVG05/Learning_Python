# REGEX

# 1. create a content for email id pattern,mobile number and pincode

# import re

# email_pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# mobile_pattern=r'^[6-9]\d{9}$'
# pincode_pattern=r'^[1-9][0-9]{5}$'

# email="varshinivg05@gmail.com"
# mobile="9655196455"
# pincode="605011"

# if re.match(email_pattern, email):
#     print(email)
# else:
#     print("invalid email")

# if re.match(mobile_pattern, mobile):
#     print(mobile)
# else:
#     print("invalid mobile number")

# if re.match(pincode_pattern, pincode):
#     print(pincode)
# else:
#     print("invalid pincode")

# # 2. ask user to enter email and pincode, check if it is valid or not 

# import re
# email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# pincode_pattern = r'^[1-9][0-9]{5}$'

# email = input("enter your email id: ")
# pincode = input("enter your pincode: ")

# if re.match(email_pattern, email):
#     print("valid email id")
# else:
#     print("invalid email id")

# if re.match(pincode_pattern, pincode):
#     print("valid pincode")
# else:
#     print("invalid pincode")
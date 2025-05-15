# from pymongo import MongoClient
# client=MongoClient("mongodb+srv://varshinivg05:gowrivenkat%4003@cluster0.krza4sw.mongodb.net/")
# db=client.VGV
# collection1=db.students
# collection2=db.employees

# student={
#     "name":"Varshini",
#     "age": 20,
#     "course": "Data Analytics"
# }

# res=collection1.insert_one(student)
# print(res.inserted_id)

# studentsData=[
#     {
#     "name":"Jana",
#     "age":"21",
#     "course":"MBA"
# },
# {
#     "name":"Vithya",
#     "age":"21",
#     "course":"BCom"
# },
# {
#     "name":"Harini",
#     "age":"20",
#     "course":"Python"
# }
# ]

# res=collection1.insert_many(studentsData)
# print (res.inserted_ids)

# employeesData=[
#     {
#     "name":"Shereen",
#     "age":"40",
#     "course":"MBA"
# },
# {
#     "name":"Shree",
#     "age":"31",
#     "course":"BCom"
# },
# {
#     "name":"Sheela",
#     "age":"35",
#     "course":"Python"
# }
# ]

# res=collection2.insert_many(employeesData)
# print (res.inserted_ids)



# res=collection1.find()
# for i in res:
#     print(i)

# query={"name":"Vithya"}
# res=collection1.find(query)
# for i in res:
#     print (i)
# previous_data={"course":"MBA"}
# present_data={"$set":{"course":"Java"}}
# collection1.update_one(previous_data,present_data)

# client=MongoClient("mongodb+srv://varshinivg05:gowrivenkat%4003@cluster0.krza4sw.mongodb.net/")
# db=client["user_database"]  
# collection=db["users"]  

# def register_user():
#     name=input("enter your name: ")
#     email=input("enter your email: ")
#     password=input("enter your password: ")
#     phone=input("nter your phone number: ")

#     user_data={
#         "name":name,
#         "email":email,
#         "password":password,
#         "phone":phone
#     }
#     res=collection.find()
#     result=collection.insert_one(user_data)
#     print(f"user registered with ID:{result.inserted_id}")

# # register_user()

# def login_user():
#     email=input("enter your email: ")
#     password=input("enter your password: ")

#     user=collection.find_one({"email": email})

#     if user:
#         if user["password"]==password:
#             print("login successful!")
            




#         else:
#             print("incorrect password.")
#     else:
#         print("user not found,please register")

# # login_user()


# user=input("do you want to reg or login?")


# if user=="reg":
#     register_user()
# elif user=="login":
#     login_user()

# else:
#     print("give valid input..")

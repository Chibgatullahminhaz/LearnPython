#
# def voter(age):
#     if age <18:
#         raise Exception("invalid for voting")
#     return  "valid for voting"
# print(voter(17))

num1 = input(input("Enter the first number"))
num2 = input(input("Enter the last number"))

try:
    result = num1 / num2
    print(result)
except TypeError:
    print("this is type Eror")


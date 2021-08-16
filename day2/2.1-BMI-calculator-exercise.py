# Height = input("enter your height in m: ")
# Weight = input("enter your weight in kg ")
# BMI = Height / Weight ** 2
# print (BMI)
# above code is not working as unsupported operand type -- str and int !!

Height = input ("Enter your Height in meters : ")
Weight = input (" Enter your weight in KG: ")

BMI = int(Weight) / float(Height) ** 2
# print (type (Height))
# print(BMI)
BMI_as_INT = int(BMI)
print (BMI_as_INT)

num_char = len(input ("what is your name ?" ) )
# print ("your name has " + num_char + "Characters.")

# Above code is not working as concatenation can be hasppend between string to sting not between sting to integer
# we can check the Data type

# print (type (len (input("what is your name ?" ) ) ) )

# Below code to do conversion 

num_char = len (input("what is your name ?" ) )
new_num_char =str(num_char)
print ("your name has " + new_num_char + "characters")
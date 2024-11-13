# Hello = 'My Name is sajol'
# print(Hello)
# print(type(Hello))

# str concentrate

# A = 'Hi ! I am sajol'
# B = 'Okey, No problem. You can go'
# print(A + ' '+ B)

# # Join 
# C = ['Bird', 'Fruit', 'Tree', 'ANimal']
# result = " ".join(C)
# print(result)
# print(" ".join(C))

# # Type
# print(type(C))
# print(type(A))
# print(type(B))

# # Count 
# print(C.count('e'))
# print(B.count('a'))
# print(A.count('v'))

# For loop 
# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     print(x)
#     print(fruits)

# print('_____________________')   

  
# Country = ['BD', 'CA', 'AU', "SZ"]
# import time 
# for x in Country:
#     print(Country)
#     time.sleep(2)
    
# print('_____________________')   

# Number = [1,2,3,4]
# print("", type(Number))

# print('_____________________')   

# Hello = ["My name is sajol"]
# for x in Hello:
#     print(x)
#     print(Hello)

# print('_____________________')   
    
# Bird = ['I saw a nice bird','Its blue colour']
# import time
# for y in Bird:
#     print(y)
#     time.sleep(2)

# print('_____________________')   
    
# Art = ['why is my art', '0123456']
# for i in range(5):
#     print(i)
#     print(Art)

# # print('_____________________')   

# language = "Python"
# for z in range(len(language)):
#     print(f'language')

# print(f'language'{z+1: } # Working

# for i in range(len(word)):
#     print(f"Letter {i+1}: {word[i]}")

#  # print('_____________________')   

# import time
# fruits = ["apple", "banana", "cherry"]
# count = 0
# while True:
# print(fruits[count])
# count += 1
# print(count)
# time.sleep(1)
# if len(fruits) == count:
# break

# Practice 
# Think = ['Tree','Fish','Bridge','01916', 0.254]

# print(Think)
# print(type(0))
# print(type(1))
# print(type(2))

# Join
# words = ["Hello", "World"]
# # result = " ".join(words)  
# # # print(result)
# # print(''. join(words))

# # Count 
# print(words.count("H"))
# print(words.count("i"))

# Class 7 
# If, else, for loop, while loop 

# Today_class = input('Eneter your class name: ')
# if Today_class == ("programming"):
#     print("I love programming")
#     print("I am writing code")
    
# else: 
#     print("wrong input")
    
# # while loop 
# while True:
#     x = input("Enter your password: ")
#     if x == ("Lovebd"):
#         for i in range(10):
#             print(i)
#     else:
#         print("Please input right password")
        
# while True:
#     abc = int(input("Enter your code: "))
#     if abc == 45:
#         for xyz in range(5):
#             print(xyz)
            
#     else:
#         print("Please input your password")


# Practive 23 # Code error
# while True:
#     omg = input("Enter your offer name: ")
#     if omg == ("Free"):
#         if i in range(10):
#             print(i)
#     else:
#         print("please input right number")

    # while True:
    #     Number = int(input("enter the number: "))
    #     if Number == 1:
    #         print("I love bangladesh")
    #         print("I love bird")
    #         print("I love river")
    #         break
            
    #     if Number == 2:
    #         print("She love england")
    #         print("She love train")
    #         print("She love sky")
                
    # for x in range (0,10):
    #     if x == 1:
    #         continue
    #     print(x)

    # for y in range (0,20):
    #     if y == 2:
    #         break
    #     print(y)

# ==================================
# var_name = input("Enter the name: ")
# if var_name == "SAJAL":
#     print("Sajal Rahaman") 
#     print("Canada") 
# else:
#     print("Wrong Input")

# ==================================
# while True:
#     x = int(input("Enter the value: "))
#     if x == 1:
#         for y in range(10):
#             print(y)
#     else:
#         print("please check your input value!")



# ==================================
# number = input("Enter the number: ")
# if int(number) == 1:
#     print("Nexus Technologies")
#     print("Python Programming Language")
#     print("Ring Road, Dhaka")

# ==================================
# for x in range(0, 10):
#     print(x)
#     if x == 7:
        # break

# ==================================
# for x in range(0, 10):
#     if x == 7:
#         continue
#     print(x)

# ==================================
# while True:
#     number = int(input("Enter the number: "))
#     if number == 1:
#         print("======================")
#         print("Nexus Technologies")
#         print("Python Programming Language")
#         print("Ring Road, Dhaka")
#         break 
#     if number == 2:
#         print("======================")
#         print("Dhaka University")
#         print("Python Programming Language")
#         print("Bangladesh")

# ==================================
# for x in range(0, 100):
#     number = int(input("Enter the number: "))
#     if number == 1:
#         print("Nexus Technologies")
#         print("Python Programming Language")
#         print("Ring Road, Dhaka")
#     if number == 2:
#         print("Dhaka University")
#         print("Python Programming Language")
#         print("Bangladesh")


# ============== List Method Oparations ==================== 
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# ==================================
# plist = ["Python", "Java", "C"]
# while True:
#     x = int(input("Enter the number: "))
#     if x == 1:
# #         for x in enumerate(plist):
#             print(x)
#     elif x == 2:
#         udata = input("\tEnter the new item: ")
#         plist.append(udata)
#         print("\tNew Data add Sucessfuly")
#     elif x == 3:
#         udata = input("\tEnter the count item: ")
#         print("\tResult value is: ",plist.count(udata))
#     elif x == 4:
#         udata = input("\tEnter the remove item: ")
#         print("\tRemove value is: ",plist.remove(udata))
#     elif x == 5:
#         plist.sort()
#         for x in enumerate(plist):
#             print(x)
#     elif x == 0:
#         break
#     else:
#         print("please enter the valid input!")

# print("This is Python programming language")
        
    
# # ==================================
# plist = ["Python", "Java", "C"]
# print(plist[1])
# print("----------------")
# for x in plist:
#     print(x)

# print("----------------")
# # for y in enumerate(plist):
# #     print(y)

# # print("----------------")
# # for y in range(len(plist)):
# #     print( y, plist[y])

# # print("----------------")
# # for abc, abdula in enumerate(plist):
# #     print(abc, abdula)

# citylist = ["Dhaka, Khulna, Sylhet, Cumilla"]
# while True:
#     x = input("Enter you city name: ")
#     if x == "CTG":
#         for x in enumerate(citylist):
#             print(x) 
#     elif x == "BCT":
#         newcity = input("\tEnter your new city: ")
#         citylist.append(newcity)
#         print("\tNew city add sucessfully")
        
#     elif x == 3:
#         clear_city = input("\tClear your old city: ")
#         citylist.clear(clear_city):
#         print("\tOld city clear sucessfully")
    
#     elif x == 4:
#         Copy_city = input("\tCopy your new city")
#         citylist.copy(Copy_city):
#         print("\tNew city copy sucessfully")
    
#     elif x == 5:
#         coun_city = input("\tCount the city name: ")
#         citylist.count(c):
#         print("\tCity count sucessfully")
        
#     elif x == 6:
#         Exte_city = input("\tEnter your extend city name: ")
#         citylist.extend(Exte_city)
#         print("\tExtend city name sucessfully")
    
    
# 11 method of list
# Appending a Single Item to a List
# List = [10, 20, 30, 40]
# List.append(50)
# print(List)

# Appending Elements to a List in a Loop
# Numbers = [1,2,3,4]
# List = [5,6,7]
# for Numbers in Numbers:
#     List.append(Numbers)
#     print(List)
    
# # Appending Lists to Create a Nested List  
# list = [7,8,9]
# list.append([1,2])
# list.append([3,4])
# list.append([5,6])
# print(list)

# Appending User Input to a List
# user_input = []   
# for i in range(5):
#     value = input("Enter your name: ")
#     user_input.append(value)
#     print(user_input)

# def user_info():
#     name = input("Enter the name: ")
#     age = int(input("Enter the age: "))
#     mobile = input("Enter the number: ")
#     print("==================================")
#     print("Your name is: " + name)
#     print("Your age is: " , age)
#     print(f"Your number is: {mobile}")
         

# def user_info():
#     Name = input("Enter your name: ")
#     Location = input("Enter your location: ")
#     Number = int(input("Enter your phonce number: "))
#     print("Your name is: " + Name)
#     print("Your location is: ", Location)
#     print(f"Your phone number is: {Number}")
# user_info()
    
# Practice home work
# def desi_murgi():
#     Food_quentity = input("Enter total food quentity: ")
#     Food_variation = input("Enter diferent types of food: ")
#     print("Total food quantity will be: "+ Food_quentity)
#     print("We nedd: "+ Food_variation, 'those types of food')
# desi_murgi()
# # Food_materials = ["Wheat, Corn, Soybean"]
# # while True:
# #     x =


# # Duplicate name count  
# Name = ["Rahim", "Karim", "Masud", "Rahim", "Karim", "Sakil", "Sakib", "Kamrul"]
# def duplicate_count(Name)

STD_Name = ["Rafi, Tausif, Kona, Henry, Sany"]

# Class 7 student info
def Rafi_Info():
    print("Name: Md Rafi Ahmed")
    print("Father Name: Md Akbor ALi")
    print("Mother Name: Taslima Akther")
    print("Class: 7")
    print("Roll No: 1")
    print("Home Address: 8665 New Saddle Drive St. Mary's, ON N4X1N8")
    print("BOD: 15 june 2012")
    print("Contact Number: 482.570.1798")

def Tausif_Info():
    print("Name: Md Tausif Khan")
    print("Father Name: Md Suvhan Molla")
    print("Mother Name: Jorina Begum")
    print("Class: 7")
    print("Roll No: 2")
    print("Home Address: 8069 Shadow Brook Circle, QC J0H 7G7 ")
    print("BOD: 10 August 2011")
    print("Contact Number: 1-655-300-3071")
   
# Class 6 student info    
def Kona_Info():
    print("Name: Miss Kona")
    print("Father Name: Md Afjal Hossain")
    print("Mother Name: Miss Selina Begum")
    print("Class: 6")
    print("Roll No: 20")
    print("Home Address: 318 Creek Circle, Lockport, MB R1B 7B1 ")
    print("BOD: 5 November 2014")
    print("Contact Number: 1-746-658-1176")

def Henry_Info():
    print("Name: Henry Anrew")
    print("Father Name: Steve Andrew")
    print("Mother Name: Anjel Grew")
    print("Class: 6")
    print("Roll No: 15")
    print("Home Address: 7047 Devonshire Rd, AB T1P 1N2 ")
    print("BOD: 20 December 2015")
    print("Contact Number: 952-608-6169")
    
# Class 5 student info 
def Sany_Info():
    print("Name: Sany Ulla Rahman")
    print("Father Name: Md Jashim Uddin")
    print("Mother Name: Jahan Akter Tuli")
    print("Class: 5")
    print("Roll No: 5")
    print("Home Address: 958 Roberts Rd, Mont-Laurier, QC J9L 8R7")
    print("BOD: 28 March 2016")
    print("Contact Number: 487-610-3583")  

# # Basic
# clname = input("Enter your class: ")
# if clname == "7":
#     roll = input("Enter your roll number: ")
#     if roll == "1":
#         Rafi_Info()
#     elif roll == "2":
#         Tausif_Info()
#     else:
#         print("Enter your valid roll number")
# else:
#     print("Enter your valid class name")

#While loop
while True:
    cname = int(input("Enter your class: "))
    if cname in range(5, 8):
        roll = int(input("Enter your roll number: "))
        if roll == 1:
            Rafi_Info()
        elif roll == 20:
            Kona_Info()
        elif roll == 5:
            Sany_Info()
        elif roll == 2:
            Tausif_Info()
        elif roll == 15:
            Henry_Info()
        else:
            print("Enter your valid roll")
    else:
        print("Enter your valid class")
    
    
While loop


        



    
    
    
    
    
    
    
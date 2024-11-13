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

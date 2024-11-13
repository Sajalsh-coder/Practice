# While loop
from practice import * #Import data from old file 
std_list = ["Rafi, Tausif, Kona, Henry, Sany"]
while True:
    name = input("\t Enter your name please: ")
    if name in std_list:
        if name == "Kona":
            Kona_Info()
        elif name == "Henry":
            Henry_Info()
    else:
        print("Please Input Valid Name")

import csv
from pprint import pprint

print("hyy there this strekyy ")
print("i want to tell something you just tell you name broooo")
Name = input("entre you name brooo :").strip().lower()


with open ('friend.csv','r') as f :
    reader = csv.DictReader(f)
    
    found = False

    for i in  reader :
        if i["Name"].strip().lower() == Name :
            pprint(i)
            found = True
            break 
        
    else :
        print("your name is not found brooo")

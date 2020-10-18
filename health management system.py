''' 28.9.20-29.9.20
author-manas verma

Instructions:
1. Create a food log file for each client
2. Create an exercise log file for each client.
3. Ask the user whether they want to log or retrieve client data.
4. Write a function that takes the user input of the client's name. After the client's name is entered,
   A message should display "What you want to log. Diet or Exercise"


 Use function

def getdate():
           import datetime
           return datetime.datetime.now()


The purpose of this function is to give time with every record of food or exercise added in the file.
Write a function to retrieve exercise or food file records for any client.

clents names = harry, rohan and hamad
'''

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")
print("health management system: ")
a=int(input("press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)








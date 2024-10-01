#dictionary in python
'''
A dictionary makes use of key-value pairs
'''
'''
Check user auth
if balance is lower than 300 print insufficient balance otherwise allow withdrawal
user should be able to add to balance -deposit

'''
Sample_db={
       "1": {"Name":"Trevor" ,
           "Age":30,
           "Account":"00001",
           "Balance":1000
           },
         "2": {"Name":"Mike" ,
           "Age":25,
           "Account":"00002",
           "Balance":1000
           },
          "3": {"Name":"Tom" ,
           "Age":30,
           "Account":"00003",
           "Balance":1000,          
           },
             "4": {"Name":"Ezekiel" ,
           "Age":27,
           "Account":"00004",
           "Balance":1000,          
           },
         
}


'''
methods in dictionary
'''

print("Welcome to our Bank")
username = input("Please enter your name")
accountname = ""
for usern in Sample_db.values():
     if username == usern["Name"]:
        print("Welcome ", username)
        print("Your Account Number is" , usern["Account"])
        print("Your current Balance is" , usern["Balance"])
     else:
         print("Invalid user")
   
if username == Sample_db["1"]["Name"]:
     print("Welcome ", username)
     print("Your Account Number is" , Sample_db["1"]["Account"])
     print("Your current Balance is" , Sample_db["1"]["Balance"])
elif username == Sample_db["2"]["Name"]:
     print("Welcome ", username)
     print("Your Account Number is" , Sample_db["2"]["Account"])
     print("Your current Balance is" , Sample_db["2"]["Balance"])
elif username == Sample_db["3"]["Name"]:
     print("Welcome ", username)
     print("Your Account Number is" , Sample_db["3"]["Account"])
     print("Your current Balance is" , Sample_db["3"]["Balance"])

else:
    print("Invalid user")

un = ""  
for key in Sample_db.values():
    if key["Name"]  == "Ezekiel":
        un = "Ezekiel"

if un != "":
    print("The current value of un is " , un)
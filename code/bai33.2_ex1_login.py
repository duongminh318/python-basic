dic={"user1":"123456",
     "user2":"123456",
     "user3":"123456",
      "user4":"123456",
     "user5":"123456",
     "user6":"123456",
     "user7":"123456",
     "user8":"123456",
     "user9":"123456",
     "user10":"123456",
     }

while True:
    name= input("enter user name: ")
    if name in dic:
        password= input("enter Password: ")
        if dic[name] == password:
            print("Login successful!")
            break
        else:
            print("wrong password!, Please try again")
    else:
        print("user not exist, Please try again")

import os.path

jsonfile = """{
  "first_account":{
    "CLIENT_ID":"",
    "CLIENT_SECRET":"",
    "USERNAME":"",
    "PASSWORD":""
  },
  "second_account":{
    "CLIENT_ID":"",
    "CLIENT_SECRET":"",
    "USERNAME":"",
    "PASSWORD":""
  },
  "third_account":{
    "CLIENT_ID":"",
    "CLIENT_SECRET":"",
    "USERNAME":"",
    "PASSWORD":""
  },
  "fourth_account":{
    "CLIENT_ID":"",
    "CLIENT_SECRET":"",
    "USERNAME":"",
    "PASSWORD":""
  },
  "fifth_account":{
    "CLIENT_ID":"",
    "CLIENT_SECRET":"",
    "USERNAME":"",
    "PASSWORD":""
  }
}
"""

acc = open("../data/AccountConfig.txt", "w")
acc.write(jsonfile)
acc.close()
exit()

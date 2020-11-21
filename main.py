import eel
import os
import subprocess
import json

eel.init("web")

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
AdsText = """Ads are chosen at random.
Use a new ad in every line:
ad #1
ad #2
ad #3
If you are using multiple accounts, it's best to have more ads."""


@eel.expose
def OpenAccounts():
    #Open account config
    subprocess.Popen("data\\AccountConfig.txt", shell=True)

@eel.expose
def OpenAds():
    #Open ad list
    subprocess.Popen("data\\AdList.txt", shell=True)

#There is probably and easier way of doing this but idk it
def CheckAccounts():
    with open("data\\AccountConfig.txt") as json_file:
        data = json.load(json_file)
    if data["first_account"]["CLIENT_ID"] == "":
        a = 0

    if not data["first_account"]["CLIENT_ID"] == "":
        if not data["first_account"]["CLIENT_SECRET"] == "":
            if not data["first_account"]["USERNAME"] == "":
                if not data["first_account"]["PASSWORD"] == "":
                    eel.sendLog("First account loaded\n")
                    a = 1

    if not data["second_account"]["CLIENT_ID"] == "":
        if not data["second_account"]["CLIENT_SECRET"] == "":
            if not data["second_account"]["USERNAME"] == "":
                if not data["second_account"]["PASSWORD"] == "":
                    eel.sendLog("Second account loaded\n")
                    a = 2

    if not data["third_account"]["CLIENT_ID"] == "":
        if not data["third_account"]["CLIENT_SECRET"] == "":
            if not data["third_account"]["USERNAME"] == "":
                if not data["third_account"]["PASSWORD"] == "":
                    eel.sendLog("Third account loaded\n")
                    a = 3

    if not data["fourth_account"]["CLIENT_ID"] == "":
        if not data["fourth_account"]["CLIENT_SECRET"] == "":
            if not data["fourth_account"]["USERNAME"] == "":
                if not data["fourth_account"]["PASSWORD"] == "":
                    eel.sendLog("Fourth account loaded\n")
                    a = 4

    if not data["fifth_account"]["CLIENT_ID"] == "":
        if not data["fifth_account"]["CLIENT_SECRET"] == "":
            if not data["fifth_account"]["USERNAME"] == "":
                if not data["fifth_account"]["PASSWORD"] == "":
                    eel.sendLog("Fifth account loaded\n")
                    a = 5
    return a

@eel.expose
def main(server_invite, post_delay, delay_type):
    #Check invite link and delay
    if server_invite == "":
        eel.sendLog("Invalid server invite\n")
        return

    if post_delay == "":
        eel.sendLog("Invalid post delay\n")
        return

    #Always things delay is too short
    if delay_type == "Minutes":
        if post_delay == "0" or "1" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" or "14":
            eel.sendLog("Minumum delay is 15 minutes\n")
            return

    #says a is not defined
    #Check how many accounts are in use
    CheckAccounts()
    if a == 0:
        eel.sendLog("No accounts detected\nConfigure accounts and retry\n")

    elif a == 1:
        eel.sendLog("\nProceeding with one account\n")
        #start script with 1 acc

    elif a == 2:
        eel.sendLog("\nProceeding with two accounts\n")
        #start script with 2 accs

    elif a == 3:
        eel.sendLog("\nProceeding with three accounts\n")
        #start script with 3 accs

    elif a == 4:
        eel.sendLog("\nProceeding with four accounts\n")
        #start script with 4 accs

    elif a == 5:
        eel.sendLog("\nProceeding with five accounts\n")
        #start script with 5 accs


#Make directories if they dont already exist
if not os.path.isdir("data"):
    os.mkdir("data")

if not os.path.isfile("data/AccountConfig.txt"):
    acc = open("data/AccountConfig.txt", "w")
    acc.write(jsonfile)
    acc.close()
    eel.sendLog("Created data/AccountConfig.txt\n")

if not os.path.isfile("data/AdList.txt"):
    ads = open("data/AdList.txt", "w")
    ads.write(AdsText)
    ads.close()
    eel.sendLog("Created data/AdList.txt\n")



eel.start("main.html", size=(705, 305))

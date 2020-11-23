import eel
import os
import subprocess
import json
import praw
import random

eel.init("web")

@eel.expose
def OpenAccounts():
    #Open account config
    subprocess.Popen("data\\AccountConfig.txt", shell=True)

@eel.expose
def OpenAds():
    #Open ad list
    subprocess.Popen("data\\AdList.txt", shell=True)

@eel.expose
def CheckInputs(server_invite, post_delay, delay_type):
    global invite
    global delay
    invite = server_invite

    #Check invite link
    if server_invite == "":
        eel.sendLog("Invalid server invite.\n")
        return
    #Check delay
    if (post_delay == "" or post_delay == "0"):
        eel.sendLog("Invalid post delay.\n")
        return

    try:
        pd = int(post_delay) #convert to integer

    except ValueError:
        eel.sendLog("Invalid post delay.\n")
        return

    if delay_type == "Minutes":
        if pd < 15 :
            eel.sendLog("Minumum delay is 15 minutes.\n")
            return
        delay = pd * 60 #Convert to minutes

    if delay_type == "Hours":
        delay = pd * 60 * 60 #Convert to hours

    if (delay_type == "Hours" and post_delay == "1"):
        eel.sendLog("Delay set to: " + post_delay + " hour.\n")

    else:
        eel.sendLog("Delay set to: " + post_delay + " " + delay_type.lower() +".\n")

    #Check how many accounts are in use
    CheckAccounts()
    if a == 0:
        eel.sendLog("\n[ERROR] No accounts detected\nConfigure accounts and retry.\n")

    elif a == 1:
        eel.sendLog("\nProceeding with one account.\n")
        OneAccount()

    elif a == 2:
        eel.sendLog("\nProceeding with two accounts.\n")
        TwoAccounts()

    elif a == 3:
        eel.sendLog("\nProceeding with three accounts.\n")
        ThreeAccounts()

    elif a == 4:
        eel.sendLog("\nProceeding with four accounts.\n")
        FourAccounts()

    elif a == 5:
        eel.sendLog("\nProceeding with five accounts.\n")
        FiveAccounts()

#this could be a seperate file but cbs setting it up
def CheckAccounts():
    global a
    with open("data/AccountConfig.txt") as json_file:
        data = json.load(json_file)
    if data["first_account"]["CLIENT_ID"] == "":
        a = 0

    if not data["first_account"]["CLIENT_ID"] == "":
        if not data["first_account"]["CLIENT_SECRET"] == "":
            if not data["first_account"]["USERNAME"] == "":
                if not data["first_account"]["PASSWORD"] == "":
                    global account_one
                    global account_one_username
                    account_one = praw.Reddit(
                                            client_id=data["first_account"]["CLIENT_ID"],
                                            client_secret=data["first_account"]["CLIENT_SECRET"],
                                            username=data["first_account"]["USERNAME"],
                                            password=data["first_account"]["PASSWORD"],
                                            user_agent='iloveikea')

                    account_one_username = data["first_account"]["USERNAME"]
                    eel.sendLog("First account loaded.\n")
                    a = 1

    if not data["second_account"]["CLIENT_ID"] == "":
        if not data["second_account"]["CLIENT_SECRET"] == "":
            if not data["second_account"]["USERNAME"] == "":
                if not data["second_account"]["PASSWORD"] == "":
                    global account_two
                    global account_two_username
                    account_two = praw.Reddit(
                                            client_id=data["second_account"]["CLIENT_ID"],
                                            client_secret=data["second_account"]["CLIENT_SECRET"],
                                            username=data["second_account"]["USERNAME"],
                                            password=data["second_account"]["PASSWORD"],
                                            user_agent='iloveikea')

                    account_two_username = data["second_account"]["USERNAME"]
                    eel.sendLog("Second account loaded.\n")
                    a = 2

    if not data["third_account"]["CLIENT_ID"] == "":
        if not data["third_account"]["CLIENT_SECRET"] == "":
            if not data["third_account"]["USERNAME"] == "":
                if not data["third_account"]["PASSWORD"] == "":
                    global account_three
                    global account_three_username
                    account_three = praw.Reddit(
                                            client_id=data["third_account"]["CLIENT_ID"],
                                            client_secret=data["third_account"]["CLIENT_SECRET"],
                                            username=data["third_account"]["USERNAME"],
                                            password=data["third_account"]["PASSWORD"],
                                            user_agent='iloveikea')

                    account_three_username = data["third_account"]["USERNAME"]
                    eel.sendLog("Third account loaded.\n")
                    a = 3

    if not data["fourth_account"]["CLIENT_ID"] == "":
        if not data["fourth_account"]["CLIENT_SECRET"] == "":
            if not data["fourth_account"]["USERNAME"] == "":
                if not data["fourth_account"]["PASSWORD"] == "":
                    global account_four
                    global account_four_username
                    account_four = praw.Reddit(
                                            client_id=data["fourth_account"]["CLIENT_ID"],
                                            client_secret=data["fourth_account"]["CLIENT_SECRET"],
                                            username=data["fourth_account"]["USERNAME"],
                                            password=data["fourth_account"]["PASSWORD"],
                                            user_agent='iloveikea')

                    account_four_username = data["fourth_account"]["USERNAME"]
                    eel.sendLog("Fourth account loaded.\n")
                    a = 4

    if not data["fifth_account"]["CLIENT_ID"] == "":
        if not data["fifth_account"]["CLIENT_SECRET"] == "":
            if not data["fifth_account"]["USERNAME"] == "":
                if not data["fifth_account"]["PASSWORD"] == "":
                    global account_five
                    global account_five_username
                    account_five = praw.Reddit(
                                            client_id=data["fifth_account"]["CLIENT_ID"],
                                            client_secret=data["fifth_account"]["CLIENT_SECRET"],
                                            username=data["fifth_account"]["USERNAME"],
                                            password=data["fifth_account"]["PASSWORD"],
                                            user_agent='iloveikea')

                    account_five_username = data["fifth_account"]["USERNAME"]
                    eel.sendLog("Fifth account loaded.\n")
                    a = 5
    return a #i dont think this is needed but im leaving it bc the script works

#############POSTING FUNCTIONS#########################################
def RandomTitle():
    with open('data/AdList.txt') as t:
        global title
        ads = t.readlines()
        rawlines = [line.replace('\n', '') for line in ads]
        title = random.choice(rawlines)

def OneAccount():
    eel.sendLog('Ads will continue to be posted as long as window is open.\n')
    while True:
        RandomTitle()
        account_one.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_one_username + " with ad: " + title)
        eel.sleep(delay)

def TwoAccounts():
    eel.sendLog('Ads will continue to be posted as long as window is open.\n')
    while True:
        #use first account
        RandomTitle()
        account_one.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_one_username + " with ad: " + title)
        eel.sleep(delay)
        #use second account
        RandomTitle()
        account_two.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_two_username + " with ad: " + title)
        eel.sleep(delay)

def ThreeAccounts():
    eel.sendLog('Ads will continue to be posted as long as window is open.\n')
    while True:
        #use first account
        RandomTitle()
        account_one.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_one_username + " with ad: " + title)
        eel.sleep(delay)
        #use second account
        RandomTitle()
        account_two.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_two_username + " with ad: " + title)
        eel.sleep(delay)
        #use third account
        RandomTitle()
        account_three.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_three_username + " with ad: " + title)
        eel.sleep(delay)

def FourAccounts():
    eel.sendLog('Ads will continue to be posted as long as window is open.\n')
    while True:
        #use first account
        RandomTitle()
        account_one.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_one_username + " with ad: " + title)
        eel.sleep(delay)
        #use second account
        RandomTitle()
        account_two.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_two_username + " with ad: " + title)
        eel.sleep(delay)
        #use third account
        RandomTitle()
        account_three.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_three_username + " with ad: " + title)
        eel.sleep(delay)
        #use fourth account
        RandomTitle()
        account_four.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_four_username + " with ad: " + title)
        eel.sleep(delay)

def FiveAccounts():
    eel.sendLog('Ads will continue to be posted as long as window is open.\n')
    while True:
        #use first account
        RandomTitle()
        account_one.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_one_username + " with ad: " + title)
        eel.sleep(delay)
        #use second account
        RandomTitle()
        account_two.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_two_username + " with ad: " + title)
        eel.sleep(delay)
        #use third account
        RandomTitle()
        account_three.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_three_username + " with ad: " + title)
        eel.sleep(delay)
        #use fourth account
        RandomTitle()
        account_four.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_four_username + " with ad: " + title)
        eel.sleep(delay)
        #use fifth account
        RandomTitle()
        account_five.subreddit('discordservers').submit(title, url=invite)
        eel.sendLog("Posted to r/discordservers using: " + account_five_username + " with ad: " + title)
        eel.sleep(delay)

#Make directories if they dont already exist
if not os.path.isfile("praw.ini"):
    subprocess.call('buildprawini.py', shell=True, cwd='subprocesses/')
    eel.sendLog("Created praw.ini.\n")

if not os.path.isdir("data"):
    os.mkdir("data")

if not os.path.isfile("data/AccountConfig.txt"):
    subprocess.call('buildAccountConfig.py', shell=True, cwd='subprocesses/')
    eel.sendLog("Created data/AccountConfig.txt.\n")

if not os.path.isfile("data/AdList.txt"):
    subprocess.call('buildAdList.py', shell=True, cwd='subprocesses/')
    eel.sendLog("Created data/AdList.txt.\n")

eel.start("main.html", size=(705, 305))

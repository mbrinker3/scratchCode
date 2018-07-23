from selenium import webdriver
import selenium
import time
import datetime
def waitForLoad():
    time.sleep(5)

  
def handleError(ch,tab="storyTab"): #Get us back to the Empress' court
    try:
        ch.find_element_by_id("storyTab").click()
    except:
        print("Unable to get to story tab")
    try:
        onwards(ch)
    except:
        print("Not onwards")
    try:
        perhapsNot(ch)
    except:
        print("Not perhaps Not")
    try:
        waitForLoad()
        ch.find_element_by_id(tab).click()
    except:
        print("Unable to go to proper tab.")
    waitForLoad()

def actionsRemaining(ch):
    test = datetime.datetime.now().time().hour
    #automated scripting is technically forbidden. If it continues through the night every night
    #someone might realize what I've done.
    if(True):#test > 6 and test < 22):
        return int(ch.find_element_by_id("infoBarCurrentActions").text)
    else:
        return 0
def perhapsNot(ch):
    waitForLoad()
    ch.find_element_by_xpath("//a[@id='perhapsnotbtn']").click()
def onwards(ch):
    waitForLoad()
    ch.find_element_by_xpath("//input[@value='ONWARDS!']").click()

def stageBallet(ch):
    waitForLoad()
    ch.find_element_by_xpath("//input[@onclick='beginEvent(284698);']").click() #Stage your Ballet
    waitForLoad()
    ch.find_element_by_xpath("(//input[@value='Go'])[5]").click()#A carnelian work
    onwards(ch)


def theLead(ch):
    inspired = 0
    waitForLoad()
    ch.find_element_by_xpath("//input[@onclick='beginEvent(286137);']").click() #The Lead
    while(int(inspired) < 24):
        waitForLoad()
        ch.find_element_by_xpath("(//input[@value='Go'])").click() #go
        waitForLoad()
        inspired = ch.find_element_by_xpath("(//div[contains(@class, 'score')])[4]").text
        if(int(inspired) < 24):
            tryAgain(ch)
    onwards(ch)

def tryAgain(ch):
    waitForLoad()
    ch.find_element_by_xpath("//input[@value='TRY THIS AGAIN']").click()

def Carousel(ch,identifier,goNumber):
    waitForLoad()
    ch.find_element_by_xpath(identifier).click()
    try:
        while(True):
            waitForLoad()
            ch.find_element_by_xpath(goNumber).click()
            tryAgain(ch)
    except:
        perhapsNot(ch)

def startNextWork(ch):
    waitForLoad()
    ch.find_element_by_xpath("//input[@onclick='beginEvent(284601);']").click() #What is your next work
    waitForLoad()
    ch.find_element_by_xpath("(//input[@value='Go'])[6]").click()
    onwards()

def grindForPoets(ch):
    try:
        stageBallet(ch)
    except:
        handleError(ch)
    try:
        startNextWork(ch)
    except:
        handleError(ch)
    try:
        theLead(ch)
    except:
        handleError(ch)

def grindForNotability(ch):
    waitForLoad()
    handleError(ch,"meTab")
    
    carouselList = [
        ["//img[@alt='//images.fallenlondon.com/icons/mountainglowsmall.png - [Scarce] An intriguing scrap of knowledge about a place far across the Unterzee. What can it mean?']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/conversationsmall.png - [Scarce] Unthinkable! Unrepeatable! Inescapable!']","(//input[@value='Go'])[1]"],
        ["//img[@alt='//images.fallenlondon.com/icons/wakesmall.png - [Scarce] Your memories of the lands across the Unterzee are something extraordinary. You can spin them into a tale to delight listeners.']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/bottledsoulbluesmall.png - [Commonplace] This was the soul of someone exceptional. A priest? A poet? A murderer of distinction?']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/scaryeyesmall.png - [Commonplace] The blood freezes! The neck-hairs rise! The spine crackles with fear! The audience is spellbound!']","(//input[@value='Go'])[2]"],
        ["//div[@id='infoBarQImage830']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/mirrorsmall.png - [Scarce] You saw something inexplicable. A rotting, succulent light lingers in your memories... [This item can be sold... but the merchants of the Bazaar are not permitted to offer cash for it, only secrets.]']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/waves3small.png - [Scarce] Strange truths are told of the waves and what lies beneath. The lies are even stranger.']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/bottlewillowsmall.png - [Commonplace] Get it off! GET IT OFF!']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/wakesmall.png - [Scarce] Your memories of the lands across the Unterzee are something extraordinary. You can spin them into a tale to delight listeners.']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/scrap2small.png - [Scarce] Wo ven in Polythreme, they say, from the sweetest of voices.']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/bookpurplesmall.png - [Commonplace] Here is recorded wickedness to freeze the blood and ravage the soul!']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/scrawl1small.png - [Scarce] A lead plaque incised, carefully, with Correspondence sigils. Not too many. Apparently even lead can burn.']","(//input[@value='Go'])[2]"],
        ["//img[@alt='//images.fallenlondon.com/icons/sunsetsmall.png - [Scarce] Wistful souls in London will pay dearly for news of the sky.']","(//input[@value='Go'])[1]"],
        ]
    for item in carouselList:
        try:
            Carousel(ch,item[0],item[1])
        except Exception as ex:
            print(ex.args)
            handleError("meTab")

ch = webdriver.Chrome()
ch.get("http://fallenlondon.storynexus.com/")
username = ch.find_element_by_id("emailAddress")
password = ch.find_element_by_id("password")
username.send_keys("")
password.send_keys("")
ch.find_element_by_class_name("homepage-btn").click()
while True:
    if(actionsRemaining(ch) == 20):
       grindForNotability(ch)
    else:
        time.sleep(60*10)#sleep for ten minutes
#####################################################################################################################################################################################
# File:         drivers.py
# Version:      1.0
# Author:       Aldo_Fonts
# Description:  The current file has the driver to star with automation in Jira
#####################################################################################################################################################################################
# Library/ies
from selenium import webdriver
# Function(s)
def webDriver(browser):
    # Upper case to the browser
    browser = browser.upper()
    try:
        if(browser == 'CHROME'):
            driver = chromeDriver()
        elif(browser == 'FIREFOX'):
            driver = firefoxDriver()
        elif(browser == 'EDGE'):
            driver = edgeDriver()
        elif(browser == 'SAFARI'):  
            driver = safariDriver()
    except:
        print("Unrecognized browser")
    else:
        return driver
        
def chromeDriver():
    options = webdriver.ChromeOptions()
    # The web driver waits until all resources were charged in the web site
    options.page_load_strategy = 'normal'
    # Options to the driver
    # Max size
    options.add_argument("--start-maximized")
    # Bring the driver all the chrome characteristics
    driver = webdriver.Chrome(options=options)
    return driver

def edgeDriver():
    options = webdriver.EdgeOptions()
    # The web driver waits until all resources were charged in the web site
    options.page_load_strategy = 'normal'
    # Options to the driver
    # Max size
    options.add_argument("--start-maximized")
    # Bring the driver all the chrome characteristics
    driver = webdriver.Edge(options=options)
    return driver    

def firefoxDriver():
    options = webdriver.FirefoxOptions()
    # The web driver waits until all resources were charged in the web site
    options.page_load_strategy = 'normal'
    # Options to the driver
    # Max size
    options.add_argument("--start-maximized")
    # Bring the driver all the chrome characteristics
    driver = webdriver.Firefox(options=options)
    return driver

def safariDriver():
    options = webdriver.safari.options.Options()
    # The web driver waits until all resources were charged in the web site
    options.page_load_strategy = 'normal'
    # Options to the driver
    # Max size
    options.add_argument("--start-maximized")
    # Bring the driver all the chrome characteristics
    driver = webdriver.Safari(options=options)
    return driver


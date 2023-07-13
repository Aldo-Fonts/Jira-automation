#####################################################################################################################################################################################
# File:         drivers.py [IN DEVELOP]
# Version:      1.0
# Author:       Aldo_Fonts
# Description:  The current file has the driver to star with automation in Jira
#####################################################################################################################################################################################
# Library/ies
import os
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Packages.login as credentials

# Function(s)
def defineWebSite(driver):
    driver.get("https://id.atlassian.com/login")
    
def clickById(driver, elementId):
    webElement = driver.find_element(By.ID, elementId)
    ActionChains(driver).click(webElement).perform()
    
def clickByCss(driver, elementCss):
    webElement = driver.find_element(By.CSS_SELECTOR, elementCss)
    ActionChains(driver).click(webElement).perform()
    
def writeInInputById(driver, elementId, text):
    webElement = driver.find_element(By.ID, elementId)
    ActionChains(driver).send_keys(text).perform()
    
def writeInInputByCss(driver, elementCss, text):
    webElement = driver.find_element(By.CSS_SELECTOR, elementCss)
    ActionChains(driver).send_keys(text).perform()

def goToMyBoard():
    webSite = []
    with open(os.getcwd() + "/files/myBoard.txt", 'r') as myBoard:
        for line in myBoard:
            webSite.append(line)
    return webSite[0]
    
def login(driver):
    credentials.saveCredentials(True, "aldo.fonts23@gmail.com","Aldo.HF230")
    user, password = credentials.getCredentials()
    # Se obtienen las credenciales
    clickById(driver, "username")
    writeInInputById(driver, "username", user)
    clickById(driver, "login-submit")
    WebDriverWait(driver,timeout=10).until(visibility_of(driver.find_element(By.ID,"password")))
    writeInInputById(driver, "password", password)
    clickById(driver, "login-submit")
    element = WebDriverWait(driver,10).until(presence_of_element_located((By.CSS_SELECTOR,".sc-lhVmIH:nth-child(1) .block-card-content")))
    driver.get(goToMyBoard())

def createTicket(driver):
    try: 
        element = driver.find_element(By.ID,"createGlobalItemIconButton")
        if(element.is_displayed()):
            print("LOOOOOO ENCONTRÉEEEEEE")
            clickByCss(driver,"#createGlobalItemIconButton .css-snhnyn")
            element = WebDriverWait(driver,10).until(visibility_of(driver.find_element(By.ID,"summary-field")))
            
    except:
        createTicket(driver)
        


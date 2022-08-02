import os
import time
import json

import eel

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

dict={}
f=open("./answer.txt","r",encoding="utf-8")
lines=f.read().splitlines()
for index,item in enumerate(lines):
    if index%2==0:
        dict[item]=lines[index+1]
f.close()

with open("./web/questions.json") as f:
    questions=json.load(f)
questions=questions[0:10]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')
s=Service('./chromedriver.exe')

with open("./config.json") as f:
    config=json.load(f)

# function definition

def login(username,pwd):
    driver=webdriver.Chrome(service=s,options=chrome_options)
    driver.get("https://www.wizard101.com/game/")
    account=driver.find_element(By.XPATH,"//*[@id='loginUserName']")
    account.clear()
    account.send_keys(username)
    password=driver.find_element(By.XPATH,"//*[@id='loginPassword']")
    password.clear()
    password.send_keys(pwd)
    loginBtn=driver.find_element(By.XPATH,"//*[@id='wizardLoginButton']/tbody/tr/td[1]/div/div/input")
    loginBtn.click()
    return driver

def checkStatus():
    try:
        content=driver.find_element(By.XPATH,"//*[@id='quizFormComponent']/div[2]/div/h2")
        content=content.text
        if content=="Come Back Tomorrow!":
            return "completed"
    except:
        pass
    return "untracked_error"

def answerQuestion(question):
    global count,driver
    driver.get(question)
    status=checkStatus()
    if status=="completed":
        eel.setTriviaStatus(question,"Completed!")
        count+=1
        if count==10:
            driver.close()
            time.sleep(2)
            return eel.complete()
        return answerQuestion(questions[count])
    previousBtnContent="Next Question!"
    while(previousBtnContent=="Next Question!"):
        try:
            problem=driver.find_element(By.XPATH,"//*[@id='quizContainer']/table[2]/tbody/tr[2]/td[2]/div[1]");
        except:
            print("Problem error:"+question)
            eel.setTriviaStatus(question,"Error:(")
            break
        findAnswer=dict.get(problem.text)
        for i in range(1,5):
            answer=driver.find_element(By.XPATH,"//*[@id='quizContainer']/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i)+"]/span[2]")
            if answer.text==findAnswer:
                answerBtn=driver.find_element(By.XPATH,"//*[@id='quizContainer']/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i)+"]/span[1]/a")
                answerBtn.click()
                while(True):
                    try:
                        nextBtn=driver.find_element(By.XPATH,"//*[@id='nextQuestion']")
                        previousBtnContent=nextBtn.text
                        nextBtn.click()
                        break
                    except:
                        time.sleep(1)
                break
    clarmYourReward=driver.find_element(By.XPATH,"//*[@id='quizFormComponent']/div[3]/div[3]/a")
    clarmYourReward.click()
    eel.handleBotMsg()

@eel.expose
def addUser(username,password):
    config.append({'username':username,'password':password});
    with open("./config.json","w") as f:
        f.write(json.dumps(config,indent=4));

@eel.expose
def getUsers():
    return config;

@eel.expose
def start(username,password):
    global count,driver
    count=0
    driver=login(username,password)
    answerQuestion(questions[count])

@eel.expose
def settle():
    global count,driver
    takeAnotherQuiz=driver.find_element(By.XPATH,"//*[@id='quizFormComponent']/div[3]/div[2]/div/a")
    takeAnotherQuiz.click()
    eel.setTriviaStatus(questions[count],"Completed!")
    count+=1
    if count==10:
        driver.close()
        time.sleep(2)
        return eel.complete()
    return answerQuestion(questions[count])

eel.init("web")
eel.start('main.html',size=(450,600))
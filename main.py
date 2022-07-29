import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

with open("./config.json") as f:
    config=json.load(f)

username=config['username']
pwd=config['password']

counted=0

dict={}
f=open("./answer.txt","r",encoding="utf-8")
lines=f.read().splitlines()
for index,item in enumerate(lines):
    if index%2==0:
        dict[item]=lines[index+1]
f.close()

questions=[
    "https://www.wizard101.com/quiz/trivia/game/wizard101-adventuring-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-conjuring-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-marleybone-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-mystical-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-spellbinding-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-spells-trivia",
    "https://www.wizard101.com/quiz/trivia/game/pirate101-valencia-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-wizard-city-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-zafaria-trivia",
    "https://www.wizard101.com/quiz/trivia/game/book-quotes-trivia",
    "https://www.wizard101.com/quiz/trivia/game/wizard101-magical-trivia"
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')

#log-in
s=Service('./chromedriver.exe')
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

print("Click any button if you resolve bot detect.")
os.system("pause")


previousBtnContent="Next Question!"

for question in questions:
    #if(counted==10):
        #break
    driver.get(question)
    while(previousBtnContent=="Next Question!"):
        time.sleep(7)
        try:
            problem=driver.find_element(By.XPATH,"//*[@id='quizContainer']/table[2]/tbody/tr[2]/td[2]/div[1]");
        except:
            print("problem error:"+question)
            break
        print(problem.text)
        findAnswer=dict.get(problem.text)
        if(findAnswer==None):
            findAnswer=input("Please enter answer:")
        for i in range(1,5):
            answer=driver.find_element(By.XPATH,"//*[@id='quizContainer']/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i)+"]/span[2]")
            if answer.text==findAnswer:
                print("clicked "+answer.text)
                answerBtn=driver.find_element(By.XPATH,"//*[@id='quizContainer']/table[2]/tbody/tr[2]/td[2]/div[2]/div["+str(i)+"]/span[1]/a")
                answerBtn.click()
                nextBtn=driver.find_element(By.XPATH,"//*[@id='nextQuestion']")
                previousBtnContent=nextBtn.text
                nextBtn.click()
                break
    print("Click any button if you resolve bot detect.")
    os.system("pause")
    counted+=1
    previousBtnContent="Next Question!"

print("Work is done")
os.system("pause")
driver.close()
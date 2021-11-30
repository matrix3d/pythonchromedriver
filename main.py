import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("F:\\chromedriver\\chromedriver_win32\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get('https://play.bnbheroes.io/market')
#time.sleep(2)
try:
    closebtn = driver.find_element(By.CSS_SELECTOR,"div.walletconnect-modal__close__wrapper")
    closebtn.click()
except:
    print("except")

running =True
arr=[]
while running:
    heroes=driver.find_element(By.CSS_SELECTOR,"div[class='heroes d-flex flex-wrap justify-content-center px-3']").find_elements(By.XPATH,"div")
    page=driver.find_element(By.CSS_SELECTOR,"a[aria-current=page]").text
    print("----------------"+page+" "+str(len(heroes)))
    try:
        for hero in heroes:
            id=hero.find_element(By.XPATH,"div[2]/div/div[2]").text
            price=hero.find_element(By.XPATH,"div[2]/div[2]/div[2]").text
            bnb=re.findall(r"\d+\.?\d*",price)[0]
            att=hero.find_element(By.XPATH,"div[2]/div[6]/div").text
            attvalue=re.findall(r"\d+\.?\d*",att)[0]
            print("hero"+id+" p:"+str(bnb)+" att:"+str(attvalue))
            arr.append([page,id,bnb,attvalue])
        nextbtn = driver.find_element(By.CSS_SELECTOR, "a.page-link[rel=next][aria-disabled=false]")
        nextbtn.click()
    except:
        running=False
print("over")
def sortFun(elem):
    return elem[2]
arr.sort(key=sortFun)
print(arr[0])
print(arr[len(arr)-1])
driver.quit()
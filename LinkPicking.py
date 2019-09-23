# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:47:52 2019

@author: sabrin sulthana
"""

from selenium import webdriver
import pyautogui
import time
import pymsgbox
from datetime import date
import os
import xlsxwriter

driver = webdriver.Chrome(executable_path='path')
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(2)

keywords=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('infosys')
time.sleep(2)
pyautogui.press('enter')
print(keywords)

# CLICK THE TOOL BUTTON
time.sleep(2)
toolsclick = driver.find_element_by_xpath('//*[@id="hdtb-tls"]').click()
print('The Tools button is clicked in the webpage: ',toolsclick)
response = pymsgbox.prompt(toolsclick,timeout=2000 )

#CLICK THE DROPDOWN BUTTON FIRST AND ANY TIME FOR CLICK THE PAST 24 HOURS
driver.find_element_by_xpath('//*[@id="hdtbMenus"]/div/div[2]/span').click()

def get_url_status():
    


#CLICK THE PAST 24 HOURS
driver.find_element_by_xpath('//*[@id="qdr_d"]/a').click()
elems = driver.find_elements_by_xpath("//a[@href]")
a = len(elems)
print("The length of the links is: ",a)
List = []

for elem in elems:
#    print("The Link is : ")
    hrefs = elem.get_attribute("href")
    List.append(hrefs)
#    print(hrefs)
for elem in List:
    print("The Link is : ",elem)
    
    
    
today = date.today()   
d1 = today.strftime("%d-%m-%Y")
pymsgbox.alert('The current date is:', d1,timeout=1000)
#response = pymsgbox.prompt(d1,timeout=2000 )
dirName = 'D:\\'+str(d1)+'\\Linkpicking Excel Sheet\\'
def main():
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists") 
        time.sleep(2)
if __name__ == '__main__':
     main()
     
workbook = xlsxwriter.Workbook(dirName+'\\linkpicksheet.xlsx') 
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Date' ) 
worksheet.write('B1',  'Links') 
#f = open(dirName+"linkpicksheet.xlsx","w+") 
row=1 
for elem in List:
    #f.write(elem.get_attribute("hrefs"))
     worksheet.write(row, 0, d1 ) 
     worksheet.write(row, 1, elem)
     row += 1
workbook.close()
driver.quit()

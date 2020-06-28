from selenium import webdriver  #SELENIUM LIBRARY
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
import xlsxwriter   #LIBRARY TO WRITE IN EXCEL
import time


options = webdriver.FirefoxOptions()
options.add_argument("--headless")  #OPTION THAT RUN FIREFOX IN BACKGROUND (INSTABLE WITH CHROME)
browserop = webdriver.Chrome(executable_path=r'INSERT YOUR GECKODRIVER PATH', options=options)
browserop.get('https://toolset.mrwebmaster.it/varie/password-generator.html')   #WEB SERVICE LINK
canclungh=browserop.find_element_by_xpath('/html/body/div[2]/section/div[1]/div[3]/div[1]/input').clear()
inslungh=browserop.find_element_by_xpath('/html/body/div[2]/section/div[1]/div[3]/div[1]/input').send_keys("16") #NUMBER OF CHARACTERS
nomin=browserop.find_element_by_xpath('/html/body/div[2]/section/div[1]/div[3]/div[3]/div/div[2]/label').click() #DEACTIVATE LOWERCASE LETTERS
nocar=browserop.find_element_by_xpath('/html/body/div[2]/section/div[1]/div[3]/div[6]/div/div[2]/label').click()  #DEACTIVATE SYMBOLS
workbook= xlsxwriter.Workbook('YOUR EXCEL PATH') #EXCEL FILE TO SAVE THE PASSWORDS
worksheet_pass= workbook.add_worksheet('NAME OF SHEET') #CREATES A NEW EXCEL SHEET

numpass= 25000 #number of passwords that will be generated and saved
exc_row = 0
exc_column = 0

while numpass!=0:     #LOOP
    #time.sleep(0.2)    UNCOMMENT IF YOU WANT TO MAKE IT SLOWER
    gen = browserop.find_element_by_xpath('/html/body/div[2]/section/div[1]/div[3]/div[7]/div[1]/button').click()   #GENERATE BUTTON
    copy = browserop.find_element_by_xpath('/html/body/div[2]/section/div[1]/div[3]/div[7]/div[2]/div/pre')         #SAVES THE PASSWORD INTO A VARIABLE

    #LOOP TO MAKE THE EXCEL FILE CLEAR
    if exc_row==999:
        exc_column+=1
        exc_row=0

    print(copy.text) #PRINTS US THE GENERATED PASSWORD

    worksheet_pass.write(   #WRITES THE PASSWORD INTO EXCEL
        exc_row,
        exc_column,
        copy.text
    )
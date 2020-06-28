from selenium import webdriver  #SELENIUM LIBRARY
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
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

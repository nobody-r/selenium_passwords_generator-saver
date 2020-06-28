from selenium import webdriver  #SELENIUM LIBRARY
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import xlsxwriter   #LIBRARY TO WRITE IN EXCEL
import time


options = webdriver.FirefoxOptions()
options.add_argument("--headless")  #OPTION THAT RUN FIREFOX IN BACKGROUND (INSTABLE WITH CHROME)
browserop = webdriver.Chrome(executable_path=r'INSERT YOUR GECKODRIVER PATH', options=options)

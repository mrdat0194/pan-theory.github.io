from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import util
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys


service = Service(executable_path=r"C:\Users\mrdat\PycharmProjects\pan-theory\main_def\ggl_api\kasa\Automate_data_model\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Global Variable

linkes = ['https://vinfastauto.com/vn_vi', 'https://shop.vinfastauto.com/vn_vi/vinfast-bike.html', 'https://vinfastauto.com/vn_vi/uu-dai']
n = 0
for link in linkes:
    driver.get(link)
    time.sleep(3)

    util.fullpage_screenshot(driver, r"C:\Users\mrdat\PycharmProjects\pan-theory\main_def\ggl_api\kasa\Automate_data_model\Pic" + str(n) + ".png")
    time.sleep(1)
    n+=1
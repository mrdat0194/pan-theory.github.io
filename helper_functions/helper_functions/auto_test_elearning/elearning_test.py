from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\Hello\AI\Webscrape\chromedriver_win32\chromedriver.exe")

driver.get('https://daotao.baominh.vn/')

dataSet = []

element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_MenuLoginMobile_lnkNotAuthen')

driver.execute_script("arguments[0].click();", element)

element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_MenuLoginMobile_lnkNotAuthen')

element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_login_txtUsername')
driver.execute_script('arguments[0].setAttribute("value","admin");', element)

element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_login_txtPassword')
driver.execute_script('arguments[0].setAttribute("value","12345678");', element)

element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_login_lbtnLogin')
driver.execute_script("arguments[0].click();", element)

# # Click vào khung manager góc phải
# element = driver.find_element_by_id('dnn_ctr490_inc_Main_ctl00_divShow')
# driver.execute_script("arguments[0].click();", element)
# # Href bài giảng
# element = driver.find_elements_by_css_selector(".text-center [href]")
# links = [elem.get_attribute('href') for elem in element]
# driver.get(links[0])
# # Quản trị đào tạo
# element = driver.find_elements_by_css_selector(".listmenumobileuser [href]")
# links = [elem.get_attribute('href') for elem in element]
# driver.get(links[0])


driver.get('https://daotao.baominh.vn/Quan-tri/quan-tri-khoa-hoc/khoa-hoc')


# driver.close()
# driver.quit()

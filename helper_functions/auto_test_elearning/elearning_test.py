from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import pickle
import pyautogui
import pyperclip
import re
import os

def login(link):
    '''
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
    :return:
    '''

    driver.get(link)

    dataSet = []
    element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_MenuLoginMobile_lnkNotAuthen')

    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_MenuLoginMobile_lnkNotAuthen')

    element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_login_txtUsername')
    driver.execute_script('arguments[0].setAttribute("value","admin");', element)

    element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_login_txtPassword')
    driver.execute_script('arguments[0].setAttribute("value","12345678");', element)

    select = Select(WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "dnn_cmsHeader_inc_HomeMenuTop_login_ddlUserType"))))
    select.options[1].click()

    element = driver.find_element_by_id('dnn_cmsHeader_inc_HomeMenuTop_login_lbtnLogin')
    driver.execute_script("arguments[0].click();", element)

def them_lop_hoc(tenlop, info_name_edit,info_desc):
    driver.get('https://daotao.baominh.vn/Quan-tri/quan-tri-khoa-hoc/khoa-hoc')

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_btnThem')
    driver.execute_script("arguments[0].click();", element)

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_lbtnAdd')
    driver.execute_script("arguments[0].click();", element)
    name_tenlop = f'arguments[0].setAttribute("value","{tenlop}");'
    time.sleep(1)
    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtName')
    driver.execute_script(name_tenlop, element)

    #Thêm avatar
    element = driver.find_element_by_xpath('//*[@id="collapse1"]/div/div[5]/div/button')
    element.click()
    tenlop_hinh = f"C:\\Users\\PeterN\\PycharmProjects\\pan-theory\\helper_functions\\auto_test_elearning\\avatar\{info_name_edit}.jpg"
    print(tenlop_hinh)

    # imgPath = r'C:\Users\PeterN\PycharmProjects\pan-theory\helper_functions\auto_test_elearning\avatar\%s' %tenlop_hinh
    time.sleep(1)

    pyperclip.copy(tenlop_hinh)
    pyautogui.hotkey('right')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')
    time.sleep(10)

    #Thêm description
    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtDescription_contentIframe')
    driver.switch_to.frame(element)
    element = driver.find_element_by_xpath('/html/body')
    element.clear()
    element.send_keys(info_desc)
    time.sleep(10)
    driver.switch_to.default_content()

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtMaxUser')
    driver.execute_script('arguments[0].setAttribute("value","0");', element)

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtNgayBDDK')
    driver.execute_script('arguments[0].setAttribute("value","30/05/2021");', element)

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtNgayKTDK')
    driver.execute_script('arguments[0].setAttribute("value","30/05/2022");', element)

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtNgayBDH')
    driver.execute_script('arguments[0].setAttribute("value","30/05/2021");', element)

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtNgayKT')
    driver.execute_script('arguments[0].setAttribute("value","30/05/2022");', element)
    time.sleep(1)

    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_lbtnAddClass')
    driver.execute_script('arguments[0].click();', element)

    WebDriverWait(driver, 2).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    time.sleep(1)

def class_getinfo():
    baocao = pd.read_excel('baocaolophoc.xlsx', engine='openpyxl')
    row_indexes = baocao.index
    for row in row_indexes:
        info_name = baocao['Name'].loc[row]
        info_desc = baocao['Description'].loc[row]
        info_avatar = baocao['Avatar'].loc[row]
        info_name_edit = re.sub('[^a-zA-Z0-9 \n\.]', '', info_name)
        print(info_name_edit)
        try:
            down_avatar(info_name_edit ,info_avatar)
            them_lop_hoc(info_name,info_name_edit, info_desc)
        except:
            print(info_name)
            continue

def down_avatar(name, portal_link):
    url = link_source + portal_link
    r = requests.get(url, allow_redirects=True)
    path_to_file = f"avatar/{name}.jpg"
    open(path_to_file, 'wb').write(r.content)

def get_all_class():
    for i in range(284):
         try:
            driver.get('http://attech.aivietnam.vn/Quan-tri/quan-tri-noi-dung/quantribaigiang')
            select = Select(WebDriverWait(driver, 1).until(
             EC.element_to_be_clickable((By.ID, "dnn_ctr437_inc_Main_ctl00_ddlType"))))
            select.options[2].click()
            select = Select(WebDriverWait(driver, 1).until(
             EC.element_to_be_clickable((By.ID, "dnn_ctr437_inc_Main_ctl00_ddlPageSize"))))
            select.options[7].click()
            print(f'//*[@id="tblObject"]/tbody/tr[{i+1}]/td[6]/div/button')
            element = driver.find_element_by_xpath(f'//*[@id="tblObject"]/tbody/tr[{i+2}]/td[6]/div/button')
            driver.execute_script('arguments[0].click();', element)
            element = driver.find_element_by_id(f'dnn_ctr437_inc_Main_ctl00_rptMedia_lnkEdit_{i}')
            driver.execute_script('arguments[0].click();', element)
            time.sleep(5)
            element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtName')
            my_dict['txtName'].append(element.get_attribute("value"))
            element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtDuration')
            my_dict['txtDuration'].append(element.get_attribute("value"))
            element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtFileLocation')
            my_dict['txtFileLocation'].append(element.get_attribute("value"))
         except:
            print(i)
            print(my_dict)
            a_file = open("data_tailieu.pkl", "wb")
            pickle.dump(my_dict, a_file)
            a_file.close()
            break

def down_class():
    for i in range(284):
        try:
            name = my_dict['txtName'][i]
            url = my_dict['txtFileLocation'][i]
            print(url)

            # with connection_pool.request('GET', url, preload_content=True) as resp, open(path_to_file, 'wb') as out_file:
            #     shutil.copyfileobj(resp, out_file)
            #     print(path_to_file)

            info_name_edit = re.sub('[^a-zA-Z0-9 \n\.]', '', name)
            r = requests.get(url)
            path_to_file = f"down/{info_name_edit}.mp4"
            open(path_to_file, 'wb').write(r.content)
        except:
            print("down",i)
            break

def get_and_down():
    get_all_class()
    down_class()


def add_beforeUpload():
    for i in range(284):
        try:
            driver.get('https://daotao.baominh.vn/Quan-tri/quan-tri-noi-dung/quantribaigiang')

            element = driver.find_element_by_id(f'dnn_ctr437_inc_Main_ctl00_lbtnAddVideo')
            driver.execute_script('arguments[0].click();', element)
            time.sleep(1)

            element = driver.find_element_by_id(f'dnn_ctr437_inc_Main_ctl00_rddtCategory')
            driver.execute_script('arguments[0].click();', element)

            WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="dnn_ctr437_inc_Main_ctl00_rddtCategory"]/span/span[1]'))).click()
            WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="dnn_ctr437_inc_Main_ctl00_rddtCategory_EmbeddedTree"]/ul/li/div/span'))).click()
            WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="dnn_ctr437_inc_Main_ctl00_rddtCategory_EmbeddedTree"]/ul/li/ul/li[2]/div/div/span'))).click()

            element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtName')
            driver.execute_script(f'arguments[0].setAttribute("value", "{my_dict["txtName"][i]}");', element)
            print(my_dict["txtDuration"][i])
            element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtDuration')
            driver.execute_script(f'arguments[0].setAttribute("placeholder", "{my_dict["txtDuration"][i]}");', element)

            element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtFileLocation')
            driver.execute_script(f'arguments[0].setAttribute("value", "{my_dict["txtFileLocation"][i]}");', element)

            element = driver.find_element_by_id(f'dnn_ctr437_inc_Main_ctl00_lbtnUpdate')
            driver.execute_script('arguments[0].click();', element)

            WebDriverWait(driver, 2).until(EC.alert_is_present())
            driver.switch_to.alert.accept()

        except:
            print("down", i)
            break



def readCourse_classSource():

    for num in range(109):
        try:
            num_file = str(num)+'.xlsx'
            driver.get('http://attech.aivietnam.vn/Quan-tri/quan-tri-khoa-hoc/khoa-hoc')
            select = Select(WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.ID, "dnn_ctr457_inc_Main_ctl00_ddlPageSize1"))))
            select.options[7].click()
            element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_rptObject_LinkButton1_{num}')
            driver.execute_script('arguments[0].click();', element)
            element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_lbtnExport')
            driver.execute_script('arguments[0].click();', element)
            time.sleep(1)
            os.rename(r'C:\Users\PeterN\Downloads\baocao19.xlsx', r'C:\Users\PeterN\Downloads\%s'%num_file)
        except:
            print(num)

def hoclieu_scorm_video():
    baocao = pd.read_excel('baocaolophoc.xlsx', engine='openpyxl')
    reversed_baocao = baocao.iloc[::-1]
    row_indexes = reversed_baocao.index
    reversed_baocao['typeClass'] = 0
    reversed_baocao['order'] = 0
    for num,index in enumerate(row_indexes):
        try:
            if num != 62 and num != 72:
                driver.get('http://attech.aivietnam.vn/Quan-tri/quan-tri-khoa-hoc/khoa-hoc')
                element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtkey')
                driver.execute_script(f'arguments[0].setAttribute("value", "{reversed_baocao["Name"].loc[index]}");',element)
                element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_lbtnSearch')
                driver.execute_script('arguments[0].click();', element)
                time.sleep(1)

                element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_rptObject_LinkButton1_0')
                driver.execute_script('arguments[0].click();', element)
                print(driver.current_url)
                if driver.current_url != 'http://attech.aivietnam.vn/ErrorPage/404.html':
                    try:
                        driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_rptObject_txtStartTime_0').text
                        element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_rptObject_lbtnEdit_0')
                        driver.execute_script('arguments[0].click();', element)
                    except:
                        element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_rptObject_lbtnEdit_1')
                        driver.execute_script('arguments[0].click();', element)


                    element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_rptData_lblType_0')

                    reversed_baocao['typeClass'].loc[index] = element.text
                    reversed_baocao['order'].loc[index] = num

        except:
            print(num)
            time.sleep(10000)
            reversed_baocao[['order','Name', 'typeClass']].to_excel("baocao.xlsx")

    reversed_baocao[['order','Name', 'typeClass']].to_excel("baocao.xlsx")




def addCourse_classDest():
    pd.set_option("display.max_rows", None, "display.max_columns", 60, 'display.width', 1000)
    baocao = pd.read_excel('baocao.xlsx', engine='openpyxl')
    row_indexes = baocao.index

    # select = Select(WebDriverWait(driver, 1).until(
    #     EC.element_to_be_clickable((By.ID, "dnn_ctr437_inc_Main_ctl00_ddlType"))))
    # select.options[2].click()
    # select = Select(WebDriverWait(driver, 1).until(
    #     EC.element_to_be_clickable((By.ID, "dnn_ctr437_inc_Main_ctl00_ddlPageSize"))))
    # select.options[7].click()
    count = 0
    for row in row_indexes:
        try:
            if baocao["typeClass"].loc[row] == 'Video':

                driver.get('https://daotao.baominh.vn/Quan-tri/quan-tri-khoa-hoc/khoa-hoc')
                element = driver.find_element_by_id('dnn_ctr457_inc_Main_ctl00_txtkey')
                driver.execute_script(f'arguments[0].setAttribute("value", "{baocao["Name"].loc[row]}");', element)
                element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_lbtnSearch')
                driver.execute_script('arguments[0].click();', element)
                time.sleep(1)
                element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_rptObject_LinkButton1_0')
                driver.execute_script('arguments[0].click();', element)
                lopcourse = pd.read_excel(f'lophocsource/{baocao["order"].loc[row]}.xlsx', engine='openpyxl')

                indexes = lopcourse.index
                for index in indexes:
                    if lopcourse['Loại dữ liệu'].loc[index] == 'Bài giảng':
                        element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_lbtnAddVideo')
                        driver.execute_script('arguments[0].click();', element)
                        element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_lbtnChooseMedia')
                        driver.execute_script('arguments[0].click();', element)
                        time.sleep(2)
                        print(lopcourse["Tên tài liệu"].loc[index])
                        element = driver.find_element_by_xpath(f'//*[@id="dnn_ctr457_inc_Main_ctl00_txtKeyword"]')
                        driver.execute_script(f'arguments[0].setAttribute("value", "{lopcourse["Tên tài liệu"].loc[index]}");', element)

                        element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_lbtnSearch')
                        driver.execute_script('arguments[0].click();', element)
                        time.sleep(1)
                        element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_rptMedia_lbtnChoose_0')
                        driver.execute_script('arguments[0].click();', element)
                        time.sleep(1)
                        element = driver.find_element_by_id(f'dnn_ctr457_inc_Main_ctl00_lbtnUpdate')
                        driver.execute_script('arguments[0].click();', element)
                        time.sleep(1)
        except:
            print(row)

# def up_classHoclieu():
#     driver.get('https://daotao.baominh.vn/Quan-tri/quan-tri-noi-dung/quantribaigiang')
#
#     element = driver.find_element_by_id(f'dnn_ctr437_inc_Main_ctl00_lbtnAddVideo')
#     driver.execute_script('arguments[0].click();', element)
#     time.sleep(2)
#
#     element = driver.find_element_by_id(f'dnn_ctr437_inc_Main_ctl00_rddtCategory')
#     driver.execute_script('arguments[0].click();', element)
#
#     # driver.execute_script('arguments[0].click();', element)
#     # select = Select(WebDriverWait(driver, 1).until(
#     #     EC.element_to_be_clickable((By.ID, "dnn_ctr437_inc_Main_ctl00_ddlCategory"))))
#     # select.options[2].click()
#
#     WebDriverWait(driver, 1).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="dnn_ctr437_inc_Main_ctl00_rddtCategory"]/span/span[1]'))).click()
#     WebDriverWait(driver, 1).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="dnn_ctr437_inc_Main_ctl00_rddtCategory_EmbeddedTree"]/ul/li/div/span'))).click()
#     WebDriverWait(driver, 1).until(
#         EC.element_to_be_clickable((By.XPATH, '//*[@id="dnn_ctr437_inc_Main_ctl00_rddtCategory_EmbeddedTree"]/ul/li/ul/li[2]/div/div/span'))).click()
#
#     element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtName')
#     driver.execute_script('arguments[0].setAttribute("value","tenhoclieu");', element)
#
#     element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtFileLocation')
#     driver.execute_script('arguments[0].setAttribute("value","tenhoclieu");', element)
#
#     element = driver.find_element_by_id('dnn_ctr437_inc_Main_ctl00_txtFileLocation')
#     driver.execute_script('arguments[0].setAttribute("value","tenhoclieu");', element)
#
#     time.sleep(160)
#
#     element = driver.find_element_by_id(f'dnn_ctr437_inc_Main_ctl00_lbtnUpdate')
#     driver.execute_script('arguments[0].click();', element)

if __name__ == '__main__':

    driver = webdriver.Chrome(
        r"C:\Users\PeterN\PycharmProjects\pan-theory\Webscrape\chromedriver_win32\chromedriver.exe")
    my_dict = {
        "txtName": [],
        "txtDuration": [],
        "txtFileLocation": []
    }

    # # info_tenlop = read_classInfo("baocao08.xlsx")
    link = 'https://daotao.baominh.vn/'
    link_source = 'http://attech.aivietnam.vn/'
    login(link)
    # login(link_source)
    # # class_getinfo()

    # get_and_down()

    # Hiện mở file dẫn và download ko còn sử dụng
    # a_file = open("data_tailieu.pkl", "rb")
    # my_dict = pickle.load(a_file)
    # a_file.close()
    # down_class()

    # a_file = open("data_tailieu.pkl", "rb")
    # my_dict = pickle.load(a_file)
    # a_file.close()
    #
    # print(len(my_dict['txtDuration']))
    #
    # add_beforeUpload()

    # readCourse_classSource()

    # hoclieu_scorm_video()

    addCourse_classDest()

    # up_classHoclieu()

    #     # driver.close()
    #     # driver.quit()


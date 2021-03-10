from selenium import webdriver
from personal_Data import userName, password

instagram_Login = webdriver.Chrome(executable_path='C:/Users/Kelechi Divine/Downloads/chromedriver_win32'
                                                   '/chromedriver.exe')

instagram_Login.get('https://www.instagram.com/accounts/login/')
instagram_Login.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div'
                                      '[1]/div/label/input').send_keys(userName)

instagram_Login.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div'
                                      '[2]/div/label/input').send_keys(password)

instagram_Login.find_element_by_css_selector('button[type= submit]').click()

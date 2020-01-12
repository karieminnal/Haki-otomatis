from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class EHaki(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def web(self):
        self.driver.get('https://e-hakcipta.dgip.go.id/login')
        sleep(1)
        self.driver.find_element_by_name('username').send_keys("lppm@poltekpos.ac.id")
        sleep(1)
        self.driver.find_element_by_name('password').send_keys('lppm2011')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
        

    def permohonan_baru(self):
        self.driver.get('https://e-hakcipta.dgip.go.id/index.php/register/hakcipta')
        sleep(2)
        self.driver.find_elements_by_class_name('close')[-1].click()
        sleep(2)
        self.driver.find_elements_by_class_name('select2-selection__rendered')[0].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-results__option')[1].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-selection__rendered')[1].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-results__option')[1].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-selection__rendered')[2].click()
        sleep(1)
        self.driver.find_elements_by_class_name('select2-results__option')[4].click()
        sleep(1)
        self.driver.find_element_by_name('title').send_keys('Tutorial Penggunaan Kepo')
        sleep(1)
        self.driver.find_elements_by_name('description')[1].send_keys('Tutorial Penggunaan Kepo')
        sleep(1)
        date = self.driver.find_element_by_xpath('//*[@id="createform"]/div[1]/div[2]/div/div[6]/div/div/input[1]')

        date.click()
        
        for i in range(len(date.get_attribute('value'))):
            date.send_keys(Keys.BACKSPACE)

        date.send_keys("1999-10-10", Keys.ENTER)

        sleep(1)
        self.driver.find_element_by_name('announced_city').send_keys("Bandung")

    def data_pencipta(self):
        self.driver.get('https://e-hakcipta.dgip.go.id/index.php/register/hakcipta')
        sleep(2)
        self.driver.find_elements_by_class_name('close')[-1].click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[3]/div[1]/div[2]/a').click()
        sleep(1)
        self.driver.find_element_by_name("name").send_keys('innal')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="creator"]/div[3]/div/textarea').send_keys('bandung')
        sleep(1)
        self.driver.find_element_by_name('city').send_keys('bandung')
        sleep(1)
        self.driver.find_element_by_name('zip_code').send_keys('404401')
        sleep(1)
        self.driver.find_element_by_name('province').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[11]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="creator"]/div[9]/input').click()

    def pemegang_hak_cipta(self):
        self.driver.get('https://e-hakcipta.dgip.go.id/index.php/register/hakcipta')
        sleep(2)
        self.driver.find_elements_by_class_name('close')[-1].click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[4]/div[1]/div[2]/a').click()
        sleep(1)
        self.driver.find_element_by_name('name').send_keys('Politeknik Pos Indonesia')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[3]/div/textarea').send_keys('Jalan Sariasih No.54, Sarijadi, Sukasari, Kota Bandung, Jawa Barat 40151')
        sleep(1)
        self.driver.find_element_by_name('city').send_keys('Bandung')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[5]/div/label/span').click()
        sleep(1)
        self.driver.find_element_by_name('zip_code').send_keys('40151')
        sleep(1)
        self.driver.find_element_by_name('province').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[8]/div/select/option[11]').click()
        sleep(1)
        self.driver.find_element_by_name('email').send_keys('humas@poltekpos.ac.id')
        sleep(1)
        self.driver.find_element_by_name('phone_number').send_keys('(022) 2009562')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="holder"]/div[11]/input').click()

    def lampiran(self):
        self.driver.get('https://e-hakcipta.dgip.go.id/index.php/register/hakcipta')
        sleep(2)
        self.driver.find_elements_by_class_name('close')[-1].click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[3]/div/div/singleupload/span[1]').click()        
        #path = r"C:/Innal/Poltekpos/IRC"
        #nameFile = filePath + ".pdf"
        #result = os.path.join(path, nameFile)
        #pdf = os.path.abspath('C:\Innal\Poltekpos\IRC\ST Tim Sentra KI Poltekpos.pdf')
        #self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[3]/div/div/singleupload/span[1]').send_keys(pdf)
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[5]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[7]/div/div/multipleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[4]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[6]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[5]/div[2]/div/div[8]/div/div/singleupload/span[1]').click()
        sleep(15)
        self.driver.find_element_by_xpath('//*[@id="createform"]/div[6]/div[1]/input').click()
        sleep(1)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class EHaki(object):
    def __init__(self, title, description, name, address, city, zip_code, province):
        self.driver = webdriver.Chrome()
        self.title = title
        self.description = description
        self.name = name 
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.province = province
        self.people = people
        
    
    def web(self):
        self.driver.get('https://e-hakcipta.dgip.go.id/login')
        sleep(1)
        self.driver.find_element_by_name('username').send_keys("lppm@poltekpos.ac.id")
        sleep(1)
        self.driver.find_element_by_name('password').send_keys('lppm2011')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/button').click()
        

    def permohonan_baru(self):
        print ("Masukan Nama : ")
        self.name=input()
        print("Masukan Alamat : ")
        self.address=input()
        print("Masukan Kota : ")
        self.city=input()
        print("Masukan Kode Pos : ")
        self.zip_code=input()
        print("masukan Provinsi")
        self.province=input()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/div/ul/li[1]/a').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div/div/ul/li[1]/ul/li[1]').click()
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
        self.driver.find_element_by_name('title').send_keys(self.title)
        sleep(1)
        self.driver.find_elements_by_name('description')[1].send_keys(self.description)
        sleep(1)
        date = self.driver.find_element_by_xpath('//*[@id="createform"]/div[1]/div[2]/div/div[6]/div/div/input[1]')

        date.click()
        
        for i in range(len(date.get_attribute('value'))):
            date.send_keys(Keys.BACKSPACE)

        date.send_keys("1999-10-10", Keys.ENTER)

        sleep(1)
        self.driver.find_element_by_name('announced_city').send_keys("Bandung")

    def data_pencipta(self):
        # self.permohonan_baru()
        # self.driver.get('https://e-hakcipta.dgip.go.id/index.php/register/hakcipta')
        # sleep(2)
        # self.driver.find_elements_by_class_name('close')[-1].click()
        # sleep(2)

        self.driver.find_element_by_xpath('//*[@id="createform"]/div[3]/div[1]/div[2]/a').click()
        sleep(1)
        self.driver.find_element_by_name("name").send_keys(self.name)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="creator"]/div[3]/div/textarea').send_keys(self.address)
        sleep(1)
        self.driver.find_element_by_name('city').send_keys(self.city)
        sleep(1)
        self.driver.find_element_by_name('zip_code').send_keys(self.zip_code)
        sleep(1)
        
        self.driver.find_element_by_name('province').click()
        sleep(1)
        if self.province == "Jawa barat" :
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[11]').click()
            sleep(1)
        elif self.province == "Bali":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[2]').click()
            sleep(1)
        elif self.province == "Bangka Belitung":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[3]').click()
            sleep(1)
        elif self.province == "Banten":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[4]').click()
            sleep(1)
        elif self.province == "Bengkulu":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[5]').click()
            sleep(1)
        elif self.province == "Di Aceh":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[6]').click()
            sleep(1)
        elif self.province == "Di Yogyakarta":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[7]').click()
            sleep(1)
        elif self.province == "DKI Jakarta":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[8]').click()
            sleep(1)
        elif self.province == "Gorontalo":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[9]').click()
            sleep(1)
        elif self.province == "Jambi":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[10]').click()
            sleep(1)
        elif self.province == "Jawa Tengah":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[12]').click()
            sleep(1)
        elif self.province == "Jawa Timur":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[13]').click()
            sleep(1)
        elif self.province == "Kalimantan Barat":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[14]').click()
            sleep(1)
        elif self.province == "Kalimantan Selatan":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[15]').click()
            sleep(1)
        elif self.province == "Kalimantan Tengah":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[16]').click()
            sleep(1)
        elif self.province == "kalimantan Timur":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[17]').click()
            sleep(1)
        elif self.province == "Kalimantan Utara":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[18]').click()
            sleep(1)
        elif self.province == "Kepulauan Riau":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[19]').click()
            sleep(1)
        elif self.province == "Lampung":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[20]').click()
            sleep(1)
        elif self.province == "Maluku":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[21]').click()
            sleep(1)
        elif self.province == "Maluku Utara":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[22]').click()
            sleep(2)
        elif self.province == "Nusa Tenggara Barat":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[23]').click()
            sleep(1)
        elif self.province == "Nusa Tenggara Timur":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[24]').click()
            sleep(1)
        elif self.province == "Papua":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[25]').click()
            sleep(1)
        elif self.province == "Papua Barat":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[26]').click()
            sleep(1)
        elif self.province == "Riau":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[27]').click()
            sleep(1)
        elif self.province == "Sulawesi Barat":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[28]').click()
            sleep(1)
        elif self.province == "Sulawesi Selatan":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[29]').click()
            sleep(1)
        elif self.province == "Sulawesi Tengah":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[30]').click()
            sleep(1)
        elif self.province == "Sulawesi Tenggara":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[31]').click()
            sleep(1)    
        elif self.province == "Sulawesi Utara":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[32]').click()
            sleep(1)
        elif self.province == "Sumatera Barat":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[33]').click()
            sleep(1)
        elif self.province == "Sumatera Selatan":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[34]').click()
            sleep(1)
        elif self.province == "Sumatera Utara":
            self.driver.find_element_by_xpath('//*[@id="creator"]/div[8]/div/select/option[35]').click()
            sleep(1)
        else :
            print("Kota tidak ditemukan !!!!")
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
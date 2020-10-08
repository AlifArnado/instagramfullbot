from selenium import webdriver
import random
from time import time,sleep

class Instagram:
    def __init__(self, username, password,driver):
        self.username=username
        self.password=password
        self.driver=driver

    def login(self):
        #self.driver.minimize_window()
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(1)
        i=0
        while i<10:
            try:
                self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
                self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
                break
            except:
                sleep(1)

        driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click() #login buttonuna tıklama
        sleep(2)

    def followbot(self,takipedilecekkullaniciadi,takipedilecekkullanicisayisi):
        #self.driver.minimize_window()
        self.takipedilecekkullaniciadi=takipedilecekkullaniciadi
        self.takipedilecekkullanicisayisi=takipedilecekkullanicisayisi
        i=0
        while i<10:
            try:
                self.driver.get("https://www.instagram.com/"+self.takipedilecekkullaniciadi+"/")
                break
            except:
                sleep(1)

        while i<10:
            try:
                self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click() #takipçi penceresi açma
                break
            except:
                sleep(1)

        while i<10:
            try:
                pencere = self.driver.find_element_by_css_selector("div[class='isgrP']")
                break
            except:
                sleep(1)

        sleep(2)

        print("Takip işlemi başladı")

        for takipedilen in range(1,takipedilecekkullanicisayisi+1):

            if(takipedilen%6==0):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
                sleep(1)
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
                sleep(1)
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;',pencere)
                sleep(1)
            else:
                sleep(1)
            
            buttons = self.driver.find_elements_by_xpath('//button[contains(text(), "Takip Et")]')
            sleep(1)
            self.driver.execute_script("arguments[0].click();", buttons[0])

            
            if(takipedilen%dongusayisi==0):
                a=200+random.random()*150+random.random()*80
                gecensure=(time()-baslangiczamani)/60
                print("{} kullanıcı takip edildi. İnstagram limitleri dolayısıyla {} saniye dinleniyor.  Geçen süre= {} dakika".format(takipedilen,round(a,3),round(gecensure,2)))
                sleep(a)

            else:
                if(takipedilen%8==0):
                    a=30+random.random()*20+random.random()*15
                    gecensure=(time()-baslangiczamani)/60
                    print("{} kullanıcı takip edildi. {} saniye dinleniyor. Geçen süre= {} dakika".format(takipedilen,round(a,3),round(gecensure,2)))
                    sleep(a)
                else:
                    if(takipedilen%11==0):
                        a=15+random.random()*5+random.random()*5
                        gecensure=(time()-baslangiczamani)/60
                        print("{} kullanıcı takip edildi. {} saniye dinleniyor. Geçen süre= {} dakika".format(takipedilen,round(a,3),round(gecensure,2)))
                        sleep(a)
                    else:
                        if(takipedilen%3 == 0): 
                            sleep(3+2*random.random()+random.random())
                        elif(takipedilen%3==1):
                            sleep(2+4*random.random()+2*random.random())
                        elif(takipedilen%3==2):
                            sleep(3+2*random.random()+2*random.random())
                        else:
                            pass

        gecensure=(time()-baslangiczamani)/60
        print("İstediğiniz sayıda kullanıcıya takip isteği gönderildi. Çıkış yapılıyor... \nTakip edilen toplam kullanıcı sayısı: {}Geçen süre= {} dakika".format(takipedilen,round(gecensure,2)))

        self.driver.delete_all_cookies()

    def unfollowbot(self,unfollow_count):
        #self.driver.minimize_window()       
        self.unfollow_count=unfollow_count
        while i<10:
            try:
                driver.get("https://www.instagram.com/"+self.username+"/") # profili açma
                break
            except:
                sleep(1)

        while i<10:
            try:
                self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click() #takipçi penceresi açma
                break
            except:
                sleep(1)

        while i<10:
            try:
                self.driver.find_element_by_class_name('isgrP').click() #butnları doğru tespit etmek için takipçi penceresine 1 kere tıklama
                break
            except:
                sleep(1)

        while i<10:
            try:
                pencere = self.driver.find_element_by_css_selector("div[class='isgrP']")
                break
            except:
                sleep(1)

        sleep(2)
        print("Takipten çıkarma işlemi başladı")
        for unfollow in range(1,unfollow_count+1):

            if(unfollow%6==0):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
                sleep(1)
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pencere)
                sleep(1)
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;',pencere)
                sleep(1)

            try:
                self.driver.find_element_by_xpath('//button[text() = "Takiptesin"]').click()
                sleep(3+2*random.random())
                self.driver.find_element_by_xpath('//button[text() = "Takibi Bırak"]').click()
                sleep(random.random())
            except:
                sleep(1)

            if(unfollow%dongusayisi==0):
                a=200+random.random()*150+random.random()*80
                gecensure=(time()-baslangiczamani)/60
                print("{} kullanıcı takipten çıkarıldı. İnstagram limitleri dolayısıyla {} saniye dinleniyor. Geçen süre= {} dakika".format(unfollow,round(a,3),round(gecensure,2)))
                sleep(a)
            
            else:
                if(unfollow%8==0):
                    a=30+random.random()*20+random.random()*15
                    gecensure=(time()-baslangiczamani)/60
                    print("{} kullanıcı takipten çıkarıldı. {} saniye dinleniliyor. Geçen süre= {} dakika".format(unfollow,round(a,3),round(gecensure,2)))
                    sleep(a)
                else:
                    if(unfollow%11==0):
                        a=15+random.random()*5+random.random()*5
                        gecensure=(time()-baslangiczamani)/60
                        print("{} kullanıcı takipten çıkarıldı. {} saniye dinleniliyor. Geçen süre= {} dakika".format(unfollow,round(a,3),round(gecensure,2)))
                        sleep(a)
                    
                    else:
                        if(unfollow%3 == 0):
                            sleep(3+2*random.random()+random.random())
                        elif(unfollow%3==1):
                            sleep(2+4*random.random()+2*random.random())
                        elif(unfollow%3==2):
                            sleep(3+2*random.random()+2*random.random())
                        else:
                            pass

           
        gecensure=(time()-baslangiczamani)/60
        print("Yapılan işlem başarıyla sonuçlandı. Çıkış yapılıyor... \nTakipten çıkarılan toplam kullanıcı sayısı: {} \nGeçen süre= {} dakika".format(unfollow,round(gecensure,2)))
        self.driver.delete_all_cookies()


    def hashtagelike(self,hashtag,begenisayisi,atlanacakgonderisayisi):
        self.hastag=hashtag
        self.begenisayisi=begenisayisi
        self.atlanacakgonderisayisi=atlanacakgonderisayisi
        self.driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(2)
        i=0
        while i<10:
            try:
                self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
                break
            except:
                sleep(1)

        while i<10:
            try:
                for a in range(0,atlanacakgonderisayisi):
                    sleep(1+2*random.random())
                    self.driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click() #sonraki
                break
            except:
                sleep(1)

        for yapilanbegeni in range(0,begenisayisi):
            sleep(3*random.random())

            while i<10:
                try:
                    like_button = self.driver.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                    break
                except:
                    sleep(1)
            i=0
            while i<10:
                try:
                    self.driver.execute_script("arguments[0].click();", like_button[0])
                    sleep(random.random()*3)
                    break
                except:
                    sleep(1)
                    i+=1
            i=0
            while i<10:
                try:   
                    self.driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click() #sonraki
                    break
                except:
                    sleep(1)
                    i+=1
            i=0
            if(yapilanbegeni%3 == 0 and yapilanbegeni>1):
                sleep(1+2*random.random()+random.random())
            elif(yapilanbegeni%3==1 and yapilanbegeni>1):
                sleep(1+4*random.random()+2*random.random())
            elif(yapilanbegeni%3==2 and yapilanbegeni>1):
                sleep(1+2*random.random()+2*random.random())

            if(yapilanbegeni%8==0 and yapilanbegeni>1):
                a=10+random.random()*5+random.random()*10
                print("{} fotoğraf beğenildi. {} saniye dinleniyor".format(yapilanbegeni,a))
                sleep(a)

            if(yapilanbegeni%11==0 and yapilanbegeni>1):
                print("{} fotoğraf beğenildi. 20 saniye dinleniyor".format(yapilanbegeni))
                sleep(10+random.random()*10+random.random()*10)

        print("Yapılan işlem sonucu {} fotoğraf başarıyla beğenildi".format(yapilanbegeni))
        print("İstediğiniz sayıda beğeni yapıldı. Çıkış Yapılıyor...\nBeğenilen toplam gönderi sayısı: {}".format(yapilanbegeni+1))
        self.driver.delete_all_cookies()

    def cikis(self):
        self.driver.get("https://www.instagram.com/"+username+"/")
        while i<10:
            try:
                self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click() # profil resmine tıklama
                break
            except:
                sleep(1)

        while i<10:
            try:
                self.driver.find_element_by_css_selector("div[class='-qQT3']").click()
                break
            except:
                sleep(1)

        sleep(3)
        self.driver.delete_all_cookies()
        self.driver.quit()
        SystemExit()

i=0
dongusayisi=28
baslangiczamani=time()

print("-" * 50)
print("Instagram Bot'a Hoş Geldiniz! ")
print("-" * 50)
print("Lütfen Kullanıcı Adı ve Şifrenizi Giriniz ")
print("-" * 50)
username=input("Kullanıcı Adı Giriniz: ")
password=input("Şifre giriniz: ")
print("-" * 50)
print(" Lütfen Chrome Driver İndirdiğinizden Emin Olunuz \n Örnek= C:/Users/yakup/Desktop/Python3_calismalarim/instabot/chromedriver.exe")
print("-" * 50)
driverpath=input("Chrome Driver Path: ")
if(driverpath=="" or driverpath==" "):
    driverpath="C:/Users/yakup/Desktop/Python3_calismalarim/instabot/chromedriver.exe"
print("-" * 50)
print("""Maden by Yakup""")
print("-" * 50)
print("  Lütfen Seçiminizi Yapınız:\n  1- Takip Etme Botu\n  2- Takipten Çıkma Botu\n  3- Hashtag Beğeni Botu")
print("-" * 50)
secim=int(input("Seçiminiz(1/2/3) :"))
print("-" * 50)

if(secim==1):
    print("Takipçisi alınacak kullanıcı adı (default=instagram) ve Takip Edilecek Kullanıcı Sayısı Giriniz:")
    print("-" * 50)
    takipedilecekkullaniciadi=input("Takip Edilecek Kullanıcı Adı: ")
    takipedilecekkullanicisayisi= int(input("Takip Edilecek Kullanıcı Sayısı: "))
    print("-" * 50)
    driver=webdriver.Chrome(driverpath)
    user1=Instagram(username,password,driver)
    user1.login()
    sleep(3)
    user1.followbot(takipedilecekkullaniciadi,takipedilecekkullanicisayisi)
    sleep(2)
    user1.cikis()
    sleep(2)
    driver.delete_all_cookies()
    driver.quit()

elif(secim==2): 
    print("Takipten Çıkılacak Kullanıcı Sayısı Giriniz")
    unfollow_count=int(input("Takipten Çıkılacak Kullanıcı Sayısı: "))
    print("-" * 50)
    driver=webdriver.Chrome(driverpath)
    user1=Instagram(username,password,driver)
    user1.login()
    sleep(3)
    user1.unfollowbot(unfollow_count)
    sleep(2)
    user1.cikis()
    sleep(2)
    driver.delete_all_cookies()
    driver.close()
    driver.quit()

elif(secim==3):
    print("Beğeni Yapılmak İstenen Hashtag Adı Giriniz:")
    hashtag=input("Beğeni Yapılmak İstenen Hashtag: ")
    print("-" * 50)
    print("Beğeni Sayısı Giriniz:")
    begenisayisi=int(input("Beğeni Sayısı: "))
    print("-" * 50)
    print("Atlamak İstediğiniz Gönderi Sayısı Giriniz (default=0) :")
    atlanacakgonderisayisi=int(input("Beğeni Sayısı: "))
    print("-" * 50)
    driver=webdriver.Chrome(driverpath)
    user1=Instagram(username,password,driver)
    user1.login()
    sleep(3)
    user1.hashtagelike(hashtag,begenisayisi,atlanacakgonderisayisi)
    sleep(2)
    user1.cikis()
    sleep(2)
    driver.delete_all_cookies()
    driver.close()
    driver.quit()

else:
    print("Hatalı Bir Seçim yaptınız")
    driver.delete_all_cookies()
    driver.close()
    driver.quit()

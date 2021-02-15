from selenium import webdriver

c=0

        

driver=webdriver.Chrome("C:\\Users\\USER.DESKTOP-PHII7LU\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
while c==0:

    name=input("Enter name or group name : -")
    msg=input("Enter message : - ")
    count=int(input("Enter count : - "))

    input("Enter anything after scanning ")

    user=driver.find_element_by_xpath("//span[@title='{}']".format(name))

    user.click()

    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for index in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

    print("Great Success!!!")

    rep=input("Do you wanna repeat : - ")
    
    if rep=="Y" or rep=="y":
        c=0
    else:
        c=1
    
exit(0)    

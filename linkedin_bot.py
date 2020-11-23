
from selenium import webdriver #connect python with webbrowser-chrome
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
import time



def login():
	file = open("login_details.txt","r")
	data = file.readlines()
	username = driver.find_element_by_id("username")
	username.send_keys(data[0].split(":")[1].split("\n")[0].strip())
	username = driver.find_element_by_id("password")
	username.send_keys(data[1].split(":")[1].strip())
	log_in=driver.find_element_by_xpath("/html/body/div/main/div[2]/form/div[3]/button")
	log_in.click()
	print("successfully logged in...")
	time.sleep(2)
 
def network():
	try:
		driver.find_element_by_id("mynetwork-tab-icon").click()

		time.sleep(3)

	except:
		print("[+] Some Error Occoured \n Directly opening networks tab")
		body = driver.find_element_by_tag_name("body")
		body.send_keys(Keys.CONTROL + "t")
		driver.get(nurl)

		time.sleep(2)

def connect(n):
	filem = open("custom_message.txt","r")
	customMessage = filem.read()
 	for i in range(0,n):
		time.sleep(4)  
		pag.click(760,600)
		time.sleep(2)
		driver.find_element_by_class_name("pv-s-profile-actions").click()
		time.sleep(2)
		pag.click(1090,400)

		#driver.find_element_by_class_name('mr1').click()
		#time.sleep(3)
		messageID=driver.find_element_by_id('custom-message')
		messageID.send_keys(customMessage)
		time.sleep(2) 
		driver.find_element_by_class_name('ml1').click()
		time.sleep(1)



		print("["+str(i)+"] Connection request sent ")
		pag.click(35,60)
 	print("done")

url = "http://linkedin.com/login"
nurl = "http://linkedin.com/mynetwork/"

#by default it is Number of connection will be 5
Num_of_times =	5   
driver = webdriver.Firefox()
driver.set_window_size(1024, 600)
driver.maximize_window()

try:
	driver.get(url)
	login()
	network(Num_of_times)
	connect()
except:
	print("Error!,Try Checking internet connection or Proxy setting")  
finally:
	driver.quit()
	print("Good Bye!!")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display
import pickle
import time

# ~ display = Display(visible=0, size=(800, 600))
# ~ display.start()

#options= Options()
#options.add_argument("--headless")


driver = webdriver.Chrome()

driver.get("https://dashboard.microverse.org/")

for cookie in pickle.load(open("cookie"),"rb"):
	driver.add_cookie(cookie)

time.sleep(5)
driver.refresh()



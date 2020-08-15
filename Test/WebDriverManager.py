import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# from selenium import webdriver
# from webdriver_manager.microsoft import IEDriverManager

# driver = webdriver.Ie(IEDriverManager().install())

driver.get("https://google.com")

time.sleep(2)
driver.close()
driver.quit()




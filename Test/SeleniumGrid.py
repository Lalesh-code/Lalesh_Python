from selenium import webdriver


desiredCapabilities={
    "browserName":"chrome"
}

driver = webdriver.Remote(desired_capabilities = desiredCapabilities)
driver.get("https://www.google.co.in/")

print(driver.title)
driver.quit()

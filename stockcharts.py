from selenium import webdriver
from selenium.webdriver.support.ui import Select

ticker = input("Enter Ticker: ").upper()
driver = webdriver.Chrome()
dropdownSelect = "Full Stochastics"
driver.get(f"https://stockcharts.com/h-sc/ui?s={ticker}")

# assert ticker in driver.title

select = Select(driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[1]/div[2]/div/form/div[6]/div/table/tbody/tr[5]/td[1]/select'))
select.select_by_visible_text(dropdownSelect)

imgURL = driver.find_element_by_id("chartImg").get_attribute('src')
driver.get(imgURL)
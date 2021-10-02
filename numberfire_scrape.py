from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# scraping is done with FireFox

# set webdriver.FireFox to driver variable
# set executable path to geckodriver.eve location ex; C:/...

# driver = webdriver.Firefox(executable_path="")
driver = webdriver.Firefox(executable_path=r"C:\python\geckodriver.exe")

# pass URL that we want to connect to
driver.get("https://www.numberfire.com/mlb/daily-fantasy/daily-baseball-projections")

# allow time for page to load and numberfire to prompt login
time.sleep(4)

# numberfire will prompt to login, following code logs in through fanduel account

# locate already have an account login link
login1 = driver.find_element_by_xpath(
    "/html/body/main/div[2]/div[4]/div/span[2]/a/strong"
)

# have selenium click link
login1.click()

# locate and click fanduel login option
fd_login = driver.find_element_by_xpath("/html/body/div[4]/div/ul/li[1]/a")
fd_login.click()

# email field
# send_keys() will type in account email
# send_keys(Keys.RETURN) mimics enter key
email = driver.find_element_by_xpath('//*[@id="forms.login.email"]')
email.click()
email.send_keys("nkalpaxis@aol.com")
email.send_keys(Keys.RETURN)

# password field
password = driver.find_element_by_xpath('//*[@id="forms.login.password"]')
password.click()
password.send_keys("kalpaxis89")
password.send_keys(Keys.RETURN)

# allow time for selenium to return to numberfire page
time.sleep(3)

# code lines 55-83 are used to select pitchers from different slates
# the default on numberfire is the 'Main Slate' so if only playing the Main Slate comment out all options lines 55-83
# using the all_day_slate option will scrape all pitchers for the day

slate_button = driver.find_element_by_css_selector(
    "div.dfs-main__options__sections__indiv:nth-child(3) > div:nth-child(2)"
)
slate_button.click()

all_day_slate = driver.find_element_by_xpath(
    "/html/body/main/div[2]/div[2]/div/div[2]/div[3]/div/ul/li[3]"
)
all_day_slate.click()

# early_only = driver.find_element_by_xpath(
#     "/html/body/main/div[2]/div[2]/div/div[2]/div[3]/div/ul/li[6]"
# )
# early_only.click()

# afternoon_only = driver.find_element_by_xpath(
#     "/html/body/main/div[2]/div[2]/div/div[2]/div[3]/div/ul/li[9]"
# )
# afternoon_only.click()

# main_slate = driver.find_element_by_xpath(
#     "/html/body/main/div[2]/div[2]/div/div[2]/div[3]/div/ul/li[8]"
# )
# main_slate.click()

# after_hours = driver.find_element_by_xpath(
#     "/html/body/main/div[2]/div[2]/div/div[2]/div[3]/div/ul/li[10]"
# )
# after_hours.click()

# locate table that contains pitchers names & projections
table = driver.find_element_by_xpath(
    "/html/body/main/div[2]/div[2]/section/div[4]/div[2]/table"
)

# create empty list to append pitcher names
pitchers = []

# locate pitcher names by class name full
# append text of each element
for pitcher in table.find_elements_by_class_name("full"):
    pitchers.append(pitcher.text)

# convert pitchers list into dataframe
df = pd.DataFrame(pitchers, columns=["Name"])

# write dataframe to csv
df.to_csv("pitchers.csv", index=False)
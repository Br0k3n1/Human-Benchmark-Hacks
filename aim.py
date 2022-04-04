from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from keyboard import is_pressed
from pyautogui import click, size

# Variables
url = "https://humanbenchmark.com/tests/aim"
driver = webdriver.Chrome(ChromeDriverManager().install())
width, height = size()
triggerKey = "/"
chromeHeaderSize = 150

driver.get(url)

# Start when trigger key is pressed
while True:
    if is_pressed(triggerKey):
        break

# Get target element
target = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/div/div'
)

click(target.location["x"], target.location["y"] + chromeHeaderSize)

# Click targets
for _number in range(0, 30):
    target = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div/div'
    )

    click(target.location["x"], target.location["y"] + chromeHeaderSize)

# End when trigger key is pressed
while True:
    if is_pressed(triggerKey):
        break

driver.quit()

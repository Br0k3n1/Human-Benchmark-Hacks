from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from keyboard import is_pressed, write
from pyautogui import click, size

# Variables
url = "https://humanbenchmark.com/tests/typing"
driver = webdriver.Chrome(ChromeDriverManager().install())
width, height = size()
triggerKey = "/"

driver.get(url)

# Start when trigger key is pressed
# Make sure when you click the trigger key your not typing in the input box
while True:
    if is_pressed(triggerKey):
        break

# Get letters that need to be typed from the screen
letters = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div'
).text

# Get the location of the first letter
lettersLoc = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div/span[1]'
).location

# Click the input box
click(lettersLoc["x"], height - lettersLoc["y"])

# Write the letters
write(letters)

# End when trigger key pressed
while True:
    if is_pressed(triggerKey):
        break

driver.quit()

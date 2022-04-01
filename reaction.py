from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from keyboard import is_pressed
import pyautogui

# Variables
url = "https://humanbenchmark.com/tests/reactiontime"
driver = webdriver.Chrome(ChromeDriverManager().install())
triggerKey = "/"
width, height = pyautogui.size()

driver.get(url)

# Start when trigger key pressed
while True:
    if is_pressed(triggerKey):
        break

# Click start if not already clicked
if (
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div[1]'
    ).text
    == "Reaction Time Test"
):
    pyautogui.click(x=width / 2, y=height / 2)

# Main loop while game is running
while True:
    # Get element that tells us if we can click the screen
    try:
        clickButton = driver.find_elements_by_xpath(
            '//*[@id="root"]/div/div[4]/div[1]/div/div/div/h1'
        )[0].text
    except:
        clickButton = "None"

    # Get page that comes up after successfull click
    try:
        continuePage = driver.find_elements_by_xpath(
            '//*[@id="root"]/div/div[4]/div[1]/div/div/div/h2'
        )[0].text
    except:
        continuePage = "None"

    # Get button that comes up when game done
    saveButton = driver.find_elements_by_xpath(
        '//*[@id="root"]/div/div[4]/div[1]/div/div/div[3]/button[1]'
    )

    # If you can click
    if clickButton == "Click!":
        pyautogui.click(x=width / 2, y=height / 2)

    # If you can continue
    elif continuePage == "Click to keep going":
        pyautogui.click(x=width / 2, y=height / 2)

    # If game is done
    if saveButton:
        break

# End when trigger key pressed
while True:
    if is_pressed(triggerKey):
        break

driver.quit()

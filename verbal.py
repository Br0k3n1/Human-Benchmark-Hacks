from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from keyboard import is_pressed
from pyautogui import size

# Variables
url = "https://humanbenchmark.com/tests/verbal-memory"
driver = webdriver.Chrome(ChromeDriverManager().install())
width, height = size()
triggerKey = "/"
endScore = 50

driver.get(url)

# Trie data stucture
class Trie:
    def __init__(self):
        self.root = {'*': "*"}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = '*'
    
    def check_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return '*' in curr_node

# Start when trigger key is pressed
while True:
    if is_pressed(triggerKey):
        break

# If start not pressed press start
if driver.find_elements_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]/button'):
    driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]/button').click()

trie = Trie()

# Loop until end score is reached
for _ in range(endScore):
    word = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div').text

    if trie.check_word(word):
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()
    else:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()
        trie.add_word(word)

# Click the wrong answers to get the score perfect to what you chose
for _ in range(3):
    word = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div').text
    if trie.check_word(word):
        driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()
        trie.add_word(word)
    else:
         driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()

# End when trigger key is pressed
while True:
    if is_pressed(triggerKey):
        break

driver.quit()
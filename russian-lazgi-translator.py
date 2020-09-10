from selenium import webdriver
from selenium.webdriver.support.ui import Select

string = input("Enter a word to translate into lazgi:")

chromedriver = "C:\\Users\\User\\Downloads\\chromedriver"
chrome_browser = webdriver.Chrome(chromedriver)
# chrome_browser.implicitly_wait(10)
chrome_browser.get("https://gaf.lezgichal.ru")
chrome_browser.set_window_position(-10000,0)
# selector_button = chrome_browser.find_element_by_class_name("dictionary")
select = Select(chrome_browser.find_element_by_class_name('dictionary'))
select.select_by_visible_text('русско-лезгинский')

# language_button = selector_button
user_message = chrome_browser.find_element_by_class_name("search-field")
user_message.clear()

user_message.send_keys(string)
chrome_browser.implicitly_wait(15)
output_message = chrome_browser.find_element_by_class_name('out')

print(output_message.text)

chrome_browser.close()
# assert 'ккал.' in output_message.text
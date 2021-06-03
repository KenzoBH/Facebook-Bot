
from selenium.webdriver import Chrome, ChromeOptions
import time

def login_in_facebook(browser, your_email, your_password):
    facebook_url = 'https://www.facebook.com/'
    browser.get(facebook_url) # Opens the Facebook page
    time.sleep(2)

    email_box = browser.find_element_by_name('email') # Box to insert the user e-mail
    email_box.send_keys(your_email)

    password_box = browser.find_element_by_id('pass') # Box to insert the user password
    password_box.send_keys(your_password)

    login_button = browser.find_element_by_name('login') # Box to click to login
    login_button.click()
    time.sleep(5)

def send_facebook_message_to(browser, name, message):
    messenger_button = browser.find_element_by_xpath('//div[@aria-label="Messenger"]') # Messenger button on the top right
    messenger_button.click()
    time.sleep(10)

    search_in_messenger = browser.find_element_by_xpath('//input[@placeholder="Pesquisar no Messenger"]') # Box to search people
    search_in_messenger.send_keys(name) # Search for the given name
    time.sleep(3)

    people_list = browser.find_elements_by_xpath('//li[@class="k4urcfbm"]') # List that contains every people found

    for person in people_list: # Checks if the person is the same as the given name
        if person.text == name: # If so, clicks
            person.click()
            break
    time.sleep(5)

    message_box = browser.find_element_by_xpath('//div[@aria-label="Aa"]') # Box to send the message
    message_box.click()
    message_box.send_keys(message + '\n') # Sends the message
    time.sleep(2)

def facebook_logout(browser):
    menu_button = browser.find_element_by_xpath('//div[@aria-label="Conta"]') # Box on the top right
    menu_button.click()
    time.sleep(3)

    menu_buttons = browser.find_elements_by_xpath('//div[@data-visualcompletion="ignore-dynamic"]')
    for button in menu_buttons:
        if button.text == 'Sair':
            button.click()
            break

your_email = input('Digite seu e-mail de login no Facebook: ')
your_password = input('Digite sua senha do Facebook: ') 
name = input('\nDigite o nome da pessoa para mandar uma mensagem: ')
message = input('Digite a mensagem a ser enviada:\n')

chrome_options = ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = Chrome(chrome_options = chrome_options)

login_in_facebook(browser, your_email, your_password)
send_facebook_message_to(browser, name, message)
facebook_logout(browser)

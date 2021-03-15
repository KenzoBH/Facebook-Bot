
from selenium.webdriver import Chrome, ChromeOptions
import time

def login_in_facebook(browser, your_email, your_password):
    facebook_url = 'https://www.facebook.com/'
    browser.get(facebook_url)
    time.sleep(2)

    email_box = browser.find_element_by_name('email')
    email_box.send_keys(your_email)

    password_box = browser.find_element_by_id('pass')
    password_box.send_keys(your_password)

    login_button = browser.find_element_by_name('login')
    login_button.click()
    time.sleep(5)

def send_facebook_message_to(browser, name, message):
    messenger_button = browser.find_element_by_xpath('//div[@aria-label="Messenger"]')
    messenger_button.click()
    time.sleep(10)

    search_in_messenger = browser.find_element_by_xpath('//input[@placeholder="Pesquisar no Messenger"]')
    search_in_messenger.send_keys(name)
    time.sleep(3)

    people_list = browser.find_elements_by_xpath('//li[@class="k4urcfbm"]')

    for person in people_list:
        if person.text == name:
            person.click()
            break
    time.sleep(5)

    message_box = browser.find_element_by_xpath('//div[@aria-label="Aa"]')
    message_box.click()
    message_box.send_keys(message + '\n')
    time.sleep(2)

def facebook_logout(browser):
    menu_button = browser.find_element_by_xpath('//div[@aria-label="Conta"]')
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

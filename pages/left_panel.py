from selene import browser, by

from pages.registration_page import RegistrationPage
from pages.simple_registration_page import SimpleRegistrationPage


class Left_panel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, group, element):
        self.container.element(by.text(group)).click()
        self.container.element(by.text(element)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
        return SimpleRegistrationPage()

    def open_registration_form(self):
        self.open('Forms', 'Practice Form')
        return RegistrationPage()
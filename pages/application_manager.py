from pages.left_panel import Left_panel
from pages.registration_page import RegistrationPage
from pages.simple_registration_page import SimpleRegistrationPage
from selene import browser


class ApplicationManager():
    def __init__(self):
        self.left_panel = Left_panel()
        self.simple_registration_page = SimpleRegistrationPage()
        self.registration_page = RegistrationPage()

    def open(self):
        browser.open('https://demoqa.com/forms')
        return self
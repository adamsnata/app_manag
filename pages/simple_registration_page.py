from selene import browser, have


class SimpleRegistrationPage():

    def register(self, user):
        browser.element('#userName').set_value(user.first_name + ' ' + user.last_name)
        browser.element('#userEmail').set_value(user.email)
        browser.element('#currentAddress').set_value(user.address)
        browser.element('#submit').click()

    def should_have_registered(self, user):
        browser.element('#name').should(have.exact_text(f'Name:{user.first_name} {user.last_name}'))
        browser.element('#email').should(have.exact_text(f'Email:{user.email}'))
        browser.element('#output').element('#currentAddress').should(have.exact_text(f'Current Address :{user.address}'))

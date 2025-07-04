import os
from selene import browser, have
from config import RESOURCES_DIR


class RegistrationPage():

    def register(self, user):
        self.__fill_first_name(user.first_name)
        self.__fill_last_name(user.last_name)
        self.__fill_email(user.email)
        self.__choose_gender(user.gender.value)
        self.__fill_phone_number(user.phone_number)
        self.__fill_date_of_birth(user.date_of_birth)
        self.__fill_subjects(user.subject)
        self.__choose_hobbie(user.hobbie.value)
        self.__upload_picture(user.file_name)
        self.__fill_address(user.address)
        self.__choose_state(user.state)
        self.__choose_city(user.city)
        self.__confirm_filling_form()

    def should_have_registered(self, user):
        browser.all('td').even.should(have.exact_texts(
            user.first_name+' '+user.last_name,
            user.email,
            user.gender.value,
            user.phone_number,
            str(user.date_of_birth.day)+' '+user.date_of_birth.strftime('%B')+','+str(user.date_of_birth.year),
            user.subject,
            user.hobbie.value,
            user.file_name,
            user.address,
            user.state+' '+user.city
        ))

    def __fill_first_name(self, first_name):
        browser.element('#firstName').set_value(first_name)
        return self

    def __fill_last_name(self, last_name):
        browser.element('#lastName').set_value(last_name)
        return self

    def __fill_email(self, email):
        browser.element('#userEmail').set_value(email)
        return self

    def __choose_gender(self, gender):
        browser.all('[name = gender]').element_by(have.value(gender)).element('..').click()
        return self

    def __fill_phone_number(self, phone_number):
        browser.element('#userNumber').set_value(phone_number)
        return self

    def __fill_date_of_birth(self, date_of_birth):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(str(date_of_birth.year))
        browser.element('.react-datepicker__month-select').type(str(date_of_birth.month))
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{date_of_birth.day}').click()
        return self

    def __fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def __choose_hobbie(self, hobbie):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobbie)).click()
        return self

    def __upload_picture(self, file_name):
        browser.element('#uploadPicture').send_keys(os.path.join(RESOURCES_DIR, file_name))
        return self

    def __fill_address(self, address):
        browser.element('#currentAddress').set_value(address)
        return self

    def __choose_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()
        return self

    def __choose_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()
        return self

    def __confirm_filling_form(self):
        browser.element('#submit').click()
        return self

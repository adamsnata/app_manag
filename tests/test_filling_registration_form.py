from pages.application_manager import ApplicationManager
from users.user import student


def test_filling_registration_form():
    app = ApplicationManager()
    app.open().left_panel.open_registration_form()
    app.registration_page.register(student)
    app.registration_page.should_have_registered(student)

def test_filling_simple_registration_form():
    app = ApplicationManager()
    app.open().left_panel.open_simple_registration_form()
    app.simple_registration_page.register(student)
    app.simple_registration_page.should_have_registered(student)
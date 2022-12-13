import os

from selene import have
from selene.support.shared import browser


def test_fill_form(open_browser):
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.75)"')
    browser.element('#firstName').type('Алена')
    browser.element('#lastName').type('Иванова')
    browser.element('#userEmail').type('angel@mail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('892777712345')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select>[value="1900"]').click()
    browser.element('.react-datepicker__month-select>[value="11"]').click()
    browser.element('.react-datepicker__day--013').click()
    browser.element('#subjectsInput').type('comp').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../files/picture.png')))
    browser.element('#currentAddress').type('г.Москва ул Ленина 3')
    browser.element('#react-select-3-input').type('e').press_enter()
    browser.element('#react-select-4-input').type('e').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.table').should(have.text(
        'Алена Иванова' and
        'angel@mail.com' and
        'Male' and
        '892777712345' and
        '11 July,1996' and
        'Maths' and
        'Reading' and
        'picture.png' and
        'г.Москва ул Ленина 3' and
        'Uttar Pradesh Merrut'
    ))
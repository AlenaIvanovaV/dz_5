import os
from selene.support.shared import browser
from selene import be, have
from selene import command


def test_fill_form(open_browser):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').type('Алена')
    browser.element('[id="lastName"]').type('Иванова')
    browser.element('[id="userEmail"]').type('angel@mail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('892777712345')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select>[value="11"]').click()
    browser.element('.react-datepicker__year-select>[value="1996"]').click()
    browser.element('.react-datepicker__day--007').click()
    browser.element('[id="subjectsInput"]').type("Maths").press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), '../files/picture.png')))
    browser.element("#state").click()
    browser.element("#react-select-3-input").type('Uttar Pradesh').press_enter()
    browser.element("#city").click()
    browser.element("#react-select-4-input").type('Agra').press_enter()

    browser.element('[id="currentAddress"]').type('г.Москва ул Ленина 3')
    browser.element('[id="subjectsInput"]').type("Maths").press_enter()
    browser.element('#submit').perform(command.js.click)
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
        'Uttar Pradesh Agra'
    ))

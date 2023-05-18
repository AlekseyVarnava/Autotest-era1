import allure

from pages.elements_page import TestElementBox

@allure.suite('Integracia')
class TestElements:
    @allure.sub_suite('All_test')
    class TestElementBox:
         @allure.suite('Smoke_test')
         def test_text_box(self, driver):
            all_page = TestElementBox(driver, 'http://i.lab5.era:8080/login')
            all_page.open()
            all_page.test_all_form()




from pages.elements_page import TestElementBox


class TestElements:
    class TestElementBox:
         def test_text_box(self, driver):
            all_page = TestElementBox(driver, 'http://i.lab5.era:8080/login')
            all_page.open()
            all_page.test_all_form()


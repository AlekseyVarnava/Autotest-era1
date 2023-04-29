from pages.elements_page import TestElementBox


class TestElements:
    class TestElementBox:
         def test_text_box(self, driver):
            text_box_page = TestElementBox(driver, 'http://i.lab5.era:8080/login')
            text_box_page.open()
            text_box_page.test_all_form()


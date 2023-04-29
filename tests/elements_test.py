from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

         def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'http://i.lab5.era:8080/login')
            text_box_page.open()
            text_box_page.fill_all_fields()


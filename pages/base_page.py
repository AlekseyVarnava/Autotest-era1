from selenium.webdriver import ActionChains as AC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_if_visible(self, locator, timeout=5):  # Находим один видимый элемент
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5): # Находим несколько элементов видимых
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5): # Берём информацию из дерева, не обязательно видимый
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5): # Несколько информации из дерева, не обязательно видимая
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5): # Находим невидимый элемент
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5): # Используем кликабельный элемент
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_presence_located(self, locator, timeout=5): # Используем кликабельный элемент
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def go_to_element(self, element): # Скролл страницы до нужного элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_triple_click(self, element): # Трипл клик левой кнопкой мыши
        action = AC(self.driver)
        action.click(element)
        action.double_click(element)
        action.perform()

    def action_double_click(self, element): # Дабл клик левой кнопкой мыши
        action = AC(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element): # Клик правой кнопкой мыши
        action = AC(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = AC(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def action_drag_and_drop_to_element(self, what, where):
        action = AC(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def action_move_to_element(self, element):
        action = AC(self.driver)
        action.move_to_element(element)
        action.perform()



import time
import os
import pyautogui
import random
import pyperclip

from ctypes import windll
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import ElementLocators
from pages.base_page import BasePage

class TestElementBox(BasePage):
    locators = ElementLocators()

    def test_all_form(self, ):
        person_info = next(generated_person()) # next-одна итерация, по одному значению
        tel_number = person_info.tel_number
        one_name = person_info.one_name
        two_name = person_info.two_name
        three_name = person_info.three_name
                # Проверка телефона
        self.element_if_visible(self.locators.TEL_NUMBER).send_keys(tel_number)
        self.element_if_visible(self.locators.WX_OD).click()
        self.element_if_visible(self.locators.PROVER_NUMBER).send_keys('123456')
                # ФИО
        fio_list = self.elements_are_visible(self.locators.FIO_ALL)
        name = fio_list[0]
        name.send_keys(one_name)
        first_name = fio_list[1]
        first_name.send_keys(two_name)
        middle_name = fio_list[2]
        middle_name.send_keys(three_name)
        # self.elements_if_visible(self.locators.ONE_NAME).send_keys(one_name)
        # self.element_if_visible(self.locators.TWO_NAME).send_keys(two_name)
        # self.element_if_visible(self.locators.THREE_NAME).send_keys(three_name)
        # print(one_name)
        # print(two_name)
        # print(three_name)
        self.element_if_visible(self.locators.ACCEPT).click()
        self.element_if_visible(self.locators.NEXT).click()
        # print(tel_number)
                # Профили
        email_me = person_info.email_me
        number_email = random.randint(1,5)
        if number_email == 1 or number_email == 2 or number_email == 3 or number_email == 4:
            self.element_if_visible(self.locators.EMAIL).send_keys(email_me)
        self.element_if_visible(self.locators.NEXT2).click()
        # print(email_me)
                # Скан-образы документов
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        self.element_if_visible(self.locators.NEXT3).click()
        os.remove(path)
                # Паспортные данные
        # file_name, path = generated_file() # Добавление скана паспорта
        # self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        # os.remove(path)
        self.element_is_clickable(self.locators.KEM_VIDAN).click()
        self.element_is_clickable(self.locators.KEM_VIDAN).send_keys('УФМС')
        time.sleep(1)
        pyautogui.typewrite(' ', 1)
        item_list_YMVD = self.elements_are_visible(self.locators.SPISOK_YMVD)
        item_ymvd = item_list_YMVD[random.randint(0, 9)]
        item_ymvd.click()
        series_number = person_info.series_number
        self.element_if_visible(self.locators.SERIES_NUMBER).send_keys(series_number)
        # print('Серия номер паспорта -', series_number)
        my_city = person_info.my_city
        self.element_if_visible(self.locators.MY_CITY).send_keys(my_city)
        # print('Место рождения -', my_city)
        data_list = self.elements_are_visible(self.locators.DATA_ALL)
        data1 = data_list[0]
        data2 = data_list[1]
            # Вводим дату выдачи на странице паспортных данных
        day_13years = person_info.day_13years
        day_list1 = list(str(day_13years))
        Y1 = day_list1[:4]
        M1 = day_list1[5:7]
        D1 = day_list1[-2:]
        all1 = D1 + M1 + Y1
        # print('Дата выдачи -', day_13years)
        # print(all1)
        data1.send_keys(all1)
            # Вводим дату рождения на странице паспортных данных
        day_18years = person_info.day_18years
        day_list2 = list(str(day_18years))
        Y2 = day_list2[:4]
        M2 = day_list2[5:7]
        D2 = day_list2[-2:]
        all2 = D2 + M2 + Y2
        # print('Дата рождения -', day_18years)
        # print(all2)
        data2.send_keys(all2)
        self.element_if_visible(self.locators.NEXT4).click()
                # Военная служба
        self.element_is_clickable(self.locators.VOENNYJ).send_keys('Военный')
        time.sleep(1)
        pyautogui.typewrite(' ', 1)
        item_list_voennyj = self.elements_are_visible(self.locators.SPISOK_VOENNYJ)
        item_voennyj = item_list_voennyj[random.randint(0, 9)]
        item_voennyj.click()
        self.element_if_visible(self.locators.GODNOST).click()
        item_list_godnost = self.elements_are_visible(self.locators.SPISOK_GODNOST)
        item_godnost = item_list_godnost[random.randint(0, 9)]
        item_godnost.click()
        self.element_if_visible(self.locators.ACCEPT2).click()
        self.element_if_visible(self.locators.NEXT5).click()
                # Образование
        self.element_is_clickable(self.locators.FGBOY).send_keys('Университет')
        time.sleep(1)
        pyautogui.typewrite(' ', 1)
        item_list_fgboy = self.elements_are_visible(self.locators.SPISOK_FGBOY)
        item_fgboy = item_list_fgboy[random.randint(0, 9)]
        item_fgboy.click()
        self.element_is_clickable(self.locators.TIP_OBR).click()
        item_list_tip_obr = self.elements_are_visible(self.locators.SPISOK_TIP_OBR)
        item_tip_obr = item_list_tip_obr[random.randint(0, 2)]
        item_tip_obr.click()
        number_special = random.randint(0, 9)
        self.element_is_clickable(self.locators.SPECIAL).send_keys(number_special)
        item_list_special = self.elements_are_visible(self.locators.SPISOK_SPECIAL)
        len_list_special = len(item_list_special)
        item_special = item_list_special[random.randint(0, len_list_special-1)]
        item_special.click()
        # self.element_is_clickable(self.locators.YEAR_END).click()
        # item_list_year = self.elements_are_visible(self.locators.SPISOK_YEAR_END)
        # len_list_year = len(item_list_year)
        # item_year = item_list_year[random.randint(0, len_list_year-1)]
        # item_year.click()
        number_tema = random.randint(1, 7)
        tema_1 = "Разработка семантических смарт-контрактов на основе технологии блокчейн"
        tema_2 = "Разработка технологий семантических предметноориентированных языков (domain-specific languages)"
        tema_3 = "Разработка гибридных систем машинного обучения на основе синтеза нейронных сетей и логико-семантических моделей"
        tema_4 = "Применение методов онтологического и семантического моделирования предметных областей"
        tema_5 = "Разработка цифровых двойников ролей в бизнеспроцессах предприятий"
        tema_6 = "Разработка алгоритмов трансляции LuNA-программ: статический анализ, конструирование поведения"
        tema_7 = "Исследование методов генерации тестовых сценариев по EDTL-требованиям в целях динамической верификации poST-программ"
        if number_tema == 1:
            self.element_if_visible(self.locators.TEMA_VIPYSK).send_keys(tema_1)
        elif number_tema == 2:
            self.element_if_visible(self.locators.TEMA_VIPYSK).send_keys(tema_2)
        elif number_tema == 3:
            self.element_if_visible(self.locators.TEMA_VIPYSK).send_keys(tema_3)
        elif number_tema == 4:
            self.element_if_visible(self.locators.TEMA_VIPYSK).send_keys(tema_4)
        elif number_tema == 5:
            self.element_if_visible(self.locators.TEMA_VIPYSK).send_keys(tema_5)
        elif number_tema == 6:
            self.element_if_visible(self.locators.TEMA_VIPYSK).send_keys(tema_6)
        elif number_tema == 7:
            self.element_if_visible(self.locators.TEMA_VIPYSK).send_keys(tema_7)
        mid_point = random.randint(30, 50)
        self.element_if_visible(self.locators.MID_POINT).send_keys(mid_point)
        number_study = random.randint(1, 3)
        series_study = person_info.series_study
        if number_study == 1 or number_study == 3:
            self.element_is_clickable(self.locators.YEAR_END).click()
            item_list_year = self.elements_are_visible(self.locators.SPISOK_YEAR_END)
            len_list_year = len(item_list_year)
            item_year = item_list_year[random.randint(1, len_list_year - 1)]
            item_year.click()
            self.element_if_visible(self.locators.SERIES_STUDY).send_keys(series_study)
        elif number_study == 2:
            self.element_is_clickable(self.locators.YEAR_END).click()
            item_list_year = self.elements_are_visible(self.locators.SPISOK_YEAR_END)
            len_list_year = len(item_list_year)
            item_year = item_list_year[0]
            item_year.click()
            self.element_if_visible(self.locators.CHECK_STUDY).click()
        self.element_if_visible(self.locators.NEXT6).click()
                # Работа
        letter_random = chr(random.randint(ord('a'), ord('z')))
        self.element_if_visible(self.locators.PAO).send_keys(letter_random)
        time.sleep(1)
        pyautogui.typewrite(' ', 1)
        item_list_pao = self.elements_are_visible(self.locators.SPISOK_PAO)
        len_list_pao = len(item_list_pao)
        item_pao = item_list_pao[random.randint(0, len_list_special - 1)]
        item_pao.click()
        # job_rol = person_info.job_rol
        # self.element_if_visible(self.locators.ROL).send_keys(job_rol)
        self.element_if_visible(self.locators.ROL).send_keys("3D печать и разработка технической документации")
        list_data_start_finish = self.elements_are_visible(self.locators.DATA_START_FINISH)
        start_job_invert = person_info.day_start_job
        finish_job_invert = person_info.day_finish_job
        day_start_job = list(str(start_job_invert))
        Y3 = day_start_job[:4]
        M3 = day_start_job[5:7]
        D3 = day_start_job[-2:]
        all3 = D3 + M3 + Y3
        day_finish_job = list(str(finish_job_invert))
        Y4 = day_finish_job[:4]
        M4 = day_finish_job[5:7]
        D4 = day_finish_job[-2:]
        all4 = D4 + M4 + Y4
        item_data_start = list_data_start_finish[0]
        item_data_finish = list_data_start_finish[1]
        item_data_start.send_keys(all3)
        item_data_finish.send_keys(all4)
        self.element_if_visible(self.locators.DESCRIPTION_JOB).send_keys("Разработка технической документации")
        self.element_if_visible(self.locators.NEXT6).click()
                # Курсы
        time.sleep(1)
        self.element_if_visible(self.locators.NEXT6).click()
        #self.element_if_visible(self.locators.K_OPITY).click()
                # Релевантный опыт
        item_list_accept = self.elements_are_visible(self.locators.SPISOK_EXP_ACCEPT)
        len_item_list_accept = len(item_list_accept)
        const_count = random.randint(1, 2)
        while const_count != 0:
            item_accept = item_list_accept[random.randint(0, len_item_list_accept-1)]
            if const_count > 0:
                self.go_to_element(item_accept)
                item_accept.click()
                const_count -= 1
            else:
                break
        self.element_if_visible(self.locators.NEXT10).click()
                # опыт 2
        item_list_accept = self.elements_are_visible(self.locators.SPISOK_EXP_ACCEPT)
        len_item_list_accept = len(item_list_accept)
        const_count = 17
        while const_count != 0:
            item_accept = item_list_accept[random.randint(0, len_item_list_accept - 1)]
            if const_count > 0:
                self.go_to_element(item_accept)
                item_accept.click()
                const_count -= 1
            else:
                break
        self.element_if_visible(self.locators.NEXT9).click()
                # Компетенции
        item_list_competencies = self.elements_are_visible(self.locators.COMPETENCIES)
        len_item_list_competencies = len(item_list_competencies)
        item_competencies = item_list_competencies[0]
        # item_competencies = item_list_competencies[random.randint(0, len_item_list_competencies-1)] # Рандомные компетенции
        item_competencies.click()
                # Навыки
        item_list_skills_card = self.elements_are_visible(self.locators.SKILLS_CARD)
        len_item_list_skills_card = len(item_list_skills_card)
        while len_item_list_skills_card != 0:
            if len_item_list_skills_card > 0:
                item_skills_card = item_list_skills_card[len_item_list_skills_card - 1]
                item_skills_card.click()
                item_skills_accept = self.elements_are_visible(self.locators.SKILLS_ACCEPT)
                len_item_list_skills_accept = len(item_skills_accept)
                const_count = 17
                while const_count != 0:
                    item_skills = item_skills_accept[random.randint(0, len_item_list_skills_accept - 1)]
                    if const_count > 0:
                        self.go_to_element(item_skills)
                        item_skills.click()
                        const_count -= 1
                    else:
                        break
                len_item_list_skills_card -= 1
            else:
                break
        item_list_skills_card = self.elements_are_visible(self.locators.SKILLS_CARD)
        len_item_list_skills_card = len(item_list_skills_card)
        item_krug = self.elements_are_visible(self.locators.KRUG_NUMBER)
        len_item_krug = len(item_krug)
        const_swap_right = len_item_krug - len_item_list_skills_card
        while const_swap_right != 0:
            if const_swap_right > 0:
                self.element_is_clickable(self.locators.SKILLS_SWAP_RIGHT_ACTIVE).click()
                item_list_skills_card = self.elements_are_visible(self.locators.SKILLS_CARD)
                item_skills_card = item_list_skills_card[2]
                item_skills_card.click()
                const_swap_right -= 1
                item_skills_accept = self.elements_are_visible(self.locators.SKILLS_ACCEPT)
                len_item_list_skills_accept = len(item_skills_accept)
                const_count = 17
                while const_count != 0:
                    item_skills = item_skills_accept[random.randint(0, len_item_list_skills_accept - 1)]
                    if const_count > 0:
                        self.go_to_element(item_skills)
                        item_skills.click()
                        const_count -= 1
                    else:
                        break
            else:
                break
        self.element_if_visible(self.locators.NEXT9).click()
        self.element_if_visible(self.locators.ESSE).send_keys("Работал, много работал и вот наконец заработал деньги на поезд до технополиса")
        self.element_if_visible(self.locators.NEXT9).click()
        # list_summary_person_info = self.elements_are_visible(self.locators.SUMMARY_PERSON_INFO)
        # const_count = 0
        list_all_info = []
        # while const_count != 3:
        #     self.action_triple_click(list_summary_person_info[const_count])
        #     pyautogui.hotkey('ctrl', 'c')
        #     time.sleep(.3)
        #     info = pyperclip.paste()
        #     print(info)
        #     list_all_info.append(info)
        #     const_count += 1
        # print(list_all_info)
        # time.sleep(1)
        list_summary = self.elements_are_visible(self.locators.SPISOK_SUMMARY)
        len_list_summary = len(list_summary)
        number_count = 3
        while number_count < (len_list_summary - 1):
            forma_summary = list_summary[number_count]
            forma_summary_text = forma_summary.text
            list_all_info.append(forma_summary_text)
            number_count += 1
        print(list_all_info)
        time.sleep(1)



from selenium.webdriver.common.by import By


class ElementLocators:

       # form fields
        # Проверка телефона
    TEL_NUMBER = (By.CSS_SELECTOR, 'input[placeholder="(999) 888-77-66"]')
    WX_OD = (By.CSS_SELECTOR, '#app > div > main > div > div > div > div > div > div.row.my-6.text-center.justify-center > div > form > div:nth-child(2) > div > button')
    PROVER_NUMBER = (By.CSS_SELECTOR, 'input[class="otp-field-box--0"]')
        # ФИО
    ONE_NAME = (By.CSS_SELECTOR, 'input[type="text"]')
    TWO_NAME = (By.CSS_SELECTOR, '#app > div > main > div > div > div > div > div > div.row.my-6.text-center.justify-center > div > form > div:nth-child(1) > div:nth-child(4) > div > div > div > div')
    THREE_NAME = (By.CSS_SELECTOR, '#app > div > main > div > div > div > div > div > div.row.my-6.text-center.justify-center > div > form > div:nth-child(1) > div:nth-child(5) > div.v-input.v-input--hide-details.theme--dark.v-text-field.v-text-field--is-booted.v-text-field--enclosed.v-text-field--outlined > div > div > div')
    FIO_ALL = (By.CSS_SELECTOR, 'input[type="text"]')
    ACCEPT = (By.CSS_SELECTOR, '#app > div > main > div > div > div > div > div > div.row.my-6.ext-center.justify-center > div > form > div:nth-child(2) > div > div > div > div.v-input__slot > div > div')
    NEXT = (By.CSS_SELECTOR, '#app > div > main > div > div > div > div > div > div.row.my-6.text-center.justify-center > div > form > div.row.mt-10.mb-4.justify-center > button.ml-4.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--dark.v-size--large')
        # Профили
    EMAIL = (By.CSS_SELECTOR, 'input[placeholder="example@ya.ru"]')
    NEXT2 = (By.CSS_SELECTOR, '#app > div > main > div > div > div > div > div > div.row.my-6.text-center.justify-center > div > form > div:nth-child(4) > button')
        # Скан-образы документов
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[multiple="multiple"]')
    NEXT3 = (By.CSS_SELECTOR, 'button[class="px-12 v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--large"]')
        # Паспортные данные
    KEM_VIDAN = (By.CSS_SELECTOR, 'input[placeholder="ОУФМС России по Краснодарскому краю в городе-курорте Анапа"]')
    SPISOK_YMVD_BUTTON = (By.CSS_SELECTOR, 'div[class="v-input__icon v-input__icon--append"]')
    SPISOK_YMVD = (By.CSS_SELECTOR, 'div[aria-selected="false"]')
    SERIES_NUMBER = (By.CSS_SELECTOR, 'input[placeholder="1234 123456"]')
    MY_CITY = (By.CSS_SELECTOR, 'input[placeholder="г. Москва"]')
    DATA_ALL = (By.CSS_SELECTOR, 'input[placeholder="дд.мм.гггг"]')
    NEXT4 = (By.CSS_SELECTOR, 'button[class="px-12 v-btn v-btn--is-elevated v-btn--has-bg theme--dark v-size--large"]')
    NEXT4_DISABLE = (By.CSS_SELECTOR, '[class="row mt-11 mb-2 justify-center"] button')
        # Военная служба
    VOENNYJ = (By.CSS_SELECTOR, 'input[placeholder="Военный комиссариат Называевского района"]')
    SPISOK_VOENNYJ = (By.CSS_SELECTOR, '.v-list-item__title')
    GODNOST = (By.CSS_SELECTOR, 'input[placeholder="A1"]')
    SPISOK_GODNOST = (By.CSS_SELECTOR, 'div.menuable__content__active div[class="v-list-item__content"]')
    ACCEPT2 = (By.CSS_SELECTOR, 'div.v-input--selection-controls__ripple')
    NEXT5 = (By.CSS_SELECTOR, 'div.row > button.v-btn--is-elevated')
        # Образование
    FGBOY = (By.CSS_SELECTOR, 'input[placeholder="ФГБОУ ВО «Воронежский государственный университет»"]')
    SPISOK_FGBOY = (By.CSS_SELECTOR, 'div.v-list-item')
    TIP_OBR = (By.CSS_SELECTOR, 'input[placeholder="Бакалавриат"]')
    SPISOK_TIP_OBR = (By.CSS_SELECTOR, 'div.menuable__content__active div[id*="item"]')
    SPECIAL = (By.CSS_SELECTOR, 'input[placeholder*="02.03"]')
    SPISOK_SPECIAL = (By.CSS_SELECTOR, 'div.menuable__content__active div[id*="list-item"]')
    YEAR_END = (By.CSS_SELECTOR, 'input[placeholder="2023"]')
    SPISOK_YEAR_END = (By.CSS_SELECTOR, 'li[class]')
    TEMA_VIPYSK = (By.CSS_SELECTOR, 'input[placeholder*="Анализ"]')
    MID_POINT = (By.CSS_SELECTOR, 'input[placeholder="4.5"]')
    CHECK_STUDY = (By.CSS_SELECTOR, 'label[class="v-label theme--dark"]')
    SERIES_STUDY = (By.CSS_SELECTOR, 'input[placeholder*="105505"]')
    NEXT6 = (By.CSS_SELECTOR, 'div.d-flex > button.v-btn--is-elevated')
        # Работа
    PAO = (By.CSS_SELECTOR, 'input[placeholder*="ПАО"]')
    SPISOK_PAO = (By.CSS_SELECTOR, 'div[id*="list-item"]')
    ROL = (By.CSS_SELECTOR, 'input[placeholder="Ведущий инженер"]')
    DATA_START_FINISH = (By.CSS_SELECTOR, 'input[placeholder="дд.мм.гггг"]')
    DESCRIPTION_JOB = (By.CSS_SELECTOR, 'textarea[placeholder*="Разработка"]')
    # NEXT7 = (By.CSS_SELECTOR, 'div.d-flex > button.v-btn--is-elevated') как NEXT 6
    # NEXT8 как NEXT6
    K_OPITY = (By.CSS_SELECTOR, 'div.col:first-child button.v-btn--block')
    SPISOK_EXP_ACCEPT = (By.CSS_SELECTOR, 'div.v-input')
    NEXT9 = (By.CSS_SELECTOR, 'button.v-btn--is-elevated')
    NEXT10 = (By.CSS_SELECTOR, 'button.v-btn--is-elevated:nth-child(2)')
            # Компетенции
    COMPETENCIES = (By.CSS_SELECTOR, 'div[class*=competence-card]')
            # Навыки
    SKILLS_CARD = (By.CSS_SELECTOR, 'div.competence-card')
    SKILLS_CARD_ONE_RIGHT = (By.CSS_SELECTOR, 'div.col-3:nth-child(4)')
    SKILLS_ACCEPT = (By.CSS_SELECTOR, 'div.v-input__slot')
    SKILLS_SWAP_RIGHT_ACTIVE = (By.CSS_SELECTOR, 'button.notranslate:enabled:nth-child(5)')
    KRUG_NUMBER = (By.CSS_SELECTOR, 'div.circle')
            # ЭССЕ
    ESSE = (By.CSS_SELECTOR, 'textarea[autofocus]')
            # SUMMARY
    SUMMARY_PERSON_INFO = (By.CSS_SELECTOR, 'input[type="text"]')
    SPISOK_SUMMARY_ONE = (By.CSS_SELECTOR, 'div.col-6')
    SUMMARY_OPIT_SKILLS = (By.CSS_SELECTOR, 'div.wrapper>span')
    SUMMARY_ESSEY = (By.CSS_SELECTOR, 'div.essay')










import random
import datetime

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()

def generated_person():
    yield Person(
        tel_number=faker_ru.phone_number(),
        one_name=faker_ru.last_name_male(),
        two_name=faker_ru.first_name_male(),
        three_name=faker_ru.middle_name_male(),
        email_me=faker_ru.ascii_free_email(),
        series_number=faker_ru.numerify(text='%### ######'),
        my_city=faker_ru.city(),
        day_13years=faker_ru.date_between(start_date='-13y', end_date='today'),
        day_18years=faker_ru.date_between(start_date='-27y', end_date='-18y'),
        series_study=faker_ru.numerify(text='%##### #######'),
        ogrn_number=faker_ru.numerify(text='%############'),
        job_rol=faker_ru.job(),
        day_start_job=faker_ru.date_between(start_date='-2y', end_date='-1y'),
        day_finish_job=faker_ru.date_between(start_date='-11m', end_date='today'),


    )

def generated_file():
    path = rf'C:\Users\Varnava_AV\Desktop\Мои документы\База данных\filetest{random.randint(0,999)}.jpg'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path
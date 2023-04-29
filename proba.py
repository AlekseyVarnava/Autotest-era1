from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

job = faker_ru.job()
print(job)
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()

day_18years=faker_ru.date_between(start_date='-30y', end_date='-18y')
day_list = list(str(day_18years))
Y = day_list[:4]
M = day_list[5:7]
D = day_list[-2:]
all = D + M + Y
print(D, M, Y)
print(all)
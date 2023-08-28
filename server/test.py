from faker import Faker
import random
import datetime

fake = Faker()

rDate = fake.date_time()
nDate = rDate + datetime.timedelta(hours=random.randint(1, 12))
fakePassword = fake.password()

# print(rDate)
# print(nDate)
print(fakePassword)
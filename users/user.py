import dataclasses
from datetime import datetime

from users.enums.gender import Gender
from users.enums.hobbie import Hobbie


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: datetime.date
    subject: str
    hobbie: Hobbie
    file_name: str
    address: str
    state: str
    city: str


student = User(
    'Тест',
    'Тестов',
    'test@mail.com',
    Gender.FEMALE,
    '9103335645',
    datetime(2000, 6, 15),
    'English',
    Hobbie.SPORTS,
    'picture.jpg',
    'Moscow, Bolshoi Zlatoustinskii pereulok, 6 st2',
    'Uttar Pradesh',
    'Lucknow'
    )
import datetime
from faker import Faker

from Python.test_data.phone_number_generator.mobile_phone import create_mobile_phone


class DataCreatorFake:

    def create_text(self, quantity):
        return Faker('uk_UA').text(quantity)

    def create_name(self, name_type):

        provider = Faker('uk_UA')
        if name_type == 'first':
            return provider.first_name()
        elif name_type == 'second':
            return provider.last_name()
        elif name_type == 'full':
            return provider.name()

    def create_address(self):

        return Faker('uk_UA').address()

    def create_birth_date(self):

        birthday = str(Faker("uk_UA").date_of_birth(minimum_age=18, maximum_age=25))
        return datetime.datetime.strptime(birthday, '%Y-%m-%d').strftime('%d/%m/%Y')

    def create_phone_number(self):

        return create_mobile_phone()

    def create_email(self):

        return Faker('uk_UA').email()

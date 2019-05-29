class DataCreatorFake:

    def create_text(self, quantity):
        from faker import Faker
        return Faker('uk_UA').text(quantity)

    def create_name(self, name_type):
        from faker.providers.person import Provider

        self.person_provider = Provider('uk_UA')
        if name_type == 'first':
            return self.person_provider.first_name()
        elif name_type == 'second':
            return self.person_provider.last_name()
        elif name_type == 'full':
            return self.person_provider.name()

    def create_address(self):
        from faker.providers.address import Provider

        return Provider('uk_UA').address()

    def create_birth_date(self):
        from faker.providers.date_time import Provider

        return Provider("uk_UA").date_of_birth(minimum_age=18, maximum_age=25)

    def create_phone_number(self):
        from faker.providers.phone_number import Provider
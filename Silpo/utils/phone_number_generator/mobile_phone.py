import random

from Python.test_data.phone_number_generator.predicates_data import predicates


def create_mobile_phone():

    predicate = random.choice(predicates)
    phone_number = ''
    for _ in range(7):
        phone_number += (str(random.randint(1, 9)))
    return predicate + phone_number

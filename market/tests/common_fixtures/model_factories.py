import uuid
from datetime import datetime

import factory
from factory import fuzzy

from market.models import User


class UserModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Sequence(uuid.uuid4())
    first_name = factory.Sequence(lambda n: "User First Name %d" % n)
    middle_name = factory.Sequence(lambda n: "User Middle Name %d" % n)
    last_name = factory.Sequence(lambda n: "User Last Name %d" % n)
    joined_at = fuzzy.FuzzyDate(datetime.date(2020, 1, 1))
    mobile_number = factory.Sequence(lambda n: "9676767%03d" % n)
    email = factory.Sequence(f"{first_name}{last_name}@gmail.com")
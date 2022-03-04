import factory

from market.models import User


class UserModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: "d32b2f96-93f5-4e2f-842d-d590783dc%03d" % n)
    first_name = factory.Faker('name')
    middle_name = factory.Sequence(lambda n: "User Middle Name %d" % n)
    last_name = factory.Sequence(lambda n: "User Last Name %d" % n)
    joined_at = factory.Faker("date_time")
    mobile_number = factory.Sequence(lambda n: "9676767%03d" % n)
    email = factory.LazyAttribute(lambda o: f"{o.first_name.replace(' ', '').lower()}@gmail.com")

import factory
import factory.fuzzy
from market.constants.constants import site_types
from market.models import User, SiteModel


class UserModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    first_name = factory.Faker('name')
    middle_name = factory.Sequence(lambda n: 'User Middle Name %d' % n)
    last_name = factory.Sequence(lambda n: 'User Last Name %d' % n)
    joined_at = factory.Faker('date_time')
    mobile_number = factory.Sequence(lambda n: '9676767%03d' % n)
    email = factory.LazyAttribute(
        lambda o: f"{o.first_name.replace(' ', '').lower()}@gmail.com"
    )


class SiteModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SiteModel

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dd%03d' % n)
    owner = factory.SubFactory(UserModelFactory)
    district = factory.Sequence(lambda n: 'District%03d' % n)
    state = factory.Sequence(lambda n: 'State%03d' % n)
    country = factory.Sequence(lambda n: 'Country%03d' % n)
    type = factory.fuzzy.FuzzyChoice(site_types)
    price = factory.fuzzy.FuzzyFloat(low=10000)
    availability = factory.fuzzy.FuzzyChoice([True, False])
    is_private = factory.fuzzy.FuzzyChoice([True, False])
    location_coordinates = ''
    street_name = ''
    village = ''
    city = ''

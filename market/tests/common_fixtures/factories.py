import factory
import factory.fuzzy
from market.constants.constants import site_types
from market.interactors.storages.dtos import (
    UserDetailsDTO,
    SiteDTO,
    UserDTO,
    AddUserDetailsDTO,
    LoginUserDTO,
)


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
    first_name = factory.Faker('name')
    username = factory.LazyAttribute(lambda o: o.first_name.lower())
    email = factory.LazyAttribute(
        lambda o: f"{o.first_name.replace(' ', '').lower()}@gmail.com"
    )


class UserDetailsDTOFactory(UserDTOFactory):
    class Meta:
        model = UserDetailsDTO

    last_name = factory.Sequence(lambda n: 'User Last Name %d' % n)
    date_joined = str(factory.Faker('date_time'))
    mobile_number = factory.Sequence(lambda n: '9676767%03d' % n)


class AddUserDetailsDTOFactory(UserDTOFactory):
    class Meta:
        model = AddUserDetailsDTO

    password = factory.Sequence(lambda n: 'password%d' % n)
    is_staff = False
    is_active = False
    last_name = factory.Sequence(lambda n: 'User Last Name %d' % n)
    date_joined = str(factory.Faker('date_time'))
    mobile_number = factory.Sequence(lambda n: '9676767%03d' % n)


class SiteDTOFactory(factory.Factory):
    class Meta:
        model = SiteDTO

    id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dd%03d' % n)
    owner_id = factory.Sequence(lambda n: 'd32b2f96-93f5-4e2f-842d-d590783dc%03d' % n)
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


class LoginUserDTOFactory(factory.Factory):
    class Meta:
        model = LoginUserDTO

    username = factory.Faker('name')
    password = factory.Sequence(lambda n: 'password%d' % n)

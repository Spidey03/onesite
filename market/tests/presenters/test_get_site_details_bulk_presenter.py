import pytest

from market.tests.common_fixtures.reset_sequence import reset

SITE_ID = "d32b2f96-93f5-4e2f-842d-d590783dd001"


class TestGetSiteDetailsBulkPresenter:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation
        return PresenterImplementation()

    @pytest.fixture
    def site_dtos(self):
        from market.tests.common_fixtures.factories import SiteDTOFactory
        reset()
        site_dto = SiteDTOFactory.create_batch(
            size=3,
            id=SITE_ID,
            price=487.059109240635,
            is_private=True,
            type='Site',
            availability=False
        )
        return site_dto

    @pytest.fixture
    def owner_dtos(self):
        from market.tests.common_fixtures.factories import UserDetailsDTOFactory
        reset()
        owner_dto = UserDetailsDTOFactory.create_batch(
            size=3,
            email='codywilliams@gmail.com',
            first_name='Cody Williams',
            joined_at='2022-03-22',
            last_name='User Last Name 0',
            middle_name='User Middle Name 0',
            mobile_number='9676767000'
        )
        return owner_dto

    @pytest.fixture
    def response_get_site_details_bulk(self):
        return [{
            'availability': False,
            'city': '',
            'country': 'Country000',
            'district': 'District000',
            'id': 'd32b2f96-93f5-4e2f-842d-d590783dd001',
            'is_private': True,
            'location_coordinates': '',
            'owner': {'email': 'codywilliams@gmail.com',
                      'first_name': 'Cody Williams',
                      'id': 'd32b2f96-93f5-4e2f-842d-d590783dc000',
                      'joined_at': '2022-03-22',
                      'last_name': 'User Last Name 0',
                      'middle_name': 'User Middle Name 0',
                      'mobile_number': '9676767000'},
            'price': 487.059109240635,
            'state': 'State000',
            'street_name': '',
            'type': 'Site',
            'village': ''
        },
            {'availability': False,
             'city': '',
             'country': 'Country001',
             'district': 'District001',
             'id': 'd32b2f96-93f5-4e2f-842d-d590783dd001',
             'is_private': True,
             'location_coordinates': '',
             'owner': {'email': 'codywilliams@gmail.com',
                       'first_name': 'Cody Williams',
                       'id': 'd32b2f96-93f5-4e2f-842d-d590783dc001',
                       'joined_at': '2022-03-22',
                       'last_name': 'User Last Name 0',
                       'middle_name': 'User Middle Name 0',
                       'mobile_number': '9676767000'},
             'price': 487.059109240635,
             'state': 'State001',
             'street_name': '',
             'type': 'Site',
             'village': ''
             },
            {'availability': False,
             'city': '',
             'country': 'Country002',
             'district': 'District002',
             'id': 'd32b2f96-93f5-4e2f-842d-d590783dd001',
             'is_private': True,
             'location_coordinates': '',
             'owner': {'email': 'codywilliams@gmail.com',
                       'first_name': 'Cody Williams',
                       'id': 'd32b2f96-93f5-4e2f-842d-d590783dc002',
                       'joined_at': '2022-03-22',
                       'last_name': 'User Last Name 0',
                       'middle_name': 'User Middle Name 0',
                       'mobile_number': '9676767000'},
             'price': 487.059109240635,
             'state': 'State002',
             'street_name': '',
             'type': 'Site',
             'village': ''
             }
        ]

    def test_get_site_details_bulk_response(self, presenter, site_dtos, owner_dtos, response_get_site_details_bulk):
        # Arrange

        # Act
        response = presenter.get_sites_bulk_response(
            site_dto_list=site_dtos,
            owner_dto_list=owner_dtos
        )

        # Arrange
        assert response == response_get_site_details_bulk

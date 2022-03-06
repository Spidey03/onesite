import pytest

from market.tests.common_fixtures.reset_sequence import reset

SITE_ID = "d32b2f96-93f5-4e2f-842d-d590783dd001"


class TestSiteNotFoundExceptionPresenter:
    @pytest.fixture
    def presenter(self):
        reset()
        from market.presenters.presenter_implementation import PresenterImplementation
        return PresenterImplementation()

    @pytest.fixture
    def site_dto(self):
        from market.tests.common_fixtures.factories import SiteDTOFactory
        site_dto = SiteDTOFactory(id=SITE_ID, price=487.059109240635, is_private=True, type='Site')
        return site_dto

    @pytest.fixture
    def owner_dto(self):
        from market.tests.common_fixtures.factories import UserDetailsDTOFactory
        owner_dto = UserDetailsDTOFactory(
            email='codywilliams@gmail.com',
            first_name='Cody Williams',
            id='d32b2f96-93f5-4e2f-842d-d590783dc000',
            joined_at='2022-03-22',
            last_name='User Last Name 0',
            middle_name='User Middle Name 0',
            mobile_number='9676767000'
        )
        return owner_dto

    @pytest.fixture
    def response_get_site_details(self):
        return {
            'availability': False,
            'city': '',
            'country': 'Country000',
            'district': 'District000',
            'id': 'd32b2f96-93f5-4e2f-842d-d590783dd001',
            'is_private': True,
            'location_coordinates': '',
            'owner': {
                'email': 'codywilliams@gmail.com',
                'first_name': 'Cody Williams',
                'id': 'd32b2f96-93f5-4e2f-842d-d590783dc000',
                'joined_at': '2022-03-22',
                'last_name': 'User Last Name 0',
                'middle_name': 'User Middle Name 0',
                'mobile_number': '9676767000'
            },
            'price': 487.059109240635,
            'state': 'State000',
            'street_name': '',
            'type': 'Site',
            'village': ''
        }

    def test_site_not_found_exception_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'SITE_NOT_FOUND_EXCEPTION',
            'response': 'Site not found with id: d32b2f96-93f5-4e2f-842d-d590783dd001',
            'status_code': 400
        }

        # Act
        response = presenter.get_site_not_found_exception_response(site_id=SITE_ID)

        # Arrange
        assert response == expected_response

    def test_get_site_details(self, presenter, site_dto, owner_dto, response_get_site_details):
        # Arrange

        # Act
        response = presenter.get_site_details_response(
            site_dto=site_dto,
            owner_dto=owner_dto
        )

        # Arrange
        assert response == response_get_site_details

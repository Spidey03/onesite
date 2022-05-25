import pytest

from market.tests.common_fixtures.factories import UserDetailsDTOFactory
from market.tests.common_fixtures.reset_sequence import reset


class TestAddUserDetailsSuccessResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    @pytest.fixture
    def user_details_dto(self):
        reset()
        return UserDetailsDTOFactory(
            username='ironman',
            first_name='Tony',
            last_name='Stark',
            mobile_number='9999877980',
            email='tony.stark@hotmail.com',
        )

    def test_add_user_details_success_response(self, presenter, user_details_dto):
        # Arrange
        import datetime
        from common.storage_implementation.dtos import UserAuthTokensDTO

        token_dto = UserAuthTokensDTO(
            user_id='f2c8cf25-10fe-4ce6-ba8b-1ab5fd355339',
            access_token='D5BlCiwEpQ6v7s9ykHIlgQlWSRelpt',
            refresh_token='OksuViZaG5dGTSI04mzQNADeUbM6zw',
            expires=datetime.datetime(2022, 5, 25, 15, 38, 46, 922544),
        )

        expected_response = {
            'access_token': 'D5BlCiwEpQ6v7s9ykHIlgQlWSRelpt',
            'email': 'tony.stark@hotmail.com',
            'first_name': 'Tony',
            'last_name': 'Stark',
            'mobile_number': '9999877980',
            'user_id': 'd32b2f96-93f5-4e2f-842d-d590783dc000',
        }
        # Act
        response = presenter.add_user_details_success_response(
            user_dto=user_details_dto, auth_token_dto=token_dto
        )

        # Arrange
        assert response == expected_response

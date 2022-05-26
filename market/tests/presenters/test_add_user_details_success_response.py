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

        expected_response = {
            'email': 'tony.stark@hotmail.com',
            'first_name': 'Tony',
            'last_name': 'Stark',
            'mobile_number': '9999877980',
            'user_id': 'd32b2f96-93f5-4e2f-842d-d590783dc000',
            'username': 'ironman',
        }
        # Act
        response = presenter.add_user_details_success_response(
            user_dto=user_details_dto
        )

        # Arrange
        assert response == expected_response

import pytest

from market.tests.common_fixtures.reset_sequence import reset


class TestGetUserDetails:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        presenter = PresenterImplementation()
        return presenter

    @pytest.fixture
    def user_details_dto(self):
        reset()
        from market.tests.common_fixtures.factories import UserDetailsDTOFactory

        return UserDetailsDTOFactory.create(
            first_name='Peter',
            last_name='',
            middle_name='',
            joined_at='2022-03-04 00:00:00',
        )

    def test_get_user_details(self, user_details_dto, presenter):
        # Arrange
        expected_response = {
            'user_id': 'd32b2f96-93f5-4e2f-842d-d590783dc000',
            'first_name': 'Peter',
            'middle_name': '',
            'last_name': '',
            'email': 'peter@gmail.com',
            'mobile_number': '9676767000',
            'joined_at': '2022-03-04 00:00:00',
        }

        # Act
        response = presenter.get_user_details(user_details_dto=user_details_dto)

        # Assert
        assert response == expected_response

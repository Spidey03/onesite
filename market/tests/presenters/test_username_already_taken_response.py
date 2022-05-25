import pytest

from market.tests.common_fixtures.reset_sequence import reset

SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd001'


class TestUsernameAlreadyTakenResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_username_already_taken_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USERNAME_ALREADY_TAKEN_EXCEPTION',
            'response': 'joey567 is already registered, please try with another username',
            'status_code': 400,
        }

        # Act
        response = presenter.username_already_taken_response(username='joey567')

        # Arrange
        assert response == expected_response

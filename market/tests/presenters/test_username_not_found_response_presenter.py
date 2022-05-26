import pytest


class TestUsernameNotFoundResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_username_not_found_response(self, presenter):
        # Arrange
        username = 'ironman'
        expected_response = {
            'res_status': 'USERNAME_NOT_FOUND',
            'response': 'Entered username not found: ironman',
            'status_code': 400,
        }

        # Act
        response = presenter.username_not_found_response(username=username)

        # Arrange
        assert response == expected_response

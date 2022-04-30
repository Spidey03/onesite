import pytest


class TestUserNotFoundResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation
        return PresenterImplementation()

    def test_user_not_present_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USER_NOT_EXISTS',
            'response': 'User not found',
            'status_code': 400
        }
        # Act
        response = presenter.user_not_present_response()

        # Arrange
        assert response == expected_response

import pytest


class TestLoginFailedResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_login_failed_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'LOGIN_FAILED',
            'response': 'Either username or password are incorrect',
            'status_code': 400,
        }

        # Act
        response = presenter.login_failed_response()

        # Arrange
        assert response == expected_response

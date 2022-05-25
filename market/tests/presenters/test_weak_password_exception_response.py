import pytest


class TestWeakPasswordResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_weak_password_exception_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'WEAK_PASSWORD_EXCEPTION',
            'response': 'A minimum 8 characters password contains a combination of '
            'uppercase and lowercase letter and number',
            'status_code': 400,
        }
        # Act
        response = presenter.weak_password_exception_response()

        # Arrange
        assert response == expected_response

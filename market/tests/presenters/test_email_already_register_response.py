import pytest


class TestA:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation
        return PresenterImplementation()

    def test_email_already_register_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'EMAIL_ALREADY_EXIST',
            'response': 'tonystark@gmail.com is already registered, please try with another email',
            'status_code': 400
        }
        # Act
        response = presenter.email_already_register_response(
            email="tonystark@gmail.com"
        )

        # Arrange
        assert response == expected_response

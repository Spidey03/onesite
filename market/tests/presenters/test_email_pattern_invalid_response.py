import pytest


class TestA:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation
        return PresenterImplementation()

    def test_email_pattern_invalid_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'EMAIL_PATTERN_INVALID',
            'response': 'tonystark.com is invalid pattern',
            'status_code': 400
        }
        # Act
        response = presenter.email_pattern_invalid_response(
            email="tonystark.com"
        )

        # Arrange
        assert response == expected_response

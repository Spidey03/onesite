import pytest


class TestMobileNumberAlreadyRegisteredResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation
        return PresenterImplementation()

    def test_mobile_number_already_registered_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'MOBILE_NUMBER_ALREADY_EXIST',
            'response': '99029783283 is already registered, please try with another mobile number',
            'status_code': 400
        }
        # Act
        response = presenter.mobile_number_already_registered_response(
            mobile_number="99029783283"
        )

        # Arrange
        assert response == expected_response

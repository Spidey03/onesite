import pytest


class TestAddUserDetailsSuccessResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_add_user_details_success_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USER_DETAILS_ADDED_SUCCESSFULLY',
            'response': 'User details added successfully',
            'status_code': 201,
        }
        # Act
        response = presenter.add_user_details_success_response()

        # Arrange
        assert response == expected_response

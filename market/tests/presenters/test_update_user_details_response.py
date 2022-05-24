import pytest


class TestUpdateUserDetailsResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_update_user_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USER_DETAILS_UPDATED_SUCCESSFULLY',
            'response': 'User details updated successfully',
            'status_code': 200,
        }
        # Act
        response = presenter.update_user_details_success_response()

        # Arrange
        assert response == expected_response

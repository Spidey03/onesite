import pytest


class TestDeleteUserSuccessfullyResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_user_deleted_successfully_response(self, presenter):
        # Arrange
        expected_response = {
            'res_status': 'USER_DELETE_SUCCESSFULLY',
            'response': 'User account removed successfully, you can recover your account when you needed',
            'status_code': 200,
        }
        # Act
        response = presenter.user_deleted_successfully_response()

        # Arrange
        assert response == expected_response

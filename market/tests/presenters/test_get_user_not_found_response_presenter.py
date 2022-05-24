import pytest

from market.constants.exception_message import USER_NOT_FOUND_EXCEPTION


class TestGetUserNotFoundResponsePresenter:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        presenter = PresenterImplementation()
        return presenter

    def test_get_response(self, presenter):
        # Arrange
        user_id = 'd32b2f96-93f5-4e2f-842d-d590783dceft'
        expected_response = {
            'response': USER_NOT_FOUND_EXCEPTION[0].format(user_id),
            'res_status': USER_NOT_FOUND_EXCEPTION[1],
            'status_code': 400,
        }

        # Act
        response = presenter.get_user_not_found_response(user_id=user_id)

        # Assert
        assert response == expected_response

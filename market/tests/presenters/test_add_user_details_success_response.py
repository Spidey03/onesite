import pytest


class TestAddUserDetailsSuccessResponse:
    @pytest.fixture
    def presenter(self):
        from market.presenters.presenter_implementation import PresenterImplementation

        return PresenterImplementation()

    def test_add_user_details_success_response(self, presenter):
        # Arrange
        import datetime
        from common.storage_implementation.dtos import UserAuthTokensDTO

        token_dto = UserAuthTokensDTO(
            user_id='f2c8cf25-10fe-4ce6-ba8b-1ab5fd355339',
            access_token='D5BlCiwEpQ6v7s9ykHIlgQlWSRelpt',
            refresh_token='OksuViZaG5dGTSI04mzQNADeUbM6zw',
            expires=datetime.datetime(2022, 5, 25, 15, 38, 46, 922544),
        )

        expected_response = {
            'access_token': 'D5BlCiwEpQ6v7s9ykHIlgQlWSRelpt',
            'expires_in': datetime.datetime(2022, 5, 25, 15, 38, 46, 922544),
            'refresh_token': 'OksuViZaG5dGTSI04mzQNADeUbM6zw',
            'user_id': 'f2c8cf25-10fe-4ce6-ba8b-1ab5fd355339',
        }
        # Act
        response = presenter.add_user_details_success_response(auth_token_dto=token_dto)

        # Arrange
        assert response == expected_response

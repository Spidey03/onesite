import pytest

from market.storages.user_storage_implementation import UserStorageImplementation
from market.tests.common_fixtures.reset_sequence import reset


class TestAuthenticateUser:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = UserStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def users_db(self):
        reset()
        from django.contrib.auth.hashers import make_password
        from market.tests.common_fixtures.model_factories import UserModelFactory

        u = UserModelFactory(
            id='d32b2f96-93f5-4e2f-842d-d590783dc001',
            username='joey123',
            email='jondoe@gmail.com',
            mobile_number='8398393229',
        )
        hash_password = make_password(password='12345')
        u.password = hash_password
        u.save()

    @pytest.fixture
    def user_dto(self):
        from market.tests.common_fixtures.factories import LoginUserDTOFactory

        reset()
        return LoginUserDTOFactory.create(username='joey123', password='12345')

    @pytest.mark.django_db
    def test_when_match_username_and_password(self, storage, users_db, user_dto):
        # Arrange
        expected_user_id = 'd32b2f96-93f5-4e2f-842d-d590783dc001'

        # Act
        user_id, is_authenticated = storage.authenticate_user(user_dto=user_dto)

        # Assert
        assert user_id == expected_user_id
        assert is_authenticated is True

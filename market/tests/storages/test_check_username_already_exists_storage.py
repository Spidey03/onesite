import pytest

from market.storages.user_storage_implementation import UserStorageImplementation
from market.tests.common_fixtures.reset_sequence import reset


class TestMobileNumberAlreadyExist:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = UserStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def users_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory

        UserModelFactory.create(
            id='d32b2f96-93f5-4e2f-842d-d590783dc001',
            username='joey123',
            email='jondoe@gmail.com',
            mobile_number='8398393229',
        )

    @pytest.mark.django_db
    def test_when_username_exists(self, storage):
        # Arrange
        username = 'joey123'

        # Act
        response = storage.check_username_already_exists(username=username)

        # Assert
        assert response is True

    @pytest.mark.django_db
    def test_when_username_does_not_exist(self, storage, users_db):
        # Arrange
        username = 'joey1234'

        # Act
        response = storage.check_username_already_exists(username=username)

        # Assert
        assert response is False

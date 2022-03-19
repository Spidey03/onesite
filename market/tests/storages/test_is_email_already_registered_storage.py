import pytest

from market.storages.user_storage_implementation import UserStorageImplementation
from market.tests.common_fixtures.reset_sequence import reset


class TestIsEmailAlreadyRegisteredStorage:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = UserStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def users_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory
        UserModelFactory.create(
            id="d32b2f96-93f5-4e2f-842d-d590783dc001",
            email="jondoe@gmail.com"
        )

    @pytest.mark.django_db
    def test_when_email_exist(self, storage):
        # Arrange
        email = "notexist@hotmail.com"

        # Act
        response = storage.is_email_already_registered(email=email)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_when_email_not_exists(self, storage, users_db):
        # Arrange
        email = "jondoe@gmail.com"

        # Act
        response = storage.is_email_already_registered(email=email)

        # Assert
        assert response is True

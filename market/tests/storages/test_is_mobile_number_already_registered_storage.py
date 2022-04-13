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
            id="d32b2f96-93f5-4e2f-842d-d590783dc001",
            email="jondoe@gmail.com",
            mobile_number="8398393229"
        )

    @pytest.mark.django_db
    def test_when_mobile_number_exist(self, storage):
        # Arrange
        mobile_number = "9088938393"

        # Act
        response = storage.is_mobile_number_already_registered(
            mobile_number=mobile_number
        )

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_when_user_exists(self, storage, users_db):
        # Arrange
        mobile_number = "8398393229"

        # Act
        response = storage.is_mobile_number_already_registered(
            mobile_number=mobile_number
        )

        # Assert
        assert response is True

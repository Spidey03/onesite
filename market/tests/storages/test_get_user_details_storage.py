import pytest

from market.storages.user_storage_implementation import UserStorageImplementation
from market.tests.common_fixtures.reset_sequence import reset


class TestGetUserDetailsStorage:
    @pytest.fixture
    def storage(self):
        storage = UserStorageImplementation()
        return storage

    @pytest.fixture
    def users_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory
        UserModelFactory.create()

    @pytest.mark.django_db
    def test_raise_user_not_found_error(self, storage):
        # Arrange
        user_id = "d32b2f96-93f5-4e2f-842d-d590783dcfeb"

        from market.exceptions.exceptions import UserNotFoundException
        with pytest.raises(UserNotFoundException):
            user_details_dto = storage.get_user(user_id=user_id)

    @pytest.mark.django_db
    def test_get_user_details(self, storage, users_db):
        # Arrange
        user_id = "d32b2f96-93f5-4e2f-842d-d590783dcfeb"
        expected_user_details_dto = None

        # Act
        user_details_dto = storage.get_user(user_id=user_id)

        # Assert
        assert user_details_dto == expected_user_details_dto
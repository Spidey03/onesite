import factory
import pytest

from market.storages.user_storage_implementation import UserStorageImplementation
from market.tests.common_fixtures.reset_sequence import reset


class TestIsAccountDisabled:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = UserStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def users_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory

        usernames = ['joey123', 'nolan123']
        user_objs = UserModelFactory.create_batch(
            size=len(usernames), username=factory.Iterator(usernames)
        )
        user_objs[-1].is_removed = True
        user_objs[-1].save()

    @pytest.mark.django_db
    def test_when_checking_with_username_not_disabled(self, storage):
        # Arrange
        username = 'joey123'

        # Act
        response = storage.is_account_disabled(username=username)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_when_checking_with_user_id_not_disabled(self, storage, users_db):
        # Arrange
        user_id = 'd32b2f96-93f5-4e2f-842d-d590783dc000'

        # Act
        response = storage.is_account_disabled(user_id=user_id)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_when_checking_with_username_disabled(self, storage, users_db):
        # Arrange
        username = 'nolan123'

        # Act
        response = storage.is_account_disabled(username=username)

        # Assert
        assert response is True

    @pytest.mark.django_db
    def test_when_checking_with_user_id_disabled(self, storage, users_db):
        # Arrange
        user_id = 'd32b2f96-93f5-4e2f-842d-d590783dc001'

        # Act
        response = storage.is_account_disabled(user_id=user_id)

        # Assert
        assert response is True

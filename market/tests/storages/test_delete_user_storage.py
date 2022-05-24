import datetime

import pytest

from market.storages.user_storage_implementation import UserStorageImplementation
from market.tests.common_fixtures.reset_sequence import reset


class TestDeleteUser:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = UserStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def users_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory

        UserModelFactory.create(id='d32b2f96-93f5-4e2f-842d-d590783dc001')

    @pytest.mark.django_db
    def test_delete_user(self, storage):
        # Arrange
        user_id = 'd32b2f96-93f5-4e2f-842d-d590783dc002'

        # Act
        response = storage.delete_user(user_id=user_id)

        # Assert
        from market.models import User

        is_deleted = not User.objects.filter(id=user_id).exists()
        assert is_deleted is True

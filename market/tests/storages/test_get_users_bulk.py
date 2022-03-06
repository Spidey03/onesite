import datetime

import factory
import pytest

from market.storages.user_storage_implementation import UserStorageImplementation
from market.tests.common_fixtures.factories import UserDetailsDTOFactory
from market.tests.common_fixtures.reset_sequence import reset

USER_IDS = [
    "d32b2f96-93f5-4e2f-842d-d590783dc001",
    "d32b2f96-93f5-4e2f-842d-d590783dc002",
]


class TestGetUsersBulkStorage:
    @pytest.fixture(autouse=True)
    def storage(self):
        storage = UserStorageImplementation()
        return storage

    @pytest.fixture(autouse=True)
    def users_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory
        UserModelFactory.create_batch(
            size=len(USER_IDS),
            id=factory.Iterator(USER_IDS),
            joined_at=datetime.datetime(2022, 3, 22),
            first_name=factory.Iterator(["Steve", "Tony"])
        )

    @pytest.mark.django_db
    def test_no_users_found(self, storage):
        # Arrange
        user_ids = [
            "d32b2f96-93f5-4e2f-842d-d590783dc008",
            "d32b2f96-93f5-4e2f-842d-d590783dc009",
        ]

        # Act
        user_details_dtos = storage.get_users_bulk(user_ids=user_ids)

        # Assert
        assert user_details_dtos == []

    @pytest.mark.django_db
    def test_get_user_details(self, storage, users_db):
        # Arrange

        # Act
        expected_user_details_dtos = UserDetailsDTOFactory.create_batch(
                size=len(USER_IDS),
                id=factory.Iterator(USER_IDS),
                joined_at=str(datetime.datetime(2022, 3, 22)),
                first_name=factory.Iterator(["Steve", "Tony"])
            )

        # Act
        user_details_dtos = storage.get_users_bulk(user_ids=USER_IDS)

        # Assert
        assert user_details_dtos == expected_user_details_dtos

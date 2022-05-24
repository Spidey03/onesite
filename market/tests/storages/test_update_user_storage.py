import datetime

import factory
import pytest

from market.tests.common_fixtures.reset_sequence import reset

USER_IDS = [
    'd32b2f96-93f5-4e2f-842d-d590783dc001',
    'd32b2f96-93f5-4e2f-842d-d590783dc002',
]


class TestAddSiteDetailsStorage:
    @pytest.fixture
    def storage(self):
        from market.storages.user_storage_implementation import (
            UserStorageImplementation,
        )

        return UserStorageImplementation()

    @pytest.fixture
    def user_dto(self):
        from market.tests.common_fixtures.factories import UserDetailsDTOFactory

        reset()
        user_dto = UserDetailsDTOFactory.create(
            id='d32b2f96-93f5-4e2f-842d-d590783dc001'
        )
        return user_dto

    @pytest.fixture
    def user_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory

        UserModelFactory.create_batch(
            size=len(USER_IDS),
            id=factory.Iterator(USER_IDS),
            joined_at=datetime.datetime(2022, 3, 22),
            first_name=factory.Iterator(['Steve', 'Tony']),
        )

    @pytest.mark.django_db
    def test_add_site_details(self, storage, user_db, user_dto):
        # Arrange
        user_id = user_dto.id

        # Act
        storage.update_user(user_details_dto=user_dto)

        # Assert
        from market.models import User

        user_obj = User.objects.get(id=user_id)
        assert user_obj.first_name == user_dto.first_name
        assert user_obj.last_name == user_dto.last_name
        assert user_obj.middle_name == user_dto.middle_name
        assert user_obj.mobile_number == user_dto.mobile_number
        assert user_obj.email == user_dto.email

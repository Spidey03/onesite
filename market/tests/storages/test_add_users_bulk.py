import pytest

from market.tests.common_fixtures.reset_sequence import reset


class TestAddSiteDetailsStorage:
    @pytest.fixture
    def storage(self):
        from market.storages.user_storage_implementation import (
            UserStorageImplementation,
        )

        return UserStorageImplementation()

    @pytest.fixture
    def user_dtos(self):
        from market.tests.common_fixtures.factories import AddUserDetailsDTOFactory

        reset()
        user_dto = AddUserDetailsDTOFactory.create_batch(size=3)
        return user_dto

    @pytest.mark.django_db
    def test_add_site_details(self, storage, user_dtos):
        # Arrange

        # Act
        storage.add_users_bulk(user_details_dto_list=user_dtos)

        # Assert
        from market.models import User

        assert User.objects.filter(id=user_dtos[-1].id).exists() is True

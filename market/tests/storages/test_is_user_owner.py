import pytest

from market.tests.common_fixtures.reset_sequence import reset

USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd001'


class TestIsUserOwner:
    @pytest.fixture
    def storage(self):
        from market.storages.site_storage_implementation import (
            SiteStorageImplementation,
        )

        return SiteStorageImplementation()

    @pytest.fixture
    def site_db(self):
        from market.tests.common_fixtures.model_factories import UserModelFactory
        from market.tests.common_fixtures.model_factories import SiteModelFactory

        user = UserModelFactory(id=USER_ID)
        SiteModelFactory(id=SITE_ID, owner=user)

    @pytest.fixture
    def site_dto(self):
        from market.tests.common_fixtures.factories import SiteDTOFactory

        reset()
        site_dto = SiteDTOFactory(
            id=SITE_ID,
            owner_id=USER_ID,
            price=99909.0,
            type='SITE',
            availability=True,
            is_private=False,
        )
        return site_dto

    @pytest.mark.django_db
    def test_when_user_is_not_owner(self, storage, site_db):
        # Arrange
        user_id = 'd32b2f96-93f5-4e2f-842d-d590783dc002'

        # Act
        is_owner = storage.is_user_owner(site_id=SITE_ID, user_id=user_id)

        # Assert
        assert is_owner is False

    @pytest.mark.django_db
    def test_when_user_is_owner(self, storage, site_db):
        # Arrange

        # Act
        is_owner = storage.is_user_owner(site_id=SITE_ID, user_id=USER_ID)

        # Assert
        assert is_owner is False

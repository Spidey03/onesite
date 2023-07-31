import pytest

from market.tests.common_fixtures.reset_sequence import reset

USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd001'


class TestGetSiteDetails:
    @pytest.fixture
    def storage(self):
        from market.storages.site_storage_implementation import (
            SiteStorageImplementation,
        )

        return SiteStorageImplementation()

    @pytest.fixture
    def site_db(self):
        from market.tests.common_fixtures.model_factories import SiteModelFactory
        from market.tests.common_fixtures.model_factories import UserModelFactory

        user = UserModelFactory(id=USER_ID)
        return SiteModelFactory.create(
            id=SITE_ID,
            owner=user,
            price=99909.0,
            type='SITE',
            availability=True,
            is_private=False,
        )

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
    def test_raises_site_not_found_exception(self, storage):
        # Arrange
        site_id = 'd32b2f96-93f5-4e2f-842d-d590783dd001'

        # Act
        from market.exceptions.exceptions import SiteNotFoundException

        with pytest.raises(SiteNotFoundException):
            storage.get_site_details(site_id=site_id)

    @pytest.mark.django_db
    def test_when_site_not_exists(self, storage, site_db, site_dto):
        # Arrange
        site_id = 'd32b2f96-93f5-4e2f-842d-d590783dd002'
        expected_result = False

        # Act
        actual_result = storage.check_site_exists(site_id=site_id)

        # Assert
        assert actual_result is expected_result

    @pytest.mark.django_db
    def test_when_site_not_exists(self, storage, site_db, site_dto):
        # Arrange
        site_id = 'd32b2f96-93f5-4e2f-842d-d590783dd001'
        expected_result = True

        # Act
        actual_result = storage.check_site_exists(site_id=site_id)

        # Assert
        assert actual_result is expected_result

import pytest

from market.tests.common_fixtures.reset_sequence import reset

USER_ID = "d32b2f96-93f5-4e2f-842d-d590783dc001"
SITE_ID = "d32b2f96-93f5-4e2f-842d-d590783dd001"


class TestAddSiteDetailsStorage:
    @pytest.fixture
    def storage(self):
        from market.storages.site_storage_implementation \
            import SiteStorageImplementation
        return SiteStorageImplementation()

    @pytest.fixture
    def site_db(self):
        from market.tests.common_fixtures.model_factories \
            import UserModelFactory
        user = UserModelFactory(id=USER_ID)

    @pytest.fixture
    def site_dto(self):
        from market.tests.common_fixtures.factories import SiteDTOFactory
        reset()
        site_dto = SiteDTOFactory(
            id=SITE_ID,
            owner_id=USER_ID,
            price=99909.0, type="SITE", availability=True, is_private=False
        )
        return site_dto

    @pytest.mark.django_db
    def test_add_site_details(self, storage, site_db, site_dto):
        # Arrange

        # Act
        storage.add_site_details(site_dto=site_dto)

        # Assert
        from market.models import SiteModel
        assert SiteModel.objects.filter(id=SITE_ID).exists() is True

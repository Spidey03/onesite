import pytest

from market.tests.common_fixtures.reset_sequence import reset


class TestGetSitesBulkStorage:

    @pytest.fixture
    def storage(self):
        from market.storages.site_storage_implementation import SiteStorageImplementation
        return SiteStorageImplementation()

    @pytest.fixture
    def sites_objs(self):
        reset()
        from market.tests.common_fixtures.model_factories import SiteModelFactory
        SiteModelFactory.create_batch(size=3, is_private=False, price=3000.0, type='Site', availability=True)
        SiteModelFactory.create(is_private=True,  availability=True, type='Site', price=100.0)
        SiteModelFactory.create(is_private=False, availability=False, type='Home', price=200.0)

    @pytest.fixture
    def site_dto_list(self):
        reset()
        from market.tests.common_fixtures.factories import SiteDTOFactory
        site_dtos = SiteDTOFactory.create_batch(size=3, is_private=False, price=3000.0, type='Site', availability=True)
        site_dtos.append(SiteDTOFactory.create(is_private=True,  availability=True, type='Site', price=100.0))
        site_dtos.append(SiteDTOFactory.create(is_private=False, availability=False, type='Home', price=200.0))
        return site_dtos

    @pytest.mark.django_db
    def test_when_no_sites_available(self, storage):
        # Arrange
        expected_site_dtos_list = []

        # Act
        site_dtos = storage.get_sites_bulk()

        # Assert
        assert site_dtos == expected_site_dtos_list

    @pytest.mark.django_db
    def test_when_sites_available(self, storage, sites_objs, site_dto_list):
        # Arrange

        # Act
        site_dtos = storage.get_sites_bulk()

        # Assert
        assert site_dtos == site_dto_list
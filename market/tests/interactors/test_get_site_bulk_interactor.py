from unittest.mock import create_autospec, Mock

import factory
import pytest

from market.tests.common_fixtures.reset_sequence import reset

USER_IDS = [
    "d32b2f96-93f5-4e2f-842d-d590783dc001",
    "d32b2f96-93f5-4e2f-842d-d590783dc002",
    "d32b2f96-93f5-4e2f-842d-d590783dc002"
]


class TestGetSiteDetailsBulkInteractor:

    @pytest.fixture
    def user_storage(self):
        from market.interactors.storages.user_storages_interface import UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def site_storage(self):
        from market.interactors.storages.site_storages_interface \
            import SiteStorageInterface
        storage = create_autospec(SiteStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, site_storage, user_storage):
        from market.interactors.get_site_details_bulk import GetSiteDetailsBulkInteractor
        return GetSiteDetailsBulkInteractor(
            site_storage=site_storage,
            user_storage=user_storage
        )

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface \
            import PresenterInterface
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def site_dto_list(self):
        reset()
        from market.tests.common_fixtures.factories import SiteDTOFactory
        return SiteDTOFactory.create_batch(
            size=3, owner_id=factory.Iterator(USER_IDS)
        )

    @pytest.fixture
    def owner_dto_list(self):
        reset()
        from market.tests.common_fixtures.factories import UserDetailsDTOFactory
        return UserDetailsDTOFactory.create_batch(
            size=len(list(set(USER_IDS))),
            id=factory.Iterator(list(set(USER_IDS)))
        )

    def test_returns_response(
            self,
            site_storage,
            user_storage,
            interactor,
            presenter,
            site_dto_list,
            owner_dto_list
    ):
        # Arrange
        site_storage.get_sites_bulk.return_value = site_dto_list
        user_storage.get_users_bulk.return_value = owner_dto_list
        presenter.get_sites_bulk_response.return_value = Mock()

        # Act
        interactor.get_site_bulk_wrapper(presenter=presenter)

        # Assert
        site_storage.get_sites_bulk.assert_called_once()
        user_storage.get_users_bulk.assert_called_once_with(user_ids=list(set(USER_IDS)))
        presenter.get_sites_bulk_response.assert_called_once_with(
            site_dto_list=site_dto_list,
            owner_dto_list=owner_dto_list
        )

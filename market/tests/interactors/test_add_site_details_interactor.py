from unittest.mock import create_autospec, Mock

import pytest

from market.tests.common_fixtures.reset_sequence import reset


class TestGetSiteDetailsBulkInteractor:
    @pytest.fixture
    def user_storage(self):
        from market.interactors.storages.user_storages_interface import (
            UserStorageInterface,
        )

        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def site_storage(self):
        from market.interactors.storages.site_storages_interface import (
            SiteStorageInterface,
        )

        storage = create_autospec(SiteStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, site_storage, user_storage):
        from market.interactors.add_site_details_interactor import (
            AddSiteDetailsInteractor,
        )

        return AddSiteDetailsInteractor(
            site_storage=site_storage, user_storage=user_storage
        )

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def site_dto(self):
        reset()
        from market.tests.common_fixtures.factories import SiteDTOFactory

        return SiteDTOFactory.create()

    def test_raises_user_not_found_exception(
        self,
        site_storage,
        user_storage,
        interactor,
        presenter,
        site_dto,
    ):
        # Arrange
        user_storage.check_user_exists.return_value = False
        presenter.get_user_not_found_response.return_value = Mock()

        # Act
        response = interactor.add_site_details_wrapper(
            site_dto=site_dto, presenter=presenter
        )

        # Assert
        user_storage.check_user_exists.assert_called_once_with(site_dto.owner_id)
        presenter.get_user_not_found_response.assert_called_once_with(site_dto.owner_id)

    def test_add_site_details(
        self,
        site_storage,
        user_storage,
        interactor,
        presenter,
        site_dto,
    ):
        # Arrange
        user_storage.check_user_exists.return_value = True
        site_storage.add_site_details.return_value = None
        presenter.add_site_details_success_response.return_value = Mock()

        # Act
        response = interactor.add_site_details_wrapper(
            site_dto=site_dto, presenter=presenter
        )

        # Assert
        user_storage.check_user_exists.assert_called_once_with(site_dto.owner_id)
        site_storage.add_site_details.assert_called_once_with(site_dto=site_dto)
        assert presenter.get_user_not_found_response.call_count == 0
        presenter.add_site_details_success_response.assert_called_once()

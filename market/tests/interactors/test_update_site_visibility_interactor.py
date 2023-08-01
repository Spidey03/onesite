from unittest.mock import create_autospec, Mock

import pytest

from market.tests.common_fixtures.factories import UserDetailsDTOFactory
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
    def interactor(self, user_storage, site_storage):
        from market.interactors.update_site_visibilit_interactor import (
            UpdateSiteVisibilityInteractor,
        )

        return UpdateSiteVisibilityInteractor(
            user_storage=user_storage, site_storage=site_storage
        )

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def user_details_dto(self):
        reset()
        return UserDetailsDTOFactory()

    def test_if_site_exists_or_not(
        self, user_storage, site_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
        SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd002'
        site_storage.check_site_exists.return_value = False

        # Act
        interactor.update_site_visibility_wrapper(
            site_id=SITE_ID, user_id=USER_ID, visibility=True, presenter=presenter
        )

        # Assert
        site_storage.check_site_exists.assert_called_once_with(site_id=SITE_ID)
        presenter.get_site_not_found_exception_response.assert_called_once_with(
            site_id=SITE_ID
        )

    def test_if_user_not_exists(
        self, user_storage, site_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
        SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd002'
        site_storage.check_site_exists.return_value = True
        user_storage.check_user_exists.return_value = False

        # Act
        interactor.update_site_visibility_wrapper(
            site_id=SITE_ID, user_id=USER_ID, visibility=True, presenter=presenter
        )

        # Assert
        site_storage.check_site_exists.assert_called_once_with(site_id=SITE_ID)
        user_storage.check_user_exists.assert_called_once_with(user_id=USER_ID)
        presenter.user_not_present_response.assert_called_once()

    def test_if_user_owner_or_not(
        self, user_storage, site_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
        SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd002'
        site_storage.check_site_exists.return_value = True
        user_storage.check_user_exists.return_value = True
        site_storage.is_user_owner.return_value = False

        # Act
        interactor.update_site_visibility_wrapper(
            site_id=SITE_ID, user_id=USER_ID, visibility=True, presenter=presenter
        )

        # Assert
        site_storage.check_site_exists.assert_called_once_with(site_id=SITE_ID)
        user_storage.check_user_exists.assert_called_once_with(user_id=USER_ID)
        site_storage.is_user_owner.assert_called_once_with(
            user_id=USER_ID, site_id=SITE_ID
        )
        presenter.user_is_not_owner_of_site.assert_called_once_with(
            site_id=SITE_ID, user_id=USER_ID
        )

    def test_when_user_is_owner_of_site(
        self, user_storage, site_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'
        SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd002'
        site_storage.check_site_exists.return_value = True
        user_storage.check_user_exists.return_value = True
        site_storage.is_user_owner.return_value = True

        # Act
        interactor.update_site_visibility_wrapper(
            site_id=SITE_ID, user_id=USER_ID, visibility=True, presenter=presenter
        )

        # Assert
        site_storage.check_site_exists.assert_called_once_with(site_id=SITE_ID)
        user_storage.check_user_exists.assert_called_once_with(user_id=USER_ID)
        site_storage.is_user_owner.assert_called_once_with(
            user_id=USER_ID, site_id=SITE_ID
        )
        site_storage.update_site_visibility.assert_called_once_with(
            site_id=SITE_ID, is_private=True
        )
        presenter.update_site_visibility_success_response.assert_called_once()

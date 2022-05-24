from unittest.mock import create_autospec, Mock

import pytest

from market.tests.common_fixtures.factories import UserDetailsDTOFactory

SITE_ID = 'd32b2f96-93f5-4e2f-842d-d590783dd001'
OWNER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dc001'


class TestGetSiteDetailsInteractor:
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
    def presenter(self):
        from market.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def interactor(self, user_storage, site_storage):
        from market.interactors.get_site_details import GetSiteInteractor

        interactor = GetSiteInteractor(
            user_storage=user_storage, site_storage=site_storage
        )
        return interactor

    @pytest.fixture
    def site_dto(self):
        from market.tests.common_fixtures.factories import SiteDTOFactory
        from market.tests.common_fixtures.reset_sequence import reset

        reset()
        return SiteDTOFactory.create(owner_id=OWNER_ID)

    def test_raise_site_not_found_exception(
        self, interactor, site_storage, user_storage, presenter
    ):
        # Arrange
        from market.exceptions.exceptions import SiteNotFoundException

        site_storage.get_site_details.side_effect = SiteNotFoundException

        expected_response = Mock()
        presenter.get_site_not_found_exception_response.return_value = expected_response

        # Act
        response = interactor.get_site_details_wrapper(
            site_id=SITE_ID, presenter=presenter
        )

        # Assert
        assert response == expected_response
        site_storage.get_site_details.assert_called_once()
        assert user_storage.get_user.call_count == 0
        presenter.get_site_not_found_exception_response.assert_called_once_with(
            site_id=SITE_ID
        )

    def test_raise_user_not_found_exception(
        self, interactor, site_storage, user_storage, presenter, site_dto
    ):
        # Arrange

        site_storage.get_site_details.return_value = site_dto

        from market.exceptions.exceptions import UserNotFoundException

        user_storage.get_user.side_effect = UserNotFoundException

        expected_response = Mock()
        presenter.get_user_not_found_response.return_value = expected_response

        # Act
        response = interactor.get_site_details_wrapper(
            site_id=SITE_ID, presenter=presenter
        )

        # Assert
        assert response == expected_response
        site_storage.get_site_details.assert_called_once()
        user_storage.get_user.assert_called_once_with(user_id=site_dto.owner_id)
        presenter.get_user_not_found_response.assert_called_once()

    def test_success_response(
        self, interactor, site_storage, user_storage, presenter, site_dto
    ):
        # Arrange

        site_storage.get_site_details.return_value = site_dto
        user_details_dto = UserDetailsDTOFactory(id=site_dto.owner_id)
        user_storage.get_user.return_value = user_details_dto

        expected_response = Mock()
        presenter.get_site_details_response.return_value = expected_response

        # Act
        response = interactor.get_site_details_wrapper(
            site_id=SITE_ID, presenter=presenter
        )

        # Assert
        assert response == expected_response
        site_storage.get_site_details.assert_called_once()
        user_storage.get_user.assert_called_once_with(user_id=site_dto.owner_id)
        presenter.get_site_details_response.assert_called_once_with(
            site_dto=site_dto, owner_dto=user_details_dto
        )

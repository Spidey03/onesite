from unittest.mock import create_autospec, Mock

import pytest

from market.tests.common_fixtures.factories import UserDetailsDTOFactory
from market.tests.common_fixtures.reset_sequence import reset


class TestGetSiteDetailsBulkInteractor:

    @pytest.fixture
    def user_storage(self):
        from market.interactors.storages.user_storages_interface import UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, user_storage):
        from market.interactors.delete_user_interactor import DeleteUserInteractor
        return DeleteUserInteractor(
            user_storage=user_storage
        )

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface \
            import PresenterInterface
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def user_details_dto(self):
        reset()
        return UserDetailsDTOFactory()

    def test_user_not_found_exception(
            self, user_storage, presenter, interactor
    ):
        # Arrange
        user_id = "d32b2f96-93f5-4e2f-842d-d590783dc%03d1"
        user_storage.check_user_exists.return_value = False
        presenter.get_user_not_found_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=user_id,
            presenter=presenter
        )

        # Assert
        user_storage.check_user_exists.assert_called_once_with(user_id=user_id)
        presenter.get_user_not_found_response.assert_called_once_with(user_id=user_id)

    def test_success_response(
            self, user_storage, presenter, interactor
    ):
        # Arrange
        user_id = "d32b2f96-93f5-4e2f-842d-d590783dc%03d1"
        user_storage.check_user_exists.return_value = True
        presenter.user_deleted_successfully_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=user_id,
            presenter=presenter
        )

        # Assert
        user_storage.check_user_exists.assert_called_once_with(user_id=user_id)
        presenter.user_deleted_successfully_response.assert_called_once()

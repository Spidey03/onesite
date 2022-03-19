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
        from market.interactors.add_user_details_interactor import AddUserDetailsInteractor
        return AddUserDetailsInteractor(
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

    def test_invalid_pattern_email(
            self, user_storage, presenter,
            interactor, user_details_dto
    ):
        # Arrange
        user_storage.is_email_already_registered.return_value = True
        presenter.email_already_register_response.return_value = Mock()

        # Act
        interactor.add_user_details_wrapper(
            user_details_dto=user_details_dto,
            presenter=presenter
        )

        # Assert
        user_storage.is_email_already_registered.assert_called_once_with(
            email=user_details_dto.email
        )
        presenter.email_already_register_response.assert_called_once_with(
            email=user_details_dto.email
        )

    def test_email_already_registered(
            self, user_storage, presenter,
            interactor, user_details_dto
    ):
        # Arrange
        user_storage.is_email_already_registered.return_value = True
        presenter.email_already_register_response.return_value = Mock()

        # Act
        interactor.add_user_details_wrapper(
            user_details_dto=user_details_dto,
            presenter=presenter
        )

        # Assert
        user_storage.is_email_already_registered.assert_called_once_with(
            email=user_details_dto.email
        )
        presenter.email_already_register_response.assert_called_once_with(
            email=user_details_dto.email
        )
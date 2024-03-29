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
    def interactor(self, user_storage):
        from market.interactors.update_user_details_interactor import (
            UpdateUserDetailsInteractor,
        )

        return UpdateUserDetailsInteractor(user_storage=user_storage)

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def user_details_dto(self):
        reset()
        return UserDetailsDTOFactory()

    def test_if_user_not_exists(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_storage.check_user_exists.return_value = False
        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.update_user_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        presenter.user_not_present_response.assert_called_once_with()

    def test_invalid_pattern_email(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_details_dto.email = user_details_dto.first_name
        user_storage.check_user_exists.return_value = True
        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.update_user_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        presenter.email_pattern_invalid_response.assert_called_once_with(
            email=user_details_dto.email
        )

    def test_email_already_registered(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_storage.check_user_exists.return_value = True
        user_storage.is_email_already_registered.return_value = True
        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.update_user_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_email_already_registered.assert_called_once()
        presenter.email_already_register_response.assert_called_once_with(
            email=user_details_dto.email
        )

    def test_mobile_number_already_registered(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_storage.check_user_exists.return_value = True
        user_storage.is_email_already_registered.return_value = False
        user_storage.is_mobile_number_already_registered.return_value = True
        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.update_user_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        presenter.mobile_number_already_registered_response.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )

    def test_success_response(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_storage.check_user_exists.return_value = True
        user_storage.is_email_already_registered.return_value = False
        user_storage.is_mobile_number_already_registered.return_value = False
        user_storage.update_user.return_value = None

        # Act
        interactor.update_user_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_email_already_registered.assert_called_once_with(
            email=user_details_dto.email
        )
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        user_storage.update_user.assert_called_once_with(
            user_details_dto=user_details_dto
        )
        presenter.update_user_details_success_response.assert_called_once()

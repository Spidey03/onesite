import datetime
from unittest.mock import create_autospec, Mock, patch

import pytest

from common.services.oauth2_service import Oauth2Service
from common.storage_implementation.dtos import UserAuthTokensDTO
from market.tests.common_fixtures.factories import AddUserDetailsDTOFactory
from market.tests.common_fixtures.reset_sequence import reset

token_dto = UserAuthTokensDTO(
    user_id='f2c8cf25-10fe-4ce6-ba8b-1ab5fd355339',
    access_token='D5BlCiwEpQ6v7s9ykHIlgQlWSRelpt',
    refresh_token='OksuViZaG5dGTSI04mzQNADeUbM6zw',
    expires=datetime.datetime(2022, 5, 25, 15, 38, 46, 922544),
)


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
        from market.interactors.add_user_details_interactor import (
            AddUserDetailsInteractor,
        )

        return AddUserDetailsInteractor(user_storage=user_storage)

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def oauth2service(self):
        from common.services.oauth2_service import Oauth2Service
        from common.storage_implementation.oauth2_storage_implementation import (
            Oauth2StorageImplementation,
        )

        oauth2storage = Oauth2StorageImplementation()
        oauth2service = Oauth2Service(oauth2storage=oauth2storage)
        return oauth2service

    @pytest.fixture
    def user_details_dto(self):
        reset()
        return AddUserDetailsDTOFactory()

    def test_invalid_pattern_email(
        self, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_details_dto.email = user_details_dto.first_name
        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.add_user_details_wrapper(
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
        user_storage.is_email_already_registered.return_value = True
        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.add_user_details_wrapper(
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
        user_storage.is_email_already_registered.return_value = False
        user_storage.is_mobile_number_already_registered.return_value = True
        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.add_user_details_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        presenter.mobile_number_already_registered_response.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )

    def test_weak_password(self, user_storage, presenter, interactor, user_details_dto):
        # Arrange
        user_storage.is_email_already_registered.return_value = False
        user_storage.is_mobile_number_already_registered.return_value = False
        user_storage.add_user.return_value = user_details_dto.id
        user_storage.get_user.return_value = user_details_dto

        presenter.weak_password_exception_response.return_value = Mock()

        # Act
        interactor.add_user_details_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_email_already_registered.assert_called_once()
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        presenter.weak_password_exception_response.assert_called_once()

    @patch.object(Oauth2Service, 'create_auth_tokens', return_value=token_dto)
    def test_success_response(
        self, oauth, user_storage, presenter, interactor, user_details_dto
    ):
        # Arrange
        user_details_dto.password = '1@M4tIsUWyI'
        user_storage.is_email_already_registered.return_value = False
        user_storage.is_mobile_number_already_registered.return_value = False
        user_storage.add_user.return_value = user_details_dto.id
        user_storage.get_user.return_value = user_details_dto

        presenter.email_pattern_invalid_response.return_value = Mock()

        # Act
        interactor.add_user_details_wrapper(
            user_details_dto=user_details_dto, presenter=presenter
        )

        # Assert
        user_storage.is_email_already_registered.assert_called_once()
        user_storage.is_mobile_number_already_registered.assert_called_once_with(
            mobile_number=user_details_dto.mobile_number
        )
        user_storage.add_user.assert_called_once_with(user_details_dto=user_details_dto)
        user_storage.get_user.assert_called_once_with(user_id=user_details_dto.id)
        presenter.add_user_details_success_response.assert_called_once_with(
            user_dto=user_details_dto, auth_token_dto=token_dto
        )

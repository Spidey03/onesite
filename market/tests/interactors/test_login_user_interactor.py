import datetime
from unittest.mock import create_autospec, Mock, patch

import pytest

from common.services.oauth2_service import Oauth2Service
from common.storage_implementation.dtos import UserAuthTokensDTO

token_dto = UserAuthTokensDTO(
    user_id='f2c8cf25-10fe-4ce6-ba8b-1ab5fd355339',
    access_token='D5BlCiwEpQ6v7s9ykHIlgQlWSRelpt',
    refresh_token='OksuViZaG5dGTSI04mzQNADeUbM6zw',
    expires=datetime.datetime(2022, 5, 25, 15, 38, 46, 922544),
)
USER_ID = 'd32b2f96-93f5-4e2f-842d-d590783dcfed'


class TestLoginUserInteractor:
    @pytest.fixture
    def user_storage(self):
        from market.interactors.storages.user_storages_interface import (
            UserStorageInterface,
        )

        user_storage = create_autospec(UserStorageInterface)
        return user_storage

    @pytest.fixture
    def presenter(self):
        from market.interactors.presenters.presenter_interface import PresenterInterface

        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def interactor(self, user_storage):
        from market.interactors.login_user_interactor import LoginUserInteractor

        return LoginUserInteractor(user_storage=user_storage)

    @pytest.fixture
    def login_user_dto(self):
        from market.tests.common_fixtures.factories import LoginUserDTOFactory
        from market.tests.common_fixtures.reset_sequence import reset

        reset()
        return LoginUserDTOFactory()

    def test_when_user_with_username_not_found(
        self, interactor, user_storage, presenter, login_user_dto
    ):
        # Arrange
        user_storage.check_username_already_exists.return_value = False
        presenter.username_not_found_response.return_value = Mock()

        # Act
        interactor.login_wrapper(user_dto=login_user_dto, presenter=presenter)

        # Assert
        user_storage.check_username_already_exists.assert_called_once_with(
            username=login_user_dto.username
        )
        presenter.username_not_found_response.assert_called_once_with(
            username=login_user_dto.username
        )

    def test_when_fields_does_not_match(
        self, interactor, user_storage, presenter, login_user_dto
    ):
        # Arrange
        user_storage.check_username_already_exists.return_value = True
        user_storage.authenticate_user.return_value = (None, False)
        presenter.login_failed_response.return_value = Mock()

        # Act
        interactor.login_wrapper(user_dto=login_user_dto, presenter=presenter)

        # Assert
        user_storage.check_username_already_exists.assert_called_once_with(
            username=login_user_dto.username
        )
        user_storage.authenticate_user.assert_called_once_with(user_dto=login_user_dto)
        presenter.login_failed_response.assert_called_once()

    @patch.object(Oauth2Service, 'create_auth_tokens', return_value=token_dto)
    def test_when_fields_match(
        self, oauth, interactor, user_storage, presenter, login_user_dto
    ):
        # Arrange
        user_storage.check_username_already_exists.return_value = True
        user_storage.authenticate_user.return_value = (USER_ID, True)
        presenter.login_failed_response.return_value = Mock()

        # Act
        interactor.login_wrapper(user_dto=login_user_dto, presenter=presenter)

        # Assert
        user_storage.check_username_already_exists.assert_called_once_with(
            username=login_user_dto.username
        )
        user_storage.authenticate_user.assert_called_once_with(user_dto=login_user_dto)
        presenter.login_success_response.assert_called_once_with(
            auth_token_dto=token_dto
        )

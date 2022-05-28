from unittest.mock import create_autospec

import pytest

from market.tests.common_fixtures.factories import AddUserDetailsDTOFactory
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
        from market.interactors.add_users_bulk_interactor import (
            AddUserDetailsBulkInteractor,
        )

        return AddUserDetailsBulkInteractor(user_storage=user_storage)

    @pytest.fixture
    def user_details_dto_list(self):
        reset()
        return AddUserDetailsDTOFactory.create_batch(size=5)

    def test_success_response(self, user_storage, interactor, user_details_dto_list):
        # Arrange
        user_details_dto_list[-1].password = '1@M4tIsUWyI'
        user_details_dto_list[-2].password = '1@M4tIsUWyI'
        user_storage.validate_email_already_exist_bulk.return_value = [
            user_details_dto_list[-1].email,
            user_details_dto_list[-2].email,
        ]
        user_storage.validate_mobile_number_already_exist_bulk.return_value = [
            user_details_dto_list[-1].mobile_number
        ]
        user_storage.validate_username_already_exist_bulk.return_value = [
            user_details_dto_list[-1].username
        ]

        emails = [user_dto.email for user_dto in user_details_dto_list[-2:]]
        mobile_numbers = [
            user_dto.mobile_number for user_dto in user_details_dto_list[-2:]
        ]
        usernames = [user_dto.username for user_dto in user_details_dto_list[-2:]]

        # Act
        interactor.add_user_details_bulk(user_details=user_details_dto_list)

        # Assert
        user_storage.validate_email_already_exist_bulk.assert_called_once_with(
            email_list=emails
        )
        user_storage.validate_mobile_number_already_exist_bulk.assert_called_once_with(
            mobile_numbers=mobile_numbers
        )
        user_storage.validate_username_already_exist_bulk.assert_called_once_with(
            usernames=usernames
        )
        user_storage.add_users_bulk.assert_called_once_with(
            user_details_dto_list=user_details_dto_list[-1:]
        )

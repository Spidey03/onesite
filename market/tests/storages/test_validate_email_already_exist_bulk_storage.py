import datetime

import factory
import pytest

from market.tests.common_fixtures.reset_sequence import reset

EMAILS = ['kinmoori@gmail.com', 'joetan@mind.com']


class TestValidateEmailAlreadyExistBulk:
    @pytest.fixture
    def storage(self):
        from market.storages.user_storage_implementation import (
            UserStorageImplementation,
        )

        return UserStorageImplementation()

    @pytest.fixture
    def user_db(self):
        reset()
        from market.tests.common_fixtures.model_factories import UserModelFactory

        UserModelFactory.create_batch(
            size=len(EMAILS),
            email=factory.Iterator(EMAILS),
            date_joined=datetime.datetime(2022, 3, 22),
            first_name=factory.Iterator(['Steve', 'Tony']),
        )

    @pytest.mark.django_db
    def test_when_no_email_exist(self, storage):
        # Arrange
        emails = ['july1999@hotmail.com', 'joetan@mind.com']
        expected_response = emails

        # Act
        valid_emails = storage.validate_email_already_exist_bulk(email_list=emails)

        # Assert
        assert list(set(valid_emails)) == list(set(expected_response))

    @pytest.mark.django_db
    def test_validate_email_already_exist_bulk(self, storage, user_db):
        # Arrange
        emails = ['july1999@hotmail.com', 'joetan@mind.com']
        expected_response = ['july1999@hotmail.com']

        # Act
        valid_emails = storage.validate_email_already_exist_bulk(email_list=emails)

        # Assert
        assert valid_emails == expected_response

    @pytest.mark.django_db
    def test_when_all_email_exist(self, storage, user_db):
        # Arrange
        emails = ['kinmoori@gmail.com', 'joetan@mind.com']
        expected_response = []

        # Act
        valid_emails = storage.validate_email_already_exist_bulk(email_list=emails)

        # Assert
        assert valid_emails == expected_response

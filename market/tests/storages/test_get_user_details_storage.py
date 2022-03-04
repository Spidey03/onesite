from market.storages.user_storage_implementation import UserStorageImplementation

import pytest

class TestGetUserDetailsStorage:

    @pytest.mark.django_db
    def test_raise_user_not_found_error(self):
        # Arrange
        user_id = "d32b2f96-93f5-4e2f-842d-d590783dcfeb"
        storage = UserStorageImplementation()

        with pytest.raises(UserNotFoundException):
            user_details = storage.get_user(user_id=user_id)

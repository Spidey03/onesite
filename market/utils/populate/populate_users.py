import uuid
from typing import List

import numpy as np
from pandas import DataFrame

from market.interactors.storages.dtos import AddUserDetailsDTO

USER_DATA_FILE_PATH = 'users.csv'


class PopulateUsers:
    def __init__(self, file_path: str = USER_DATA_FILE_PATH):
        self.file_path = file_path

    def populate(self):
        data = self._get_data()
        user_details_dto_list = self._create_user_dtos(data=data)
        self._save_users(user_details_dto_list=user_details_dto_list)

    def _get_data(self) -> DataFrame:
        import pandas as pd

        data = pd.read_csv(filepath_or_buffer=self.file_path)
        data.replace(np.nan, '', inplace=True)
        data = data.astype(
            {
                'id': str,
                'username': str,
                'email': str,
                'first_name': str,
                'last_name': str,
                'mobile_number': str,
                'is_staff': bool,
                'is_active': bool,
                'password': str,
            }
        )
        return data

    def _create_user_dtos(self, data) -> List[AddUserDetailsDTO]:
        return [self._create_dto(row) for index, row in data.iterrows()]

    @staticmethod
    def _create_dto(row):
        user_dto = AddUserDetailsDTO(
            id=row.id if row.id != '' else str(uuid.uuid4()),
            username=row.username,
            first_name=row.first_name,
            last_name=row.last_name,
            mobile_number=row.mobile_number,
            email=row.email,
            is_staff=row.is_staff,
            is_active=row.is_active,
            password=row.password,
        )
        return user_dto

    @staticmethod
    def _save_users(user_details_dto_list: List[AddUserDetailsDTO]):
        from market.storages.user_storage_implementation import (
            UserStorageImplementation,
        )
        from market.interactors.add_users_bulk_interactor import (
            AddUserDetailsBulkInteractor,
        )

        user_storage = UserStorageImplementation()
        interactor = AddUserDetailsBulkInteractor(user_storage=user_storage)
        interactor.add_user_details_bulk(user_details=user_details_dto_list)


if __name__ == '__main__':
    o = PopulateUsers()
    o.populate()

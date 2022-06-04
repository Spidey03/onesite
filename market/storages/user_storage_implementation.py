import datetime
from typing import List, Union, Optional

from market.interactors.storages.dtos import (
    UserDetailsDTO,
    AddUserDetailsDTO,
    LoginUserDTO,
)
from market.interactors.storages.user_storages_interface import UserStorageInterface


class UserStorageImplementation(UserStorageInterface):
    def get_user(self, user_id: str) -> UserDetailsDTO:
        from market.models import User
        from market.exceptions.exceptions import UserNotFoundException

        if not User.objects.filter(id=user_id).exists():
            raise UserNotFoundException()
        user_details = User.objects.get(id=user_id)
        user_dto = self._get_user_details_dto(user_details)
        return user_dto

    @staticmethod
    def _get_user_details_dto(user_details):
        user_dto = UserDetailsDTO(
            id=str(user_details.id),
            username=str(user_details.username),
            first_name=user_details.first_name,
            last_name=user_details.last_name,
            mobile_number=user_details.mobile_number,
            email=user_details.email,
            date_joined=str(user_details.date_joined.replace(tzinfo=None)),
        )
        return user_dto

    def get_users_bulk(self, user_ids: List[str]):
        from market.models import User

        user_objs = User.objects.filter(id__in=user_ids)
        user_dto_list = [self._get_user_details_dto(user_obj) for user_obj in user_objs]
        return user_dto_list

    def check_user_exists(self, user_id: str):
        from market.models import User

        return User.objects.filter(id=user_id, is_removed=False).exists()

    def is_email_already_registered(self, email: str) -> bool:
        from market.models import User

        return User.objects.filter(email=email).exists()

    def add_user(self, user_details_dto: AddUserDetailsDTO):
        user_obj = self._create_user_obj(user_details_dto=user_details_dto)
        user_obj.save()
        return user_obj.id

    def add_users_bulk(self, user_details_dto_list: List[AddUserDetailsDTO]):
        from market.models import User

        user_objs = [
            self._create_user_obj(user_details_dto=user_details_dto)
            for user_details_dto in user_details_dto_list
        ]
        User.objects.bulk_create(user_objs)

    @staticmethod
    def _create_user_obj(user_details_dto: AddUserDetailsDTO):
        from market.models import User
        from django.contrib.auth.hashers import make_password

        user_obj = User(
            id=user_details_dto.id,
            username=user_details_dto.username,
            first_name=user_details_dto.first_name,
            mobile_number=user_details_dto.mobile_number,
            email=user_details_dto.email,
            last_name=user_details_dto.last_name,
            password=make_password(user_details_dto.password),
            is_staff=user_details_dto.is_staff,
            is_active=user_details_dto.is_active,
            date_joined=datetime.datetime.now(),
        )
        return user_obj

    def is_mobile_number_already_registered(self, mobile_number: str) -> bool:
        from market.models.user import User

        return User.objects.filter(mobile_number=mobile_number).exists()

    def update_user(self, user_details_dto: UserDetailsDTO):
        from market.models import User

        User.objects.filter(id=user_details_dto.id).update(
            first_name=user_details_dto.first_name,
            last_name=user_details_dto.last_name,
            mobile_number=user_details_dto.mobile_number,
            email=user_details_dto.email,
        )

    def delete_user(self, user_id):
        from market.models import User

        User.objects.filter(id=user_id).update(is_removed=True)

    def check_username_already_exists(self, username: str) -> bool:
        from market.models import User

        return User.objects.filter(username=username).exists()

    def is_account_disabled(
        self, username: Optional[str] = '', user_id: Optional[str] = ''
    ) -> bool:
        from market.models import User

        user_obj = (
            User.objects.get(id=user_id)
            if user_id
            else User.objects.get(username=username)
        )
        return user_obj.is_removed

    def authenticate_user(self, user_dto: LoginUserDTO) -> (Union[str, None], bool):
        from market.models import User

        user = User.objects.get(username=user_dto.username)
        is_authenticated = user.check_password(raw_password=user_dto.password)
        user_id = str(user.id)

        # set active status to True
        user.is_active = True
        user.save()

        return user_id, is_authenticated

    def validate_email_already_exist_bulk(self, email_list: List[str]) -> List[str]:
        from market.models import User

        user_objs = User.objects.filter(email__in=email_list)
        return list(set(email_list) - set([user_obj.email for user_obj in user_objs]))

    def validate_mobile_number_already_exist_bulk(
        self, mobile_numbers: List[str]
    ) -> List[str]:
        from market.models import User

        user_objs = User.objects.filter(mobile_number__in=mobile_numbers)
        return list(
            set(mobile_numbers)
            - set([user_obj.mobile_number for user_obj in user_objs])
        )

    def validate_username_already_exist_bulk(self, usernames: List[str]) -> List[str]:
        from market.models import User

        user_objs = User.objects.filter(username__in=usernames)
        return list(set(usernames) - set([user_obj.username for user_obj in user_objs]))

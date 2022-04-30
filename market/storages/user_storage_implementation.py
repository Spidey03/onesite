import datetime
from typing import List

from market.interactors.storages.dtos import UserDetailsDTO
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
            first_name=user_details.first_name,
            middle_name=user_details.middle_name,
            last_name=user_details.last_name,
            mobile_number=user_details.mobile_number,
            email=user_details.email,
            joined_at=str(user_details.joined_at.replace(tzinfo=None))
        )
        return user_dto

    def get_users_bulk(self, user_ids: List[str]):
        from market.models import User
        user_objs = User.objects.filter(id__in=user_ids)
        user_dto_list = [
            self._get_user_details_dto(user_obj)
            for user_obj in user_objs
        ]
        return user_dto_list

    def check_user_exists(self, user_id: str):
        from market.models import User
        return User.objects.filter(id=user_id).exists()

    def is_email_already_registered(self, email: str) -> bool:
        from market.models import User
        return User.objects.filter(email=email).exists()

    def add_user(self, user_details_dto: UserDetailsDTO):
        from market.models import User
        User.objects.create(
            id=user_details_dto.id,
            email=user_details_dto.email,
            first_name=user_details_dto.first_name,
            last_name=user_details_dto.last_name,
            middle_name=user_details_dto.middle_name,
            joined_at=datetime.datetime.now(),
            mobile_number=user_details_dto.mobile_number
        )

    def is_mobile_number_already_registered(self, mobile_number: str) -> bool:
        from market.models.user import User
        return User.objects.filter(mobile_number=mobile_number).exists()

    def update_user(self, user_details_dto: UserDetailsDTO):
        from market.models import User
        User.objects.filter(id=user_details_dto.id).update(
            first_name=user_details_dto.first_name,
            last_name=user_details_dto.last_name,
            middle_name=user_details_dto.middle_name,
            mobile_number=user_details_dto.mobile_number,
            email=user_details_dto.email
        )
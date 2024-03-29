import abc
from typing import Optional, List

from common.storage_implementation.dtos import UserAuthTokensDTO
from market.interactors.storages.dtos import UserDetailsDTO, SiteDTO


class PresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_user_details(self, user_details_dto: UserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_user_not_found_response(self, user_id: Optional[str] = None):
        pass

    @abc.abstractmethod
    def get_site_details_response(self, site_dto: SiteDTO, owner_dto: UserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_site_not_found_exception_response(self, site_id):
        pass

    @abc.abstractmethod
    def get_sites_bulk_response(
        self, site_dto_list: List[SiteDTO], owner_dto_list: List[UserDetailsDTO]
    ):
        pass

    @abc.abstractmethod
    def add_site_details_success_response(self):
        pass

    @abc.abstractmethod
    def email_already_register_response(self, email: str):
        pass

    @abc.abstractmethod
    def email_pattern_invalid_response(self, email):
        pass

    @abc.abstractmethod
    def mobile_number_already_registered_response(self, mobile_number):
        pass

    @abc.abstractmethod
    def add_user_details_success_response(self, user_dto: UserDetailsDTO):
        pass

    @abc.abstractmethod
    def update_user_details_success_response(self):
        pass

    @abc.abstractmethod
    def user_not_present_response(self):
        pass

    @abc.abstractmethod
    def user_deleted_successfully_response(self):
        pass

    @abc.abstractmethod
    def weak_password_exception_response(self):
        pass

    @abc.abstractmethod
    def username_already_taken_response(self, username: str):
        pass

    @abc.abstractmethod
    def username_not_found_response(self, username: str):
        pass

    @abc.abstractmethod
    def login_failed_response(self):
        pass

    @abc.abstractmethod
    def login_success_response(self, auth_token_dto: UserAuthTokensDTO):
        pass

    @abc.abstractmethod
    def user_is_not_owner_of_site(self, user_id: str, site_id: str):
        pass

    @abc.abstractmethod
    def update_site_visibility_success_response(self):
        pass

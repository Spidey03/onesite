from typing import Optional, List

from common.storage_implementation.dtos import UserAuthTokensDTO
from market.constants.constants import StatusCode
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import UserDetailsDTO, SiteDTO


class PresenterImplementation(PresenterInterface):
    def get_user_details(self, user_details_dto: UserDetailsDTO):
        return {
            'user_id': user_details_dto.id,
            'first_name': user_details_dto.first_name,
            'last_name': user_details_dto.last_name,
            'date_joined': user_details_dto.date_joined,
            'email': user_details_dto.email,
        }

    def get_user_not_found_response(self, user_id: Optional[str] = None):
        from market.constants.exception_message import USER_NOT_FOUND_EXCEPTION

        response = USER_NOT_FOUND_EXCEPTION[0].format(user_id)
        res_status = USER_NOT_FOUND_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def get_site_details_response(self, site_dto: SiteDTO, owner_dto: UserDetailsDTO):
        response = site_dto.__dict__
        response['owner'] = owner_dto.__dict__
        response.pop('owner_id')
        return response

    def get_site_not_found_exception_response(self, site_id):
        from market.constants.exception_message import SITE_NOT_FOUND_EXCEPTION

        response = SITE_NOT_FOUND_EXCEPTION[0].format(site_id)
        res_status = SITE_NOT_FOUND_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def get_sites_bulk_response(
        self, site_dto_list: List[SiteDTO], owner_dto_list: List[UserDetailsDTO]
    ):
        from collections import defaultdict

        owner_dtos_dict = defaultdict()
        for owner_dto in owner_dto_list:
            owner_dtos_dict[owner_dto.id] = owner_dto
        response = []

        for site_dto in site_dto_list:
            owner_dto = owner_dtos_dict.get(site_dto.owner_id)
            site_response = site_dto.__dict__
            site_response.pop('owner_id')
            site_response['owner'] = owner_dto.__dict__
            response.append(site_response)

        return response

    def add_site_details_success_response(self):
        from market.constants.exception_message import SITE_ADDED_SUCCESSFULLY

        response = SITE_ADDED_SUCCESSFULLY[0]
        res_status = SITE_ADDED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Created_Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def email_already_register_response(self, email: str):
        from market.constants.exception_message import EMAIL_ALREADY_EXIST

        response = EMAIL_ALREADY_EXIST[0].format(email)
        res_status = EMAIL_ALREADY_EXIST[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def email_pattern_invalid_response(self, email):
        from market.constants.exception_message import EMAIL_PATTERN_INVALID

        response = EMAIL_PATTERN_INVALID[0].format(email)
        res_status = EMAIL_PATTERN_INVALID[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def mobile_number_already_registered_response(self, mobile_number):
        from market.constants.exception_message import MOBILE_NUMBER_ALREADY_EXIST

        response = MOBILE_NUMBER_ALREADY_EXIST[0].format(mobile_number)
        res_status = MOBILE_NUMBER_ALREADY_EXIST[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def add_user_details_success_response(self, user_dto: UserDetailsDTO):
        return {
            'user_id': user_dto.id,
            'username': user_dto.username,
            'first_name': user_dto.first_name,
            'last_name': user_dto.last_name,
            'email': user_dto.email,
            'mobile_number': user_dto.mobile_number,
        }

    def update_user_details_success_response(self):
        from market.constants.exception_message import USER_DETAILS_UPDATED_SUCCESSFULLY

        response = USER_DETAILS_UPDATED_SUCCESSFULLY[0]
        res_status = USER_DETAILS_UPDATED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def user_not_present_response(self):
        from market.constants.exception_message import USER_NOT_EXISTS

        response = USER_NOT_EXISTS[0]
        res_status = USER_NOT_EXISTS[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def user_deleted_successfully_response(self):
        from market.constants.exception_message import USER_DELETE_SUCCESSFULLY

        response = USER_DELETE_SUCCESSFULLY[0]
        res_status = USER_DELETE_SUCCESSFULLY[1]
        http_status_code = StatusCode.Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def weak_password_exception_response(self):
        from market.constants.exception_message import WEAK_PASSWORD_EXCEPTION

        response = WEAK_PASSWORD_EXCEPTION[0]
        res_status = WEAK_PASSWORD_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def username_already_taken_response(self, username: str):
        from market.constants.exception_message import USERNAME_ALREADY_TAKEN_EXCEPTION

        response = USERNAME_ALREADY_TAKEN_EXCEPTION[0].format(username)
        res_status = USERNAME_ALREADY_TAKEN_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def username_not_found_response(self, username: str):
        from market.constants.exception_message import USERNAME_NOT_FOUND

        response = USERNAME_NOT_FOUND[0].format(username)
        res_status = USERNAME_NOT_FOUND[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def login_failed_response(self):
        from market.constants.exception_message import LOGIN_FAILED

        response = LOGIN_FAILED[0]
        res_status = LOGIN_FAILED[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def login_success_response(self, auth_token_dto: UserAuthTokensDTO):
        return {
            'user_id': auth_token_dto.user_id,
            'access_token': auth_token_dto.access_token,
            'refresh_token': auth_token_dto.refresh_token,
            'expires': auth_token_dto.expires,
        }

    def user_is_not_owner_of_site(self, user_id: str, site_id: str):
        from market.constants.exception_message import USER_NOT_OWNER

        response = USER_NOT_OWNER[0].format(user_id=user_id, site_id=site_id)
        res_status = USER_NOT_OWNER[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

    def update_site_visibility_success_response(self):
        from market.constants.exception_message import (
            SITE_VISIBILITY_UPDATED_SUCCESSFULLY,
        )

        response = SITE_VISIBILITY_UPDATED_SUCCESSFULLY[0]
        res_status = SITE_VISIBILITY_UPDATED_SUCCESSFULLY[1]
        http_status_code = StatusCode.Success.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code,
        }

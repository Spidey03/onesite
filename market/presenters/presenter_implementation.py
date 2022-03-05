from typing import Optional

from market.constants.constants import StatusCode
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import UserDetailsDTO


class PresenterImplementation(PresenterInterface):

    def get_user_details(self, user_details_dto: UserDetailsDTO):
        return {
            "user_id": user_details_dto.id,
            "first_name": user_details_dto.first_name,
            "last_name": user_details_dto.last_name,
            "middle_name": user_details_dto.middle_name,
            "joined_at": user_details_dto.joined_at,
            "mobile_number": user_details_dto.mobile_number,
            "email": user_details_dto.email
        }

    def get_user_not_found_response(self, user_id: Optional[str] = None):
        from market.constants.exception_message import USER_NOT_FOUND_EXCEPTION
        response = USER_NOT_FOUND_EXCEPTION[0].format(user_id)
        res_status = USER_NOT_FOUND_EXCEPTION[1]
        http_status_code = StatusCode.BadRequest.value
        return {
            'response': response,
            'res_status': res_status,
            'status_code': http_status_code
        }

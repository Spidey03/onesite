from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from market.interactors.storages.dtos import UserDetailsDTO


def get_user_details_dto(data, user_id: str) -> UserDetailsDTO:
    return UserDetailsDTO(
        id=user_id,
        first_name=data.get('first_name'),
        mobile_number=data.get('mobile_number'),
        email=data.get('email'),
        last_name=data.get('last_name'),
        username=data.get('username'),
    )


@login_required()
@api_view(['POST'])
def update_user_details(request):
    user_id = str(request.user.id)

    from market.storages.user_storage_implementation import UserStorageImplementation
    from market.presenters.presenter_implementation import PresenterImplementation
    from market.interactors.update_user_details_interactor import (
        UpdateUserDetailsInteractor,
    )

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    interactor = UpdateUserDetailsInteractor(user_storage=user_storage)

    response = interactor.update_user_wrapper(
        user_details_dto=get_user_details_dto(data=request.data, user_id=user_id),
        presenter=presenter,
    )
    return Response(response)

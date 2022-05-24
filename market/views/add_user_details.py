import datetime
import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_user_details_dto(data):
    from market.interactors.storages.dtos import UserDetailsDTO

    return UserDetailsDTO(
        id=str(uuid.uuid4()),
        first_name=data.get('first_name'),
        mobile_number=data.get('mobile_number'),
        email=data.get('email'),
        middle_name=data.get('middle_name'),
        last_name=data.get('last_name'),
    )


@api_view(['POST'])
def add_user_details(request):
    from market.serializers.user_serializer import UserSerializer

    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)

    from market.storages.user_storage_implementation import UserStorageImplementation

    user_storage = UserStorageImplementation()

    from market.interactors.add_user_details_interactor import AddUserDetailsInteractor

    interactor = AddUserDetailsInteractor(user_storage=user_storage)

    from market.presenters.presenter_implementation import PresenterImplementation

    presenter = PresenterImplementation()

    response = interactor.add_user_details_wrapper(
        user_details_dto=get_user_details_dto(request.data), presenter=presenter
    )
    return Response(response)

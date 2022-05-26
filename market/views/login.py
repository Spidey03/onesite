from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_login_user_details_dto(data):
    from market.interactors.storages.dtos import LoginUserDTO

    return LoginUserDTO(
        username=data.get('username'),
        password=data.get('password', ''),
    )


@api_view(['POST'])
def add_user_details(request):
    from market.storages.user_storage_implementation import UserStorageImplementation

    user_storage = UserStorageImplementation()

    from market.interactors.login_user_interactor import LoginUserInteractor

    interactor = LoginUserInteractor(user_storage=user_storage)

    from market.presenters.presenter_implementation import PresenterImplementation

    presenter = PresenterImplementation()

    response = interactor.login_wrapper(
        user_dto=get_login_user_details_dto(request.data), presenter=presenter
    )
    return Response(response)

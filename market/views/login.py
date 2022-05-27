from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_login_user_details_dto(data):
    from market.interactors.storages.dtos import LoginUserDTO

    return LoginUserDTO(
        username=data.get('username'),
        password=data.get('password', ''),
    )


@api_view(['POST'])
def login(request):
    from market.storages.user_storage_implementation import UserStorageImplementation
    from market.presenters.presenter_implementation import PresenterImplementation
    from market.interactors.login_user_interactor import LoginUserInteractor

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = LoginUserInteractor(user_storage=user_storage)
    response = interactor.login_wrapper(
        user_dto=get_login_user_details_dto(request.data), presenter=presenter
    )
    return Response(response)

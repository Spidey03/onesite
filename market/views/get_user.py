from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_user(request, id: str):
    from market.storages.user_storage_implementation import UserStorageImplementation

    storage = UserStorageImplementation()

    from market.presenters.presenter_implementation import PresenterImplementation

    presenter = PresenterImplementation()

    from market.interactors.get_user_details import GetUserDetailsInteractor

    interactor = GetUserDetailsInteractor(storage=storage)

    response = interactor.get_user_details_wrapper(user_id=id, presenter=presenter)
    return Response(response)


@api_view(['GET'])
def get_profile(request):
    user_id = request.data.get('user_id')
    from market.storages.user_storage_implementation import UserStorageImplementation

    storage = UserStorageImplementation()

    from market.presenters.presenter_implementation import PresenterImplementation

    presenter = PresenterImplementation()

    from market.interactors.get_user_details import GetUserDetailsInteractor

    interactor = GetUserDetailsInteractor(storage=storage)

    response = interactor.get_user_details_wrapper(user_id=user_id, presenter=presenter)
    return Response(response)

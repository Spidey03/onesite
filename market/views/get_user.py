from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required()
@api_view(['GET'])
def get_user(request, id: str):
    from market.storages.user_storage_implementation import UserStorageImplementation
    from market.presenters.presenter_implementation import PresenterImplementation
    from market.interactors.get_user_details import GetUserDetailsInteractor

    storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetUserDetailsInteractor(storage=storage)
    response = interactor.get_user_details_wrapper(user_id=id, presenter=presenter)
    return Response(response)


@login_required()
@api_view(['GET'])
def get_profile(request):
    user_id = str(request.user.id)
    from market.storages.user_storage_implementation import UserStorageImplementation
    from market.presenters.presenter_implementation import PresenterImplementation
    from market.interactors.get_user_details import GetUserDetailsInteractor

    storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetUserDetailsInteractor(storage=storage)
    response = interactor.get_user_details_wrapper(user_id=user_id, presenter=presenter)
    return Response(response)

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required()
@api_view(['DELETE'])
def delete_user(request, id: str):
    from market.serializers.user_serializer import UserSerializer
    from market.storages.user_storage_implementation import UserStorageImplementation
    from market.presenters.presenter_implementation import PresenterImplementation
    from market.interactors.delete_user_interactor import DeleteUserInteractor

    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)

    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = DeleteUserInteractor(user_storage=user_storage)
    response = interactor.delete_user_wrapper(user_id=id, presenter=presenter)
    return Response(response)

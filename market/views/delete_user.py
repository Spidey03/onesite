from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["DELETE"])
def delete_user(request):
    from market.serializers.user_serializer import UserSerializer
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)

    from market.storages.user_storage_implementation import UserStorageImplementation
    user_storage = UserStorageImplementation()

    from market.interactors.delete_user_interactor import DeleteUserInteractor
    interactor = DeleteUserInteractor(user_storage=user_storage)

    from market.presenters.presenter_implementation import PresenterImplementation
    presenter = PresenterImplementation()

    response = interactor.delete_user_wrapper(
        user_id=id, presenter=presenter
    )
    return Response(response)

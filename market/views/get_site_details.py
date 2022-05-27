from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required()
@api_view(['GET'])
def get_site_details(request, site_id: str):
    from market.storages.site_storage_implementation import SiteStorageImplementation
    from market.storages.user_storage_implementation import UserStorageImplementation
    from market.presenters.presenter_implementation import PresenterImplementation
    from market.interactors.get_site_details import GetSiteInteractor

    site_storage = SiteStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetSiteInteractor(site_storage=site_storage, user_storage=user_storage)
    response = interactor.get_site_details_wrapper(site_id=site_id, presenter=presenter)

    return Response(response)

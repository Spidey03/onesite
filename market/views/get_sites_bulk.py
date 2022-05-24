from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required()
@api_view(['GET'])
def get_sites_bulk(request):
    from market.storages.site_storage_implementation import SiteStorageImplementation
    from market.storages.user_storage_implementation import UserStorageImplementation

    site_storage = SiteStorageImplementation()
    user_storage = UserStorageImplementation()

    from market.interactors.get_site_details_bulk import GetSiteDetailsBulkInteractor

    interactor = GetSiteDetailsBulkInteractor(
        site_storage=site_storage, user_storage=user_storage
    )

    from market.presenters.presenter_implementation import PresenterImplementation

    presenter = PresenterImplementation()
    response = interactor.get_site_bulk_wrapper(presenter=presenter)

    return Response(response)

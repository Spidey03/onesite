import uuid

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

from market.serializers.site_serializers import SiteSerializer


def get_site_dto(data):
    from market.interactors.storages.dtos import SiteDTO

    return SiteDTO(
        id=str(uuid.uuid4()),
        owner_id=data.get('owner_id'),
        district=data.get('district'),
        state=data.get('state'),
        country=data.get('country'),
        type=data.get('type'),
        price=data.get('price'),
        availability=data.get('availability', True),
        is_private=data.get('is_private', False),
        location_coordinates=data.get('location_coordinates'),
        street_name=data.get('street_name'),
        village=data.get('village'),
        city=data.get('city'),
    )


@login_required()
@api_view(['POST'])
def add_site_details(request):
    from market.storages.site_storage_implementation import SiteStorageImplementation
    from market.storages.user_storage_implementation import UserStorageImplementation

    site_storage = SiteStorageImplementation()
    user_storage = UserStorageImplementation()

    from market.interactors.add_site_details_interactor import AddSiteDetailsInteractor

    interactor = AddSiteDetailsInteractor(
        site_storage=site_storage, user_storage=user_storage
    )

    from market.presenters.presenter_implementation import PresenterImplementation

    presenter = PresenterImplementation()
    serializer = SiteSerializer(data=request.data)
    if serializer.is_valid():
        site_dto = get_site_dto(request.data)
        response = interactor.add_site_details_wrapper(
            site_dto=site_dto, presenter=presenter
        )
    else:
        response = serializer.errors
    return Response(response)

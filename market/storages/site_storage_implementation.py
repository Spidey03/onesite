from typing import List

from market.exceptions.exceptions import SiteNotFoundException
from market.interactors.storages.dtos import SiteDTO
from market.interactors.storages.site_storages_interface import SiteStorageInterface


class SiteStorageImplementation(SiteStorageInterface):
    def get_site_details(self, site_id: str) -> SiteDTO:
        from market.models import SiteModel

        if not SiteModel.objects.filter(id=site_id).exists():
            raise SiteNotFoundException()
        site_obj = SiteModel.objects.get(id=site_id)
        site_dto = self._convert_to_site_dto(site_obj)
        return site_dto

    @staticmethod
    def _convert_to_site_dto(site_obj) -> SiteDTO:
        site_dto = SiteDTO(
            id=str(site_obj.id),
            owner_id=str(site_obj.owner.id),
            district=site_obj.district,
            state=site_obj.state,
            country=site_obj.country,
            type=site_obj.type,
            price=site_obj.price,
            availability=site_obj.availability,
            is_private=site_obj.is_private,
            location_coordinates=site_obj.location_coordinates,
            street_name=site_obj.street_name,
            village=site_obj.village,
            city=site_obj.city,
        )
        return site_dto

    def get_sites_bulk(self) -> List[SiteDTO]:
        from market.models import SiteModel

        site_objs = SiteModel.objects.filter()
        site_dto_list = [
            self._convert_to_site_dto(site_obj=site_obj) for site_obj in site_objs
        ]
        return site_dto_list

    def add_site_details(self, site_dto: SiteDTO):
        from market.models import SiteModel

        SiteModel.objects.create(
            id=site_dto.id,
            owner_id=site_dto.owner_id,
            street_name=site_dto.street_name,
            village=site_dto.village,
            city=site_dto.city,
            district=site_dto.district,
            state=site_dto.state,
            country=site_dto.country,
            location_coordinates=site_dto.location_coordinates,
            type=site_dto.type,
            price=site_dto.price,
            availability=site_dto.availability,
            is_private=site_dto.is_private,
        )

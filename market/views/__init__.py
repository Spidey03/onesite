from market.views.add_site_details import add_site_details
from market.views.add_user_details import add_user_details
from market.views.delete_user import delete_user
from market.views.get_site_details import get_site_details
from market.views.get_sites_bulk import get_sites_bulk
from market.views.get_user import get_user, get_profile
from market.views.login import login


__all__ = [
    'get_user',
    'get_site_details',
    'get_sites_bulk',
    'add_site_details',
    'add_user_details',
    'get_profile',
    'delete_user',
    'login',
]

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_site_details(request, site_id: str):
    response = ""
    return Response(response)

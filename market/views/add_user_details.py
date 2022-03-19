from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def add_user_details(request):
    from market.serializers.user_serializer import UserSerializer
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors)

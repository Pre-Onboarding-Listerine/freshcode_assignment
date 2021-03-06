from rest_framework.viewsets import ModelViewSet

from members.authentications import FreshcodeAuthentication
from members.permissions import IsWritableOrReadOnly
from menus.models import Menu
from menus.serializers import MenuSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [FreshcodeAuthentication]
    permission_classes = [IsWritableOrReadOnly]


menu_not_detail = MenuViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

menu_detail = MenuViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

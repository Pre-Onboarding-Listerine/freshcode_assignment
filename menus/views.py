from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from menus.models import Menu
from menus.serializers import MenuSerializer
from permission import IsAdminOnly


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOnly]


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

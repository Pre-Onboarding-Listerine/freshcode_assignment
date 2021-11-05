from rest_framework.viewsets import ModelViewSet

from menus.models import Menu, Item, Tag
from menus.serializers import MenuSerializer, ItemSerializer, TagSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


menu_not_detail = MenuViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

menu_detail = MenuViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})


item_not_detail = ItemViewSet.as_view({
    'post': 'create',
})

item_detail = ItemViewSet.as_view({
    'put': 'update',
    'delete': 'destroy'
})


tag_not_detail = TagViewSet.as_view({
    'post': 'create',
})

tag_detail = TagViewSet.as_view({
    'put': 'update',
    'delete': 'destroy',
})

from rest_framework.viewsets import ModelViewSet

from items.models import Item


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


item_not_detail = ItemViewSet.as_view({
    'post': 'create',
})

item_detail = ItemViewSet.as_view({
    'put': 'update',
    'delete': 'destroy'
})

from rest_framework.viewsets import ModelViewSet

from items.models import Item
from items.serializers import ItemSerializer
from members.authentications import FreshcodeAuthentication
from members.permissions import IsWritableOrReadOnly


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [FreshcodeAuthentication]
    permission_classes = [IsWritableOrReadOnly]


item_not_detail = ItemViewSet.as_view({
    'post': 'create',
})

item_detail = ItemViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

from rest_framework.viewsets import ModelViewSet

from members.authentications import FreshcodeAuthentication
from members.permissions import IsWritableOrReadOnly
from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [FreshcodeAuthentication]
    permission_classes = [IsWritableOrReadOnly]


tag_not_detail = TagViewSet.as_view({
    'post': 'create',
})

tag_detail = TagViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

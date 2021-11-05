from rest_framework.viewsets import ModelViewSet

from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


tag_not_detail = TagViewSet.as_view({
    'post': 'create',
})

tag_detail = TagViewSet.as_view({
    'put': 'update',
    'delete': 'destroy',
})

from rest_framework.serializers import ModelSerializer

from items.serializers import ItemSerializer
from menus.models import Menu
from tags.serializers import TagSerializer


class MenuSerializer(ModelSerializer):
    items = ItemSerializer(many=True, required=False, read_only=True)
    tags = TagSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'

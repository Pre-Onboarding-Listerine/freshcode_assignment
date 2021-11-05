from rest_framework.serializers import ModelSerializer

from menus.models import Menu, Item, Tag


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

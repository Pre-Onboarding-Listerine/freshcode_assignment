from rest_framework.serializers import ModelSerializer

from tags.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        extra_kwargs = {'menu_id': {'read_only': True}}

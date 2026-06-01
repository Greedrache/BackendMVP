from rest_framework import serializers
from ..models import Theme, Statement

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'name', 'description']


class StatementSerializer(serializers.ModelSerializer):
    theme_name = serializers.CharField(source='theme.name', read_only=True)

    class Meta:
        model = Statement
        fields = ['id', 'theme', 'theme_name', 'title', 'text', 'explanation']
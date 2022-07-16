"""Serializers for recipe APIs"""
from core.models import Recipe

from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Recipe Serializer"""
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']


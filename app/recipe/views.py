from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient

from recipe import serializers


class BaseRecipeAttrViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """Base ViewSet for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """Return the objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new one"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage Ingredients in the database"""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()

from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from digitalmenu.models import Meal, MealCategory
from digitalmenu.serializers import MealCategorySerializer, MealSerializer

class MealCategoryListView(ListAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer
    permission_classes = {permissions.AllowAny,}

class MealListView(APIView):
    serializer_class = MealSerializer
    def get(self, request, slug):
        queryset = Meal.objects.all()
        queryset = queryset.filter(category__slug=slug, available=True)
        serializer = MealSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class MealDetailView(RetrieveAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = {permissions.AllowAny,}
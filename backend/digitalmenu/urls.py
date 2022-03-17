from django.urls import path
from .views import MealListView, MealCategoryListView, MealDetailView

urlpatterns = [
    path('categories/', MealCategoryListView.as_view()),
    path('categories/<str:slug>/', MealListView.as_view()),
    path('meal/<int:pk>/', MealDetailView.as_view())
]
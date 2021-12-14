from django.urls import path
from .views import FruitListView, FruitDetailView

urlpatterns = [
    path('', FruitListView.as_view(), name = 'Fruit_list'),
    path('<int:pk>/', FruitDetailView.as_view(), name = 'Fruit_detail'),
]
from django.shortcuts import render
from rest_framework import generics
from .serializers import FruitSerializer
from .models import Fruit
from .permissions import IsAuthenticatedOrReadOnly


# CR methods in the list view
class FruitListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

# RUD methods in the detailed view
class FruitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



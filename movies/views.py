from rest_framework import viewsets

from .models import MovieData
from .serializers import MovieDataSerializer


class MovieDataViewset(viewsets.ModelViewSet):
	queryset = MovieData.objects.all()
	serializer_class = MovieDataSerializer

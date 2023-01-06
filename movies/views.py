from rest_framework import viewsets

from .models import MovieData
from .serializers import MovieDataSerializer


class MovieDataViewset(viewsets.ModelViewSet):
	queryset = MovieData.objects.all()
	serializer_class = MovieDataSerializer


class ActionViewset(viewsets.ModelViewSet):
	queryset = MovieData.objects.filter(genre='action')
	serializer_class = MovieDataSerializer


class ComedyViewset(viewsets.ModelViewSet):
	queryset = MovieData.objects.filter(genre='comédia')
	serializer_class = MovieDataSerializer

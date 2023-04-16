from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from vacancies import serializers, models
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class VacancyView(ModelViewSet):
    serializer_class = serializers.VacancySerializer
    queryset = models.Vacancy.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]
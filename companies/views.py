from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from companies import serializers, models
from vacancies.serializers import VacancySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ComponyView(ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,]

class CompanyVacanciesView(ViewSet):
    def list(self, request, pk=None):
        queryset = models.Company.objects.get(id=pk)
        vacancies = queryset.vacancies
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
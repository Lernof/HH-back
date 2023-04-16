from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('companies.urls.v1')),
    path('', include('vacancies.urls.v1'))
]
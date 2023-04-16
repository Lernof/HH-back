from rest_framework import routers
from companies import views
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'companies', views.ComponyView)

urlpatterns = [
    path('companies/<int:pk>/vacancies/',views.CompanyVacanciesView.as_view({'get':'list'}))
]

urlpatterns += router.urls
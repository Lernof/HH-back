from django.db import models
from companies.models import Company


# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, related_name='vacancies')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
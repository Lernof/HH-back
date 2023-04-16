from rest_framework import routers
from vacancies import views


router = routers.SimpleRouter()
router.register(r'vacancies', views.VacancyView)
urlpatterns = router.urls
from django.urls import include, path
from rest_framework import routers

from sales import views

router = routers.DefaultRouter()
router.register('', views.SalesViewSet)

urlpatterns = [
    path('', include(router.urls))
]

from django.urls import include, path
from rest_framework import routers

from seller import views

router = routers.DefaultRouter()
router.register('', views.SellerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('seller/<int:month>',views.RetrieveSellerView.as_view()),
]

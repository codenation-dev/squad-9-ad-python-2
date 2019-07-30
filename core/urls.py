"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from notifications import views as notifications_views
from seller import views as seller_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comissions/', include('comission.urls')),
    path('notifications/', include('notifications.urls')),
    path('check_commision/', notifications_views.check_commision),
    path('sellers/', include('seller.urls')),
    path('best_sellers/<int:month>', seller_views.best_sellers),
    path('month_comission/', include('sales.urls'))
]
